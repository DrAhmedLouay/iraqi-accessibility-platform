# -*- coding: utf-8 -*-
"""
grand_components.py
Contains HTML and JS definitions for the 5 grand modules.
"""

def generate_gis_section():
    return '''      <!-- NATIONAL GIS ACCESSIBILITY & GOVERNORATES SURVEILLANCE -->
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="flex flex-wrap justify-between items-center gap-3 border-b border-slate-200 dark:border-slate-800 pb-4 mb-5">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xl">🗺️</span>
              <h3 class="text-base sm:text-lg font-black text-slate-900 dark:text-slate-100">الخارطة الجغرافية الوطنية التفاعلية لمباني العراق (GIS Accessibility Map)</h3>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">رصد ميداني لنسب الجاهزية والامتثال عبر محافظات جمهورية العراق الـ 18 وفق الخطة الوطنية (2026-2029).</p>
          </div>
          <!-- Regional Filter Buttons -->
          <div class="flex flex-wrap gap-1 text-xs">
            <button onclick="filterGovRegion('all')" id="btn-reg-all" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold transition">كل المحافظات (18)</button>
            <button onclick="filterGovRegion('center')" id="btn-reg-center" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">بغداد والوسط</button>
            <button onclick="filterGovRegion('south')" id="btn-reg-south" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الجنوب</button>
            <button onclick="filterGovRegion('north')" id="btn-reg-north" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الشمال وكردستان</button>
            <button onclick="filterGovRegion('west')" id="btn-reg-west" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الأنبار وغرب العراق</button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Interactive GIS Map Graphic (SVG) -->
          <div class="lg:col-span-7 bg-slate-950 rounded-2xl p-4 border border-slate-800 flex flex-col items-center justify-center relative overflow-hidden">
            <div class="w-full flex justify-between items-center text-xs text-slate-400 mb-2">
              <span class="font-bold text-slate-300">انقر على المحافظة لعرض سجلات الامتثال:</span>
              <span id="gis-selected-gov" class="text-emerald-400 font-black">المحافظة المختارة: بغداد (العاصمة)</span>
            </div>

            <!-- SVG Map of Iraq with Interactive Governorates -->
            <svg id="iraq-gis-svg" viewBox="0 0 500 480" class="w-full h-80 max-w-md">
              <defs>
                <linearGradient id="gov-grad-gold" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#059669" />
                  <stop offset="100%" stop-color="#10b981" />
                </linearGradient>
                <linearGradient id="gov-grad-silver" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#0284c7" />
                  <stop offset="100%" stop-color="#38bdf8" />
                </linearGradient>
                <linearGradient id="gov-grad-amber" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#d97706" />
                  <stop offset="100%" stop-color="#fbbf24" />
                </linearGradient>
              </defs>

              <!-- Rivers: Tigris & Euphrates -->
              <path d="M 120 40 Q 230 180 380 430" fill="none" stroke="#0ea5e9" stroke-width="3.5" opacity="0.6"/>
              <path d="M 90 90 Q 200 240 370 440" fill="none" stroke="#0284c7" stroke-width="3" opacity="0.5"/>

              <!-- Governorates as Interactive Polygonal Regions -->
              <!-- DUHOK -->
              <polygon points="180,30 240,25 245,60 190,65" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('دهوك')" id="poly-دهوك"/>
              <text x="210" y="50" fill="#fff" font-size="9" text-anchor="middle">دهوك</text>

              <!-- ERBIL -->
              <polygon points="240,25 295,45 280,105 235,80 245,60" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('أربيل')" id="poly-أربيل"/>
              <text x="260" y="70" fill="#fff" font-size="9" text-anchor="middle">أربيل</text>

              <!-- SULAIMANIYAH -->
              <polygon points="295,45 345,95 320,150 275,120 280,105" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('السليمانية')" id="poly-السليمانية"/>
              <text x="310" y="105" fill="#fff" font-size="9" text-anchor="middle">السليمانية</text>

              <!-- NINEVEH (MOSUL) -->
              <polygon points="130,50 180,30 190,65 235,80 215,140 140,125" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('نينوى')" id="poly-نينوى"/>
              <text x="175" y="95" fill="#fff" font-size="10" text-anchor="middle" font-weight="bold">نينوى</text>

              <!-- KIRKUK -->
              <polygon points="235,80 280,105 275,120 230,120" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('كركوك')" id="poly-كركوك"/>
              <text x="255" y="105" fill="#fff" font-size="8.5" text-anchor="middle">كركوك</text>

              <!-- SALAH AL-DIN -->
              <polygon points="170,135 230,120 270,140 250,210 190,195" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('صلاح الدين')" id="poly-صلاح_الدين"/>
              <text x="215" y="165" fill="#fff" font-size="9" text-anchor="middle">صلاح الدين</text>

              <!-- DIYALA -->
              <polygon points="270,140 330,170 300,245 250,210" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('ديالى')" id="poly-ديالى"/>
              <text x="290" y="195" fill="#fff" font-size="9" text-anchor="middle">ديالى</text>

              <!-- ANBAR -->
              <polygon points="40,110 140,125 190,195 180,290 80,310 30,220" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('الأنبار')" id="poly-الأنبار"/>
              <text x="110" y="210" fill="#fff" font-size="12" text-anchor="middle" font-weight="bold">الأنبار</text>

              <!-- BAGHDAD (CAPITAL - Highlighted) -->
              <circle cx="250" cy="225" r="22" fill="url(#gov-grad-gold)" stroke="#facc15" stroke-width="3" class="gov-poly cursor-pointer hover:scale-110 transition" onclick="selectGov('بغداد')" id="poly-بغداد"/>
              <text x="250" y="229" fill="#fff" font-size="10" text-anchor="middle" font-weight="black">بغداد 🏛️</text>

              <!-- BABIL -->
              <polygon points="225,245 265,245 260,285 220,285" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('بابل')" id="poly-بابل"/>
              <text x="242" y="268" fill="#fff" font-size="8.5" text-anchor="middle">بابل</text>

              <!-- KARBALA -->
              <polygon points="185,255 225,245 220,285 180,290" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('كربلاء المقدسة')" id="poly-كربلاء"/>
              <text x="202" y="272" fill="#fff" font-size="8" text-anchor="middle">كربلاء</text>

              <!-- WASIT -->
              <polygon points="265,245 320,240 330,300 275,305" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('واسط')" id="poly-واسط"/>
              <text x="295" y="275" fill="#fff" font-size="8.5" text-anchor="middle">واسط</text>

              <!-- NAJAF -->
              <polygon points="175,290 220,285 240,350 170,390" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('النجف الأشرف')" id="poly-النجف"/>
              <text x="195" y="335" fill="#fff" font-size="9" text-anchor="middle">النجف</text>

              <!-- QADISIYYAH (DIWANIYAH) -->
              <polygon points="220,285 260,285 265,335 225,335" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('الديوانية')" id="poly-الديوانية"/>
              <text x="242" y="312" fill="#fff" font-size="8" text-anchor="middle">الديوانية</text>

              <!-- MAYSAN (AMARAH) -->
              <polygon points="325,295 385,325 365,385 320,355" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('ميسان')" id="poly-ميسان"/>
              <text x="350" y="345" fill="#fff" font-size="8.5" text-anchor="middle">ميسان</text>

              <!-- DHI QAR (NASIRIYAH) -->
              <polygon points="265,335 320,335 340,395 285,405" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('ذي قار')" id="poly-ذي_قار"/>
              <text x="300" y="370" fill="#fff" font-size="8.5" text-anchor="middle">ذي قار</text>

              <!-- MUTHANNA (SAMAWAH) -->
              <polygon points="170,390 240,350 285,405 240,465 160,435" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5" class="gov-poly cursor-pointer hover:fill-emerald-600 transition" onclick="selectGov('المثنى')" id="poly-المثنى"/>
              <text x="215" y="415" fill="#fff" font-size="9" text-anchor="middle">المثنى</text>

              <!-- BASRA -->
              <polygon points="340,390 405,405 400,470 330,460" fill="url(#gov-grad-silver)" stroke="#0ea5e9" stroke-width="2" class="gov-poly cursor-pointer hover:fill-blue-500 transition" onclick="selectGov('البصرة')" id="poly-البصرة"/>
              <text x="370" y="435" fill="#fff" font-size="10.5" text-anchor="middle" font-weight="bold">البصرة ⚓</text>
            </svg>

            <!-- Map Legend -->
            <div class="flex items-center gap-4 text-[11px] text-slate-300 mt-2 bg-slate-900/80 px-3 py-1.5 rounded-xl border border-slate-800">
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span> معتمد ≥ 80% (فئة ذهبية)</span>
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-sky-500 inline-block"></span> قيد التأهيل (فئة فضية)</span>
              <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-amber-500 inline-block"></span> خطة تدخل عاجل</span>
            </div>
          </div>

          <!-- Governorate Live Intelligence Card -->
          <div class="lg:col-span-5 space-y-4">
            <div class="p-4 rounded-2xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-3">
              <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
                <div>
                  <h4 id="gov-card-title" class="font-black text-slate-900 dark:text-slate-100 text-sm sm:text-base">محافظة بغداد (أمانة بغداد والمحافظة)</h4>
                  <span id="gov-card-status" class="text-[10px] bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-bold px-2 py-0.5 rounded-full">لجنة فحص مفعلة</span>
                </div>
                <div class="text-right">
                  <div class="text-[10px] text-slate-400">نسبة الامتثال العامة:</div>
                  <div id="gov-card-rate" class="text-xl font-black text-emerald-600 dark:text-emerald-400">76.4%</div>
                </div>
              </div>

              <!-- Governorate Stats Grid -->
              <div class="grid grid-cols-3 gap-2 text-center text-xs">
                <div class="p-2 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
                  <div class="text-[10px] text-slate-400">المباني المفحوصة</div>
                  <div id="gov-stat-total" class="text-base font-black text-slate-800 dark:text-slate-200 mt-0.5">142 مبنى</div>
                </div>
                <div class="p-2 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/60">
                  <div class="text-[10px] text-emerald-700 dark:text-emerald-300">المعتمدة رسمياً</div>
                  <div id="gov-stat-pass" class="text-base font-black text-emerald-600 dark:text-emerald-400 mt-0.5">89 مبنى</div>
                </div>
                <div class="p-2 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/60">
                  <div class="text-[10px] text-amber-700 dark:text-amber-300">قيد التأهيل</div>
                  <div id="gov-stat-retro" class="text-base font-black text-amber-600 dark:text-amber-400 mt-0.5">53 مبنى</div>
                </div>
              </div>

              <!-- Top Audited Projects in Governorate -->
              <div>
                <div class="text-xs font-bold text-slate-700 dark:text-slate-300 mb-1.5 flex items-center justify-between">
                  <span>أبرز المشاريع المفحوصة في المحافظة:</span>
                  <span class="text-[10px] text-slate-400">تحديث أسبوعي</span>
                </div>
                <div id="gov-projects-list" class="space-y-1.5 text-xs">
                  <!-- Injected via JS -->
                </div>
              </div>

              <div class="pt-2 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
                <button onclick="switchTab('audit')" class="text-xs bg-emerald-600 hover:bg-emerald-500 text-white font-bold px-3 py-1.5 rounded-lg transition shadow">📋 بدء فحص مبنى جديد في هذه المحافظة</button>
                <button onclick="exportGovReport()" class="text-xs bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 text-slate-700 dark:text-slate-300 font-bold px-2.5 py-1.5 rounded-lg transition">تصدير تقرير المحافظة</button>
              </div>
            </div>
          </div>
        </div>
      </div>'''

