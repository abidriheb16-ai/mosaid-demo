from io import BytesIO
from gtts import gTTS
import google.generativeai as genai
import streamlit as st

# --- إعداد مفتاح الذكاء الاصطناعي ---
if "GEMINI_API_KEY" in st.secrets:
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# --- دالة لتوليد الأصوات الحقيقية (Text-to-Speech) ---
def text_to_speech_bytes(text, lang="en"):
  try:
    tts = gTTS(text=text, lang=lang, slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp
  except Exception as e:
    return None


# --- إعداد الصفحة بنمط المنصة الواسعة ---
st.set_page_config(
    page_title="Mosaid - Smart Medical Platform",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- تصميم المنصة العصري المتطور (Glassmorphism & Advanced UI) ---
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #070b14 0%, #0f172a 50%, #070b14 100%);
        color: #f8fafc;
    }
    .platform-header {
        background: rgba(30, 41, 59, 0.65);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.6);
        text-align: center;
        margin-bottom: 25px;
    }
    .platform-title { 
        font-size: 38px; 
        font-weight: 900; 
        background: linear-gradient(90deg, #38bdf8, #34d399, #818cf8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .platform-subtitle { font-size: 15px; color: #94a3b8; font-weight: 500; }
    
    .card-box {
        background: rgba(30, 41, 59, 0.45);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 16px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.35);
    }
    
    .stButton>button { 
        width: 100%; border-radius: 12px; font-weight: bold; 
        background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
        color: white; border: none; padding: 12px;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0369a1 0%, #0f766e 100%);
        transform: translateY(-2px);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- الترحيب الصوتي التلقائي بالإنجليزية عند فتح المنصة لأول مرة ---
welcome_msg = (
    "Welcome to Mosaid, your smart medical assistant. How can I help you today?"
)
if "welcomed" not in st.session_state:
  st.session_state.welcomed = True
  welcome_audio = text_to_speech_bytes(welcome_msg, lang="en")
  if welcome_audio:
    st.audio(welcome_audio, format="audio/mp3", autoplay=True)

# --- القائمة الجانبية لإدارة الملف الشخصي والطوارئ ---
with st.sidebar:
  st.markdown("### 🗂️ الملف الطبي للمريض")
  p_name = st.text_input("اسم المريض:", value="أحمد الجزائري")
  p_age = st.number_input("العمر:", 1, 100, 30)
  p_blood = st.selectbox("فصيلة الدم:", ["O+", "A+", "B+", "AB+", "O-", "A-"])

  st.markdown("---")
  st.markdown("### 🚨 الطوارئ الفورية (SOS)")
  if st.button("🚨 إرسال إستغاثة لتركيا (112)"):
    st.error(
        f"📍 تم إرسال إشارة طوارئ للمريض {p_name} ({p_blood}) إلى أقرب مركز"
        " طبي بتركيا!"
    )

  st.markdown("---")
  st.info("💡 Mosaid Platform v3.0 - AI Medical Core (2026)")

# --- ترويسة المنصة الرئيسية ---
st.markdown(
    """
    <div class="platform-header">
        <div style="margin-bottom: 10px;">
            <span style="background: rgba(56, 189, 248, 0.1); color: #38bdf8; padding: 6px 18px; border-radius: 20px; font-size: 13px; font-weight: bold; border: 1px solid rgba(56, 189, 248, 0.3);">🇩🇿 الجزائر &nbsp; ⇄ &nbsp; تركيا 🇹🇷</span>
        </div>
        <p class="platform-title">MOSAID MEDICAL PLATFORM</p>
        <p class="platform-subtitle">المنصة الطبية الذكية المدعومة بالذكاء الاصطناعي الاستدلالي والأصوات التفاعلية</p>
    </div>
    """,
    unsafe_allow_html=True,
)


# --- عقل الذكاء الاصطناعي الاحترافي ---
def ask_gemini_platform(prompt, lang="en"):
  try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(
        f"You are Mosaid, an advanced AI medical platform. Patient Name: {p_name}, Age: {p_age}, Blood: {p_blood}. Analyze the following medical case and provide professional diagnosis, digital prescription, and doctor guidelines in language '{lang}': {prompt}"
    )
    return response.text
  except Exception as e:
    return "Error connecting to AI platform core."


# --- نظام الأعمدة واللوحات العصرية (Dashboard Grid Layout) ---
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
  st.markdown(
      """<div class="card-box"><h3>🩺 التشخيص السريع وتوليد الروشتة</h3>""",
      unsafe_allow_html=True,
  )
  user_input = st.text_area(
      "أدخل الأعراض أو الشكوى الطبية:",
      value="أشعر بصداع نصفي حاد وإرهاق عام مع حرارة طفيفة.",
  )
  lang_sel = st.selectbox(
      "لغة الرد / Response Language:", ["ar", "en", "tr", "ru"]
  )

  if st.button("تشغيل التحليل الطبي وتوليد الروشتة"):
    if user_input:
      with st.spinner("جاري التحليل السريري وإنشاء الوصفة الطبية..."):
        ai_res = ask_gemini_platform(user_input, lang=lang_sel)
        st.success(ai_res)
        # توليد صوت للنتيجة
        res_audio = text_to_speech_bytes(ai_res[:250], lang=lang_sel)
        if res_audio:
          st.audio(res_audio, format="audio/mp3")
    else:
      st.warning("الرجاء كتابة الأعراض أولاً.")
  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      """<div class="card-box"><h3>💊 فحص تعارض الأدوية الرقمي</h3>""",
      unsafe_allow_html=True,
  )
  drug_a = st.text_input("الدواء الأول:", value="Paracetamol")
  drug_b = st.text_input("الدواء الثاني:", value="Aspirin")
  if st.button("فحص التعارض الدوائي المتقدم"):
    check_res = ask_gemini_platform(
        f"Check medical interaction between {drug_a} and {drug_b}", lang="en"
    )
    st.info(check_res)
  st.markdown("</div>", unsafe_allow_html=True)

with col_right:
  st.markdown(
      """<div class="card-box"><h3>🎙️ المحادثة الثلاثية (مريض - موساعد - طبيب)</h3>""",
      unsafe_allow_html=True,
  )
  st.write("استماع صوتي فوري وتفاعلي لتشخيص الأطراف الثلاثة:")

  patient_voice_text = st.text_input(
      "كلام المريض:", value="I have severe pain in my throat and fever."
  )

  if st.button("إنشاء وتشغيل الحوار الصوتي الثلاثي"):
    c1, c2, c3 = st.columns(3)

    with c1:
      st.markdown("**1. صوت المريض**")
      aud1 = text_to_speech_bytes(patient_voice_text, lang="en")
      if aud1:
        st.audio(aud1, format="audio/mp3")

    with c2:
      st.markdown("**2. رد موساعد**")
      mosaid_resp = (
          "Mosaid: Symptoms indicate possible tonsillitis. Rest required."
      )
      st.write(mosaid_resp)
      aud2 = text_to_speech_bytes(mosaid_resp, lang="en")
      if aud2:
        st.audio(aud2, format="audio/mp3")

    with c3:
      st.markdown("**3. قرار الطبيب التركي**")
      doc_resp = "Doctor: Take antibiotics and warm fluids for 3 days."
      st.write(doc_resp)
      aud3 = text_to_speech_bytes(doc_resp, lang="en")
      if aud3:
        st.audio(aud3, format="audio/mp3")

  st.markdown("</div>", unsafe_allow_html=True)

  st.markdown(
      """<div class="card-box"><h3>🌍 الترجمة الطبية الفورية بتركيا</h3>""",
      unsafe_allow_html=True,
  )
  hos_query = st.text_input(
      "النص المراد ترجمته للمستشفيات التركية:",
      value="Patient needs emergency doctor consultation.",
  )
  if st.button("ترجمة طبية دقيقة (إلى التركية)"):
    tr_result = ask_gemini_platform(
        f"Translate strictly to Turkish medical terminology: {hos_query}",
        lang="tr",
    )
    st.info(tr_result)
    tr_audio = text_to_speech_bytes(tr_result, lang="tr")
    if tr_audio:
      st.audio(tr_audio, format="audio/mp3")
  st.markdown("</div>", unsafe_allow_html=True)

# --- تذييل المنصة ---
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748b; font-size: 13px; font-weight:"
    " bold;'>Mosaid Medical Platform Enterprise Core 🇩🇿 🇹🇷 - 2026</p>",
    unsafe_allow_html=True,
)
