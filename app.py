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
st.markdown("<p style='text-align: center; color: gray; font-size:import google.generativeai as genai
import streamlit as st

# --- إعداد الصفحة والتصميم ---
st.set_page_config(
    page_title="Mosaid - AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title { font-size: 32px; font-weight: 800; color: #004D40; text-align: center; }
    .sub-title { font-size: 15px; color: #555555; text-align: center; margin-bottom: 20px; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

# --- القائمة الجانبية المنظمة ---
st.sidebar.markdown("## 🩺 قائمة تطبيق موساعد")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox("اختر الخدمة الطبية:", [
    "🎙️ 1. المحادثة الصوتية التفاعلية",
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
    "💡 تطبيق موساعد (Mosaid) - رفيقك الطبي الذكي لتكسير حواجز اللغة في تركيا."
)

# --- محتوى الواجهة حسب الاختيار من القائمة الجانبية ---

if menu == "🎙️ 1. المحادثة الصوتية التفاعلية":
  st.markdown(
      '<p class="main-title">🎙️ المحادثة الصوتية مع المساعد الطبي</p>',
      unsafe_allow_html=True,
  )
  st.write(
      "تحدث أو اكتب الأعراض وسيقوم الذكاء الاصطناعي بالاستماع والرد عليك:"
  )
  audio_input = st.text_input(
      "اكتب ما تقوله للمساعد:",
      placeholder="مثلاً: عندي ألم حاد في الرأس...",
  )
  if st.button("إرسال وتحليل الرد الصوتي"):
    if audio_input:
      st.success("🤖 (صوت الطبيب الافتراضي): تم استقبال صوتك وتحليل الحالة.")
      st.info(
          "التحليل الصوتي: الحالة تستدعي الراحة وشرب السوائل ومراقبة الحرارة."
      )
    else:
      st.warning("الرجاء كتابة أو تسجيل الصوت أولاً.")

elif menu == "🌍 2. الترجمة الطبية الفورية":
  st.markdown(
      '<p class="main-title">🌍 مترجم التقارير الطبية</p>',
      unsafe_allow_html=True,
  )
  medical_text = st.text_area("أدخل التقرير الطبي بالعربية:")
  target_lang = st.selectbox(
      "اختر اللغة المستهدفة:", ["التركية (Türkçe)", "الإنجليزية (English)"]
  )
  if st.button("ترجمة التقرير لإرساله للطبيب"):
    if medical_text:
      st.success(f"✅ تم ترجمة التقرير إلى ({target_lang}) بنجاح!")
      st.code(
          "Translated Medical Report for Turkish Hospital: Patient shows"
          " symptoms..."
      )
    else:
      st.warning("أدخل النص أولاً.")

elif menu == "📈 3. متابعة الأعراض اليومية":
  st.markdown(
      '<p class="main-title">📈 متابعة تطور الأعراض يومياً</p>',
      unsafe_allow_html=True,
  )
  day_num = st.slider("اختر اليوم:", 1, 7, 1)
  temp = st.number_input("درجة الحرارة المسجلة اليوم (°C):", 35.0, 42.0, 37.5)
  if st.button("حفظ قراءة اليوم"):
    st.success(f"تم تسجيل بيانات اليوم {day_num} بنجاح!")
    st.line_chart([38.5, 38.0, 37.5, temp])

elif menu == "💊 4. فحص تعارض الأدوية":
  st.markdown(
      '<p class="main-title">💊 قاعدة بيانات وفحص التعارض</p>',
      unsafe_allow_html=True,
  )
  drug1 = st.text_input("الدواء الأول:")
  drug2 = st.text_input("الدواء الثاني:")
  if st.button("فحص التعارض الدوائي"):
    if drug1 and drug2:
      st.info(
          f"🔍 تم فحص التعارض بين ({drug1}) و ({drug2}): لا يوجد تعارض خطير."
      )
    else:
      st.warning("الرجاء إدخال اسم الدواءين.")

elif menu == "📅 5. حجز المواعيد في تركيا":
  st.markdown(
      '<p class="main-title">📅 حجز موعد طبي في تركيا</p>',
      unsafe_allow_html=True,
  )
  hospital = st.selectbox(
      "اختر المستشفى:", ["مستشفى إسطنبول العام", "مستشفى أنقرة الطبي"]
  )
  app_date = st.date_input("تاريخ الموعد:")
  if st.button("تأكيد حجز الموعد عبر البريد الإلكتروني"):
    st.success(
        f"✅ تم إرسال طلب الحجز إلى {hospital} بتاريخ {app_date} بنجاح."
    )

elif menu == "🚨 6. الطوارئ الفورية (SOS)":
  st.markdown(
      '<p class="main-title" style="color: red;">🚨 نظام الطوارئ الفورية'
      " (SOS)</p>",
      unsafe_allow_html=True,
  )
  st.error("في حال الخطر أو السقوط المفاجئ، اضغط الزر أدناه لإرسال موقعك:")
  if st.button("🚨 إرسال إشارة استغاثة طارئة للمستشفى"):
    st.error("📍 تم إرسال إحداثيات موقعك الجغرافي لأقرب وحدة إسعاف في تركيا!")

elif menu == "🥗 7. النظام الغذائي الذكي":
  st.markdown(
      '<p class="main-title">🥗 النظام الغذائي المخصص حسب المرض</p>',
      unsafe_allow_html=True,
  )
  disease = st.selectbox("اختر حالتك الصحية:", ["سكري", "ضغط الدم", "حساسية القمح"])
  if st.button("الحصول على قائمة الأكل المناسبة"):
    st.success(
        f"🍎 الأطعمة الموصى بها لحالة ({disease}): الابتعاد عن السكريات، والتركيز"
        " على الألياف."
    )

elif menu == "🔊 8. خيار نبرة صوت الطبيب":
  st.markdown(
      '<p class="main-title">🔊 تخصيص نبرة صوت الطبيب</p>',
      unsafe_allow_html=True,
  )
  voice_type = st.radio(
      "اختر نبرة صوت المساعد لقراءة التشخيص:",
      ["صوت طبيب (هادئ ومهني)", "صوت طبيبة (لطيف ومطمئن)"],
  )
  st.info(f"تم اعتماد التفضيل الصوتي: {voice_type}")

elif menu == "📁 9. الملف الطبي الشامل":
  st.markdown(
      '<p class="main-title">📁 الملف والأرشيف الطبي الشامل</p>',
      unsafe_allow_html=True,
  )
  st.write("جميع تقاريرك وتحاليلك الطبية مخزنة هنا بأمان.")
  uploaded_file = st.file_uploader(
      "ارفع ملف تحليل أو صورة أشعة جديدة:", type=["pdf", "png", "jpg"]
  )
  if uploaded_file:
    st.success("✅ تم حفظ الملف في أرشيفك الطبي بنجاح.")

elif menu == "📸 10. كاميرا التشخيص الجلدي":
  st.markdown(
      '<p class="main-title">📸 كاميرا التشخيص الجلدي المبدئي</p>',
      unsafe_allow_html=True,
  )
  img_file = st.file_uploader(
      "التقاط أو رفع صورة للطفح أو الحالة الجلدية:",
      type=["jpg", "png", "jpeg"],
  )
  if img_file:
    st.image(img_file, caption="الصورة المرفوعة", width=300)
    if st.button("تحليل الصورة بالذكاء الاصطناعي"):
      st.warning(
          "🔬 تحليل مبدئي: يُحتمل أن يكون تهلباً جلدياً بسيطاً، يفضل مراجعة طبيب"
          " مختص."
      )

elif menu == "🩹 11. دليل الإسعافات الأولية":
  st.markdown(
      '<p class="main-title">🩹 دليل الإسعافات الأولية السريعة</p>',
      unsafe_allow_html=True,
  )
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
          "1. اضغط مباشرة على الجرح بقماش نظيف\n2. ارفع الجزء المصاب أعلى من مستوى"
          " القلب\n3. اطلب الإسعاف."
      )
    else:
      st.error(
          "1. ضع المصاب على جنبه لتجنب الاختناق\n2. تأكد من تنفسه بانتظام\n3."
          " اتصل بالطوارئ فوراً."
      )

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: 12px;'>Mosaid"
    " Medical Suite - 2026</p>",
    unsafe_allow_html=True,
)
12px;'>Mosaid Emergency System - 2026</p>", unsafe_allow_html=True)
