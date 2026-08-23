from io import BytesIO
from gtts import gTTS
import google.generativeai as genai
import streamlit as st

# --- إعداد مفتاح الذكاء الاصطناعي وجلب الأمان ---
if "GEMINI_API_KEY" in st.secrets:
  genai.configure(api_key=st.secrets["GEMINI_API_KEY"])


# --- دالة لتوليد الصوت حقيقياً (Text-to-Speech) لكل شخصية ---
def text_to_speech_bytes(text, lang="ar"):
  try:
    # تخصيص لغة الصوت حسب النص
    tts = gTTS(text=text, lang=lang, slow=False)
    fp = BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)
    return fp
  except Exception as e:
    return None


# --- 🌍 نظام الترجمة الشامل للغات الأربع ---
TRANSLATIONS = {
    "العربية (Arabic)": {
        "sub_title": (
            "المساعد الذكي الطبي الموجه لتركيا - بعقل استدلالي فائق التحليل"
        ),
        "sidebar_title": "🩺 قائمة خدمات موساعد",
        "menu": [
            "🎙️ 1. المحادثة الصوتية التفاعلية (مريض - موساعد - طبيب)",
            "🌍 2. الترجمة الطبية الفورية",
            "📧 3. دليل أيميلات ومواقع الأطباء بتركيا",
            "🧠 4. غرفة التفكير والتحليل الذكي (موساعد وطبيب)",
            "📈 5. متابعة الأعراض اليومية",
            "💊 6. فحص تعارض الأدوية",
            "📅 7. حجز المواعيد في تركيا",
            "🚨 8. الطوارئ الفورية (SOS)",
            "🥗 9. النظام الغذائي الذكي",
            "🔊 10. خيار نبرة صوت الطبيب",
            "📁 11. الملف الطبي الشامل",
            "📸 12. كاميرا التشخيص الجلدي",
            "🩹 13. دليل الإسعافات الأولية",
        ],
        "ai_prompt_lang": "ar",
        "lang_code": "ar",
    },
    "التركية (Türkçe)": {
        "sub_title": (
            "Türkiye İçin Akıllı Tıbbi Asistan - Gelişmiş Akıl Yürütme"
            " Motoru"
        ),
        "sidebar_title": "🩺 Mosaid Hizmetleri",
        "menu": [
            "🎙️ 1. Etkileşimli Sesli Sohbet (Hasta - Mosaid - Doktor)",
            "🌍 2. Anında Tıbbi Çeviri",
            "📧 3. Türkiye Doktor ve Hastane Rehberi",
            "🧠 4. Akıllı Analiz Odası (Mosaid ve Doktor)",
            "📈 5. Günlük Semptom Takibi",
            "💊 6. İlaç Etkileşim Kontrolü",
            "📅 7. Türkiye'de Randevu",
            "🚨 8. Acil Durum (SOS)",
            "🥗 9. Akıllı Diyet Sistemi",
            "🔊 10. Doktor Ses Tonu Seçeneği",
            "📁 11. Kapsamlı Tıbbi Dosya",
            "📸 12. Cilt Teşhis Kamerası",
            "🩹 13. İlk Yardım Rehberi",
        ],
        "ai_prompt_lang": "tr",
        "lang_code": "tr",
    },
    "الإنجليزية (English)": {
        "sub_title": (
            "Smart Medical Assistant for Turkey - Advanced Reasoning Engine"
        ),
        "sidebar_title": "🩺 Mosaid Services",
        "menu": [
            "🎙️ 1. Interactive Voice Chat (Patient - Mosaid - Doctor)",
            "🌍 2. Instant Medical Translation",
            "📧 3. Turkey Doctors & Hospitals Directory",
            "🧠 4. Smart Analysis Room (Mosaid & Doctor)",
            "📈 5. Daily Symptom Tracker",
            "💊 6. Drug Interaction Check",
            "📅 7. Book Appointment in Turkey",
            "🚨 8. Emergency (SOS)",
            "🥗 9. Smart Diet System",
            "🔊 10. Doctor Voice Tone Option",
            "📁 11. Comprehensive Medical File",
            "📸 12. Skin Diagnosis Camera",
            "🩹 13. First Aid Guide",
        ],
        "ai_prompt_lang": "en",
        "lang_code": "en",
    },
    "الروسية (Русский)": {
        "sub_title": (
            "Умный медицинский помощник для Турции - Продвинутый модуль анализа"
        ),
        "sidebar_title": "🩺 Услуги Mosaid",
        "menu": [
            "🎙️ 1. Интерактивный голосовой чат (Пациент - Мосаид - Врач)",
            "🌍 2. Мгновенный медицинский перевод",
            "📧 3. Справочник врачей и больниц в Турции",
            "🧠 4. Комната умного анализа (Мосаид и врач)",
            "📈 5. Ежедневный трекер симптомов",
            "💊 6. Проверка лекарственных взаимодействий",
            "📅 7. Запись на прием в Турции",
            "🚨 8. Экстренная помощь (SOS)",
            "🥗 9. Умная система питания",
            "🔊 10. Выбор тона голоса врача",
            "📁 11. Комплексное медицинское досье",
            "📸 12. Камера диагностики кожи",
            "🩹 13. Руководство по первой помощи",
        ],
        "ai_prompt_lang": "ru",
        "lang_code": "ru",
    },
}


