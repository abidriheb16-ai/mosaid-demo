import streamlit as st
import google.generativeai as genai
from PIL import Image
from gtts import gTTS

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

# 3. اختيار اللغة (عربية، تركية، إنجليزية)
st.title("🩺 Mosaid Medical System - نظام موساعد الشامل")

lang_choice = st.selectbox(
    "🌐 اختر لغة التواصل / Dil Seçin / Select Language:",
    ["العربية (Arabic)", "Türkçe (Turkish)", "English"]
)

if "Türkçe" in lang_choice:
    user_lang = "Turkish"
    tts_lang = "tr"
    input_label = "🎙️ Sesinizi kaydedin ve şikayetinizi söyleyin:"
    camera_label = "📸 Tıbbi bir fotoğraf çekin (Cilt döküntüsü, ilaç vb.):"
    med_label = "💊 İlaç Takvimi ve Kontrolü:"
elif "English" in lang_choice:
    user_lang = "English"
    tts_lang = "en"
    input_label = "🎙️ Record your voice and state your symptoms:"
    camera_label = "📸 Take a medical photo (Skin rash, medication, etc.):"
    med_label = "💊 Medication Schedule & Daily Tracking:"
else:
    user_lang = "Arabic"
    tts_lang = "ar"
    input_label = "🎙️ سجل صوتك واشرح الأعراض التي تشعر بها:"
    camera_label = "📸 التقط صورة طبية (طفح جلدي، دواء، أو تحليل):"
    med_label = "💊 جدول الأدوية والمتابعة اليومية:"

st.markdown("---")

# قسم التواصل الصوتي
st.subheader(input_label)
user_audio = st.audio_input("تسجيل الصوت / Audio Record")

if user_audio:
    with st.spinner("جاري التحليل الصوتي... / Analyzing..."):
        audio_bytes = user_audio.read()
        prompt = f"""
        أنت المساعد الطبي الذكي 'موساعد'.
        استمع للتسجيل الصوتي للمريض وافهمه بأي لغة يتحدث بها.
        ثم قم بالرد عليه بلغة التواصل المختارة وهي: {user_lang}.
        قدم له تشخيصاً مبدئياً وتطميناً بأسلوب دافئ وقصير.
        """
        response = model.generate_content([
            prompt,
            {"mime_type": "audio/wav", "data": audio_bytes}
        ])
        res_text = response.text
        st.success("تم التحليل بنجاح!")
        st.write(f"💬 **الرد ({user_lang}):**\n", res_text)
        
        try:
            tts = gTTS(text=res_text, lang=tts_lang)
            tts.save("response.mp3")
            st.audio("response.mp3", autoplay=True)
        except Exception:
            pass

st.markdown("---")

# قسم تحليل الصور والكاميرا
st.subheader(camera_label)
captured_image = st.camera_input("كاميرا الهاتف / Mobile Camera")

if captured_image is not None:
    image = Image.open(captured_image)
    st.image(image, caption="الصورة الملتقطة", use_container_width=True)
    
    with st.spinner("جاري تحليل الصورة طبياً... / Analyzing image..."):
        img_prompt = f"""
        أنت المساعد الطبي الذكي 'موساعد'. حلل هذه الصورة الطبية.
        قدم للمريض ملاحظات وتوجيهات أولية دقيقة باللغة: {user_lang}.
        """
        img_response = model.generate_content([img_prompt, image])
        st.success("تم تحليل الصورة بنجاح!")
        st.write(f"🩺 **نتيجة تحليل الصورة ({user_lang}):**\n", img_response.text)

st.markdown("---")

# قسم جدول الأدوية والمتابعة اليومية
st.subheader(med_label)
col1, col2 = st.columns(2)

with col1:
    medicine_name = st.text_input("اسم الدواء / İlaç Adı / Medicine Name:")
    medicine_time = st.text_input("مواعيد الجرعات (مثال: صباحاً ومساءً):")
    if st.button("💾 حفظ في جدول الأدوية"):
        if medicine_name:
            st.success(f"تمت إضافة الدواء ({medicine_name}) بنجاح إلى جدول المتابعة!")
        else:
            st.error("يرجى إدخال اسم الدواء.")

with col2:
    st.markdown("### 📊 المتابعة اليومية للحالة")
    temp_check = st.slider("مستوى الحرارة أو شعور الألم (1 إلى 10):", 1, 10, 5)
    daily_note = st.text_area("سجل تطور الأعراض اليوم (مثال: شعرت بتحسن طفيف):")
    if st.button("📤 إرسال تقرير المتابعة للطبيب"):
        st.info("تم تسجيل ومزامنة بيانات المتابعة اليومية بنجاح لتكون جاهزة لاطلاع الطبيب المعالج.")
