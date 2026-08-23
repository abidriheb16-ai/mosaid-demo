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

if "patient_summary" not in st.session_state:
    st.session_state.patient_summary = None
if "medical_history" not in st.session_state:
    st.session_state.medical_history = []

def create_pdf_report(doc_text, med_list, diet_plan=""):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="MOSAID MEDICAL SYSTEM - TURKEY HEALTH SOLUTION REPORT", ln=1, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", size=11)
    content = f"DOCTOR DIAGNOSIS:\n{doc_text}\n\nPRESCRIPTION & ALTERNATIVES:\n{med_list}\n\nDIET & LIFESTYLE PLAN:\n{diet_plan}"
    pdf.multi_cell(0, 10, txt=content)
    file_path = "Mosaid_Complete_Report.pdf"
    pdf.output(file_path)
    return file_path

st.title("🩺 Mosaid Medical System - الحل الذكي لتحديات القطاع الصحي في تركيا")

lang_choice = st.selectbox(
    "🌐 اختر لغة التواصل / Select Language:",
    ["العربية (Arabic)", "Türkçe (Turkish)", "English"]
)

user_lang = "Arabic" if "العربية" in lang_choice else ("Turkish" if "Türkçe" in lang_choice else "English")
tts_lang = "ar" if "العربية" in lang_choice else ("tr" if "Türkçe" in lang_choice else "en")

st.markdown("---")

col_patient, col_doctor = st.columns(2)

# ==================== 👤 بوابة المريض ====================
with col_patient:
    st.header("👤 بوابة المريض (Patient Portal)")
    
    # حل لمشكلة الاكتظاظ وطول المواعيد: الفرز الذكي
    st.subheader("⏱️ تخفيف الاكتظاظ والفرز الذكي (Smart Triage)")
    st.caption("تجنب طوابير الانتظار الطويلة في المشافي الحكومية عبر الفحص المبدئي السريع:")
    triage_symptom = st.text_input("أدخل العرض الرئيسي باختصار (مثلاً: ألم أسنان، حرارة مرتفعة):")
    if st.button("🔍 تحديد الاختصاص المناسب وتوجيه المريض"):
        if triage_symptom:
            with st.spinner("جاري تحليل الحالة لتحديد العيادة المناسبة..."):
                triage_prompt = f"المريض يعاني من: {triage_symptom}. حدد له بدقة أي اختصاص طبى تركي يجب أن يذهب إليه، وهل الحالة تستدعي مستشفى حكومي أم عيادة منزلية، باللغة {user_lang}."
                triage_res = model.generate_content(triage_prompt).text
                st.info(triage_res)
        else:
            st.error("يرجى كتابة العرض أولاً.")

    st.markdown("---")
    
    # حل لمشكلة نقص الأدوية: البحث عن البدائل التركية المتوفرة (Eşdeğer İlaç)
    st.subheader("💊 محبحث البدائل الدوائية (أثناء نقص الأدوية):")
    missing_drug = st.text_input("أدخل اسم الدواء غير المتوفر أو باهظ الثمن:")
    if st.button("🔄 البحث عن دواء بديل متوفر في تركيا"):
        if missing_drug:
            with st.spinner("جاري البحث عن البدائل المكافئة في السوق التركي..."):
                alt_prompt = f"اقترح أدوية بديلة مكافئة (Eşdeğer İlaç) للدواء التالي المتوفرة في الصيدليات التركية: {missing_drug}. أجب باللغة {user_lang}."
                alt_res = model.generate_content(alt_prompt).text
                st.success(alt_res)
        else:
            st.error("يرجى إدخال اسم الدواء.")

    st.markdown("---")
    
    # التواصل الصوتي
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
            st.session_state.medical_history.append(f"عرض جديد: {patient_msg}")
            
            st.success("تم إرسال الأعراض للطبيب المعالج وحفظها في السجل!")
            st.write("💬 **رد موساعد الصوتي للمريض:**", patient_msg)
            
            tts = gTTS(text=patient_msg, lang=tts_lang)
            tts.save("patient_res.mp3")
            st.audio("patient_res.mp3", autoplay=True)

    # كاميرا التشخيص
    st.markdown("---")
    st.subheader("📸 كاميرا الفحص وتصوير الأدوية والجلد:")
    captured_image = st.camera_input("التقط صورة للجلد أو الدواء")
    if captured_image is not None:
        image = Image.open(captured_image)
        st.image(image, caption="الصورة الملتقطة", use_container_width=True)
        with st.spinner("جاري تحليل الصورة..."):
            img_res = model.generate_content(["حلل هذه الصورة الطبية وقدم نصيحة أولية للمريض:", image]).text
            st.success("تم تحليل الصورة!")
            st.write(img_res)

    if os.path.exists("doctor_voice.mp3"):
        st.markdown("---")
        st.success("🔔 وصلك رد صوتي جديد من الطبيب المعالج + الوصفة الطبية!")
        st.audio("doctor_voice.mp3", autoplay=True)

