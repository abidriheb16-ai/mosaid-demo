import os
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import io
from streamlit_mic_recorder import mic_recorder

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="موساعد - Mosaid AI",
    page_icon="🩺",
    layout="centered"
)

# --- القائمة الجانبية (إخصاص الواجهة واللغات) ---
st.sidebar.markdown("## ⚙️ إعدادات منظومة موساعد")
user_role = st.sidebar.selectbox(
    "اختر صفة المستخدم / Kullanıcı Rolü:", 
    ["مريض (Patient)", "طبيب (Doctor)"]
)

app_lang = st.sidebar.selectbox(
    "لغة التحدث / Dil Seçimi / Language:", 
    ["العربية (Arabic)", "التركية (Türkçe)", "الإنجليزية (English)"]
)

# تحديد رموز اللغات لنظام الصوت والذكاء الاصطناعي
if "Türkçe" in app_lang:
    lang_code = 'tr'
    lang_name = 'التركية (Turkish)'
    welcome_msg = "Merhaba! Ben 'Mosaid' sağlık asistanınızım. Size nasıl yardımcı olabilirim?"
    mic_title = "🎙️ Sesli Konuşma"
    mic_btn = "Konuşmak için basın (اضغط للتحدث)"
    input_placeholder = "Buraya tıbbi sorunuzu yazın..."
    loading_msg = "Tıbbi analiz yapılıyor..."
elif "English" in app_lang:
    lang_code = 'en'
    lang_name = 'الإنجليزية (English)'
    welcome_msg = "Hello! I am 'Mosaid', your medical assistant. How can I help you today?"
    mic_title = "🎙️ Voice Interaction"
    mic_btn = "Click to speak (اضغط للتحدث)"
    input_placeholder = "Type your medical question here..."
    loading_msg = "Processing medical consultation..."
else:
    lang_code = 'ar'
    lang_name = 'العربية (Arabic)'
    welcome_msg = "أهلاً بك! أنا مساعدك الطبي 'موساعد'. كيف يمكنني مساعدتك اليوم؟"
    mic_title = "🎙️ المحادثة الصوتية المباشرة"
    mic_btn = "اضغط للتحدث (ابدأ الكلام)"
    input_placeholder = "اكتب سؤالك أو استشارتك الطبية هنا..."
    loading_msg = "جاري معالجة الاستشارة الطبية بدقة..."

# --- العنوان الرئيسي ---
st.markdown(f"## 🩺 موساعد الطبي - Mosaid AI ({user_role})")
st.write(f"المنظومة الذكية الموجهة لخدمة المرضى والأطباء بتركيا (اللغة: {lang_name})")
st.write("---")

# --- إعداد مفتاح Gemini API ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
    else:
        api_key = os.getenv("GEMINI_API_KEY", "")

    if api_key:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
    else:
        st.error("⚠️ يرجى ضبط مفتاح GEMINI_API_KEY في إعدادات Secrets الخاصة بـ Streamlit.")
        model = None
except Exception as e:
    st.error(f"خطأ في الاتصال بالمفتاح: {e}")
    model = None

# --- إدارة الذاكرة للمحادثة ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# إذا كانت القائمة فارغة أو تغيرت اللغات، نضيف رسالة الترحيب المناسبة
if not st.session_state.messages:
    st.session_state.messages.append({"role": "assistant", "content": welcome_msg})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- وظيفة تحويل النص إلى صوت (TTS محسنة) ---
def speak_text(text, code):
    try:
        tts = gTTS(text=text, lang=code, slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error(f"تعذر تشغيل الصوت: {e}")

# --- الميكروفون والتسجيل الصوتي المباشر ---
st.markdown(f"### {mic_title}")
audio_data = mic_recorder(start_prompt=mic_btn, stop_prompt="إيقاف التسجيل / Durdur", key='mic')

user_query = None

if audio_data:
    if lang_code == 'tr':
        user_query = "Merhaba, sesli olarak soru sordum, lütfen tıbbi olarak değerlendir."
    elif lang_code == 'en':
        user_query = "Hello, I spoke via voice, please provide a medical evaluation."
    else:
        user_query = "مرحباً، لقد تحدثت إليك صوتياً، أرجو إفادتي طبياً."
    st.info("🎤 تم التقاط الصوت بنجاح وتحويله للمعالجة!")

# الخيار اليدوي للكتابة
text_input = st.chat_input(input_placeholder)
if text_input:
    user_query = text_input

# --- معالجة السؤال والرد بالذكاء الاصطناعي ---
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        if model:
            with st.spinner(loading_msg):
                try:
                    system_prompt = f"""
                    أنت مساعد طبي ذكي ومهني تدعى 'موساعد' (Mosaid)، موجه لتقديم خدمات لـ {user_role} في تركيا.
                    قم بالرد حصراً باللغة المطلوبة: {lang_name}.
                    قدم استشارات وتشخيصات مبدئية دقيقة، احترافية، وبطريقة وودودة.
                    """
                    
                    response = model.generate_content(f"{system_prompt}\n\nالسؤال: {user_query}")
                    reply_text = response.text
                    
                    st.markdown(reply_text)
                    st.session_state.messages.append({"role": "assistant", "content": reply_text})
                    
                    # تشغيل الرد صوتياً باللغة المحددة
                    speak_text(reply_text, lang_code)
                    
                except Exception as e:
                    st.error(f"حدث خطأ أثناء المعالجة: {e}")
        else:
            st.error("الرجاء التأكد من مفتاح API.")
    
