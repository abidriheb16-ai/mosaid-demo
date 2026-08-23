import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

st.set_page_config(page_title="موساعد", layout="centered")
st.title("🎤 موساعد - ترجمة صوتية")
st.write("اختاري اللغات وتكلمي")

col1, col2 = st.columns(2)
with col1:
    lang_in = st.selectbox("من:", ["ar", "en", "fr", "tr"], format_func=lambda x: {"ar":"العربية","en":"English","fr":"Français","tr":"Türkçe"}[x])
with col2:
    lang_out = st.selectbox("إلى:", ["ar", "en", "fr", "tr"], format_func=lambda x: {"ar":"العربية","en":"English","fr":"Français","tr":"Türkçe"}[x])

if st.button("🎙️ اضغطي وتكلمي"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("اسمع فيك... تكلمي")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=lang_in)
        st.success(f"انتِ قلتي: {text}")
        tts = gTTS(text, lang=lang_out)
        tts.save("reply.mp3")
        st.audio("reply.mp3")
    except:
        st.error("ما فهمتش. عاودي")import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os

st.set_page_config(page_title="موساعد", layout="centered")
st.title("🎤 موساعد - ترجمة صوتية")
st.write("اختاري اللغات وتكلمي")

col1, col2 = st.columns(2)
with col1:
    lang_in = st.selectbox("من:", ["ar", "en", "fr", "tr"], format_func=lambda x: {"ar":"العربية","en":"English","fr":"Français","tr":"Türkçe"}[x])
with col2:
    lang_out = st.selectbox("إلى:", ["ar", "en", "fr", "tr"], format_func=lambda x: {"ar":"العربية","en":"English","fr":"Français","tr":"Türkçe"}[x])

if st.button("🎙️ اضغطي وتكلمي"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("اسمع فيك... تكلمي")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, language=lang_in)
        st.success(f"انتِ قلتي: {text}")
        tts = gTTS(text, lang=lang_out)
        tts.save("reply.mp3")
        st.audio("reply.mp3")
    except:
        st.error("ما فهمتش. عاودي")