def generate_ai_audit_tab():
    return '''    <!-- TAB: AI ARCHITECTURAL PLAN CHECKER & VISION AUDIT -->
    <section id="tab-ai-audit" class="tab-content hidden space-y-6">
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xl">🤖</span>
              <h2 class="text-base sm:text-lg font-black text-slate-900 dark:text-slate-100">المدقق الذكي للمخططات المعمارية (AI Architectural Plan Checker)</h2>
              <span class="text-[10px] bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300 font-bold px-2 py-0.5 rounded-full border border-purple-300">عرض المخطط المرفوع والتأشيرات الحية</span>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">فحص المخططات المعمارية بصيغة PDF أو CAD أو صور المساقط، وإظهار المخطط المرفوع مباشرة داخل اللوحة مع التأشيرات الهندسية (Redlines).</p>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-xs text-slate-500 font-semibold">تحميل عينة سريعة:</span>
            <button onclick="loadSamplePlan('needs_retrofit')" class="text-xs bg-amber-50 dark:bg-amber-950/40 text-amber-800 dark:text-amber-300 font-bold px-2.5 py-1.5 rounded-lg border border-amber-300">عينة مبنى به مخالفات</button>
            <button onclick="loadSamplePlan('compliant')" class="text-xs bg-emerald-50 dark:bg-emerald-950/40 text-emerald-800 dark:text-emerald-300 font-bold px-2.5 py-1.5 rounded-lg border border-emerald-300">عينة مبنى مطابق 100%</button>
          </div>
        </div>

        <!-- Upload & Analysis Controls -->
        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-4 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">رفع مخطط معماري (PDF, CAD, صور):</label>
              <div id="plan-dropzone" class="border-2 border-dashed border-purple-300 dark:border-purple-700 rounded-xl p-4 text-center hover:border-purple-500 hover:bg-purple-50/30 transition cursor-pointer bg-white dark:bg-slate-800" onclick="document.getElementById('plan-file-input').click()">
                <div class="text-3xl mb-1">📑</div>
                <div class="font-bold text-slate-800 dark:text-slate-200">انقر لاختيار ملف أو اسحب المخطط هنا</div>
                <div class="text-[11px] text-purple-700 dark:text-purple-300 font-semibold mt-1">يتم عرض المخطط وفحصه فوراً في اللوحة</div>
                <div class="text-[10px] text-slate-400 mt-1">يدعم: PDF, DWG, DXF, PNG, JPG (معالجة محلية آمنة 100%)</div>
                <input type="file" id="plan-file-input" class="hidden" accept=".pdf,application/pdf,image/*,.png,.jpg,.jpeg,.dxf,.dwg" onchange="handlePlanUpload(event)">
              </div>

              <!-- Uploaded file metadata card -->
              <div id="uploaded-file-info" class="hidden mt-2 p-2.5 rounded-xl bg-purple-50 dark:bg-purple-950/40 border border-purple-200 dark:border-purple-800 flex items-center justify-between">
                <div class="flex items-center gap-2 overflow-hidden">
                  <span class="text-lg">📄</span>
                  <div class="truncate">
                    <div id="uploaded-file-name" class="font-bold text-purple-950 dark:text-purple-200 truncate">مخطط.pdf</div>
                    <div id="uploaded-file-size" class="text-[10px] text-slate-400">1.2 MB</div>
                  </div>
                </div>
                <span class="text-[10px] bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-bold px-2 py-0.5 rounded-full whitespace-nowrap">معروض في اللوحة</span>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نطاق الفحص التلقائي المستهدف:</label>
              <div class="space-y-1 text-slate-700 dark:text-slate-300">
                <label class="flex items-center gap-2"><input type="checkbox" checked id="chk-scan-doors" onchange="runAIPlanScan()"> <span>فحص عروض الأبواب والعتبات (≥ 90 سم)</span></label>
                <label class="flex items-center gap-2"><input type="checkbox" checked id="chk-scan-ramps" onchange="runAIPlanScan()"> <span>فحص ميول المنحدرات والبسطات (1:12)</span></label>
                <label class="flex items-center gap-2"><input type="checkbox" checked id="chk-scan-toilets" onchange="runAIPlanScan()"> <span>فحص أبعاد دورات المياه وحرم الدوران (2×2م)</span></label>
                <label class="flex items-center gap-2"><input type="checkbox" checked id="chk-scan-elevators" onchange="runAIPlanScan()"> <span>فحص اتساع مقصورات المصاعد وأزرار برايل</span></label>
              </div>
            </div>

            <button onclick="triggerAIScanClick()" id="btn-run-scan" class="w-full py-2.5 rounded-xl bg-purple-600 hover:bg-purple-500 text-white font-bold text-xs transition shadow flex items-center justify-center gap-1.5">
              <span>⚡</span> <span>بدء التحليل الهندسي واستخراج التأشيرات (AI Scan)</span>
            </button>

            <!-- Offline PWA Banner -->
            <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/60 text-[11px] text-emerald-900 dark:text-emerald-200">
              <span class="font-bold">📱 جاهز للعمل الميداني بدون إنترنت (Offline Ready):</span>
              <p class="mt-0.5 text-slate-600 dark:text-slate-300">يمكن لمهندسي التفتيش في البلديات فحص المخططات في الموقع الإنشائي وعرض التأشيرات المعمارية مباشرة.</p>
            </div>
          </div>

          <!-- Canvas Preview with Interactive Redlines -->
          <div class="lg:col-span-8 space-y-4">
            <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 shadow-xl">
              
              <!-- Header Bar with Title & Status -->
              <div class="flex justify-between items-center text-xs text-slate-400 mb-2 flex-wrap gap-2">
                <div class="flex items-center gap-2">
                  <span class="font-bold text-slate-200">لوحة المخطط المعماري وتأشيرات الكود (Redlines & Violations):</span>
                  <span id="ai-scan-status-badge" class="text-purple-400 font-bold bg-purple-950/60 px-2 py-0.5 rounded-full border border-purple-800 text-[10px]">جاهز للفحص</span>
                </div>
                
                <!-- Viewport Controls (Zoom, Filter, Pages) -->
                <div class="flex items-center gap-2 flex-wrap">
                  <!-- Filter Switcher -->
                  <div class="flex items-center bg-slate-900 rounded-lg p-0.5 border border-slate-800 text-[10px]">
                    <button onclick="setPlanFilter('blueprint')" id="btn-filter-blueprint" class="px-2 py-0.5 rounded bg-purple-600 text-white font-bold transition" title="عرض بنمط كود أزرق داكن عالي التباين">مخطط أزرق</button>
                    <button onclick="setPlanFilter('original')" id="btn-filter-original" class="px-2 py-0.5 rounded text-slate-400 hover:text-white transition" title="عرض بالألوان الأصلية للملف">طبيعي</button>
                    <button onclick="setPlanFilter('mono')" id="btn-filter-mono" class="px-2 py-0.5 rounded text-slate-400 hover:text-white transition" title="عرض أبيض وأسود عالي التباين">رمادي</button>
                  </div>

                  <!-- Zoom Tools -->
                  <div class="flex items-center bg-slate-900 rounded-lg p-0.5 border border-slate-800 text-[11px] gap-1">
                    <button onclick="zoomPlan(-0.15)" class="px-2 py-0.5 hover:bg-slate-800 text-slate-300 rounded transition font-bold" title="تصغير">-</button>
                    <span id="ai-zoom-val" class="text-[10px] text-purple-300 font-bold min-w-[32px] text-center">100%</span>
                    <button onclick="zoomPlan(0.15)" class="px-2 py-0.5 hover:bg-slate-800 text-slate-300 rounded transition font-bold" title="تكبير">+</button>
                    <button onclick="zoomPlan(0)" class="px-1.5 py-0.5 hover:bg-slate-800 text-slate-400 rounded transition text-[10px]" title="إعادة ضبط">⟲</button>
                  </div>

                  <!-- PDF Page Navigator (Multi-page PDFs) -->
                  <div id="ai-pdf-pagenav" class="hidden items-center bg-slate-900 rounded-lg p-0.5 border border-slate-800 text-[10px] gap-1">
                    <button onclick="changePdfPage(-1)" class="px-1.5 py-0.5 hover:bg-slate-800 text-slate-300 rounded transition font-bold">◀</button>
                    <span id="ai-page-label" class="text-slate-300 px-1 font-bold">صفحة 1 من 1</span>
                    <button onclick="changePdfPage(1)" class="px-1.5 py-0.5 hover:bg-slate-800 text-slate-300 rounded transition font-bold">▶</button>
                  </div>
                </div>
              </div>

              <!-- Main Canvas Viewport -->
              <div class="w-full bg-slate-900 rounded-xl p-2 min-h-[360px] flex items-center justify-center relative overflow-hidden border border-slate-800" id="ai-canvas-wrapper">
                
                <!-- Laser Scanning Effect -->
                <div id="ai-scan-laser" class="hidden absolute left-0 right-0 h-1 bg-gradient-to-r from-transparent via-cyan-400 to-transparent shadow-[0_0_18px_#22d3ee] pointer-events-none z-30 transition-all duration-300"></div>

                <!-- Loading Spinner for PDF.js / Rendering -->
                <div id="ai-plan-loading" class="hidden absolute inset-0 bg-slate-950/80 backdrop-blur-sm z-40 flex flex-col items-center justify-center gap-2">
                  <div class="w-8 h-8 border-3 border-purple-500 border-t-transparent rounded-full animate-spin"></div>
                  <div id="ai-loading-text" class="text-xs font-bold text-purple-300">جاري معالجة المخطط المعماري وعرضه في اللوحة...</div>
                </div>

                <!-- Scalable Plan Viewport Layer -->
                <div id="ai-plan-layer" class="relative w-full h-full flex items-center justify-center transition-transform duration-150 origin-center">
                  
                  <!-- 1. Default Sample Vector Blueprint (Displayed for sample buttons) -->
                  <svg id="ai-sample-svg" viewBox="0 0 540 300" class="w-full max-h-[350px]">
                    <!-- Blueprint Grid Background -->
                    <defs>
                      <pattern id="blueprint-grid" width="20" height="20" patternUnits="userSpaceOnUse">
                        <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="0.5"/>
                      </pattern>
                    </defs>
                    <rect width="540" height="300" fill="#0f172a"/>
                    <rect width="540" height="300" fill="url(#blueprint-grid)"/>

                    <!-- Architectural Floorplan Group -->
                    <g id="ai-sample-blueprint-group">
                      <rect x="40" y="30" width="460" height="240" fill="none" stroke="#38bdf8" stroke-width="3" rx="4"/>
                      <text id="ai-svg-title" x="270" y="25" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">مسقط معماري: الطابق الأرضي للمبنى الحكومي النموذجي</text>
                      <line x1="40" y1="150" x2="260" y2="150" stroke="#475569" stroke-width="2.5"/>
                      <line x1="260" y1="30" x2="260" y2="270" stroke="#475569" stroke-width="2.5"/>
                      <line x1="380" y1="30" x2="380" y2="150" stroke="#475569" stroke-width="2.5"/>
                      <text x="150" y="90" fill="#64748b" font-size="10" text-anchor="middle">قاعة خدمة المواطنين</text>
                      <text x="150" y="210" fill="#64748b" font-size="10" text-anchor="middle">دورة مياه الزوار</text>
                      <text x="320" y="90" fill="#64748b" font-size="10" text-anchor="middle">بهو المصاعد</text>
                      <text x="440" y="90" fill="#64748b" font-size="10" text-anchor="middle">المكاتب الإدارية</text>
                      <text x="380" y="210" fill="#64748b" font-size="10" text-anchor="middle">المدخل الرئيسي والمنحدر</text>
                      <line x1="340" y1="270" x2="420" y2="270" stroke="#22c55e" stroke-width="5"/>
                      <text x="380" y="285" fill="#22c55e" font-size="8.5" text-anchor="middle" font-weight="bold">المدخل</text>
                    </g>
                  </svg>

                  <!-- 2. The Rendered Uploaded PDF Canvas (Directly displays the uploaded PDF page!) -->
                  <canvas id="ai-pdf-canvas" class="hidden max-h-[350px] max-w-full object-contain rounded-lg shadow-2xl transition-all"></canvas>

                  <!-- 3. The Rendered Uploaded Image (Directly displays PNG/JPG/WEBP floorplan!) -->
                  <img id="ai-uploaded-img" class="hidden max-h-[350px] max-w-full object-contain rounded-lg shadow-2xl transition-all" src="" alt="المخطط المعماري المرفوع">

                  <!-- 4. Interactive Redline & Violation Overlay SVG (Placed DIRECTLY on top of the uploaded plan!) -->
                  <svg id="ai-overlay-svg" viewBox="0 0 540 300" class="absolute inset-0 w-full h-full pointer-events-none z-20" preserveAspectRatio="none">
                    <g id="ai-redlines-group">
                      <!-- Redline 1: Threshold Violation -->
                      <g class="ai-pin-marker cursor-pointer" onclick="highlightFinding(0)" style="pointer-events: auto;">
                        <circle cx="380" cy="270" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="3"/>
                        <text x="380" y="274" fill="#ffffff" font-size="11" text-anchor="middle" font-weight="bold">!</text>
                        <line x1="395" y1="270" x2="435" y2="250" stroke="#ef4444" stroke-width="1.5"/>
                        <rect x="435" y="238" width="98" height="24" rx="5" fill="#1e1b4b" stroke="#ef4444" stroke-width="1.2"/>
                        <text x="484" y="253" fill="#fecaca" font-size="8" text-anchor="middle" font-weight="bold">عتبة 4.5 سم (م.ب.ع 202)</text>
                      </g>

                      <!-- Redline 2: Narrow Restroom Door -->
                      <g class="ai-pin-marker cursor-pointer" onclick="highlightFinding(1)" style="pointer-events: auto;">
                        <circle cx="260" cy="200" r="14" fill="#7f1d1d" stroke="#ef4444" stroke-width="2.5" stroke-dasharray="3"/>
                        <text x="260" y="204" fill="#ffffff" font-size="11" text-anchor="middle" font-weight="bold">!</text>
                        <line x1="260" y1="186" x2="220" y2="165" stroke="#ef4444" stroke-width="1.5"/>
                        <rect x="125" y="153" width="95" height="24" rx="5" fill="#1e1b4b" stroke="#ef4444" stroke-width="1.2"/>
                        <text x="172" y="168" fill="#fecaca" font-size="8" text-anchor="middle" font-weight="bold">باب 78 سم (المطلوب ≥90)</text>
                      </g>

                      <!-- Redline 3: Compliant Ramp -->
                      <g class="ai-pin-marker cursor-pointer" onclick="highlightFinding(3)" style="pointer-events: auto;">
                        <circle cx="340" cy="230" r="12" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                        <text x="340" y="234" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">✓</text>
                        <line x1="330" y1="220" x2="290" y2="210" stroke="#10b981" stroke-width="1.5"/>
                        <rect x="205" y="198" width="85" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
                        <text x="247" y="212" fill="#a7f3d0" font-size="7.5" text-anchor="middle" font-weight="bold">منحدر مطابق (1:14)</text>
                      </g>

                      <!-- Redline 4: Elevator Turning Space -->
                      <g class="ai-pin-marker cursor-pointer" onclick="highlightFinding(4)" style="pointer-events: auto;">
                        <circle cx="320" cy="70" r="12" fill="#064e3b" stroke="#10b981" stroke-width="2"/>
                        <text x="320" y="74" fill="#ffffff" font-size="10" text-anchor="middle" font-weight="bold">✓</text>
                        <line x1="332" y1="70" x2="355" y2="60" stroke="#10b981" stroke-width="1.5"/>
                        <rect x="355" y="49" width="90" height="22" rx="4" fill="#064e3b" stroke="#10b981" stroke-width="1"/>
                        <text x="400" y="63" fill="#a7f3d0" font-size="7.5" text-anchor="middle" font-weight="bold">كابينة 1.4×1.4م مطابقة</text>
                      </g>
                    </g>
                  </svg>
                </div>

              </div>

              <!-- Viewport Footer Legend & Opacity -->
              <div class="flex justify-between items-center text-[10px] text-slate-400 mt-2 px-1 flex-wrap gap-2">
                <div class="flex items-center gap-3">
                  <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-rose-500 inline-block"></span> مخالفات معمارية (انقر للمعاينة)</span>
                  <span class="flex items-center gap-1"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block"></span> عناصر مطابقة لكود 202</span>
                </div>
                <div class="flex items-center gap-2">
                  <span>شفافية المخطط:</span>
                  <input type="range" id="plan-opacity-slider" min="30" max="100" value="95" oninput="applyPlanFilter()" class="w-20 accent-purple-600 h-1.5 cursor-pointer">
                </div>
              </div>
            </div>

            <!-- AI Findings Summary Table -->
            <div class="bg-slate-50 dark:bg-slate-900 rounded-xl p-4 border border-slate-200 dark:border-slate-800 space-y-2 text-xs">
              <div class="flex justify-between items-center font-bold text-slate-800 dark:text-slate-200 border-b border-slate-200 dark:border-slate-800 pb-2 flex-wrap gap-1">
                <span>جدول الملاحظات المعمارية الصادرة من التدقيق الذكي (AI Audit Sheet):</span>
                <span id="ai-score-badge" class="text-amber-600 dark:text-amber-400 font-black">درجة الامتثال: 68% (يحتاج تصحيحات قبل الترخيص)</span>
              </div>
              <div id="ai-findings-list" class="space-y-1.5">
                <!-- Injected by JS -->
              </div>
              <div class="pt-2 flex justify-between items-center flex-wrap gap-2">
                <button onclick="downloadAIReport()" class="bg-purple-600 hover:bg-purple-500 text-white font-bold px-3 py-1.5 rounded-lg transition shadow flex items-center gap-1.5">
                  <span>📄</span> <span>تنزيل تقرير التدقيق المعماري المعتمد</span>
                </button>
                <span class="text-[11px] text-slate-400">كود التحقق الرقمي: IQ-AI-AUDIT-2026</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>'''

