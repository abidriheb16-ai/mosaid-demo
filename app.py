import google.generativeai as genai
import streamlit as st

# إعداد مفتاح الذكاء الاصطناعي (تأكد من وضع مفتاحك الخاص)
# genai.configure(api_key="YOUR_API_KEY")

def analyze_patient_vocal_stress(symptom_text, transcribed_audio_context):
    """
    دالة لتحليل نبرة الكلام والمشاعر وتوليد مؤشر التوتر الطبي للطبيب التركي
    """
    prompt = f"""
    You are an advanced medical AI assistant integrated into 'Mosaid'. 
    Analyze the following patient's input (which was converted from voice):
    Patient Input: "{symptom_text}"
    Additional Audio Context/Tone notes: "{transcribed_audio_context}"
    
    Task:
    1. Estimate the patient's stress/pain urgency level (Low, Moderate, High/Critical).
    2. Provide a professional medical summary in Turkish for the doctor, highlighting potential emotional distress or hidden pain markers.
    3. Keep it concise and professional.
    """
    
    # استدعاء نموذج جيميني للتحليل
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text

# --- واجهة الاستخدام في Streamlit ---
st.subheader("🎙️ Mosaid: Vocal Biomarker & Stress Analysis")
st.write("محلل نبرة الصوت ومؤشر التوتر الطبي للمريض")

user_input = st.text_area("أدخل الأعراض أو الكلام المسجل صوتياً للمريض:")
audio_notes = st.selectbox("ملاحظات نبرة الصوت (كيف يبدو صوت المريض؟):", 
                           ["صوت هادئ وطبيعي", 
                            "صوت مرتبك ومتردد", 
                            "صوت يظهر عليه الألم الشديد والهلع", 
                            "صوت متقطع بسبب ضيق التنفس"])

if st.button("تحليل الحالة وإرسال التقرير للطبيب"):
    if user_input:
        with st.spinner("جاري تحليل نبرة الصوت والمؤشر الطبي..."):
            analysis_result = analyze_patient_vocal_stress(user_input, audio_notes)
            
            st.success("تم التحليل بنجاح!")
            st.markdown("### 📊 التقرير الطبي الموجه للطبيب التركي:")
            st.write(analysis_result)
    else:
            st.warning("الرجاء إدخال الأعراض أولاً.")
    