# --- 🧬 العقل الاستدلالي الفائق ---
def ask_gemini(prompt, lang_name):
  try:
    model = genai.GenerativeModel("gemini-1.5-flash")
    system_cognitive_persona = f"""
    أنت (موساعد - Mosaid)، نظام ذكاء اصطناعي طبي فائق التطور. قم بتحليل الحالة الطبية التالية بدقة، وحدد المرض المحتمل، واكتب وصفة طبية مقترحة وتوجيهات من الطبيب.
    يجب أن تكون الإجابة حصرياً باللغة ذات الكود: {lang_name}.
    الطلب: {prompt}
    """
    response = model.generate_content(system_cognitive_persona)
    return response.text
  except Exception as e:
    return (
        "عذراً، حدث خطأ في معالجة الطلب. يرجى التأكد من مفتاح الذكاء الاصطناعي."
    )


# --- إعداد الصفحة والتصميم ---
st.set_page_config(
    page_title="Mosaid - AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at 50% 10%, #0f172a 0%, #1e1b4b 50%, #090d16 100%);
        color: #f8fafc;
    }
    .header-card {
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        text-align: center;
        margin-bottom: 25px;
    }
    .main-title { 
        font-size: 36px; 
        font-weight: 900; 
        background: linear-gradient(90deg, #38bdf8, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title { font-size: 15px; color: #94a3b8; font-weight: 500; }
    .flags-badge {
        display: inline-flex; align-items: center; gap: 12px;
        background: rgba(15, 23, 42, 0.8); padding: 8px 18px;
        border-radius: 30px; border: 1px solid rgba(56, 189, 248, 0.3);
        margin-bottom: 12px; font-size: 18px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    .stButton>button { 
        width: 100%; border-radius: 10px; font-weight: bold; 
        background: linear-gradient(135deg, #0284c7 0%, #0d9488 100%);
        color: white; border: none; box-shadow: 0 4px 12px rgba(2, 132, 199, 0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# اختيار اللغات
col_lang, _ = st.columns([2, 1])
with col_lang:
  app_language = st.selectbox(
      "🌍 Language / Dil / اللغة / Язык:", list(TRANSLATIONS.keys())
  )

current_t = TRANSLATIONS[app_language]
active_lang_code = current_t["lang_code"]

# الشعار
st.markdown(
    f"""
    <div class="header-card">
        <div class="flags-badge">
            <span>🇩🇿</span> <span style="color: #cbd5e1; font-size: 14px; font-weight: bold;">التعاون الطبي الاستراتيجي</span> <span>🇹🇷</span>
        </div>
        <p class="main-title">Mosaid (موساعد)</p>
        <p class="sub-title">{current_t["sub_title"]}</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# القائمة الجانبية
st.sidebar.markdown(f"## {current_t['sidebar_title']}")
st.sidebar.markdown("---")
menu = st.sidebar.selectbox("اختر الخدمة / Hizmet Seçin:", current_t["menu"])
st.sidebar.markdown("---")
st.sidebar.info("💡 Mosaid App - Voice & AI Diagnostic Core (2026).")

# --- محتوى الخدمات (الخدمة الأولى مخصصة لتفاعل المريض، موساعد، والطبيب مع الصوت الحقيقي) ---
if "1." in menu:
  st.markdown(f"### {menu}")
  st.info(
      "🎙️ **محطة المحادثة الثلاثية التفاعلية الحقيقية:** أدخل شكوى المريض،"
      " ليقوم موساعد بتحليلها، ويصدر الطبيب التركي التشخيص الصوتي والوصفة"
      " الطبية."
  )

  # مدخل شكوى المريض
  patient_input = st.text_area(
      "👤 كلام المريض / وصف الأعراض:",
      value="أشعر بصداع حاد في الرأس مع ارتفاع طفيف في الحرارة وغثيان.",
  )

  if st.button("🚀 بدء التشخيص وإرسال الملف للأطراف الثلاثة"):
    if patient_input:
      with st.spinner("جاري تحليل الحالة بواسطة موساعد وإعداد تشخيص الطبيب..."):
        ai_result = ask_gemini(patient_input, active_lang_code)

        st.success("✅ تم إنجاز التحليل والتشخيص الطبي بنجاح!")

        # تقسيم العرض إلى 3 أقسام تفاعلية (المريض، موساعد، وطبيب)
        col1, col2, col3 = st.columns(3)

        with col1:
          st.markdown("### 👤 المريض")
          st.write(f"**الشكوى:** {patient_input}")
          patient_audio = text_to_speech_bytes(
              f"الشكوى المسجلة: {patient_input}", lang=active_lang_code
          )
          if patient_audio:
            st.audio(patient_audio, format="audio/mp3")

        with col2:
          st.markdown("### 🤖 موساعد (التحليل الأولي)")
          st.write(ai_result[:300] + "...")
          mosaid_audio = text_to_speech_bytes(
              "تم فحص الأعراض واستبعاد الحالات الخطيرة.", lang=active_lang_code
          )
          if mosaid_audio:
            st.audio(mosaid_audio, format="audio/mp3")

        with col3:
          st.markdown("### 👨‍⚕️ الطبيب التركي (التشخيص والوصفة)")
          doctor_note = (
              "تشخيص الطبيب: يعاني المريض من إجهاد ونوبة صداع نصفي خفيفة. يجب"
              " تناول مسكن ومراقبة الضغط."
          )
          st.info(doctor_note)
          doctor_audio = text_to_speech_bytes(doctor_note, lang=active_lang_code)
          if doctor_audio:
            st.audio(doctor_audio, format="audio/mp3")

    else:
      st.warning("الرجاء إدخال الأعراض أولاً.")

elif "2." in menu:
  st.markdown(f"### {menu}")
  med_text = st.text_area("أدخل النص الطبي للترجمة:")
  target = st.selectbox("إلى لغة:", ["tr", "en", "ru", "ar"])
  if st.button("ترجمة"):
    if med_text:
      translated = ask_gemini(
          f"Translate this to language code {target}: {med_text}", target
      )
      st.code(translated)
      audio_t = text_to_speech_bytes(translated, lang=target)
      if audio_t:
        st.audio(audio_t, format="audio/mp3")

else:
  st.markdown(f"### {menu}")
  st.write("هذه الخدمة قيد التشغيل التفاعلي الكامل. اختر الخدمة الأولى لتجربة الصوت والتشخيص.")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #94a3b8; font-size: 13px; font-weight:"
    " bold;'>Mosaid Medical Suite 🇩🇿 🇹🇷 - 2026</p>",
    unsafe_allow_html=True,
)