def generate_community_tab():
    return '''    <!-- TAB: COMMUNITY ACCESSIBILITY BARRIER REPORTING -->
    <section id="tab-community" class="tab-content hidden space-y-6">
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xl">👥</span>
              <h2 class="text-base sm:text-lg font-black text-slate-900 dark:text-slate-100">صوت المواطن للبيئة الدامجة (Community Barrier Reporting)</h2>
              <span class="text-[10px] bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 font-bold px-2 py-0.5 rounded-full border border-rose-300">مشاركة مجتمعية حية</span>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">منصة تفاعلية مخصصة للأشخاص ذوي الإعاقة، كبار السن، والمهتمين للتبليغ المباشر عن العوائق المعمارية في الدوائر والمرافق العامة في العراق.</p>
          </div>
          <button onclick="switchTab('audit')" class="text-xs bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-bold px-3 py-1.5 rounded-lg border border-slate-300">انتقال للتدقيق الرسمي للمباني</button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Submission Form -->
          <div class="lg:col-span-5 space-y-3.5 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <h4 class="font-bold text-slate-900 dark:text-slate-100 border-b border-slate-200 dark:border-slate-800 pb-1 flex items-center gap-1.5">
              <span>📢</span> <span>تسجيل بلاغ عن عائق معماري:</span>
            </h4>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">المحافظة وموقع العائق:</label>
              <div class="grid grid-cols-2 gap-2">
                <select id="com-gov" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                  <option value="بغداد">بغداد</option>
                  <option value="البصرة">البصرة</option>
                  <option value="نينوى">نينوى</option>
                  <option value="أربيل">أربيل</option>
                  <option value="النجف الأشرف">النجف الأشرف</option>
                  <option value="كربلاء المقدسة">كربلاء المقدسة</option>
                  <option value="بابل">بابل</option>
                  <option value="الأنبار">الأنبار</option>
                  <option value="ذي قار">ذي قار</option>
                  <option value="كركوك">كركوك</option>
                  <option value="ديالى">ديالى</option>
                  <option value="صلاح الدين">صلاح الدين</option>
                  <option value="السليمانية">السليمانية</option>
                  <option value="دهوك">دهوك</option>
                  <option value="واسط">واسط</option>
                  <option value="الديوانية">الديوانية</option>
                  <option value="ميسان">ميسان</option>
                  <option value="المثنى">المثنى</option>
                </select>
                <input type="text" id="com-location" placeholder="اسم المبنى أو الشارع" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">تصنيف العائق المعماري:</label>
              <select id="com-category" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="entrance">مداخل وسلالم بدون منحدر (Entrance & Ramps)</option>
                <option value="restroom">دورة مياه غير ميسرة أو مقفلة (Inaccessible Restroom)</option>
                <option value="elevator">مصاعد معطلة أو تفتقر لأزرار برايل (Elevators & Calls)</option>
                <option value="parking">احتلال أو انعدام مواقف ذوي الإعاقة (Parking & Aisles)</option>
                <option value="sidewalk">رصيف مقطوع أو غير مزود ببلاط لمسي (Sidewalks & Tactile)</option>
                <option value="counter">كاونترات خدمة مرتفعة جداً (High Service Counters)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">مستوى الضرر أو الإعاقة الناتجة:</label>
              <select id="com-severity" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="critical">🔴 حرج (يمنع الدخول تماماً لمستخدمي الكراسي المتحركة)</option>
                <option value="major">🟡 متوسط (يسبب مشقة بالغة أو خطر سقوط لكبار السن)</option>
                <option value="minor">🟢 بسيط (نقص في الإشارات الإرشادية أو برايل)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">وصف العائق بالتفصيل:</label>
              <textarea id="com-desc" rows="3" placeholder="اكتب تفاصيل العائق، مثلاً: وجود 3 درجات عند المدخل دون أي منحدر بديل..." class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold"></textarea>
            </div>

            <button onclick="submitCommunityReport()" class="w-full py-2.5 rounded-xl bg-rose-600 hover:bg-rose-500 text-white font-bold transition shadow flex items-center justify-center gap-1.5">
              <span>📤</span> <span>إرسال البلاغ إلى مرصد المنصة الوطنية</span>
            </button>
          </div>

          <!-- Community Feed & Records -->
          <div class="lg:col-span-7 space-y-3.5">
            <div class="flex justify-between items-center text-xs font-bold text-slate-700 dark:text-slate-300 border-b border-slate-200 dark:border-slate-800 pb-2">
              <span class="flex items-center gap-1.5">
                <span>📋</span> <span>سجل البلاغات الميدانية الحية (محدث آنياً):</span>
              </span>
              <span id="com-reports-count" class="text-rose-600 font-bold">5 بلاغات مسجلة</span>
            </div>

            <div id="com-reports-feed" class="space-y-2.5 max-h-[460px] overflow-y-auto pr-1">
              <!-- Injected by JS -->
            </div>
          </div>
        </div>
      </div>
    </section>'''


