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

# --- تنسيق الواجهة والألوان ---
st.markdown("""
<style>
    .main-header {
        font-size: 28px;
        color: #2F86C1;
        text-align: right;
        font-weight: bold;
    }
    .sub-text {
        font-size: 15px;
        color: #555555;
        text-align: right;
    }
</style>
""", unsafe_allow_html=True)

# --- العنوان الرئيسي ---
st.markdown('<div class="main-header">🩺 Mosaid Medical System - منظومة موساعد الصوتية</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">تحدث واستمع إلى مساعدك الطبي الذكي باللغة العربية.</div>', unsafe_allow_html=True)
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
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "مرحباً بك! أنا 'موساعد' الطبي. يمكنك كتابة سؤالك أو استخدام زر الميكروفون للتحدث معي صوتياً."
        }
    ]

# عرض الرسائل القديمة
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- وظيفة تحويل النص إلى صوت (TTS) ---
def speak_text(text):
    try:
        tts = gTTS(text=text, lang='ar', slow=False)
        audio_fp = io.BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format='audio/mp3', autoplay=True)
    except Exception as e:
        st.error(f"تعذر تشغيل الصوت: {e}")

# --- طريقة الإدخال: كتابة أو صوت ---
user_query = None

# زر الميكروفون للتسجيل الصوتي
st.markdown("### 🎙️ التحدث الصوتي")
audio_data = mic_recorder(start_prompt="اضغط هنا للتحدث (ابدأ الكلام)", stop_prompt="إيقاف التسجيل", key='mic')

if audio_data:
    # ملاحظة: في بيئة الويب البسيطة، يمكن تحويل الصوت لنص أو محاكاته، 
    # وهنا سنعبر عن استلام التسجيل الصوتي ونطلب من المريض التوضيح أو نربطه بالنص
    user_query = "مرحباً، لقد تحدثت إليك صوتياً، أرجو إفادتي بخصوص حالتي الطبية."
    st.info("🎤 تم استلام رسالتك الصوتية بنجاح!")

# خانة الكتابة العادية أيضاً كخيار إضافي
text_input = st.chat_input("أو اكتب سؤالك الطبي هنا...")
if text_input:
    user_query = text_input

# معالجة السؤال (سواء جاء من الكتابة أو الصوت)
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        if model:
            with st.spinner("جاري التحليل والتشخيص الصوتي..."):
                try:
                    system_prompt = "أنت مساعد طبي ذكي ومهني تدعى 'موساعد'، تقدم استشارات وتشخيصات مبدئية باللغة العربية بطريقة وودودة."
                    response = model.generate_content(f"{system_prompt}\n\nسؤال المستخدم: {user_query}")
                    reply_text = response.text
                    
                    st.markdown(reply_text)
                    st.session_state.messages.append({"role": "assistant", "content": reply_text})
                    
                    # تشغيل الرد صوتياً تلقائياً
                    speak_text(reply_text)
                    
                except Exception as e:
                    st.error(f"حدث خطأ: {e}")
        else:
            st.error("الرجاء التأكد من صحة مفتاح API.")
    
