import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
from gtts import gTTS
import io
import base64

st.set_page_config(page_title="موساعد الذكي", page_icon="🎤")

st.title("🎤 موساعد - المساعد الذكي")
st.write("اضغطي على الميكرو واهدري، ونسمعك ونرد عليك")

# اختيار اللغة
lang = st.selectbox(
    "اختر اللغة / Choose Language / Choisissez la langue",
    ("العربية", "English", "Français")
)

lang_code = {"العربية": "ar", "English": "en", "Français": "fr"}

# الميكرو
audio = mic_recorder(
    start_prompt="🎤 اضغطي واهدري",
    stop_prompt="⏹️ وقف",
    key="recorder"
)

if audio:
    st.audio(audio['bytes'])

    # تحويل الصوت لنص
    r = sr.Recognizer()
    with sr.AudioFile(io.BytesIO(audio['bytes'])) as source:
        audio_data = r.record(source)

    try:
        if lang == "العربية":
            text = r.recognize_google(audio_data, language="ar-DZ")
        elif lang == "English":
            text = r.recognize_google(audio_data
