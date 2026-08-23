simport streamlit as st
from streamlit_mic_recorder import mic_recorder

st.title("🎤 شات صوتي ذكي")
st.write("اهدر معايا بالعربي، الانجليزية، أو التركية")

# اختيار اللغة
lang = st.radio("اختاري اللغة", ["العربية", "English", "Türkçe"])

audio = mic_recorder(start_prompt="🎤 اضغطي واهدرى", stop_prompt="⏹️ وقف")

if audio:
    st.audio(audio['bytes'])
    st.success(f"سمعتك! اللغة: {lang}")
    st.info("ضرك نزيدو الذكاء الاصطناعي باش يرد عليك بصوت")
