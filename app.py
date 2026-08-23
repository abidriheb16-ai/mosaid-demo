import streamlit as st
import google.generativeai as genai

# 1. تهيئة الشاشة
st.set_page_config(page_title="موساعد - Mosaid AI", page_icon="🩺", layout="wide")

# 2. قراءة المفتاح بآمان
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception:
    st.error("⚠️ يرجى التأكد من ضبط GEMINI_API_KEY في Secrets.")
    st.stop()

# 3. النواة الأولى: اختيار اللغة
st.title("🩺 Mosaid Medical System")
selected_lang = st.selectbox(
    "Choose Language / اختر اللغة / Dil Seçin:",
    ["العربية (Arabic)", "Türkçe (Turkish)", "English"]
)

st.success(f"تم ضبط واجهة موساعد على: {selected_lang}")