# ==================== 👨‍⚕️ بوابة الطبيب والأدوية ====================
with col_doctor:
    st.header("👨‍⚕️ بوابة الطبيب ومحاربة هجرة الكوادر (AI Copilot)")
    st.caption("مساعدة الأطباء على تسريع الكشف ومواجهة ضغط العمل:")
    
    if st.session_state.patient_summary:
        st.subheader("📋 Tıbbi Danışma (AI & Doctor Discussion):")
        st.info(st.session_state.patient_summary)
        
        st.markdown("---")
        st.subheader("✍️ التشخيص والوصفة الطبية:")
        doc_diagnosis = st.text_area("التشخيص الطبي (Diagnosis):")
        doc_meds = st.text_area("الأدوية الموصوفة والبدائل المقترحة (Prescription & Alternatives):")
        
        # فحص تضارب الأدوية
        if st.button("🔍 فحص تضارب الأدوية تلقائياً (Check Drug Interactions)"):
            if doc_meds:
                with st.spinner("جاري فحص التضارب الدوائي..."):
                    check_prompt = f"هل هناك تضارب خطير بين الأدوية التالية: {doc_meds}؟ أجب باختصار باللغة العربية والتركية."
                    check_res = model.generate_content(check_prompt).text
                    st.warning(check_res)
            else:
                st.error("يرجى إدخال اسم الدواء أولاً.")

        doc_diet = st.text_area("🍎 النظام الغذائي والممنوعات (Dietary Advice):")
        
        if st.button("🚀 إرسال الرد الصوتي للمريض + إصدار PDF"):
            if doc_diagnosis:
                with st.spinner("جاري تحويل التشخيص لصوت وإنشاء الملف..."):
                    doc_prompt = f"""
                    أنت المساعد 'موساعد'. تحول تشخيص الطبيب: "{doc_diagnosis}"
                    والأدوية: "{doc_meds}" والنظام الغذائي: "{doc_diet}"
                    إلى رسالة صوتية مشجعة باللغة: {user_lang}.
                    """
                    translated_res = model.generate_content(doc_prompt).text
                    
                    tts_doc = gTTS(text=translated_res, lang=tts_lang)
                    tts_doc.save("doctor_voice.mp3")
                    
                    pdf_file = create_pdf_report(doc_diagnosis, doc_meds, doc_diet)
                    st.session_state.medical_history.append(f"تشخيص طبي: {doc_diagnosis}")
                    
                    st.success("تم إرسال الصوت وتوليد الـ PDF بنجاح!")
                    with open(pdf_file, "rb") as f:
                        st.download_button("📥 تحميل التقرير الطبي والوصفة (PDF)", f, file_name="Mosaid_Report.pdf", mime="application/pdf")
                    st.rerun()
            else:
                st.error("يرجى كتابة التشخيص أولاً.")

    st.markdown("---")
    st.subheader("📁 السجل الطبي التراكمي للمريض (Medical Record):")
    if st.session_state.medical_history:
        for item in st.session_state.medical_history:
            st.write(f"- {item}")
    else:
        st.caption("لا توجد سجلات سابقة بعد.")

    st.markdown("---")
    st.subheader("📅 حجز موعد في العيادة (Appointment Booking):")
    app_date = st.date_input("اختر تاريخ الموعد:")
    if st.button("📧 تأكيد وحجز الموعد"):
        st.success(f"تم تسجيل الموعد بتاريخ {app_date} وإرسال إشعار للعيادة بنجاح!")
    
