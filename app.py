import google.generativeai as genai
import streamlit as st

# --- إعداد الصفحة بتصميم عصري واحترافي ---
st.set_page_config(
    page_title="Mosaid - AI Medical Assistant",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

# تصميم وتنسيق بصري بلغة CSS لجعل التطبيق يبدو مذهلاً
st.markdown(
    """
    <style>
    .main-title {
        font-size: 38px;
        font-weight: 800;
        color: #004D40;
        text-align: center;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 18px;
        color: #555555;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        width: 100%;
        background-color: #00796B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #004D40;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# العنوان الرئيسي المحدث
st.markdown('<p class="main-title">🩺 Mosaid (موساعد)</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">المساعد الذكي العابر للحدود للرعاية الطبية الفورية'
    ' وتكسير حواجز اللغة</p>',
    unsafe_allow_html=True,
)

# --- إعداد مفتاح الذكاء الاصطناعي ---
# genai.configure(api_key="YOUR_GEMINI_API_KEY")


# --- الشريط الجانبي (Sidebar) لاختيار اللغات والإعدادات ---
st.sidebar.title("⚙️ الإعدادات واللغات")
st.sidebar.write("اختر لغة الطبيب أو وجهة المستشفى:")

target_language = st.sidebar.selectbox(
    "لغة التقرير الموجهة للمستشفى:",
    [
        "التركية (Türkçe)",
        "الإنجليزية (English)",
        "الروسية (Русский)",
        "العربية",
    ],
)

patient_mode = st.sidebar.radio(
    "وضع الاستخدام:", ["مريض (Patient)", "طبيب (Doctor)"]
)


# --- دالة تحليل نبرة الصوت وتوتر المريض المتقدمة ---
def analyze_patient_vocal_stress(
    symptom_text, transcribed_audio_context, lang
):
  prompt = f"""
    You are an advanced medical AI assistant integrated into 'Mosaid'. 
    Analyze the following patient's input (converted from voice):
    Patient Input: "{symptom_text}"
    Audio Tone / Stress Notes: "{transcribed_audio_context}"
    Target Language for output medical report: "{lang}"
    
    Task:
    1. Estimate the patient's stress/pain urgency level (Low, Moderate, High/Critical).
    2. Provide a professional medical summary in the target language specified above, highlighting potential emotional distress or hidden pain markers.
    3. Keep it concise, medical, and professional.
    """

  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)
  return response.text


# --- الواجهة الرئيسية للميزة الفائقة ---
st.markdown("---")
st.markdown(
    "### 🎙️ محلل المؤشرات الصوتية ونبرة الألم (Vocal Biomarker & Stress"
    " Analysis)"
)
st.write(
    "هذه الميزة تقرأ الأعراض وتحلل نبرة الصوت وحالة التوتر لإنتاج تقرير طبي"
    " دقيق باللغة المختارة."
)

user_input = st.text_area(
    "اكتب أو الصق ما يشتكي منه المريض:",
    placeholder="مثلاً: عندي ألم حاد في الصدر ودوخة منذ الصباح...",
    height=120,
)

audio_notes = st.selectbox(
    "تقييم نبرة صوت المريض وحالته الظاهرة:",
    [
        "صوت هادئ وطبيعي (Calm / Normal)",
        "صوت مرتبك ومتردد (Anxious / Hesitant)",
        "صوت يظهر عليه الألم الشديد والهلع (Severe Pain / Panic)",
        "صوت متقطع بسبب ضيق التنفس (Shortness of Breath)",
    ],
)

# زر التشغيل والتنفيذ
if st.button("🚀 تحليل الحالة وتوليد التقرير الطبي الذكي"):
  if user_input:
    with st.spinner("جاري تحليل نبرة الصوت والذكاء الاصطناعي الطبي..."):
      try:
        analysis_result = analyze_patient_vocal_stress(
            user_input, audio_notes, target_language
        )
        st.success("تم توليد التقرير بنجاح!")
        st.markdown(f"### 📊 التقرير الطبي الموجه (بـ {target_language}):")
        st.info(analysis_result)
      except Exception as e:
        st.error(
            "يرجى التأكد من إعداد مفتاح الذكاء الاصطناعي (API Key) في الكود."
        )
  else:
    st.warning("الرجاء إدخال الأعراض أولاً.")

# تذييل الصفحة
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>Mosaid Project"
    " - Built with Passion & AI (2026)</p>",
    unsafe_allow_html=True,
)
