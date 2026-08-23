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
elif "English" in lang_choice:
    user_lang = "English"
    tts_lang = "en"
    input_label = "🎙️ Record your voice and state your symptoms:"
    camera_label = "📸 Take a medical photo (Skin rash, medication, etc.):"
else:
    user_lang = "Arabic"
    tts_lang = "ar"
    input_label = "🎙️ سجل صوتك واشرح الأعراض التي تشعر بها:"
    camera_label = "📸 التقط صورة طبية (طفح جلدي، دواء، أو تحليل):"

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

# قسم تحليل الصور والكاميرا (للطفح الجلدي والأدوية)
st.subheader(camera_label)
captured_image = st.camera_input("كاميرا الهاتف / Mobile Camera")

if captured_image is not None:
    image = Image.open(captured_image)
    st.image(image, caption="الصورة الملتقطة", use_container_width=True)
    
    with st.spinner("جاري تحليل الصورة طبياً... / Analyzing image..."):
        img_prompt = f"""
        أنت المساعد الطبي الذكي 'موساعد'. حلل هذه الصورة الطبية (قد تكون طفحاً جلدياً، علبة دواء، أو ورقة تحليل).
        قدم للمريض ملاحظات وتوجيهات أولية دقيقة باللغة: {user_lang}.
        تذكر دائماً أن تنصح بزيارة الطبيب المختص للتأكيد.
        """
        img_response = model.generate_content([img_prompt, image])
        img_res_text = img_response.text
        
        st.success("تم تحليل الصورة بنجاح!")
        st.write(f"🩺 **نتيجة تحليل الصورة ({user_lang}):**\n", img_res_text)
