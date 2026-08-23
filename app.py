import streamlit as st
from streamlit_mic_recorder import mic_recorder
import time

st.set_page_config(page_title="شات صوتي ذكي", layout="centered")

st.title("🎤 شات صوتي ذكي - 3 لغات")
st.write("اهدر معايا: عربي، English، Türkçe")

# اختيار اللغة
lang = st.radio("اختاري اللغة:", ["العربية", "English", "Türkçe"], horizontal=True)

# الميكرو
audio = mic_recorder(
    start_prompt="🎤 اضغطي واهدرى", 
    stop_prompt="⏹️ وقف",
    key="recorder"
)

if audio:
    st.audio(audio['bytes'])
    st.success(f"سمعتك! اللغة: {lang}")
    
    # هنا الرد الذكي حسب اللغة
    with st.spinner("جاري التفكير..."):
        time.sleep(1)
        
        if lang == "العربية":
            st.write("🤖: مرحبا بيك! كيف نقدر نعاونك اليوم؟")
        elif lang == "English":
            st.write("🤖: Hello! How can I help you today?")
        else:
            st.write("🤖: Merhaba! Sana nasıl yardımcı olabilirim?")
    
    st.info("الخطوة الجاية نخلوه يرد بصوت حقيقي")
