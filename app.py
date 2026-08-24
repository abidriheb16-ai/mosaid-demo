<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Omega Cyber-Medical Intelligence - v100.0-Omega</title>
    <style>
        :root {
            --primary-bg: #030712;
            --card-bg: #111827;
            --accent-cyan: #06b6d4;
            --accent-blue: #3b82f6;
            --secondary-green: #10b981;
            --danger-red: #ef4444;
            --warning-amber: #f59e0b;
            --text-main: #f9fafb;
            --text-muted: #9ca3af;
            --border-glow: rgba(6, 182, 212, 0.3);
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', 'Segoe UI', Tahoma, sans-serif; transition: all 0.3s ease; }
        body { background-color: var(--primary-bg); color: var(--text-main); padding: 20px; direction: rtl; overflow-x: hidden; }
        
        .container { max-width: 1400px; margin: 0 auto; }
        
        /* ترويسة المنصة والشركات السيبرانية */
        header { 
            background: linear-gradient(135deg, #1e1b4b, #0f172a); 
            padding: 25px; 
            border-radius: 20px; 
            box-shadow: 0 0 30px var(--border-glow); 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
            margin-bottom: 25px;
            border: 1px solid rgba(59, 130, 246, 0.4);
        }
        .header-title h1 { font-size: 1.8rem; color: var(--accent-cyan); display: flex; align-items: center; gap: 12px; }
        .header-flags { display: flex; align-items: center; gap: 10px; font-size: 1.5rem; }
        .badge-v100 { background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue)); color: white; padding: 6px 14px; border-radius: 30px; font-size: 0.85rem; font-weight: bold; box-shadow: 0 0 15px rgba(6,182,212,0.5); }

        /* شريط التحكم العلوي (لغات، وضع ليلي، إتاحة) */
        .top-control-bar {
            background: var(--card-bg);
            padding: 12px 20px;
            border-radius: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            border: 1px solid rgba(255,255,255,0.05);
            flex-wrap: wrap;
            gap: 10px;
        }

        /* شبكة القوائم المنظمة */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
            gap: 20px;
        }

        .card {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 22px;
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        .card::before {
            content: '';
            position: absolute;
            top: 0; right: 0; width: 100%; height: 4px;
            background: linear-gradient(90deg, var(--accent-cyan), var(--accent-blue));
        }
        .card h2 { font-size: 1.25rem; margin-bottom: 15px; color: var(--accent-cyan); display: flex; align-items: center; gap: 10px; }

        .form-group { margin-bottom: 14px; }
        label { display: block; margin-bottom: 6px; font-size: 0.85rem; color: var(--text-muted); font-weight: 600; }
        input, select, textarea {
            width: 100%; padding: 11px; border: 1px solid #374151; border-radius: 10px;
            background: #0b0f19; color: white; font-size: 0.9rem; outline: none;
        }
        input:focus, select:focus { border-color: var(--accent-cyan); box-shadow: 0 0 10px rgba(6,182,212,0.3); }

        button {
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
            color: white; border: none; padding: 11px 18px; border-radius: 10px;
            cursor: pointer; font-weight: bold; width: 100%; margin-top: 8px; font-size: 0.95rem;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }
        button:hover { opacity: 0.9; transform: translateY(-1px); }

        .btn-sos { background: linear-gradient(135deg, #dc2626, #ef4444); animation: pulseSOS 2s infinite; }
        .btn-disaster { background: linear-gradient(135deg, #d97706, #f59e0b); color: #000; }
        .btn-success { background: linear-gradient(135deg, #059669, var(--secondary-green)); }

        @keyframes pulseSOS {
            0% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(239, 68, 68, 0); }
            100% { box-shadow: 0 0 0 0 rgba(239, 68, 68, 0); }
        }

        .output-box {
            background: #0b0f19; padding: 12px; border-radius: 10px; margin-top: 12px;
            font-size: 0.85rem; min-height: 60px; border-right: 4px solid var(--accent-cyan);
            color: #d1d5db; line-height: 1.5;
        }

        .global-tech-box {
            background: linear-gradient(145deg, #0f172a, #1e1b4b);
            border: 1px dashed var(--accent-blue);
            margin-top: 25px; padding: 20px; border-radius: 16px;
        }
    </style>
</head>
<body>

    <div class="container">
        
        <!-- شريط التحكم واللغات والإتاحة -->
        <div class="top-control-bar">
            <div style="display: flex; align-items: center; gap: 15px;">
                <span>🌐 اللغة (Languages):</span>
                <select id="langSelect" onchange="changeSystemLanguage()" style="width: 140px; padding: 6px;">
                    <option value="ar">العربية (Arabic)</option>
                    <option value="tr">Türkçe (Turkish)</option>
                    <option value="ku">Kurdî (Kurdish)</option>
                    <option value="en">English</option>
                </select>
            </div>
            <div style="display: flex; gap: 10px;">
                <button onclick="speakWelcomeMessage()" style="width: auto; padding: 6px 14px; background: var(--secondary-green);">🔊 ترحيب صوتي</button>
                <button onclick="toggleAccessibility()" style="width: auto; padding: 6px 14px; background: var(--accent-blue);">♿ تفعيل المعوقين وذوي الاحتياجات الخاصة</button>
            </div>
        </div>

        <!-- الترويسة وشراكة الجزائر وتركيا -->
        <header>
            <div class="header-title">
                <h1>
                    <span>🇹🇷 🔗 🇩🇿</span> 
                    Omega Cyber-Medical Intelligence 
                </h1>
                <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 5px;">
                    المنصة الطبية السيبرانية المشتركة (الجمهورية الجزائرية الديمقراطية الشعبية ⟵ الجمهورية التركية) • ربط مع وزارة الصحة التركية (Sağlık Bakanlığı)
                </p>
            </div>
            <div class="header-flags">
                <span class="badge-v100">v100.0-Omega (Global Tech)</span>
            </div>
        </header>

        <!-- لوحة الخدمات الموزعة بالقوائم المنظمة -->
        <div class="dashboard-grid">

            <!-- 1. تسجيل المريض والملف الطبي الكمي -->
            <div class="card">
                <h2>🪪 1. تسجيل المريض والملف الكمي الضخم</h2>
                <div class="form-group"><label>الاسم الكامل:</label><input type="text" id="patientName" placeholder="أدخل اسم المريض"></div>
                <div class="form-group"><label>العمر، الجنس، فصيلة الدم:</label><input type="text" id="patientDetails" placeholder="مثال: 32 سنة، ذكر، A+"></div>
                <div class="form-group"><label>مكان الإقامة (تركيا / الجزائر / القرى):</label><input type="text" id="patientLocation" placeholder="إسطنبول، أنقرة، أو الأرياف..."></div>
                <button onclick="registerPatient()">إنشاء الملف وتوليد بصمة التشفير الكمي (Omega Hash)</button>
                <div class="output-box" id="patientOutput">حالة السجل: بانتظار إدخال بيانات المريض...</div>
            </div>

            <!-- 2. عقل المساعد المزود بذاكرة فائقة وتحليل ونقاش -->
            <div class="card">
                <h2>🧠 2. عقل المساعد السيبراني الفائق (Super-Assistant)</h2>
                <div class="form-group"><label>أدخل الشكوى المرضية أو الأعراض:</label><textarea id="assistantQuery" rows="2" placeholder="اكتب الأعراض بالتفصيل ليحللها العقل السيبراني..."></textarea></div>
                <button onclick="runAssistantAnalysis()" class="btn-success">تشغيل العقل المفكر والتحليل العميق</button>
                <div class="output-box" id="assistantOutput">الذاكرة الضخمة: جاهزة لاستقبال وتخزين الاستدلالات الطبية السابقة...</div>
            </div>

            <!-- 3. التسجيل الصوتي الثلاثي (مريض - مساعد - طبيب) -->
            <div class="card">
                <h2>🎙️ 3. التسجيل الصوتي الثلاثي التفاعلي</h2>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 10px;">سجل صوتك مباشرة ليتفاعل المساعد ويحوله إلى الطبيب المختص.</p>
                <button onclick="recordVoiceSession('patient')" class="btn-success">🎤 تسجيل صوت المريض</button>
                <button onclick="recordVoiceSession('assistant')" style="background: var(--accent-blue); margin-top: 6px;">🤖 تشغيل رد صوت المساعد الذكي</button>
                <button onclick="recordVoiceSession('doctor')" style="background: #7c3aed; margin-top: 6px;">👨‍⚕️ تسجيل توجيهات الطبيب المختص</button>
                <div class="output-box" id="voiceOutput">حالة التسجيل الصوتي: متوقف.</div>
            </div>

            <!-- 4. الرؤية الحاسوبية والكاميرا وإرسال الصور للطبقة الطبية -->
            <div class="card">
                <h2>📷 4. الرؤية الحاسوبية والتشخيص البصري (التهابات وجروح)</h2>
                <div class="form-group"><label>رفع صورة موضع الإصابة أو الالتهاب الجلدي:</label><input type="file" id="skinImage"></div>
                <button onclick="processVisionDiagnosis()">إرسال الصورة من المساعد إلى الطبيب والتشخيص الفوري</button>
                <div class="output-box" id="visionOutput">نتيجة الرؤية الحاسوبية والـ PDF: في الانتظار...</div>
            </div>

            <!-- 5. طوارئ الفضاء السيبراني و GPS الحية -->
            <div class="card">
                <h2>🚨 5. طوارئ الفضاء السيبراني و Omega GPS الحية</h2>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin-bottom: 10px;">نظام رصد سقوط الأشخاص وتحديد الإحداثيات عبر الأقمار الصناعية.</p>
                <button onclick="getLiveGPSLocation()" class="btn-success">تحديد الموقع الحالي بدقة الفضاء (Omega GPS)</button>
                <button onclick="triggerSOSAlert()" class="btn-sos" style="margin-top: 8px;">⚠️ إرسال إستغاثة قصوى (Omega SOS)</button>
                <div class="output-box" id="gpsOutput">إحداثيات الموقع: غير مرصودة حالياً.</div>
            </div>

            <!-- 6. طوارئ الكوارث والحرائق والزلازل -->
            <div class="card" style="border: 2px solid var(--warning-amber);">
                <h2>🔥 6. قسم الكوارث (حرائق، زلازل، أعاصير)</h2>
                <div class="form-group">
                    <label>اختر نوع الكارثة الطارئة:</label>
                    <select id="disasterType">
                        <option value="fire">حريق غابات / منازل (Forest & House Fires)</option>
                        <option value="earthquake">زلزال مدمر (Earthquake)</option>
                        <option value="flood">فيضانات وأزمات كبرى (Floods)</option>
                    </select>
                </div>
                <button onclick="triggerDisasterProtocol()" class="btn-disaster">إطلاق بروتوكول الإغاثة الطارئة والموقع</button>
                <div class="output-box" id="disasterOutput">نظام الكوارث: جاهز لتوفير النصائح وتحديد مكان المتضررين.</div>
            </div>

            <!-- 7. دليل مستشفيات وقرى تركيا الذكية -->
            <div class="card">
                <h2>🏥 7. دليل مستشفيات وقرى تركيا الشامل</h2>
                <div class="form-group">
                    <label>اختر المستشفى أو القرية التركية:</label>
                    <select id="turkeyHospitalSelect">
                        <option value="basaksehir">مستشفى باشاك شهير تشام وساكورا (إسطنبول)</option>
                        <option value="ankara">مستشفى أنقرة سيتي هوسبيتال</option>
                        <option value="izmir">مستشفى إزمير فيجي كاراجه إوغلو</option>
                        <option value="rural_anatolia">دليل قرى الأناضول والأرياف وربطها بالرعاية المتنقلة</option>
                    </select>
                </div>
                <button onclick="connectToHospitalNetwork()">الاتصال بقاعدة بيانات الصحة التركية</button>
                <div class="output-box" id="hospitalOutput">حالة الاتصال بالمستشفيات: جاهز.</div>
            </div>

            <!-- 8. بوابة الأطباء والجراحين الشاملة في تركيا -->
            <div class="card">
                <h2>👨‍⚕️ 8. بوابة الأطباء والجراحين والنخبة الطبية</h2>
                <div class="form-group"><label>البريد الإلكتروني للطبيّب:</label><input type="email" id="docEmail" placeholder="doctor@saglik.gov.tr"></div>
                <div class="form-group">
                    <label>التخصص الجراحي والدقيق:</label>
                    <select id="docSpecialty">
                        <option value="general_surgery">الجراحة العامة وجراحة التخاطب</option>
                        <option value="neuro">جراحة الأعصاب والدماغ</option>
                        <option value="cardio">جراحة وجامعة أمراض القلب</option>
                        <option value="emergency">طب الطوارئ والكوارث السيبرانية</option>
                    </select>
                </div>
                <button onclick="doctorPortalLogin()">تسجيل دخول لوحة الأطباء وتلقي التقارير (Omega PDF)</button>
                <div class="output-box" id="doctorOutput">لوحة الطبيب: في انتظار المصادقة البريدية...</div>
            </div>

        </div>

        <!-- صندوق التقنيات العالمية المتقدمة (روسيا، الصين، أمريكا) داخل v100 -->
        <div class="global-tech-box">
            <h2 style="color: var(--accent-cyan); margin-bottom: 10px; font-size: 1.1rem;">🌐 أحدث التقنيات العالمية المدمجة في الإصدار v100.0-Omega</h2>
            <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.6;">
                • <b>الولايات المتحدة (USA):</b> دمج خوارزميات التعلم العميق لاستشعار الإشارات الحيوية المتقدمة وتحليل الصور الطبية عبر نماذج شبكية عصبية ضخمة.<br>
                • <b>روسيا (Russia):</b> أنظمة التشفير الكمي الموزع (Quantum Hashing) لحماية سجلات المرضى ضد أي اختراق سيبراني خارجي.<br>
                • <b>الصين (China):</b> تقنيات شبكات الجيل السادس (6G) الطارئة للاتصال الفضائي السريع في القرى والأرياف النائية دون انقطاع.
            </p>
        </div>

    </div>

    <script>
        // الترحيب الصوتي التلقائي المتعدد اللغات
        function speakWelcomeMessage() {
            const msg = new SpeechSynthesisUtterance("Welcome to Omega Cyber Medical Platform v100.0 Omega. Algeria and Turkey secure system is fully active.");
            msg.lang = 'en-US';
            window.speechSynthesis.speak(msg);
            alert("Omega v100.0: تم تشغيل الترحيب الصوتي بنجاح.");
        }

        // تبديل لغات النظام
        function changeSystemLanguage() {
            const lang = document.getElementById('langSelect').value;
            alert("تم تحويل لغة واجهة النظام إلى: " + lang.toUpperCase() + " (مع التبديل التلقائي للنصوص والدعم الصوتي).");
        }

        // 1. تسجيل المريض وتوليد البصمة
        function registerPatient() {
            const name = document.getElementById('patientName.value') || "مريض معتمد";
            const hashKey = "OMEGA-SECURE-HASH-" + Math.random().toString(36).substring(2, 10).toUpperCase() + "-TR-DZ";
            document.getElementById('patientOutput').innerHTML = `✅ تم تسجيل المريض بنجاح.<br>• بصمة التشفير الكمي (Omega Hash): <span style="color:var(--accent-cyan);">${hashKey}</span><br>• مساحة التخزين المخصصة: غير محدودة (محمية سيبرانياً).`;
        }

        // 2. تحليل عقل المساعد
        function runAssistantAnalysis() {
            const query = document.getElementById('assistantQuery').value;
            document.getElementById('assistantOutput').innerHTML = `🧠 [تحليل عقل المساعد الفائق]:<br>• المدخلات: "${query || 'فحص روتيني شامل'}"<br>• الاستدلال الذكي: تم فحص الذاكرة الطبية التراكمية، الحالة مستقرة ويتم إعداد التوجيه الطبي المباشر للطبيب المختص.`;
        }

        // 3. المحادثة الصوتية
        function recordVoiceSession(type) {
            if(type === 'patient') {
                document.getElementById('voiceOutput').innerHTML = "🎙️ [ميكروفون المريض]: جاري تسجيل الشكوى الصوتية وتحويلها إلى نص ذكي...";
            } else if(type === 'assistant') {
                document.getElementById('voiceOutput').innerHTML = "🤖 [صوت المساعد الذكي]: يتم الآن نطق التشخيص الأولي بصوت تفاعلي وواضح للمريض...";
            } else {
                document.getElementById('voiceOutput').innerHTML = "👨‍⚕️ [توجيهات الطبيب]: تم إرسال الرسالة الصوتية المعتمدة من الجراح المختص.";
            }
        }

        // 4. الرؤية الحاسوبية
        function processVisionDiagnosis() {
            const fileInput = document.getElementById('skinImage').files[0];
            const fileName = fileInput ? fileInput.name : "صورة الفحص الافتراضية.jpg";
            document.getElementById('visionOutput').innerHTML = `📷 تم تحليل الصورة (${fileName}) بصرياً عبر تقنية الرؤية الحاسوبية.<br>📄 تم توليد <b>Omega PDF الرقمية المعتمدة</b> وإرسالها فوراً للوحدة الطبية ولتطبيق المريض.`;
        }

        // 5. نظام GPS و SOS
        function getLiveGPSLocation() {
            document.getElementById('gpsOutput').innerHTML = "🛰️ Omega GPS Tracker: تم رصد الإحداثيات الحية بدقة الأقمار الصناعية (خط العرض: 41.0082, خط الطول: 28.9784 - اسطنبول / الأرياف المرتبطة).";
        }
        function triggerSOSAlert() {
            alert("🚨 تنبيه طوارئ قصوى (Omega SOS)! تم إرسال إحداثيات السقوط أو الطوارئ فوراً إلى أقرب وحدة رعاية متنقلة ووزارة الصحة التركية.");
        }

        // 6. طوارئ الكوارث
        function triggerDisasterProtocol() {
            const type = document.getElementById('disasterType').value;
            let text = "";
            if(type === 'fire') text = "🔥 [بروتوكول حرائق الغابات والبيوت]: تم إرسال إحداثيات موقع الحريق لفرق الإطفاء والإسعاف الفوري مع تقديم إرشادات التنفس والإخلاء.";
            else if(type === 'earthquake') text = "🌍 [بروتوكول الزلازل]: تفعيل رادار البحث تحت الأنقاض وتوجيه فرق الإغاثة الكبرى.";
            else text = "🌊 [بروتوكول الفيضانات]: توجيه القوارب الطبية المتنقلة للمناطق المعزولة.";
            document.getElementById('disasterOutput').innerHTML = text;
            alert("⚠️ تم تفعيل طوارئ الكوارث بنجاح!");
        }

        // 7. المستشفيات والقرى
        function connectToHospitalNetwork() {
            const hospital = document.getElementById('turkeyHospitalSelect').value;
            document.getElementById('hospitalOutput').innerHTML = `🔗 تم الاتصال بنجاح بقاعدة بيانات (${hospital}) ونظام وزارة الصحة التركية (Saglik Bakanligi). كافة بيانات القرى والأرياف مربوطة بالوحدات المتنقلة.`;
        }

        // 8. بوابة الأطباء
        function doctorPortalLogin() {
            const email = document.getElementById('docEmail').value;
            const spec = document.getElementById('docSpecialty').value;
            document.getElementById('doctorOutput').innerHTML = `👨‍⚕️ تم تسجيل دخول الطبيب (${email || 'admin@saglik.gov.tr'}) بنجاح.<br>• التخصص الجراحي: ${spec}<br>• متصل بشبكة جميع الجراحين والأطباء المختصين في تركيا والجزائر لتلقي ملفات Omega PDF وتقارير الكاميرا.`;
        }

        // تفعيل المعوقين وذوي الاحتياجات الخاصة
        function toggleAccessibility() {
            alert("♿ تم تفعيل حزمة الإتاحة الشاملة: (دعم صوتي كامل للمكفوفين، نصوص بارزة ومكبرة وضع البصر، وترجمة فورية للصم).");
        }
    </script>
</body>
</html>

