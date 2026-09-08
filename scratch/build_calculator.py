# -*- coding: utf-8 -*-
"""
Script to build and inject all 7 interactive Universal Design calculators & simulators
into iraqi_accessibility_platform.html and index.html.
"""

def get_calculator_html():
    return '''    <!-- TAB 2: ARCHITECTURAL CALCULATOR & 2D UNIVERSAL DESIGN SIMULATOR LAB -->
    <section id="tab-calculator" class="tab-content hidden space-y-6">
      
      <!-- SUB-NAVIGATION TABS (PILLS) FOR THE 7 SIMULATORS -->
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-3 shadow-sm">
        <div class="flex items-center justify-between flex-wrap gap-2 mb-2 pb-2 border-b border-slate-100 dark:border-slate-800">
          <div class="flex items-center gap-2">
            <span class="text-base">🧪</span>
            <h2 class="text-sm sm:text-base font-black text-slate-900 dark:text-slate-100">المعالجات المعمارية الهندسية التفصيلية  للوصول الشامل (7 أدوات تفاعلية)</h2>
          </div>
          <span class="text-[11px] text-emerald-700 dark:text-emerald-400 font-bold bg-emerald-50 dark:bg-emerald-950/40 px-2.5 py-0.5 rounded-full border border-emerald-300 dark:border-emerald-800">م.ب.ع 202 & ADA 2010</span>
        </div>
        <div class="flex flex-wrap items-center gap-1.5 text-xs font-bold">
          <button onclick="switchCalcSubTab('all')" id="subtab-btn-all" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-emerald-600 text-white shadow-sm transition">📋 عرض كل الأدوات</button>
          <button onclick="switchCalcSubTab('ramps')" id="subtab-btn-ramps" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">📐 1. المنحدرات والميول</button>
          <button onclick="switchCalcSubTab('restroom')" id="subtab-btn-restroom" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🚻 2. المرفق الصحي (2×2م)</button>
          <button onclick="switchCalcSubTab('parking')" id="subtab-btn-parking" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🚗 3. مواقف السيارات</button>
          <button onclick="switchCalcSubTab('doors')" id="subtab-btn-doors" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🚪 4. مناورة الأبواب</button>
          <button onclick="switchCalcSubTab('elevators')" id="subtab-btn-elevators" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🛗 5. مقصورة المصاعد</button>
          <button onclick="switchCalcSubTab('curb')" id="subtab-btn-curb" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🦯 6. الأرصفة والبلاط اللمسي</button>
          <button onclick="switchCalcSubTab('reach')" id="subtab-btn-reach" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">📏 7. مديات الوصول والكاونتر</button>
        </div>
      </div>

      <!-- MODULE 1: RAMP CALCULATOR -->
      <div id="calc-sec-ramps" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-emerald-500 font-black">1.</span>
              <span>الحاسبة الهندسية الذكية للمنحدرات (Ramp & Slope Calculator)</span>
            </h3>
            <p class="text-xs text-slate-500">حساب الأطوال والميول وعدد البسطات الإلزامية وفق معايير م.ب.ع 202 (الباب 3-4).</p>
          </div>
          <span class="text-[10px] bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 font-bold px-2 py-0.5 rounded border border-slate-200 dark:border-slate-700">الحد الإلزامي 1:12</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">فرق الارتفاع الرأسي المطلوب تجاوزه (بالسنتيمتر):</label>
              <div class="relative">
                <input type="number" id="calc-height" value="60" min="5" max="300" oninput="runCalculator()" class="w-full px-3 py-2 text-sm font-bold rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 focus:ring-2 focus:ring-emerald-500">
                <span class="absolute left-3 top-2 text-slate-400 font-bold">سم</span>
              </div>
              <span class="text-[10px] text-slate-500">مثال: 4 درجات بارتفاع 15 سم = 60 سم.</span>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نسبة الميل المستهدفة:</label>
              <select id="calc-ratio" onchange="runCalculator()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="12">1:12 (8.3%) - الحد الأقصى الإلزامي في الكود</option>
                <option value="14">1:14 (7.1%) - ميل مريح للمستخدم المستقل</option>
                <option value="16" selected>1:16 (6.25%) - موصى به لكبار السن وضعاف البنية</option>
                <option value="20">1:20 (5.0%) - ميل مثالي فائق السهولة للمسارات الخارجية</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">شكل المسار الهندسي:</label>
              <div class="grid grid-cols-2 gap-2">
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="ramp-layout" value="straight" checked onchange="runCalculator()">
                  <span>مستقيم ممتد</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="ramp-layout" value="switchback" onchange="runCalculator()">
                  <span>منكسر (حرف U / L)</span>
                </label>
              </div>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 font-bold">طول المنحدر المائل</div>
                <div class="text-xl font-black text-emerald-700 dark:text-emerald-400 mt-1" id="res-ramp-length">9.60 م</div>
              </div>
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">بسطات الاستراحة</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="res-landings-count">2 بسطة</div>
              </div>
              <div class="p-3 rounded-xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800">
                <div class="text-[11px] text-purple-800 dark:text-purple-300 font-bold">إجمالي الطول الكلي</div>
                <div class="text-xl font-black text-purple-700 dark:text-purple-400 mt-1" id="res-total-footprint">12.60 م</div>
              </div>
            </div>

            <!-- SVG Ramp Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المحاكاة البصرية للمقطع الجانبي:</span>
                <span id="res-slope-angle" class="text-emerald-400 font-bold">الزاوية: 3.58°</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-end justify-center min-h-[120px] relative border border-slate-800">
                <svg id="ramp-svg" viewBox="0 0 500 110" class="w-full h-24">
                  <line x1="20" y1="95" x2="480" y2="95" stroke="#475569" stroke-width="2" stroke-dasharray="4"/>
                  <rect x="20" y="25" width="75" height="70" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                  <text x="57" y="18" fill="#38bdf8" font-size="9" text-anchor="middle" font-weight="bold">المدخل</text>
                  <polygon points="95,25 395,95 95,95" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2.5"/>
                  <rect x="395" y="92" width="65" height="5" fill="#f59e0b"/>
                  <text x="427" y="85" fill="#f59e0b" font-size="8" text-anchor="middle">استراحة</text>
                  <line x1="95" y1="15" x2="395" y2="85" stroke="#e2e8f0" stroke-width="2"/>
                  <text x="245" y="45" fill="#10b981" font-size="10" text-anchor="middle" font-weight="bold" id="svg-text-ratio">1:16</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center gap-1.5">
                <span class="text-emerald-400">✓</span>
                <span id="calc-verdict">تصميم مطابق ومريح ومناسب لكبار السن وللاستخدام الذاتي.</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 2: RESTROOM SIMULATOR -->
      <div id="calc-sec-restroom" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-4 flex flex-wrap justify-between items-center gap-2">
          <div>
            <div class="flex items-center gap-2">
              <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
                <span class="text-emerald-500 font-black">2.</span>
                <span>محاكي الفضاءات المعمارية 2D: المرفق الصحي الشامل (2.0 × 2.0 م)</span>
              </h3>
              <span class="text-[10px] bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-bold px-2 py-0.5 rounded-full">معايير الأبعاد الصافية</span>
            </div>
            <p class="text-xs text-slate-500">فحص تفاعلي لموقع المرحاض والمحور (45-50 سم)، مساحة الدوران (Ø 150 سم)، مساند الارتكاز (113 كغم)، وحرم المغسلة المعلقة.</p>
          </div>
          <div class="flex flex-wrap items-center gap-2">
            <button onclick="toggleSimElement('grabBars')" id="btn-toggle-bars" class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-300">مساند الارتكاز (L & Drop-down)</button>
            <button onclick="toggleSimElement('doorSwing')" id="btn-toggle-door" class="px-2.5 py-1 text-xs rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 border border-slate-300">فحص اتجاه فتح الباب (داخل/خارج)</button>
            <button onclick="toggleSimElement('tTurn')" id="btn-toggle-tturn" class="px-2.5 py-1 text-xs rounded-lg bg-amber-100 dark:bg-amber-950 text-amber-800 dark:text-amber-300 border border-amber-300 font-bold">بديل المباني القديمة: دوران حرف T (150×90 سم)</button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-center">
          <div class="lg:col-span-7 flex justify-center">
            <!-- 2D Canvas Simulator Area -->
            <div class="relative bg-slate-950 p-4 rounded-2xl border-4 border-slate-800 shadow-2xl">
              <svg id="sim-svg" width="360" height="360" viewBox="0 0 360 360" class="rounded-xl bg-slate-900">
                <defs>
                  <pattern id="grid" width="37.5" height="37.5" patternUnits="userSpaceOnUse">
                    <path d="M 37.5 0 L 0 0 0 37.5" fill="none" stroke="#334155" stroke-width="0.5"/>
                  </pattern>
                </defs>
                <rect width="300" height="300" x="30" y="30" fill="url(#grid)" stroke="#0ea5e9" stroke-width="3" rx="4"/>
                <text x="180" y="20" fill="#0ea5e9" font-size="11" text-anchor="middle" font-weight="bold">عرض الغرفة الصافي: 2.00 م (200 سم)</text>
                <text x="14" y="180" fill="#0ea5e9" font-size="11" text-anchor="middle" transform="rotate(-90 14 180)" font-weight="bold">طول الغرفة الصافي: 2.00 م (200 سم)</text>

                <g id="sim-circle-group">
                  <circle cx="180" cy="180" r="112" fill="rgba(16, 185, 129, 0.16)" stroke="#10b981" stroke-width="2" stroke-dasharray="5"/>
                  <text x="180" y="175" fill="#10b981" font-size="11" text-anchor="middle" font-weight="bold">دائرة دوران الكرسي المتحرك</text>
                  <text x="180" y="190" fill="#10b981" font-size="10" text-anchor="middle">قطر 150 سم (دوران 360° حر تماماً)</text>
                </g>

                <g id="sim-tturn-group" style="display: none;">
                  <rect x="112.5" y="67.5" width="135" height="225" fill="rgba(245, 158, 11, 0.22)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4" rx="4"/>
                  <rect x="67.5" y="112.5" width="225" height="135" fill="rgba(245, 158, 11, 0.22)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4" rx="4"/>
                  <text x="180" y="175" fill="#f59e0b" font-size="11" text-anchor="middle" font-weight="bold">مساحة مناورة حرف T</text>
                  <text x="180" y="190" fill="#f59e0b" font-size="9.5" text-anchor="middle">(150 × 90 سم) استثناء الأبنية القديمة</text>
                </g>

                <line x1="285" y1="35" x2="330" y2="35" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="2"/>
                <text x="307" y="26" fill="#f43f5e" font-size="8" text-anchor="middle" font-weight="bold">45-50 سم للمحور</text>

                <rect x="265" y="35" width="45" height="60" rx="12" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
                <circle cx="287.5" cy="75" r="14" fill="#94a3b8"/>
                <text x="287" y="108" fill="#f1f5f9" font-size="8" text-anchor="middle" font-weight="bold">مرحاض (ارتفاع 45-50 سم)</text>

                <circle cx="323" cy="70" r="5" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
                <text x="323" y="85" fill="#38bdf8" font-size="7" text-anchor="middle">شطاف (60-70سم)</text>

                <g id="sim-bars">
                  <path d="M 326 40 L 326 95 L 305 95" fill="none" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                  <text x="326" y="105" fill="#f59e0b" font-size="7" text-anchor="end">مسند L ثابت (80-90سم)</text>
                  <line x1="250" y1="40" x2="250" y2="95" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                  <text x="248" y="105" fill="#f59e0b" font-size="7" text-anchor="middle">مسند متحرك قابل للطي (تحمل 113 كغم)</text>
                </g>

                <path d="M 260 275 Q 290 255 320 275 L 320 325 L 260 325 Z" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
                <circle cx="290" cy="290" r="5" fill="#38bdf8"/>
                <rect x="255" y="270" width="70" height="55" fill="none" stroke="#38bdf8" stroke-width="1" stroke-dasharray="2"/>
                <text x="285" y="255" fill="#38bdf8" font-size="8" text-anchor="middle" font-weight="bold">مغسلة معلقة (ارتفاع 80-85 سم)</text>
                <text x="285" y="265" fill="#94a3b8" font-size="7" text-anchor="middle">فراغ سفلي: ارتفاع ≥ 70سم، عمق ≥ 20سم</text>

                <line x1="270" y1="327" x2="310" y2="327" stroke="#60a5fa" stroke-width="3"/>
                <text x="290" y="342" fill="#60a5fa" font-size="7" text-anchor="middle">مرآة مائلة (الحافة ≤ 100 سم)</text>

                <line x1="30" y1="330" x2="120" y2="330" stroke="#22c55e" stroke-width="5"/>
                <path id="sim-door-arc" d="M 120 330 A 90 90 0 0 1 30 330" fill="rgba(34, 197, 94, 0.15)" stroke="#22c55e" stroke-width="2" stroke-dasharray="3"/>
                <text x="75" y="345" fill="#22c55e" font-size="9" text-anchor="middle" font-weight="bold">عرض الباب: 90 سم (يفتح للخارج - بدون عتبة)</text>

                <circle cx="45" cy="45" r="7" fill="#dc2626" stroke="#fecaca" stroke-width="2"/>
                <line x1="45" y1="45" x2="45" y2="65" stroke="#dc2626" stroke-width="2"/>
                <text x="45" y="77" fill="#f87171" font-size="7.5" text-anchor="middle" font-weight="bold">حبل طوارئ (10 سم عن الأرض)</text>
              </svg>
            </div>
          </div>

          <div class="lg:col-span-5 space-y-2.5 text-xs">
            <div class="p-3.5 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-2">
              <h4 class="font-bold text-slate-900 dark:text-slate-100 text-xs border-b border-slate-200 dark:border-slate-800 pb-1 flex items-center justify-between">
                <span>المواصفة التفصيلية للمرفق الصحي الميسر:</span>
                <span class="text-[10px] text-emerald-600 font-bold">كود عراقي 2026</span>
              </h4>
              <div class="space-y-1.5 text-slate-700 dark:text-slate-300 text-[11.5px]">
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>المساحة والدوران:</strong> فضاء صافٍ 2.0 × 2.0 م مع دائرة دوران حرة بقطر 150 سم (360°).</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>الباب الصافي:</strong> عرض ≥ 90 سم، يفتح للخارج أو سحاب، مع إلغاء العتبات تماماً.</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>المرحاض:</strong> ارتفاع المقعد 45-50 سم، والمحور المركزي 45-50 سم عن أقرب جدار جانبي.</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>الشطاف والورق:</strong> تثبيت على ارتفاع 60-70 سم في متناول اليد المباشر.</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>المغسلة:</strong> حافة علوية 80-85 سم، معلقة مع فراغ سفلي بارتفاع ≥ 70 سم وعمق ≥ 20 سم، بخلاط رافع أو مستشعر.</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>مساند الارتكاز:</strong> ارتفاع 80-90 سم، تحمل ≥ 113 كغم (مسند L ثابت + مسند Drop-down متحرك).</div>
                </div>
                <div class="flex items-start gap-1.5">
                  <span class="text-emerald-500 font-bold">▪</span>
                  <div><strong>الملحقات والسلامة:</strong> مرآة بحافة سفلية ≤ 100 سم أو مائلة، وحبل إنذار طوارئ يتدلى حتى 10 سم عن الأرض مربوط بإنذار صوتي ضوئي خارجي.</div>
                </div>
              </div>
            </div>

            <div class="p-2.5 rounded-xl bg-amber-50 dark:bg-amber-950/20 border border-amber-200 dark:border-amber-800 text-amber-900 dark:text-amber-300 text-[11px]">
              <strong>تحذير الإشغال الإلزامي:</strong> يُحظر ترخيص أي دورة مياه ميسرة تقل أبعادها الصافية عن 2.00 × 2.00 م، أو يُفتح بابها للداخل، لما يسببه ذلك من إعاقة حرجة لعمليات الإنقاذ والإسعاف في حالات السقوط.
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 3: ACCESSIBLE PARKING & AISLE SIMULATOR (NEW) -->
      <div id="calc-sec-parking" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-blue-500 font-black">3.</span>
              <span>محاكي وحاسبة مواقف سيارات ذوي الإعاقة وممر العبور (Accessible Parking Simulator)</span>
            </h3>
            <p class="text-xs text-slate-500">حساب عدد المواقف الإلزامية ونسبة Van-Accessible ومحاكاة ممر النزول الآمن وفق م.ب.ع 202 (الباب 4-6) و ADA 2010 (Sec 502).</p>
          </div>
          <span class="text-[10px] bg-blue-100 text-blue-800 dark:bg-blue-950 dark:text-blue-300 font-bold px-2 py-0.5 rounded-full border border-blue-300">مسافة المشي ≤ 50م للمدخل</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">إجمالي سعة مواقف المشروع (Total Parking Capacity):</label>
              <div class="relative">
                <input type="number" id="park-total" value="100" min="1" max="3000" oninput="runParkingCalc()" class="w-full px-3 py-2 text-sm font-bold rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 focus:ring-2 focus:ring-blue-500">
                <span class="absolute left-3 top-2 text-slate-400 font-bold">موقف</span>
              </div>
              <span class="text-[10px] text-slate-500">مثال: مبنى تجاري أو حكومي يضم 100 سيارة.</span>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نوع الموقف المستعرض في المحاكاة:</label>
              <select id="park-type" onchange="runParkingCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="standard" selected>موقف سيارة صالون ميسر (Car Accessible: 2.40م + ممر 1.50م)</option>
                <option value="van">مركبة مجهزة بمصعد هيدروليكي (Van Accessible: 2.40م + ممر 2.44م أو 3.35م)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">زاوية الركن والتخطيط:</label>
              <div class="grid grid-cols-2 gap-2">
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="park-angle" value="90" checked onchange="runParkingCalc()">
                  <span>تعامد رأسي 90° (معياري)</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="park-angle" value="60" onchange="runParkingCalc()">
                  <span>مائل بزاوية 60°</span>
                </label>
              </div>
            </div>

            <div class="p-3 rounded-lg bg-blue-50 dark:bg-blue-950/40 border border-blue-200 dark:border-blue-800/60 text-blue-900 dark:text-blue-200 space-y-1">
              <div class="font-bold">قاعدة الكود العراقي والأمريكي:</div>
              <p class="text-[11px] leading-relaxed">
                يجب ألا تتجاوز مسافة السير بين الموقف ومدخل المبنى الميسر <strong>50 متراً</strong>، ويحظر تثبيت مواقف ذوي الإعاقة في مسار تتجاوز نسبة ميله 1:48 (2%).
              </p>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">المواقف المخصصة الإلزامية</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="park-res-required">4 مواقف</div>
              </div>
              <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 font-bold">منها مجهزة لفان (Van)</div>
                <div class="text-xl font-black text-emerald-700 dark:text-emerald-400 mt-1" id="park-res-van">1 موقف فان</div>
              </div>
              <div class="p-3 rounded-xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800">
                <div class="text-[11px] text-purple-800 dark:text-purple-300 font-bold">عرض الموقف + الممر</div>
                <div class="text-xl font-black text-purple-700 dark:text-purple-400 mt-1" id="park-res-total-w">3.90 م</div>
              </div>
            </div>

            <!-- SVG Parking Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المسقط الأفقي للموقف وممر العبور المحمي (Access Aisle):</span>
                <span id="park-visual-badge" class="text-blue-400 font-bold">Car Accessible (عرض 3.90م)</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-center justify-center min-h-[160px] relative border border-slate-800">
                <svg id="park-svg" viewBox="0 0 460 200" class="w-full h-44">
                  <!-- Asphalt Road -->
                  <rect x="10" y="10" width="440" height="180" fill="#0f172a" rx="6"/>
                  
                  <!-- Sidewalk curb at top -->
                  <rect x="10" y="10" width="440" height="30" fill="#334155" stroke="#475569" stroke-width="1"/>
                  <text x="230" y="28" fill="#94a3b8" font-size="10" text-anchor="middle" font-weight="bold">الرصيف المحمي المؤدي للمدخل الميسر</text>
                  
                  <!-- Curb cut ramp (in front of access aisle) -->
                  <polygon id="park-curb-ramp" points="260,10 260,40 330,40 330,10" fill="#eab308" opacity="0.9"/>
                  <text x="295" y="28" fill="#000" font-size="8" text-anchor="middle" font-weight="bold">منحدر رصيف</text>

                  <!-- Parking Stall (Left Bay: 2.40m wide = 180px) -->
                  <rect x="80" y="40" width="180" height="145" fill="#1e293b" stroke="#facc15" stroke-width="3"/>
                  
                  <!-- Wheelchair Painted Marking in Stall -->
                  <circle cx="170" cy="110" r="18" fill="#0284c7"/>
                  <path d="M 165 105 A 7 7 0 1 0 175 105 A 7 7 0 1 0 165 105 M 170 102 L 170 115 L 178 115 M 166 112 A 9 9 0 0 0 178 122" fill="none" stroke="#ffffff" stroke-width="2.2" stroke-linecap="round"/>
                  <text x="170" y="150" fill="#facc15" font-size="10" text-anchor="middle" font-weight="bold">موقف مخصص (2.40 م)</text>

                  <!-- Vehicle Outline Inside Stall -->
                  <rect x="100" y="55" width="140" height="75" rx="8" fill="#38bdf8" fill-opacity="0.15" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="170" y="96" fill="#38bdf8" font-size="9" text-anchor="middle">سيارة ميسرة</text>

                  <!-- Access Aisle (Right side: 1.50m / 2.44m wide) -->
                  <g id="park-aisle-group">
                    <rect id="park-aisle-rect" x="260" y="40" width="100" height="145" fill="#0284c7" fill-opacity="0.2" stroke="#0284c7" stroke-width="2"/>
                    <!-- Diagonal Hatch lines -->
                    <line x1="260" y1="55" x2="360" y2="105" stroke="#38bdf8" stroke-width="1.5"/>
                    <line x1="260" y1="85" x2="360" y2="135" stroke="#38bdf8" stroke-width="1.5"/>
                    <line x1="260" y1="115" x2="360" y2="165" stroke="#38bdf8" stroke-width="1.5"/>
                    <line x1="260" y1="145" x2="330" y2="180" stroke="#38bdf8" stroke-width="1.5"/>
                    <text id="park-aisle-text" x="310" y="115" fill="#e0f2fe" font-size="9" text-anchor="middle" font-weight="bold" transform="rotate(-90 310 115)">ممر نزول ميسر (1.50م)</text>
                  </g>

                  <!-- Sign Post (Top Left) -->
                  <circle cx="85" cy="45" r="4" fill="#3b82f6" stroke="#fff" stroke-width="1.5"/>
                  <rect x="40" y="32" width="40" height="16" rx="3" fill="#1d4ed8" stroke="#ffffff" stroke-width="1"/>
                  <text x="60" y="44" fill="#fff" font-size="7" text-anchor="middle" font-weight="bold">شاخصة 1.5م</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span>✓ ممر النزول المائل يمنع وقوف سيارات أخرى ويؤمن فتح الأبواب والمنحدر الجانبي.</span>
                <span class="text-blue-400 font-bold" id="park-verdict">تصميم مطابق لكود م.ب.ع 202</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 4: DOOR MANEUVERING CLEARANCE SIMULATOR (NEW) -->
      <div id="calc-sec-doors" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-amber-500 font-black">4.</span>
              <span>محاكي مناورة الأبواب وحرم حركة المقبض (Door Maneuvering Clearances)</span>
            </h3>
            <p class="text-xs text-slate-500">فحص خلوص جانب المقبض (Latch Clearance) وفراغ حركة الكرسي عند السحب والدفع وفق م.ب.ع 202 (الباب 3-7) و ADA 2010 (Sec 404).</p>
          </div>
          <span class="text-[10px] bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300 font-bold px-2 py-0.5 rounded-full border border-amber-300">خلوص المقبض ≥ 45-60 سم</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">اتجاه الاقتراب نحو الباب (Approach Direction):</label>
              <select id="door-approach" onchange="runDoorCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="front" selected>اقتراب أمامي مباشر (Front Approach)</option>
                <option value="latch">اقتراب جانبي من جهة المقبض (Latch-side Approach)</option>
                <option value="hinge">اقتراب جانبي من جهة المفصلات (Hinge-side Approach)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">حركة فتح الباب بالنسبة للمستخدم:</label>
              <div class="grid grid-cols-2 gap-2">
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="door-swing-dir" value="pull" checked onchange="runDoorCalc()">
                  <span>سحب نحو المستخدم (Pull)</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="door-swing-dir" value="push" onchange="runDoorCalc()">
                  <span>دفع بعيداً (Push)</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">عرض فتحة الباب الصافية (Clear Opening):</label>
              <div class="flex items-center gap-3">
                <input type="range" id="door-width-slider" min="75" max="115" value="90" step="5" oninput="runDoorCalc()" class="flex-1 accent-amber-600">
                <span id="door-width-val" class="font-black text-sm text-amber-600 w-16 text-left">90 سم</span>
              </div>
              <span class="text-[10px] text-slate-500">الحد الأدنى الإلزامي في م.ب.ع 202 هو 90 سم صافياً.</span>
            </div>

            <div class="p-3 rounded-lg bg-amber-50 dark:bg-amber-950/40 border border-amber-200 dark:border-amber-800/60 text-amber-900 dark:text-amber-200 space-y-1">
              <div class="font-bold">محددات هندسية إلزامية للأبواب:</div>
              <ul class="text-[11px] list-disc list-inside space-y-0.5">
                <li>عتبة الباب (Threshold): الحد الأقصى 13 ملم مع شطف مائل 1:2.</li>
                <li>قوة فتح الباب (Operating Force): ألا تزيد عن 22 نيوتن (5 أرطال).</li>
                <li>نوع المقبض: رافعة (Lever) يُفتح بضغطة كف دون الحاجة للإمساك والتدوير.</li>
              </ul>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800">
                <div class="text-[11px] text-amber-800 dark:text-amber-300 font-bold">خلوص جانب المقبض</div>
                <div class="text-xl font-black text-amber-700 dark:text-amber-400 mt-1" id="door-res-latch">45 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">عمق فضاء المناورة</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="door-res-depth">150 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 font-bold">حالة المطابقة</div>
                <div class="text-base font-black text-emerald-700 dark:text-emerald-400 mt-1" id="door-res-status">مطابق 100%</div>
              </div>
            </div>

            <!-- SVG Door Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المحاكاة البصرية لحرم مناورة الباب ومسار حركة المقبض:</span>
                <span id="door-visual-subtext" class="text-amber-400 font-bold">سحب أمامي - خلوص مقبض 45 سم</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-center justify-center min-h-[170px] relative border border-slate-800">
                <svg id="door-svg" viewBox="0 0 460 210" class="w-full h-44">
                  <!-- Main Partition Wall -->
                  <rect x="20" y="40" width="130" height="20" fill="#475569" stroke="#64748b"/>
                  <rect x="240" y="40" width="200" height="20" fill="#475569" stroke="#64748b"/>
                  <text x="80" y="32" fill="#94a3b8" font-size="9" text-anchor="middle">جدار فاصل</text>
                  <text x="340" y="32" fill="#94a3b8" font-size="9" text-anchor="middle">جدار المقبض (Latch Wall)</text>

                  <!-- Door Opening Gap (150 to 240 = 90px / 90cm) -->
                  <!-- Door Leaf (Swinging 90 deg) -->
                  <line id="door-leaf" x1="150" y1="50" x2="150" y2="140" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
                  <!-- Swing Arc -->
                  <path id="door-arc-path" d="M 240 50 A 90 90 0 0 1 150 140" fill="rgba(245, 158, 11, 0.12)" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="3"/>
                  <!-- Lever Handle Symbol -->
                  <circle cx="150" cy="130" r="4" fill="#ef4444"/>
                  <line x1="150" y1="130" x2="162" y2="130" stroke="#ef4444" stroke-width="2.5"/>

                  <!-- Maneuvering Clearance Zone (Box) -->
                  <rect id="door-clearance-box" x="150" y="60" width="135" height="135" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="2" stroke-dasharray="4" rx="4"/>
                  <text id="door-box-text" x="217" y="130" fill="#10b981" font-size="10" text-anchor="middle" font-weight="bold">فضاء مناورة حر (150 × 135 سم)</text>

                  <!-- Latch Clearance Dimension (From right jamb to clear zone) -->
                  <g id="door-latch-dim">
                    <line x1="240" y1="50" x2="285" y2="50" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="240" y1="45" x2="240" y2="55" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="285" y1="45" x2="285" y2="55" stroke="#38bdf8" stroke-width="2"/>
                    <text x="262" y="42" fill="#38bdf8" font-size="8.5" text-anchor="middle" font-weight="bold">45 سم خلوص</text>
                  </g>

                  <!-- User Avatar (Wheelchair) in approach position -->
                  <g id="door-user-avatar" transform="translate(190, 110)">
                    <rect x="-10" y="-12" width="20" height="24" rx="4" fill="#0284c7" stroke="#fff" stroke-width="1.5"/>
                    <circle cx="0" cy="-2" r="5" fill="#f8fafc"/>
                    <!-- Wheels -->
                    <rect x="-13" y="-10" width="3" height="20" rx="1" fill="#94a3b8"/>
                    <rect x="10" y="-10" width="3" height="20" rx="1" fill="#94a3b8"/>
                  </g>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span id="door-calc-hint">✓ يوفر الفضاء الجانبي للمقبض إمكانية سحب الباب دون اضطرار مستخدم الكرسي للرجوع للخلف.</span>
                <span class="text-emerald-400 font-bold">كود ADA & م.ب.ع 202</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 5: ACCESSIBLE ELEVATOR CABIN & CONTROLS (NEW) -->
      <div id="calc-sec-elevators" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-purple-500 font-black">5.</span>
              <span>محاكي مقصورة المصاعد الشاملة ولوحات التحكم وبرايل (Elevator Cabin Simulator)</span>
            </h3>
            <p class="text-xs text-slate-500">أبعاد الكابينة الصافية، اتساع الباب، الدرابزين الثلاثي وارتفاعات لوحات أزرار برايل وفق م.ب.ع 202 (الباب 6) و ADA 2010 (Sec 407).</p>
          </div>
          <span class="text-[10px] bg-purple-100 text-purple-800 dark:bg-purple-950 dark:text-purple-300 font-bold px-2 py-0.5 rounded-full border border-purple-300">أزرار الطلب 90-120 سم</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نموذج وتصنيف مقصورة المصعد المعمارية:</label>
              <select id="elev-type" onchange="runElevatorCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="side" selected>م.ب.ع 202 قياسي - باب جانبي (1.40 م عرض × 1.10 م عمق)</option>
                <option value="center">م.ب.ع 202 مثالي - باب وسطي (1.40 م عرض × 1.40 م عمق - دوران 360°)</option>
                <option value="hospital">مصعد نقالات وخدمات طبية كبرى (2.00 م عمق × 1.40 م عرض)</option>
              </select>
            </div>

            <div class="space-y-2">
              <label class="block font-bold text-slate-700 dark:text-slate-300">تجهيزات الإتاحة الإلزامية داخل المقصورة:</label>
              <div class="grid grid-cols-2 gap-2 text-[11px]">
                <label class="flex items-center gap-1.5 p-2 border rounded-lg bg-white dark:bg-slate-800">
                  <input type="checkbox" id="elev-braille" checked onchange="runElevatorCalc()">
                  <span>لوحة أزرار برايل بارزة</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg bg-white dark:bg-slate-800">
                  <input type="checkbox" id="elev-audio" checked onchange="runElevatorCalc()">
                  <span>منظومة نداء صوتي وضوئي</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg bg-white dark:bg-slate-800">
                  <input type="checkbox" id="elev-mirror" checked onchange="runElevatorCalc()">
                  <span>مرآة خلفية لتسهيل الخروج</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg bg-white dark:bg-slate-800">
                  <input type="checkbox" id="elev-rails" checked onchange="runElevatorCalc()">
                  <span>درابزين ارتكاز ثلاثي (85سم)</span>
                </label>
              </div>
            </div>

            <div class="p-3 rounded-lg bg-purple-50 dark:bg-purple-950/40 border border-purple-200 dark:border-purple-800/60 text-purple-900 dark:text-purple-200 space-y-1">
              <div class="font-bold">اشتراطات الأمان وزمن فتح الباب:</div>
              <p class="text-[11px] leading-relaxed">
                يجب ألا يقل زمن فتح الباب التلقائي عن <strong>5 ثوانٍ</strong> مع مستشعر ضوئي غير تلامسي لمنع انغلاق الباب على الكراسي المتحركة أو بطيئي الحركة.
              </p>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800">
                <div class="text-[11px] text-purple-800 dark:text-purple-300 font-bold">أبعاد الكابينة الصافية</div>
                <div class="text-base font-black text-purple-700 dark:text-purple-400 mt-1" id="elev-res-dims">140 × 110 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">عرض الباب الصافي</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="elev-res-door">90 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 font-bold">إمكانية الدوران</div>
                <div class="text-base font-black text-emerald-700 dark:text-emerald-400 mt-1" id="elev-res-turn">خروج عكسي</div>
              </div>
            </div>

            <!-- SVG Elevator Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المسقط الأفقي للمقصورة والمقطع الرأسي للوحة التحكم:</span>
                <span id="elev-badge-text" class="text-purple-400 font-bold">1.40 × 1.10 م (م.ب.ع 202)</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-center justify-center min-h-[170px] relative border border-slate-800">
                <svg id="elev-svg" viewBox="0 0 460 200" class="w-full h-44">
                  <!-- LEFT: Plan View of Cabin (x: 20 to 220) -->
                  <g id="elev-plan-group">
                    <rect id="elev-plan-box" x="30" y="30" width="160" height="130" fill="#1e293b" stroke="#a855f7" stroke-width="3" rx="4"/>
                    <text x="110" y="22" fill="#a855f7" font-size="9" text-anchor="middle" font-weight="bold" id="elev-plan-w-text">العرض: 1.40 م</text>
                    <text x="18" y="95" fill="#a855f7" font-size="9" text-anchor="middle" transform="rotate(-90 18 95)" id="elev-plan-d-text">1.10 م</text>

                    <!-- Handrails (3 sides) -->
                    <line x1="36" y1="36" x2="36" y2="154" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                    <line x1="36" y1="154" x2="184" y2="154" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>
                    <line x1="184" y1="154" x2="184" y2="36" stroke="#f59e0b" stroke-width="3" stroke-linecap="round"/>

                    <!-- Elevator Door at Top (Clear 90cm) -->
                    <line id="elev-door-line" x1="40" y1="30" x2="130" y2="30" stroke="#22c55e" stroke-width="6"/>
                    <text x="85" y="44" fill="#22c55e" font-size="8" text-anchor="middle" font-weight="bold">باب منزلق (90 سم)</text>

                    <!-- Wheelchair User Inside -->
                    <circle cx="110" cy="100" r="14" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="1.5"/>
                    <text x="110" y="103" fill="#fff" font-size="8" text-anchor="middle">كرسي</text>
                  </g>

                  <!-- RIGHT: Wall Elevation of Control Panel & Handrail (x: 250 to 440) -->
                  <g id="elev-elev-group">
                    <rect x="250" y="20" width="190" height="160" fill="#1e293b" stroke="#64748b" stroke-width="1" rx="4"/>
                    <text x="345" y="16" fill="#94a3b8" font-size="9" text-anchor="middle" font-weight="bold">مقطع رأسي لجدار التحكم الداخلي</text>
                    
                    <!-- Ground Line -->
                    <line x1="250" y1="175" x2="440" y2="175" stroke="#475569" stroke-width="2"/>
                    <text x="430" y="171" fill="#64748b" font-size="7">الأرضية</text>

                    <!-- Handrail Elevation (85-90 cm from ground) -->
                    <line x1="260" y1="120" x2="430" y2="120" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
                    <text x="400" y="113" fill="#f59e0b" font-size="7.5" font-weight="bold">درابزين (85 سم)</text>

                    <!-- Control Panel Column (90 - 120 cm range) -->
                    <rect x="300" y="70" width="45" height="75" fill="#334155" stroke="#38bdf8" stroke-width="1.5" rx="3"/>
                    
                    <!-- Braille Buttons (Dots) -->
                    <circle cx="312" cy="85" r="4" fill="#e2e8f0"/>
                    <circle cx="332" cy="85" r="4" fill="#e2e8f0"/>
                    <circle cx="312" cy="100" r="4" fill="#e2e8f0"/>
                    <circle cx="332" cy="100" r="4" fill="#e2e8f0"/>
                    <!-- Emergency Call Button (Red, at 90cm) -->
                    <circle cx="322" cy="125" r="5" fill="#dc2626"/>
                    <text x="322" y="141" fill="#f87171" font-size="6.5" text-anchor="middle">نداء طوارئ</text>
                    
                    <text x="322" y="62" fill="#38bdf8" font-size="7.5" text-anchor="middle" font-weight="bold">أزرار برايل (90-120سم)</text>

                    <!-- Audible Chime / Floor Indicator at Top -->
                    <rect x="305" y="32" width="35" height="15" fill="#000" stroke="#facc15" stroke-width="1" rx="2"/>
                    <text x="322" y="43" fill="#facc15" font-size="8" text-anchor="middle" font-weight="bold">🔔 G</text>
                  </g>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span>✓ يدعم مستخدمي الكراسي المتحركة والمكفوفين (أزرار بارزة + مؤشر صوتي).</span>
                <span class="text-purple-400 font-bold" id="elev-verdict">مطابق لمواصفات م.ب.ع 202</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 6: CURB RAMPS & TACTILE PAVING (NEW) -->
      <div id="calc-sec-curb" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-teal-500 font-black">6.</span>
              <span>محاكي منحدرات خفض الأرصفة والبلاط اللمسي (Curb Ramps & Tactile Paving)</span>
            </h3>
            <p class="text-xs text-slate-500">منحدر خفض الرصيف (Curb Cut)، أجنحة الأمان المائلة (1:10)، وشريط البلاط اللمسي التحذيري وفق م.ب.ع 202 و ISO 21542.</p>
          </div>
          <span class="text-[10px] bg-teal-100 text-teal-800 dark:bg-teal-950 dark:text-teal-300 font-bold px-2 py-0.5 rounded-full border border-teal-300">أجنحة جانبية 1:10 إلزامي</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">ارتفاع بردورة الرصيف عن الشارع (Curb Height):</label>
              <div class="flex items-center gap-3">
                <input type="range" id="curb-height-slider" min="10" max="25" value="15" step="1" oninput="runCurbCalc()" class="flex-1 accent-teal-600">
                <span id="curb-height-val" class="font-black text-sm text-teal-600 w-16 text-left">15 سم</span>
              </div>
              <span class="text-[10px] text-slate-500">الارتفاع المعتاد لأرصفة البلديات في العراق 15-20 سم.</span>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نسبة ميل المنحدر المنحدر للشارع:</label>
              <select id="curb-slope" onchange="runCurbCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="12" selected>1:12 (8.3%) - كود عراقي قياسي ومعتمد</option>
                <option value="10">1:10 (10.0%) - حد أقصى في الأرصفة الضيقة القائمة</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نمط البلاط اللمسي الحسي (Tactile Ground Surface Indicator):</label>
              <select id="curb-tactile-type" onchange="runCurbCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="blister" selected>بلاط تحذيري بنقاط بارزة (Hazard Warning Blister Studs)</option>
                <option value="directional">بلاط توجيهي ببروزات طولية (Directional / Sinusoidal Ribs)</option>
              </select>
            </div>

            <div class="p-3 rounded-lg bg-teal-50 dark:bg-teal-950/40 border border-teal-200 dark:border-teal-800/60 text-teal-900 dark:text-teal-200 space-y-1">
              <div class="font-bold">قاعدة التباين اللوني والشطف:</div>
              <p class="text-[11px] leading-relaxed">
                يجب أن يحقق البلاط اللمسي تبايناً لونياً (LRV Contrast ≥ 30%) مثل الأصفر الفاقع على الخرسانة الرمادية، مع صفر سم عتبة مع الإسفلت (Flush transition).
              </p>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-teal-50 dark:bg-teal-950/30 border border-teal-200 dark:border-teal-800">
                <div class="text-[11px] text-teal-800 dark:text-teal-300 font-bold">طول المنحدر الصافي</div>
                <div class="text-xl font-black text-teal-700 dark:text-teal-400 mt-1" id="curb-res-length">1.80 م</div>
              </div>
              <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800">
                <div class="text-[11px] text-amber-800 dark:text-amber-300 font-bold">عرض الأجنحة المائلة (1:10)</div>
                <div class="text-xl font-black text-amber-700 dark:text-amber-400 mt-1" id="curb-res-flare">1.50 م</div>
              </div>
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">عرض شريط التحذير</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="curb-res-tactile">60 سم</div>
              </div>
            </div>

            <!-- SVG Curb Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المسقط الأفقي لمنحدر خفض الرصيف مع الأجنحة والبلاط اللمسي:</span>
                <span id="curb-visual-badge" class="text-teal-400 font-bold">بردورة 15 سم | ميل 1:12</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-center justify-center min-h-[170px] relative border border-slate-800">
                <svg id="curb-svg" viewBox="0 0 460 200" class="w-full h-44">
                  <!-- Sidewalk Pavement (Top) -->
                  <rect x="20" y="20" width="420" height="70" fill="#334155" stroke="#475569" stroke-width="1.5"/>
                  <text x="230" y="45" fill="#94a3b8" font-size="10" text-anchor="middle" font-weight="bold">مستوى الرصيف العلوي (+15 سم)</text>

                  <!-- Asphalt Roadway (Bottom) -->
                  <rect x="20" y="140" width="420" height="50" fill="#0f172a" stroke="#1e293b"/>
                  <text x="230" y="170" fill="#64748b" font-size="10" text-anchor="middle">قارعة طريق السيارات / الشارع (منسوب 0.00)</text>

                  <!-- Left Flared Wing (1:10 Slope) -->
                  <polygon points="100,90 160,90 160,140 100,140" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                  <!-- Triangular slope lines -->
                  <line x1="100" y1="90" x2="160" y2="140" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2"/>
                  <text x="130" y="118" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">جناح 1:10</text>

                  <!-- Right Flared Wing (1:10 Slope) -->
                  <polygon points="300,90 360,90 360,140 300,140" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                  <line x1="360" y1="90" x2="300" y2="140" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2"/>
                  <text x="330" y="118" fill="#f59e0b" font-size="8" text-anchor="middle" font-weight="bold">جناح 1:10</text>

                  <!-- Central Ramp (Clear 1:12) -->
                  <rect x="160" y="90" width="140" height="50" fill="#14b8a6" fill-opacity="0.25" stroke="#14b8a6" stroke-width="2"/>
                  <text x="230" y="112" fill="#2dd4bf" font-size="9" text-anchor="middle" font-weight="bold" id="curb-ramp-text">منحدر النزول (ميل 1:12)</text>

                  <!-- Tactile Paving Strip (60cm deep = 20px) at transition -->
                  <rect id="curb-tactile-strip" x="160" y="122" width="140" height="18" fill="#eab308" stroke="#ca8a04" stroke-width="1.5"/>
                  <!-- Studs pattern -->
                  <g id="curb-studs-group">
                    <circle cx="175" cy="131" r="2.5" fill="#713f12"/>
                    <circle cx="195" cy="131" r="2.5" fill="#713f12"/>
                    <circle cx="215" cy="131" r="2.5" fill="#713f12"/>
                    <circle cx="235" cy="131" r="2.5" fill="#713f12"/>
                    <circle cx="255" cy="131" r="2.5" fill="#713f12"/>
                    <circle cx="275" cy="131" r="2.5" fill="#713f12"/>
                  </g>
                  <text x="230" y="135" fill="#000" font-size="7" text-anchor="middle" font-weight="bold">بلاط تحذيري للمكفوفين (60 سم)</text>

                  <!-- Zero-Lip Flush Transition Line -->
                  <line x1="100" y1="140" x2="360" y2="140" stroke="#38bdf8" stroke-width="2.5"/>
                  <text x="230" y="152" fill="#38bdf8" font-size="7.5" text-anchor="middle" font-weight="bold">انعدام العتبة مع الشارع (0 مم - Flush)</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span>✓ الأجنحة المائلة تمنع تعثر المشاة العاديين أثناء السير الموازي للرصيف.</span>
                <span class="text-teal-400 font-bold">مطابق لمواصفات م.ب.ع 202</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 7: ERGONOMIC REACH RANGES & RECEPTION COUNTERS (NEW) -->
      <div id="calc-sec-reach" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-rose-500 font-black">7.</span>
              <span>حاسبة ومحاكي مديات الوصول الهندسي وكاونترات الاستقبال (Reach Ranges & Counters)</span>
            </h3>
            <p class="text-xs text-slate-500">الحدود المريحة للمفاتيح، الشاشات، كاونترات خدمة المواطنين وتجويف الركبتين وفق م.ب.ع 202 (الباب 6) و ADA 2010 (Sec 308/904).</p>
          </div>
          <span class="text-[10px] bg-rose-100 text-rose-800 dark:bg-rose-950 dark:text-rose-300 font-bold px-2 py-0.5 rounded-full border border-rose-300">ارتفاع الكاونتر ≤ 85 سم</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">وضعية ومدى وصول المستخدم:</label>
              <div class="grid grid-cols-2 gap-2">
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="reach-mode" value="forward" checked onchange="runReachCalc()">
                  <span>وصول أمامي (Forward Reach)</span>
                </label>
                <label class="flex items-center gap-1.5 p-2 border rounded-lg cursor-pointer bg-white dark:bg-slate-800">
                  <input type="radio" name="reach-mode" value="side" onchange="runReachCalc()">
                  <span>وصول جانبي (Side Reach)</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نوع العنصر الهندسي المطلوب فحصه:</label>
              <select id="reach-element" onchange="runReachCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="counter" selected>كاونتر خدمة المواطنين / الاستقبال (Reception & Service)</option>
                <option value="switch">مفاتيح الإنارة وأجهزة التحكم (Light Switches & Controls)</option>
                <option value="atm">شاشات التفاعل والصراف الآلي (ATM & Kiosks)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">ارتفاع العنصر المصمم من الأرضية (سم):</label>
              <div class="flex items-center gap-3">
                <input type="range" id="reach-height-slider" min="30" max="150" value="85" step="5" oninput="runReachCalc()" class="flex-1 accent-rose-600">
                <span id="reach-height-val" class="font-black text-sm text-rose-600 w-16 text-left">85 سم</span>
              </div>
            </div>

            <div class="p-3 rounded-lg bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-800/60 text-rose-900 dark:text-rose-200 space-y-1">
              <div class="font-bold">أبعاد كاونتر خدمة المواطنين الميسر:</div>
              <ul class="text-[11px] list-disc list-inside space-y-0.5">
                <li>الارتفاع الأقصى: 85 سم (مقارنة بـ 110 سم للاعتيادي).</li>
                <li>طول الجزء الميسر: لا يقل عن 90 سم أفقياً.</li>
                <li>فراغ الركبتين: ارتفاع سفلي ≥ 68 سم وعمق سفلي ≥ 48 سم.</li>
              </ul>
            </div>
          </div>

          <div class="lg:col-span-7 space-y-4">
            <div class="grid grid-cols-3 gap-3 text-center">
              <div class="p-3 rounded-xl bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800">
                <div class="text-[11px] text-rose-800 dark:text-rose-300 font-bold">الحد الأقصى المسموح</div>
                <div class="text-xl font-black text-rose-700 dark:text-rose-400 mt-1" id="reach-res-max">120 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
                <div class="text-[11px] text-blue-800 dark:text-blue-300 font-bold">الحد الأدنى المسموح</div>
                <div class="text-xl font-black text-blue-700 dark:text-blue-400 mt-1" id="reach-res-min">38 سم</div>
              </div>
              <div class="p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
                <div class="text-[11px] text-emerald-800 dark:text-emerald-300 font-bold">تقييم النفاذية</div>
                <div class="text-base font-black text-emerald-700 dark:text-emerald-400 mt-1" id="reach-res-eval">في النطاق المثالي</div>
              </div>
            </div>

            <!-- SVG Reach Visual -->
            <div class="bg-slate-900 rounded-xl p-4 text-white">
              <div class="flex justify-between items-center text-xs mb-2 text-slate-400">
                <span>المقطع الرأسي لمدى الوصول الإرجونومي (Ergonomic Section):</span>
                <span id="reach-visual-badge" class="text-rose-400 font-bold">وصول أمامي مريح (38-120 سم)</span>
              </div>
              <div class="w-full bg-slate-950 rounded-lg p-2 flex items-center justify-center min-h-[170px] relative border border-slate-800">
                <svg id="reach-svg" viewBox="0 0 460 210" class="w-full h-44">
                  <!-- Ground Level -->
                  <line x1="20" y1="180" x2="440" y2="180" stroke="#475569" stroke-width="2.5"/>
                  <text x="430" y="195" fill="#64748b" font-size="8">الأرضية (0)</text>

                  <!-- Height Zones (Shaded) -->
                  <!-- Red Non-compliant Bottom Zone: 0 to 38cm (y: 180 to 142) -->
                  <rect x="330" y="142" width="90" height="38" fill="rgba(239, 68, 68, 0.15)"/>
                  <!-- Green Compliant Ergonomic Zone: 38 to 120cm (y: 142 to 60) -->
                  <rect x="330" y="60" width="90" height="82" fill="rgba(16, 185, 129, 0.22)" stroke="#10b981" stroke-width="1" stroke-dasharray="3"/>
                  <text x="375" y="105" fill="#10b981" font-size="9" text-anchor="middle" font-weight="bold">نطاق الوصول المريح (38-120 سم)</text>
                  <!-- Red Non-compliant Top Zone: > 120cm (y: 60 to 20) -->
                  <rect x="330" y="20" width="90" height="40" fill="rgba(239, 68, 68, 0.15)"/>
                  <text x="375" y="42" fill="#ef4444" font-size="8" text-anchor="middle">نطاق محظور (>120سم)</text>

                  <!-- Wheelchair Silhouette at Left (x: 80 to 180) -->
                  <g id="reach-user-figure">
                    <!-- Wheels -->
                    <circle cx="120" cy="150" r="28" fill="none" stroke="#38bdf8" stroke-width="2.5"/>
                    <circle cx="120" cy="150" r="4" fill="#38bdf8"/>
                    <circle cx="170" cy="170" r="8" fill="none" stroke="#94a3b8" stroke-width="2"/>
                    <!-- Frame & Seat (Height 48cm = y: 132) -->
                    <line x1="120" y1="150" x2="145" y2="132" stroke="#38bdf8" stroke-width="3"/>
                    <line x1="110" y1="132" x2="160" y2="132" stroke="#38bdf8" stroke-width="4"/>
                    <!-- Backrest -->
                    <line x1="110" y1="132" x2="105" y2="85" stroke="#38bdf8" stroke-width="4"/>
                    <!-- Human Torso & Head -->
                    <circle cx="125" cy="65" r="10" fill="#f8fafc"/>
                    <line x1="120" y1="75" x2="135" y2="132" stroke="#f8fafc" stroke-width="5" stroke-linecap="round"/>
                    <!-- Knees projecting forward (clearance check) -->
                    <line x1="135" y1="132" x2="185" y2="132" stroke="#f8fafc" stroke-width="5" stroke-linecap="round"/>
                    <line x1="185" y1="132" x2="185" y2="165" stroke="#f8fafc" stroke-width="5" stroke-linecap="round"/>
                    <!-- Outstretched Arm reaching toward target -->
                    <line id="reach-arm-line" x1="125" y1="85" x2="250" y2="95" stroke="#f8fafc" stroke-width="3.5" stroke-linecap="round"/>
                  </g>

                  <!-- Target Counter or Object (x: 230 to 320) -->
                  <g id="reach-target-group">
                    <!-- Standard High Counter (110cm = y: 70) -->
                    <rect x="270" y="70" width="50" height="110" fill="#334155" stroke="#475569" stroke-width="1.5"/>
                    <text x="295" y="62" fill="#94a3b8" font-size="7.5" text-anchor="middle">كاونتر 110سم</text>

                    <!-- Accessible Lower Counter Tier (85cm = y: 95) with knee clearance -->
                    <path id="reach-counter-shape" d="M 210 95 L 270 95 L 270 180 L 250 180 L 250 112 L 210 112 Z" fill="#0284c7" fill-opacity="0.35" stroke="#0284c7" stroke-width="2"/>
                    <text id="reach-target-label" x="240" y="88" fill="#38bdf8" font-size="8.5" text-anchor="middle" font-weight="bold">ميسر (85 سم)</text>
                    <!-- Knee clearance dimension -->
                    <line x1="205" y1="112" x2="205" y2="180" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2"/>
                    <text x="195" y="148" fill="#f59e0b" font-size="7" text-anchor="middle" transform="rotate(-90 195 148)">فراغ ركبة ≥ 68سم</text>
                  </g>

                  <!-- Dynamic Target Level Indicator (Red or Green dot + line) -->
                  <line id="reach-level-indicator" x1="20" y1="95" x2="430" y2="95" stroke="#10b981" stroke-width="2" stroke-dasharray="4"/>
                  <circle id="reach-target-dot" cx="240" cy="95" r="5" fill="#10b981" stroke="#fff" stroke-width="1.5"/>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span id="reach-verdict-note">✓ الارتفاع 85 سم يتيح استخدام الكاونتر جلوساً ووقوفاً مع فراغ مريح للركبتين والقدمين.</span>
                <span class="text-rose-400 font-bold" id="reach-verdict-code">كود م.ب.ع 202: بند 6-2</span>
              </div>
            </div>
          </div>
        </div>
      </div>

    </section>'''

