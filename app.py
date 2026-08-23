import streamlit as st
import google.generativeai as genai
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
st.title("🩺 Mosaid Medical System - نظام موساعد")

lang_choice = st.selectbox(
    "🌐 اختر لغة التواصل / Dil Seçin / Select Language:",
    ["العربية (Arabic)", "Türkçe (Turkish)", "English"]
)

if "Türkçe" in lang_choice:
    user_lang = "Turkish"
    tts_lang = "tr"
    input_label = "🎙️ Sesinizi kaydedin ve şikayetinizi söyleyin:"
elif "English" in lang_choice:
    user_lang = "English"
    tts_lang = "en"
    input_label = "🎙️ Record your voice and state your symptoms:"
else:
    user_lang = "Arabic"
    tts_lang = "ar"
    input_label = "🎙️ سجل صوتك واشرح الأعراض التي تشعر بها:"

st.markdown("---")

# 4. التقاط صوت المريض
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
        except Exception as e:
            st.warning("تم عرض النص (لم نتمكن من توليد الصوت لهذا النص).")
