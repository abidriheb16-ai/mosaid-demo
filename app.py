import google.generativeai as genai
import streamlit as st

# --- إعداد الصفحة بتصميم عصري واحترافي ---
st.set_page_config(
    page_title="Mosaid - AI Medical Assistant",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded",
)

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

st.markdown('<p class="main-title">🩺 Mosaid (موساعد)</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-title">المساعد الذكي العابر للحدود للرعاية الطبية الفورية'
    ' وتكسير حواجز اللغة</p>',
    unsafe_allow_html=True,
)

# --- الشريط الجانبي لاختيار اللغات ---
st.sidebar.title("⚙️ الإعدادات واللغات")
target_language = st.sidebar.selectbox(
    "لغة التقرير الموجهة للمستشفى:",
    [
        "التركية (Türkçe)",
        "الإنجليزية (English)",
        "الروسية (Русский)",
        "العربية",
    ],
)


# --- دالة تحليل نبرة الصوت والمؤشر الطبي ---
def analyze_patient_vocal_stress(
    symptom_text, transcribed_audio_context, lang
):
  prompt = f"""
    You are an advanced medical AI assistant integrated into 'Mosaid'. 
    Analyze the following patient's input and vocal indicators:
    Patient Input / Speech: "{symptom_text}"
    Audio Tone / Stress Notes: "{transcribed_audio_context}"
    Target Language for output medical report: "{lang}"
    
    Task:
    1. Estimate the patient's stress/pain urgency level (Low, Moderate, High/Critical).
    2. Provide a professional medical summary in the target language specified above.
    3. Keep it concise, medical, and professional.
    """
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)
  return response.text


# --- الواجهة الرئيسية للتعامل الصوتي والنصي ---
st.markdown("---")
st.markdown("### 🎙️ إدخال الأعراض وصوت المريض (Voice & Symptoms Analysis)")
st.write(
    "بما أنك أشرتِ إلى أن الصوت غير موجود، يمكنكِ هنا إما تسجيل الملاحظات الصوتية"
    " أو كتابتها مباشرة ليقوم الذكاء الاصطناعي بتحليلها:"
)

# خيار إدخال صوتي أو كتابي دقيق
input_method = st.radio(
    "اختر طريقة الإدخال:", ["تسجيل صوتي / وصف الصوت", "كتابة الأعراض مباشرة"]
)

user_input = ""
audio_notes = ""

if input_method == "تسجيل صوتي / وصف الصوت":
  st.info(
    "💡 نصيحة: صفي نبرة صوت المريض وكلامه بدقة لكي يقوم الذكاء الاصطناعي"
    " بتحليله كأنك سجلته بالصوت."
  )
  user_input = st.text_area(
    "ماذا قال المريض بالصوت؟",
    placeholder="اكتب ما نطق به المريض صوتياً هنا...",
  )
  audio_notes = st.selectbox(
    "حدد نبرة صوت المريض الحقيقية أثناء الكلام:",
    [
        "صوت هادئ وطبيعي (Calm / Normal)",
        "صوت مرتبك ومتردد (Anxious / Hesitant)",
        "صوت يظهر عليه الألم الشديد والهلع (Severe Pain / Panic)",
        "صوت متقطع بسبب ضيق التنفس (Shortness of Breath)",
    ],
  )
else:
  user_input = st.text_area(
    "اكتب الأعراض بالتفصيل:",
    placeholder="مثلاً: ألم شديد في البطن وغثيان...",
  )
  audio_notes = "إدخال نصي مباشر من المريض"

# زر التحليل
if st.button("🚀 تحليل الحالة وتوليد التقرير الطبي الذكي"):
  if user_input:
    with st.spinner(
        "جاري تحليل نبرة الصوت والمشاعر وتوليد التقرير الطبي..."
    ):
      try:
        analysis_result = analyze_patient_vocal_stress(
            user_input, audio_notes, target_language
        )
        st.success("تم توليد التقرير بنجاح!")
        st.markdown(f"### 📊 التقرير الطبي الموجه (بـ {target_language}):")
        st.info(analysis_result)
      except Exception as e:
        st.error("يرجى التحقق من إعداد مفتاح الذكاء الاصطناعي في التطبيق.")
  else:
    st.warning("الرجاء إدخال تفاصيل الحالة أو الصوت أولاً.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>Mosaid Project"
    " - Built with Passion & AI (2026)</p>",
    unsafe_allow_html=True,
)

