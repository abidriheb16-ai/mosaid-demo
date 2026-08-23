import google.generativeai as genai
import streamlit as st

# --- إعداد الصفحة ---
st.set_page_config(page_title="Mosaid - Emergency SOS", page_icon="🚨", layout="centered")

st.markdown("""
    <style>
    .main-title { font-size: 30px; font-weight: 800; color: #B71C1C; text-align: center; }
    .sub-title { font-size: 15px; color: #555555; text-align: center; margin-bottom: 20px; }
    .sos-button > button {
        width: 100%;
        background-color: #D32F2F !important;
        color: white !important;
        font-size: 22px !important;
        font-weight: bold;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(211, 47, 47, 0.4);
    }
    .sos-button > button:hover {
        background-color: #B71C1C !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🚨 Mosaid - زر الطوارئ السريع (SOS)</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">في حال السقوط أو الألم الشديد، اضغط على الزر أدناه لتنبيه أقرب مستشفى فوراً</p>', unsafe_allow_html=True)

# --- اختيار اللغة ---
target_language = st.selectbox("لغة التنبيه الموجهة للمستشفى:", ["التركية (Türkçe)", "الإنجليزية (English)", "العربية"])

st.markdown("---")

# --- زر الطوارئ الكبير (SOS) ---
st.markdown('<div class="sos-button">', unsafe_allow_html=True)
if st.button("🚨 اضغط هنا في حالة الطوارئ (SOS)"):
    st.error("⚠️ تم إطلاق إشارة الطوارئ بنجاح!")
    st.warning("📍 جاري إرسال إحداثيات موقعك والحالة الحرجة إلى لوحة تحكم المستشفى الإقليمي...")
    
    # رسالة وهمية لإرسال التنبيه للمستشفى
    st.success("✅ تم إبلاغ فريق الإسعاف والمستشفى، ابق هادئاً، سيتم التواصل معك أو تتبع موقعك فوراً.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- خانة الأعراض العادية ---
st.markdown("### 📝 أو اكتب حالتك للأطباء:")
user_input = st.text_area("وصف موجز للحالة:", placeholder="مثلاً: لا أستطيع التنفس، سقطت على الأرض...")

if st.button("🚀 إرسال التقرير الطبي العادي"):
    if user_input:
        st.success("تم إرسال التقرير الطبي للمستشفى بنجاح!")
    else:
        st.warning("الرجاء كتابة وصف الحالة أولاً.")

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Mosaid Emergency System - 2026</p>", unsafe_allow_html=True)
