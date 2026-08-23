import streamlit as st
from streamlit_mic_recorder import mic_recorder
import speech_recognition as sr
from gtts import gTTS
import io
import base64

st.set_page_config(page_title="موساعد الذكي", page_icon="🎤")
st.title("🎤 موساعد - المساعد الذكي")
st.write("اضغطي على الميكرو واهدري، ونسمعك ونرد عليك")

lang = st.selectbox(
    "اختر اللغة / Choose Language / Choisissez la langue",
    ("العربية", "English", "Français")
)
lang_code = {"العربية": "ar", "English": "en", "Français": "fr"}

audio = mic_recorder(start_prompt="🎤 اضغطي واهدري", stop_prompt="⏹️ وقف", key="recorder")

if audio:
    st.audio(audio['bytes'])
    r = sr.Recognizer()
    with sr.AudioFile(io.BytesIO(audio['bytes'])) as source:
        audio_data = r.record(source)
    try:
        if lang == "العربية":
            text = r.recognize_google(audio_data, language="ar-DZ")
        elif lang == "English":
            text = r.recognize_google(audio_data, language="en-US")
        else:
            text = r.recognize_google(audio_data, language="fr-FR")
        st.success(f"سمعتك: {text}")
        if lang == "العربية":
            response = f"فهمتك قلتي: {text}. كيف نقدر نعاونك؟"
        elif lang == "English":
            response = f"I heard you say: {text}. How can I help you?"
        else:
            response = f"J'ai entendu: {text}. Comment puis-je vous aider?"
        st.write("**الرد:**", response)
        tts = gTTS(response, lang=lang_code[lang])
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        b64 = base64.b64encode(mp3_fp.read()).decode()
        audio_html = f'<audio autoplay src="data:audio/mp3;base64,{b64}"></audio>'
        st.markdown(audio_html, unsafe_allow_html=True)
    except:
        st.error("ما فهمتش مليح، عاودي من فضلك")
