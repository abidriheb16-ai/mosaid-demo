import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import io
import speech_recognition as sr
from streamlit_mic_recorder import mic_recorder

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="موساعد - Mosaid AI",
    page_icon="🩺",
    layout="centered"
)

# --- القائمة الجانبية ---
st.sidebar.markdown("## ⚙️ إعدادات منظومة موساعد")
user_role = st.sidebar.selectbox(
    "اختر صفة المستخدم:", 
    ["مريض (Patient)", "طبيب (Doctor)"]
)

app_lang = st.sidebar.selectbox(
    "لغة التحدث:", 
    ["العربية", "التركية (Türkçe)", "الإنجليزية (English)"]
)

# تحديد إعدادات اللغة بناءً على الاختيار
if "Türkçe" in app_lang:
    lang_code = 'tr'
    lang_name = 'التركية'
    welcome_msg = "Merhaba! Ben 'Mosaid' sağlık asistanınızım. Tıbbi sorunuzu sesli olarak sorabilirsiniz."
    mic_btn = "🎤 Ses kaydetmek için buraya basın"
    stop_btn = "⏹️ Kaydı Durdur"
elif "English" in app_lang:
    lang_code = 'en'
    lang_name = 'الإنجليزية'
    welcome_msg = "Hello! I am 'Mosaid', your medical assistant. You can ask your medical questions by voice."
    mic_btn = "🎤 Click here to record audio"
    stop_btn = "⏹️ Stop Recording"
else:
    lang_code = 'ar'
    lang_name = 'العربية'
    welcome_msg = "أهلاً بك! أنا مساعدك الطبي 'موساعد'. يمكنك طرح سؤالك الطبي صوتياً وسأجيبك."
    mic_btn = "🎤 اضغط هنا لتسجيل صوتك"
    stop_btn = "⏹️ إيقاف التسجيل"

# --- العنوان الرئيسي ---
st.markdown(f"## 🩺 موساعد الطبي - Mosaid AI ({user_role})")
st.write(f"المنظومة الذكية للتفاعل الصوتي. (اللغة: {lang_name})")
st.write("---")

# --- إعداد مفتاح API ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    else:
        api_key = os.getenv("GEMINI_API_KEY", "")

    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
    else:
        st.error("⚠️ يرجى ضبط مفتاح API.")
        model = None
except Exception as e:
    st.error(f"خطأ في الاتصال بالمفتاح: {e}")
    model = None

# --- الذاكرة ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- وظيفة نطق الرد (TTS) ---
def speak_text(text, code):
    try:
        tts = gTTS(text=text, lang=code, slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error(f"تعذر تشغيل الصوت: {e}")

# --- وظيفة تحويل الصوت المسجل إلى نص (STT) ---
def recognize_speech(audio_bytes, lang):
    r = sr.Recognizer()
    audio_file = io.BytesIO(audio_bytes)
    
    # تحديد كود اللغة للتعرف على الصوت
    recog_lang = 'ar-SA'
    if lang == 'tr':
        recog_lang = 'tr-TR'
    elif lang == 'en':
        recog_lang = 'en-US'

    try:
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=recog_lang)
            return text
    except sr.UnknownValueError:
        return "⚠️ عذراً، لم أتمكن من فهم الصوت بوضوح. يرجى إعادة المحاولة."
    except Exception as e:
        return f"⚠️ خطأ في معالجة الصوت: {e}"

# --- واجهة تسجيل الصوت للمستخدم ---
st.markdown("### 🎙️ تحدث معي:")
audio_data = mic_recorder(
    start_prompt=mic_btn,
    stop_prompt=stop_btn,
    key='mic'
)

user_query = None

# إذا قام المستخدم بالتسجيل
if audio_data:
    st.info("🔄 جاري معالجة صوتك...")
    # تحويل صوت المستخدم إلى نص
    transcribed_text = recognize_speech(audio_data['bytes'], lang_code)
    
    if "⚠️" not in transcribed_text:
        user_query = transcribed_text
    else:
        st.warning(transcribed_text)

# خيار الكتابة الاحتياطي
text_input = st.chat_input("أو يمكنك الكتابة هنا إذا أردت...")
if text_input:
    user_query = text_input

# --- معالجة السؤال والرد ---
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        if model:
            with st.spinner("جاري التفكير..."):
                try:
                    system_prompt = f"""
                    أنت مساعد طبي ذكي ومهني تدعى 'موساعد'.
                    المستخدم يتواصل معك بصفة: {user_role}.
                    لغة التواصل المطلوبة: {lang_name}.
                    أجب بطريقة مبسطة وواضحة جداً لأن الرد سيتم قراءته صوتياً للمستخدم (الذي قد يكون أمياً أو لا يقرأ).
                    """
                    
                    response = model.generate_content(f"{system_prompt}\n\nالسؤال: {user_query}")
                    reply_text = response.text
                    
                    st.markdown(reply_text)
                    st.session_state.messages.append({"role": "assistant", "content": reply_text})
                    
                    # نطق الرد صوتياً
                    speak_text(reply_text, lang_code)
                    
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
    
