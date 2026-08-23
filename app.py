import streamlit as st
import google.generativeai as genai
from PIL import Image
from gtts import gTTS
from fpdf import FPDF
import os

# 1. تهيئة واجهة التطبيق
st.set_page_config(page_title="موساعد - Mosaid AI", page_icon="🩺", layout="wide")

# 2. قراءة المفتاح بآمان من Secrets
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("⚠️ يرجى التأكد من ضبط GEMINI_API_KEY في Secrets.")
    st.stop()

# إدارة جلسة البيانات المؤقتة
if "patient_summary" not in st.session_state:
    st.session_state.patient_summary = None

# دالة إنشاء تقرير PDF الوصفة الطبية
def create_pdf_report(doc_text, med_list):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="MOSAID MEDICAL SYSTEM - PRESCRIPTION & REPORT", ln=1, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 10, txt=f"DOCTOR DIAGNOSIS:\n{doc_text}\n\nPRESCRIPTION / MEDICATIONS:\n{med_list}")
    file_path = "Mosaid_Prescription.pdf"
    pdf.output(file_path)
    return file_path

st.title("🩺 Mosaid Medical System - منصة موساعد التفاعلية")

# اختيار اللغة
lang_choice = st.selectbox(
    "🌐 اختر لغة التواصل / Select Language:",
    ["العربية (Arabic)", "Türkçe (Turkish)", "English"]
)

user_lang = "Arabic" if "العربية" in lang_choice else ("Turkish" if "Türkçe" in lang_choice else "English")
tts_lang = "ar" if "العربية" in lang_choice else ("tr" if "Türkçe" in lang_choice else "en")

st.markdown("---")

# تقسيم الشاشة إلى بوابتين (المريض والطبيب)
col_patient, col_doctor = st.columns(2)

# ==================== 👤 بوابة المريض ====================
with col_patient:
    st.header("👤 بوابة المريض (Patient Portal)")
    st.subheader("🎙️ سجل أعراضك بالصوت:")
    user_audio = st.audio_input("تسجيل الصوت / Audio Record")

    if user_audio:
        with st.spinner("جاري التحليل ومشاركة الأعراض مع الطبيب..."):
            audio_bytes = user_audio.read()
            prompt = f"""
            أنت المساعد الطبي الذكي 'موساعد'.
            استمع لمشكلة المريض، اعطه رد تطميني قصير بلغة المريض ({user_lang}).
            ثم أنشئ ملخصاً طبياً باللغة التركية مسبوقاً بكلمة [TURKISH_SUMMARY] ليتناقش به الطبيب.
            """
            response = model.generate_content([prompt, {"mime_type": "audio/wav", "data": audio_bytes}])
            full_res = response.text
            
            if "[TURKISH_SUMMARY]" in full_res:
                parts = full_res.split("[TURKISH_SUMMARY]")
                patient_msg = parts[0].strip()
                turk_msg = parts[1].strip()
            else:
                patient_msg = full_res
                turk_msg = full_res

            st.session_state.patient_summary = turk_msg
            
            st.success("تم إرسال الأعراض للطبيب المعالج!")
            st.write("💬 **رد موساعد الصوتي للمريض:**", patient_msg)
            
            tts = gTTS(text=patient_msg, lang=tts_lang)
            tts.save("patient_res.mp3")
            st.audio("patient_res.mp3", autoplay=True)

    # عرض رد الطبيب الصوتي والوصفة فور صدورهما
    if os.path.exists("doctor_voice.mp3"):
        st.markdown("---")
        st.success("🔔 وصلك رد صوتي جديد من الطبيب المعالج + الوصفة الطبية!")
        st.audio("doctor_voice.mp3", autoplay=True)

# ==================== 👨‍⚕️ بوابة الطبيب والمناقشة ====================
with col_doctor:
    st.header("👨‍⚕️ بوابة الطبيب (Doctor & AI Discussion)")
    
    if st.session_state.patient_summary:
        st.subheader("📋 Tıbbi Danışma (AI & Doctor Discussion):")
        st.info(st.session_state.patient_summary)
        
        st.markdown("---")
        st.subheader("✍️ تشخيص الطبيب والوصفة الطبية:")
        doc_diagnosis = st.text_area("التشخيص الطبي والتعليمات (Doctor's Diagnosis):")
        doc_meds = st.text_area("الوصفة الطبية والأدوية (Prescription Medications):")
        
        if st.button("🚀 تحويل تشخيص الطبيب لرد صوتي للمريض + PDF"):
            if doc_diagnosis:
                with st.spinner("جاري تحويل كلام الطبيب لصوت المريض وإنشاء الوصفة..."):
                    # موساعد يصيغ كلام الطبيب والوصفة للمريض باللغة المناسبة
                    doc_prompt = f"""
                    أنت المساعد 'موساعد'. قم بتحويل تشخيص الطبيب التالي: "{doc_diagnosis}"
                    والأدوية الموصوفة: "{doc_meds}"
                    إلى رسالة صوتية مشجعة وواضحة للمريض باللغة: {user_lang}.
                    يشرح له فيها اسم المرض بوضوح وطريقة أخذ الدواء.
                    """
                    translated_res = model.generate_content(doc_prompt).text
                    
                    # تحويل رد الطبيب إلى صوت
                    tts_doc = gTTS(text=translated_res, lang=tts_lang)
                    tts_doc.save("doctor_voice.mp3")
                    
                    # إنشاء ملف PDF للوصفة
                    pdf_file = create_pdf_report(doc_diagnosis, doc_meds)
                    
                    st.success("تم تحويل تشخيص الطبيب لصوت وإصدار ملف PDF الوصفة بنجاح!")
                    
                    with open(pdf_file, "rb") as f:
                        st.download_button(
                            label="📥 تحميل الوصفة الطبية (PDF Prescription)",
                            data=f,
                            file_name="Mosaid_Prescription.pdf",
                            mime="application/pdf"
                        )
                    st.rerun()
            else:
                st.error("يرجى كتابة التشخيص الطبي قبل إرساله.")
    else:
        st.write("👈 بانتظار تسجيل صوت المريض لبدء المناقشة الطبية.")
    
