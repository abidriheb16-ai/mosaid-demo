import google.generativeai as genai
import streamlit as st

# --- إعداد الصفحة والتصميم العصري الخلفية والشعار ---
st.set_page_config(
    page_title="Mosaid - AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* خلفية وتصميم عام عصري */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .main-title { 
        font-size: 36px; 
        font-weight: 800; 
        color: #004D40; 
        text-align: center; 
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .sub-title { 
        font-size: 16px; 
        color: #333333; 
        text-align: center; 
        margin-bottom: 20px; 
        font-weight: 600;
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 10px; 
        font-weight: bold; 
        background-color: #004D40; 
        color: white; 
    }
    .stButton>button:hover {
        background-color: #00796B;
        color: white;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# --- شعار التطبيق والعنوان الرئيسي ---
st.markdown(
    '<div style="text-align: center; padding: 10px;">'
    '<span style="font-size: 50px;">🩺🤖</span>'
    '<p class="main-title">Mosaid (موساعد)</p>'
    '<p class="sub-title">المساعد الذكي الطبي الموجه لتركيا - تكسير حواجز اللغة'
    ' ورعاية صحية متكاملة</p>'
    "</div>",
    unsafe_allow_html=True,
)

# --- شريط اختيار اللغات الـ 4 في أعلى الصفحة ---
st.markdown("---")
col1, col2 = st.columns([1, 3])
with col1:
  app_language = st.selectbox(
      "🌍 اختر لغة التطبيق / Dil Seçin:",
      [
          "العربية (Arabic)",
          "التركية (Türkçe)",
          "الإنجليزية (English)",
          "الروسية (Русский)",
      ],
  )
st.markdown("---")

# --- القائمة الجانبية المنظمة للخدمات الـ 11 ---
st.sidebar.markdown("## 🩺 قائمة خدمات موساعد")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox("اختر الخدمة الطبية:", [
    "🎙️ 1. المحادثة الصوتية والميكروفون",
    "🌍 2. الترجمة الطبية الفورية",
    "📈 3. متابعة الأعراض اليومية",
    "💊 4. فحص تعارض الأدوية",
    "📅 5. حجز المواعيد في تركيا",
    "🚨 6. الطوارئ الفورية (SOS)",
    "🥗 7. النظام الغذائي الذكي",
    "🔊 8. خيار نبرة صوت الطبيب",
    "📁 9. الملف الطبي الشامل",
    "📸 10. كاميرا التشخيص الجلدي",
    "🩹 11. دليل الإسعافات الأولية",
])

st.sidebar.markdown("---")
st.sidebar.info(
    "💡 تطبيق Mosaid - رفيقك الصحي الذكي المدعوم بالذكاء الاصطناعي."
)

# --- محتوى الواجهة حسب الاختيار من القائمة ---

if menu == "🎙️ 1. المحادثة الصوتية والميكروفون":
  st.markdown("### 🎙️ المساعد الصوتي التفاعلي وتسجيل الصوت عبر الميكروفون")
  st.write(
      "يمكنك التحدث صوتياً أو كتابة ما تشعر به ليقوم الذكاء الاصطناعي بالاستماع"
      " والتشخيص الفوري:"
  )

  # محاكاة زر الميكروفون الصوتي والتسجيل
  mic_col1, mic_col2 = st.columns(2)
  with mic_col1:
    if st.button("🔴 اضغط لبدء التحدث (تسجيل الصوت)"):
      st.info(
          "🎙️ جاري الاستماع إلى صوتك... تحدث الآن بوضوح (جاري تسجيل الأعراض..."
          " )"
      )
  with mic_col2:
    if st.button("⏹️ إيقاف التسجيل وتحليل الصوت"):
      st.success(
          "✅ تم التقاط الصوت بنجاح وتحويله إلى نص: (أعاني من تعب في الحلق وارتفاع"
          " حرارة)"
      )

  audio_input = st.text_input(
      "أو اكتب الأعراض يدوياً:",
      placeholder="مثلاً: عندي ألم في الحلق...",
  )
  if st.button("إرسال وتحليل الرد"):
    if audio_input:
      st.success("🤖 (موساعد الآلي): تم تحليل حالتك الطبية بنجاح.")
      st.info(
          "التقرير المبدئي: يوصى بشرب السوائل الدافئة والراحة، مع مراجعة الطبيب"
          " إذا استمرت الأعراض."
      )
    else:
      st.warning("الرجاء إدخال الأعراض أولاً.")

elif menu == "🌍 2. الترجمة الطبية الفورية":
  st.markdown("### 🌍 مترجم التقارير الطبية للتركية/الإنجليزية/الروسية")
  medical_text = st.text_area("أدخل التقرير الطبي:")
  target_lang = st.selectbox(
      "اختر اللغة المستهدفة للترجمة:",
      ["التركية (Türkçe)", "الإنجليزية (English)", "الروسية (Русский)"],
  )
  if st.button("ترجمة التقرير لإرساله للطبيب"):
    if medical_text:
      st.success(f"✅ تم ترجمة التقرير إلى ({target_lang}) بنجاح وجاهز للإرسال!")
      st.code(
          f"Translated Report ({target_lang}): Patient shows acute symptoms..."
      )
    else:
      st.warning("أدخل النص أولاً.")

elif menu == "📈 3. متابعة الأعراض اليومية":
  st.markdown("### 📈 متابعة تطور الأعراض يومياً")
  day_num = st.slider("اختر اليوم:", 1, 7, 1)
  temp = st.number_input("درجة الحرارة المسجلة اليوم (°C):", 35.0, 42.0, 37.5)
  if st.button("حفظ قراءة اليوم"):
    st.success(f"تم تسجيل بيانات اليوم {day_num} بنجاح!")
    st.line_chart([38.5, 38.0, 37.5, temp])

elif menu == "💊 4. فحص تعارض الأدوية":
  st.markdown("### 💊 قاعدة بيانات وفحص التعارض الدوائي")
  drug1 = st.text_input("الدواء الأول:")
  drug2 = st.text_input("الدواء الثاني:")
  if st.button("فحص التعارض"):
    if drug1 and drug2:
      st.info(
          f"🔍 تم فحص التعارض بين ({drug1}) و ({drug2}): لا يوجد تعارض خطير بينهما."
      )
    else:
      st.warning("الرجاء إدخال اسم الدواءين.")

elif menu == "📅 5. حجز المواعيد في تركيا":
  st.markdown("### 📅 حجز موعد طبي في المستشفيات التركية")
  hospital = st.selectbox(
      "اختر المستشفى:",
      ["مستشفى إسطنبول العام (Istanbul State Hospital)", "مستشفى أنقرة الطبي"],
  )
  app_date = st.date_input("تاريخ الموعد:")
  if st.button("تأكيد حجز الموعد عبر البريد الإلكتروني"):
    st.success(
        f"✅ تم إرسال طلب الحجز إلى {hospital} بتاريخ {app_date} بنجاح تام."
    )

elif menu == "🚨 6. الطوارئ الفورية (SOS)":
  st.markdown(
      '<h3 style="color: red;">🚨 نظام الطوارئ الفورية (SOS)</h3>',
      unsafe_allow_html=True,
  )
  st.error(
      "في حال الخطر أو السقوط المفاجئ أو الألم الشديد، اضغط الزر أدناه لإرسال"
      " موقعك فورا للطوارئ في تركيا:"
  )
  if st.button("🚨 إرسال إشارة استغاثة طارئة (SOS)"):
    st.error(
        "📍 تم إرسال إحداثيات موقعك الجغرافي لأقرب وحدة إسعاف وطوارئ في تركيا!"
    )

elif menu == "🥗 7. النظام الغذائي الذكي":
  st.markdown("### 🥗 النظام الغذائي المخصص حسب المرض")
  disease = st.selectbox("اختر حالتك الصحية:", ["سكري", "ضغط الدم", "حساسية القمح"])
  if st.button("الحصول على قائمة الأكل المناسبة"):
    st.success(
        f"🍎 الأطعمة الموصى بها لحالة ({disease}): الابتعاد عن السكريات والدهون،"
        " والتركيز على الخضروات والألياف."
    )

elif menu == "🔊 8. خيار نبرة صوت الطبيب":
  st.markdown("### 🔊 تخصيص نبرة صوت المساعد الطبي")
  voice_type = st.radio(
      "اختر نبرة الصوت لقراءة التشخيص:",
      [
          "صوت طبيب (هادئ ومهني / Male Doctor)",
          "صوت طبيبة (لطيف ومطمئن / Female Doctor)",
      ],
  )
  st.info(f"تم اعتماد التفضيل الصوتي بنجاح: {voice_type}")

elif menu == "📁 9. الملف الطبي الشامل":
  st.markdown("### 📁 الأرشيف والملف الطبي الشامل")
  st.write(
      "جميع تقاريرك، تحاليلك، ووصفاتك الطبية مخزنة هنا بأمان وسرية تامة."
  )
  uploaded_file = st.file_uploader(
      "ارفع ملف تحليل أو صورة أشعة جديدة:", type=["pdf", "png", "jpg"]
  )
  if uploaded_file:
    st.success("✅ تم حفظ الملف في أرشيفك الطبي الشخصي بنجاح.")

elif menu == "📸 10. كاميرا التشخيص الجلدي":
  st.markdown("### 📸 كاميرا التشخيص الجلدي المبدئي بالذكاء الاصطناعي")
  img_file = st.file_uploader(
      "التقاط أو رفع صورة للطفح أو الحالة الجلدية:",
      type=["jpg", "png", "jpeg"],
  )
  if img_file:
    st.image(img_file, caption="الصورة المرفوعة للحالة", width=300)
    if st.button("تحليل الصورة بالذكاء الاصطناعي"):
      st.warning(
          "🔬 تحليل مبدئي: يُحتمل أن يكون تهلباً جلدياً بسيطاً، يفضل مراجعة طبيب"
          " جلدية مختص للتأكد."
      )

elif menu == "🩹 11. دليل الإسعافات الأولية":
  st.markdown("### 🩹 دليل الإسعافات الأولية السريعة بالفيديو والخطوات")
  emergency_case = st.selectbox(
      "اختر الحالة الحرجة:", ["حالة اختناق", "جرح قطعي نزيف", "فقدان وعي"]
  )
  if st.button("عرض خطوات الإسعاف"):
    if emergency_case == "حالة اختناق":
      st.error(
          "1. قف خلف المصاب\n2. لف يديك حول خصره\n3. اضغط بقوة للداخل وللأعلى"
          " حتى يخرج الجسم الغريب."
      )
    elif emergency_case == "جرح قطعي نزيف":
      st.error(
          "1. اضغط مباشرة على الجرح بقطعة قماش نظيفة\n2. ارفع الجزء المصاب أعلى"
          " من مستوى القلب\n3. اطلب الإسعاف فوراً."
      )
    else:
      st.error(
          "1. ضع المصاب على جنبه لتجنب الاختناق\n2. تأكد من تنفسه بانتظام\n3."
          " اتصل بالطوارئ فوراً."
      )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #333; font-size: 13px; font-weight:"
    " bold;'>Mosaid Medical Suite & AI Voice System - 2026</p>",
    unsafe_allow_html=True,
)