def get_calculator_js():
    return '''    // --- ARCHITECTURAL CALCULATOR & SIMULATOR LAB (7-IN-1 MODULES) ---
    
    // Sub-Tab Switcher
    function switchCalcSubTab(subtab) {
      const sections = ['ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach'];
      const buttons = ['all', 'ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach'];
      
      // Update Buttons
      buttons.forEach(b => {
        const btn = document.getElementById('subtab-btn-' + b);
        if (btn) {
          if (b === subtab) {
            btn.className = 'calc-sub-btn px-3 py-1.5 rounded-xl bg-emerald-600 text-white shadow-sm transition font-bold';
          } else {
            btn.className = 'calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition font-bold';
          }
        }
      });

      // Update Section Visibility
      sections.forEach(s => {
        const sec = document.getElementById('calc-sec-' + s);
        if (sec) {
          if (subtab === 'all' || subtab === s) {
            sec.style.display = 'block';
          } else {
            sec.style.display = 'none';
          }
        }
      });
    }

    // --- MODULE 1: RAMP CALCULATOR ---
    function runCalculator() {
      const height = parseFloat(document.getElementById('calc-height').value) || 0;
      const ratio = parseFloat(document.getElementById('calc-ratio').value) || 12;
      const layout = document.querySelector('input[name="ramp-layout"]:checked').value;

      const rampLength = (height * ratio) / 100;
      const landings = 2 + Math.floor(rampLength / 9.0) + (layout === 'switchback' ? 1 : 0);
      const totalFootprint = rampLength + (landings * 1.5);

      const angleDeg = (Math.atan(1 / ratio) * (180 / Math.PI)).toFixed(2);

      document.getElementById('res-ramp-length').innerText = rampLength.toFixed(2) + ' م';
      document.getElementById('res-landings-count').innerText = landings + ' بسطات';
      document.getElementById('res-total-footprint').innerText = totalFootprint.toFixed(2) + ' م';
      document.getElementById('res-slope-angle').innerText = `الزاوية: ${angleDeg}°`;
      document.getElementById('svg-text-ratio').innerText = `1:${ratio}`;
    }

    // --- MODULE 2: RESTROOM SIMULATOR ---
    let barsVisible = true;
    let doorOutward = true;
    let tTurnMode = false;

    function toggleSimElement(elem) {
      if (elem === 'grabBars') {
        barsVisible = !barsVisible;
        document.getElementById('sim-bars').style.display = barsVisible ? 'block' : 'none';
        document.getElementById('btn-toggle-bars').classList.toggle('bg-emerald-100', barsVisible);
      } else if (elem === 'doorSwing') {
        doorOutward = !doorOutward;
        const arc = document.getElementById('sim-door-arc');
        if (doorOutward) {
          arc.setAttribute('d', 'M 120 330 A 90 90 0 0 1 30 330');
          arc.setAttribute('stroke', '#22c55e');
        } else {
          arc.setAttribute('d', 'M 120 330 A 90 90 0 0 0 30 240');
          arc.setAttribute('stroke', '#dc2626');
          alert('تحذير كود البناء: فتح الباب نحو الداخل يعترض دائرة دوران الكرسي (Ø 150 سم) ويُعد مخالفة هندسية حرجة تعيق الإنقاذ!');
        }
      } else if (elem === 'tTurn') {
        tTurnMode = !tTurnMode;
        document.getElementById('sim-circle-group').style.display = tTurnMode ? 'none' : 'block';
        document.getElementById('sim-tturn-group').style.display = tTurnMode ? 'block' : 'none';
        const btn = document.getElementById('btn-toggle-tturn');
        btn.classList.toggle('bg-amber-600', tTurnMode);
        btn.classList.toggle('text-white', tTurnMode);
      }
    }

    // --- MODULE 3: ACCESSIBLE PARKING & AISLE SIMULATOR ---
    function runParkingCalc() {
      const total = parseInt(document.getElementById('park-total').value) || 1;
      const type = document.getElementById('park-type').value;
      const angle = document.querySelector('input[name="park-angle"]:checked') ? document.querySelector('input[name="park-angle"]:checked').value : '90';

      // ADA & Iraqi Code 202 table
      let req = 1;
      if (total <= 25) req = 1;
      else if (total <= 50) req = 2;
      else if (total <= 75) req = 3;
      else if (total <= 100) req = 4;
      else if (total <= 150) req = 5;
      else if (total <= 200) req = 6;
      else if (total <= 300) req = 7;
      else if (total <= 400) req = 8;
      else if (total <= 500) req = 9;
      else if (total <= 1000) req = Math.ceil(total * 0.02);
      else req = 20 + Math.ceil((total - 1000) / 100);

      const vans = Math.max(1, Math.ceil(req / 6));
      const isVan = (type === 'van');

      const aisleW = isVan ? 2.44 : 1.50;
      const stallW = 2.40;
      const totalW = stallW + aisleW;

      document.getElementById('park-res-required').innerText = req + ' مواقف';
      document.getElementById('park-res-van').innerText = vans + ' موقف فان';
      document.getElementById('park-res-total-w').innerText = totalW.toFixed(2) + ' م';

      const badge = document.getElementById('park-visual-badge');
      const aisleRect = document.getElementById('park-aisle-rect');
      const aisleText = document.getElementById('park-aisle-text');
      const curbRamp = document.getElementById('park-curb-ramp');

      if (isVan) {
        badge.innerText = `Van Accessible (عرض ${totalW.toFixed(2)}م - ممر عريض 2.44م)`;
        if (aisleRect) aisleRect.setAttribute('width', '135');
        if (aisleText) {
          aisleText.setAttribute('x', '327');
          aisleText.setAttribute('transform', 'rotate(-90 327 115)');
          aisleText.textContent = 'ممر فان عريض (2.44م)';
        }
        if (curbRamp) curbRamp.setAttribute('points', '260,10 260,40 350,40 350,10');
      } else {
        badge.innerText = `Car Accessible (عرض ${totalW.toFixed(2)}م - ممر 1.50م)`;
        if (aisleRect) aisleRect.setAttribute('width', '100');
        if (aisleText) {
          aisleText.setAttribute('x', '310');
          aisleText.setAttribute('transform', 'rotate(-90 310 115)');
          aisleText.textContent = 'ممر نزول ميسر (1.50م)';
        }
        if (curbRamp) curbRamp.setAttribute('points', '260,10 260,40 330,40 330,10');
      }
    }

    // --- MODULE 4: DOOR MANEUVERING CLEARANCE SIMULATOR ---
    function runDoorCalc() {
      const approach = document.getElementById('door-approach').value;
      const swing = document.querySelector('input[name="door-swing-dir"]:checked').value;
      const width = parseInt(document.getElementById('door-width-slider').value) || 90;

      document.getElementById('door-width-val').innerText = width + ' سم';

      // Standards logic
      let latchClearance = 45;
      let depth = 150;
      let compliant = true;
      let hint = '';

      if (swing === 'pull') {
        if (approach === 'front') {
          latchClearance = 45;
          depth = 150;
          hint = 'اقتراب أمامي مع سحب: يلزم خلوص 45 سم بجانب المقبض وعمق 150 سم.';
        } else if (approach === 'latch') {
          latchClearance = 60;
          depth = 150;
          hint = 'اقتراب من جهة المقبض (سحب): يلزم خلوص 60 سم وعمق 150 سم لفسح مجال دوران الكرسي.';
        } else {
          latchClearance = 90;
          depth = 150;
          hint = 'اقتراب من جهة المفصلات (سحب): يلزم خلوص 90 سم لتفادي انحصار المستخدم خلف الدرفة.';
        }
      } else {
        // Push
        if (approach === 'front') {
          latchClearance = 30;
          depth = 120;
          hint = 'اقتراب أمامي مع دفع: يلزم خلوص 30 سم وعمق 120 سم.';
        } else if (approach === 'latch') {
          latchClearance = 60;
          depth = 120;
          hint = 'اقتراب من جهة المقبض (دفع): يلزم خلوص 60 سم وعمق 120 سم.';
        } else {
          latchClearance = 55;
          depth = 110;
          hint = 'اقتراب من جهة المفصلات (دفع): يلزم خلوص 55 سم وعمق 110 سم.';
        }
      }

      if (width < 90) {
        compliant = false;
        hint = '⚠️ مخالفة كود صريحة: عرض فتحة الباب الصافية أقل من 90 سم!';
      }

      document.getElementById('door-res-latch').innerText = latchClearance + ' سم';
      document.getElementById('door-res-depth').innerText = depth + ' سم';

      const statusElem = document.getElementById('door-res-status');
      if (compliant) {
        statusElem.innerText = 'مطابق 100%';
        statusElem.className = 'text-base font-black text-emerald-700 dark:text-emerald-400 mt-1';
      } else {
        statusElem.innerText = 'غير مطابق (عرض ناقص)';
        statusElem.className = 'text-base font-black text-rose-600 dark:text-rose-400 mt-1';
      }

      document.getElementById('door-calc-hint').innerText = '✓ ' + hint;
      document.getElementById('door-visual-subtext').innerText = `${swing === 'pull' ? 'سحب' : 'دفع'} | ${approach === 'front' ? 'أمامي' : 'جانبي'} | خلوص ${latchClearance}سم | عمق ${depth}سم`;

      // Update SVG Box dimensions and color
      const box = document.getElementById('door-clearance-box');
      const boxText = document.getElementById('door-box-text');
      const boxWidth = Math.min(220, Math.max(120, width + latchClearance));
      const boxDepth = Math.min(140, depth * 0.9);

      if (box) {
        box.setAttribute('width', boxWidth);
        box.setAttribute('height', boxDepth);
        if (compliant) {
          box.setAttribute('fill', 'rgba(16, 185, 129, 0.18)');
          box.setAttribute('stroke', '#10b981');
        } else {
          box.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          box.setAttribute('stroke', '#ef4444');
        }
      }
      if (boxText) {
        boxText.textContent = `فضاء مناورة حر (${depth} × ${width + latchClearance} سم)`;
      }
    }

    // --- MODULE 5: ACCESSIBLE ELEVATOR CABIN SIMULATOR ---
    function runElevatorCalc() {
      const type = document.getElementById('elev-type').value;
      const braille = document.getElementById('elev-braille').checked;
      const audio = document.getElementById('elev-audio').checked;
      const mirror = document.getElementById('elev-mirror').checked;
      const rails = document.getElementById('elev-rails').checked;

      let dims = '140 × 110 سم';
      let doorW = '90 سم';
      let turn = 'خروج عكسي';
      let verdict = 'مطابق لمواصفات م.ب.ع 202 (الباب 6-6)';
      let boxW = 160, boxH = 130;

      if (type === 'side') {
        dims = '140 × 110 سم';
        doorW = '90 سم';
        turn = 'خروج عكسي بمساعدة المرآة';
        boxW = 160; boxH = 130;
      } else if (type === 'center') {
        dims = '140 × 140 سم';
        doorW = '90 سم';
        turn = 'دوران حر كامل 360° (Ø 140)';
        boxW = 160; boxH = 160;
        verdict = 'النموذج المثالي للكود: يتيح دوران الكرسي بالكامل دون رجوع عكسي.';
      } else if (type === 'hospital') {
        dims = '200 × 140 سم';
        doorW = '110 سم';
        turn = 'دوران ونقالة طبية ممتدة';
        boxW = 160; boxH = 190;
        verdict = 'مطابق لمعايير المستشفيات والمراكز التخصصية الكبرى.';
      }

      document.getElementById('elev-res-dims').innerText = dims;
      document.getElementById('elev-res-door').innerText = doorW;
      document.getElementById('elev-res-turn').innerText = turn;
      document.getElementById('elev-verdict').innerText = verdict;
      document.getElementById('elev-badge-text').innerText = `${dims} | باب ${doorW}`;

      const box = document.getElementById('elev-plan-box');
      if (box) {
        box.setAttribute('height', boxH);
      }
    }

    // --- MODULE 6: CURB RAMPS & TACTILE PAVING SIMULATOR ---
    function runCurbCalc() {
      const height = parseInt(document.getElementById('curb-height-slider').value) || 15;
      const slope = parseInt(document.getElementById('curb-slope').value) || 12;
      const tactileType = document.getElementById('curb-tactile-type').value;

      document.getElementById('curb-height-val').innerText = height + ' سم';

      const rampLength = (height * slope) / 100;
      const flareWidth = (height * 10) / 100;

      document.getElementById('curb-res-length').innerText = rampLength.toFixed(2) + ' م';
      document.getElementById('curb-res-flare').innerText = flareWidth.toFixed(2) + ' م';
      document.getElementById('curb-res-tactile').innerText = '60 سم';

      document.getElementById('curb-visual-badge').innerText = `بردورة ${height} سم | ميل 1:${slope} (طول ${rampLength.toFixed(2)}م)`;
      document.getElementById('curb-ramp-text').textContent = `منحدر النزول (طول ${rampLength.toFixed(2)}م)`;

      const studsGroup = document.getElementById('curb-studs-group');
      if (studsGroup) {
        if (tactileType === 'directional') {
          // Replace studs with directional bars
          studsGroup.innerHTML = `
            <line x1="175" y1="124" x2="175" y2="138" stroke="#713f12" stroke-width="2.5"/>
            <line x1="195" y1="124" x2="195" y2="138" stroke="#713f12" stroke-width="2.5"/>
            <line x1="215" y1="124" x2="215" y2="138" stroke="#713f12" stroke-width="2.5"/>
            <line x1="235" y1="124" x2="235" y2="138" stroke="#713f12" stroke-width="2.5"/>
            <line x1="255" y1="124" x2="255" y2="138" stroke="#713f12" stroke-width="2.5"/>
            <line x1="275" y1="124" x2="275" y2="138" stroke="#713f12" stroke-width="2.5"/>
          `;
        } else {
          studsGroup.innerHTML = `
            <circle cx="175" cy="131" r="2.5" fill="#713f12"/>
            <circle cx="195" cy="131" r="2.5" fill="#713f12"/>
            <circle cx="215" cy="131" r="2.5" fill="#713f12"/>
            <circle cx="235" cy="131" r="2.5" fill="#713f12"/>
            <circle cx="255" cy="131" r="2.5" fill="#713f12"/>
            <circle cx="275" cy="131" r="2.5" fill="#713f12"/>
          `;
        }
      }
    }

    // --- MODULE 7: ERGONOMIC REACH RANGES & COUNTERS SIMULATOR ---
    function runReachCalc() {
      const mode = document.querySelector('input[name="reach-mode"]:checked').value;
      const element = document.getElementById('reach-element').value;
      const height = parseInt(document.getElementById('reach-height-slider').value) || 85;

      document.getElementById('reach-height-val').innerText = height + ' سم';

      const maxReach = 120;
      const minReach = (mode === 'forward') ? 38 : 25;

      document.getElementById('reach-res-max').innerText = maxReach + ' سم';
      document.getElementById('reach-res-min').innerText = minReach + ' سم';

      const evalElem = document.getElementById('reach-res-eval');
      let evalText = 'في النطاق المريح الممتاز';
      let evalClass = 'text-base font-black text-emerald-700 dark:text-emerald-400 mt-1';
      let compliant = true;

      if (height > maxReach) {
        evalText = 'مرتفع جداً (خارج المتناول)';
        evalClass = 'text-base font-black text-rose-600 dark:text-rose-400 mt-1';
        compliant = false;
      } else if (height < minReach) {
        evalText = 'منخفض جداً (يتطلب انحناءً حرجاً)';
        evalClass = 'text-base font-black text-rose-600 dark:text-rose-400 mt-1';
        compliant = false;
      } else {
        evalText = 'نطاق مريح ومطابق لكود م.ب.ع 202';
        evalClass = 'text-base font-black text-emerald-700 dark:text-emerald-400 mt-1';
      }

      evalElem.innerText = evalText;
      evalElem.className = evalClass;

      // Update SVG Target position
      // Ground is at y: 180. 150cm = y: 30. Scale: 1cm = 1.0px approximately.
      const targetY = 180 - (height * 1.0);
      const indicator = document.getElementById('reach-level-indicator');
      const targetDot = document.getElementById('reach-target-dot');
      const targetLabel = document.getElementById('reach-target-label');
      const arm = document.getElementById('reach-arm-line');

      if (indicator) {
        indicator.setAttribute('y1', targetY);
        indicator.setAttribute('y2', targetY);
        indicator.setAttribute('stroke', compliant ? '#10b981' : '#ef4444');
      }
      if (targetDot) {
        targetDot.setAttribute('cy', targetY);
        targetDot.setAttribute('fill', compliant ? '#10b981' : '#ef4444');
      }
      if (targetLabel) {
        targetLabel.setAttribute('y', targetY - 6);
        targetLabel.textContent = `${element === 'counter' ? 'كاونتر' : 'عنصر'}: ${height} سم`;
      }
      if (arm) {
        arm.setAttribute('y2', targetY);
      }
    }
'''

def apply_updates():
    calc_html = get_calculator_html()
    calc_js = get_calculator_js()

    targets = [
        "/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html",
        "/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html"
    ]

    for fpath in targets:
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # 1. Replace HTML section
        # Find start of tab-calculator and end of </section>
        start_tag = '<section id="tab-calculator"'
        end_tag = '</section>'
        
        idx_start = content.find(start_tag)
        if idx_start == -1:
            print(f"Error: Could not find {start_tag} in {fpath}")
            continue
        
        idx_end = content.find(end_tag, idx_start)
        if idx_end == -1:
            print(f"Error: Could not find {end_tag} in {fpath}")
            continue
        idx_end += len(end_tag)

        new_content = content[:idx_start] + calc_html + content[idx_end:]

        # 2. Replace JS section
        # Find start of '// --- RAMP CALCULATOR ---' and end before '// --- AUDIT SYSTEM & CHECKLIST ---'
        js_start_tag = '// --- RAMP CALCULATOR ---'
        js_end_tag = '// --- AUDIT SYSTEM & CHECKLIST ---'

        js_start = new_content.find(js_start_tag)
        js_end = new_content.find(js_end_tag)

        if js_start != -1 and js_end != -1:
            new_content = new_content[:js_start] + calc_js + '\n    ' + new_content[js_end:]
            print(f"Successfully replaced JS in {fpath}")
        else:
            print(f"Warning: JS markers not found in {fpath}, js_start={js_start}, js_end={js_end}")

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {fpath} successfully!")

if __name__ == "__main__":
    apply_updates()
