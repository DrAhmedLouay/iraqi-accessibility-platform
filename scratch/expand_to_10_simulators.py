#!/usr/bin/env python3
"""
expand_to_10_simulators.py
Expands the architectural calculator and simulator lab from 7 to 10 interactive tools:
- Tool 8: Emergency Rescue & Evacuation Areas in Stairwells (calc-sec-rescue)
- Tool 9: Accessible Stairs, Step Geometry & Dual Handrails (calc-sec-stairs)
- Tool 10: Auditorium, Theater & Stadium Wheelchair Seating Calculator (calc-sec-theater)
"""

import re
import sys

def build_expansion():
    print("=" * 70)
    print("EXPANDING ARCHITECTURAL SIMULATOR LAB FROM 7 TO 10 TOOLS")
    print("=" * 70)

    with open('iraqi_accessibility_platform.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update Title from 7 to 10 in Tab 2 header
    old_header_title = 'المعالجات المعمارية الهندسية التفصيلية  للوصول الشامل (7 أدوات تفاعلية)'
    new_header_title = 'المعالجات المعمارية الهندسية التفصيلية للوصول الشامل (10 أدوات تفاعلية)'
    html = html.replace(old_header_title, new_header_title)
    html = html.replace('المعالجات المعمارية الهندسية التفصيلية للوصول الشامل (7 أدوات تفاعلية)', new_header_title)
    print("✓ Updated Lab Title to 10 Interactive Tools")

    # 2. Add sub-tab buttons for Tools 8, 9, 10
    old_pills = '''          <button onclick="switchCalcSubTab('reach')" id="subtab-btn-reach" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">📏 7. مديات الوصول والكاونتر</button>
        </div>'''

    new_pills = '''          <button onclick="switchCalcSubTab('reach')" id="subtab-btn-reach" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">📏 7. مديات الوصول والكاونتر</button>
          <button onclick="switchCalcSubTab('rescue')" id="subtab-btn-rescue" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🚨 8. فضاءات الإنقاذ بالطوارئ</button>
          <button onclick="switchCalcSubTab('stairs')" id="subtab-btn-stairs" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🪜 9. السلالم والدرابزين المزدوج</button>
          <button onclick="switchCalcSubTab('theater')" id="subtab-btn-theater" class="calc-sub-btn px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-700 dark:text-slate-300 hover:bg-slate-200 transition">🎭 10. مقاعد المسارح والقاعات</button>
        </div>'''

    if old_pills in html:
        html = html.replace(old_pills, new_pills)
        print("✓ Injected 3 new sub-tab buttons into HTML")
    else:
        print("Warning: old_pills pattern not found exactly, using regex...")
        html = re.sub(r'(<button onclick="switchCalcSubTab\(\'reach\'\)"[^>]*>.*?<\/button>\s*<\/div>)',
                      lambda m: new_pills, html, count=1)

    # 3. HTML Modules 8, 9, 10
    modules_html = '''
      <!-- MODULE 8: EMERGENCY RESCUE AREAS IN STAIRWELLS -->
      <div id="calc-sec-rescue" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-rose-500 font-black">8.</span>
              <span>محاكي فضاءات الإنقاذ والإخلاء في الطوارئ (Emergency Rescue & Refugee Areas)</span>
            </h3>
            <p class="text-xs text-slate-500">فحص فضاءات الكراسي المتحركة المحمية من الدخان داخل بيت الدرج وفق م.ب.ع 202 (الباب 7) و ADA Sec 207/1009.</p>
          </div>
          <span class="text-[10px] bg-rose-50 dark:bg-rose-950/40 text-rose-700 dark:text-rose-300 font-bold px-2 py-0.5 rounded border border-rose-300">أمان وحريق 2 ساعة</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">عرض مهرب الدرج الصافي (Stair Landing Width):</label>
              <select id="rescue-stair-width" onchange="runRescueCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="120">120 سم (عرض المسار القياسي)</option>
                <option value="150" selected>150 سم (موصى به للمباني العامة)</option>
                <option value="180">180 سم (فضاء واسع لتدفق المشاة الكثيف)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">عدد فضاءات الكراسي المتحركة المخصصة في البسطة:</label>
              <div class="grid grid-cols-2 gap-2">
                <label class="flex items-center gap-2 p-2 rounded border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 cursor-pointer">
                  <input type="radio" name="rescue-spaces" value="1" checked onchange="runRescueCalc()">
                  <span class="font-bold">موقع واحد (76×122 سم)</span>
                </label>
                <label class="flex items-center gap-2 p-2 rounded border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-800 cursor-pointer">
                  <input type="radio" name="rescue-spaces" value="2" onchange="runRescueCalc()">
                  <span class="font-bold">موقعان (152×122 سم)</span>
                </label>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">تجهيزات الأمان والسلامة الإلزامية:</label>
              <div class="space-y-1.5">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-rescue-firewall" checked onchange="runRescueCalc()">
                  <span>جدار وباب مقاوم للحريق 2 ساعة مع ضغط هوائي للدخان</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-rescue-intercom" checked onchange="runRescueCalc()">
                  <span>هاتف طوارئ ثنائي الاتجاه (Two-way Comms) إلى غرفة التحكم</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-rescue-clearpath" checked onchange="runRescueCalc()">
                  <span>فضاء الكرسي خارج خط مسار فتح الباب وتدفق الهاربين (Zero Encroachment)</span>
                </label>
              </div>
            </div>

            <!-- Results Card -->
            <div class="p-3 bg-white dark:bg-slate-800 rounded-lg border border-slate-200 dark:border-slate-700 space-y-2">
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">أبعاد فضاء الكرسي الصافي:</span>
                <span class="font-bold text-slate-800 dark:text-slate-200" id="rescue-res-dims">76 × 122 سم</span>
              </div>
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">خلوص ممر هروب المشاة المتبقي:</span>
                <span class="font-bold text-slate-800 dark:text-slate-200" id="rescue-res-path">120 سم (حر تماماً)</span>
              </div>
              <div class="border-t border-slate-100 dark:border-slate-700 pt-2">
                <span class="text-slate-500 text-[10px] block">التقييم الهندسي والترخيص:</span>
                <div id="rescue-res-eval" class="text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5">مطابق لكود السلامة العراقي م.ب.ع 202</div>
              </div>
            </div>

            <!-- Export Buttons -->
            <div class="flex items-center gap-2 pt-1">
              <button onclick="exportToDXF('rescue')" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📐</span> <span>تصدير كاد (.DXF)</span>
              </button>
              <button onclick="exportTenderSpecs('rescue')" class="flex-1 bg-rose-700 hover:bg-rose-600 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📑</span> <span>كراسة المواصفات</span>
              </button>
            </div>
          </div>

          <!-- Visual SVG Simulator (Module 8) -->
          <div class="lg:col-span-7 space-y-2">
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center relative overflow-hidden">
              <div class="text-[11px] font-bold text-slate-300 mb-2 flex justify-between items-center">
                <span>مسقط أفقي تفاعلي: فضاء الإنقاذ الآمن داخل بيت الدرج (Scale: 1:30)</span>
                <span class="text-rose-400 font-mono text-[10px]">مقاومة حريق 2 ساعة</span>
              </div>
              <div class="w-full overflow-x-auto flex justify-center">
                <svg id="rescue-svg" viewBox="0 0 520 280" class="w-full max-w-[500px] h-[260px] bg-slate-950 rounded-lg border border-slate-800">
                  <!-- Fire Rated Outer Walls -->
                  <rect x="20" y="20" width="480" height="240" fill="#0f172a" stroke="#ef4444" stroke-width="4" rx="4"/>
                  
                  <!-- Stair Flights (Up and Down) -->
                  <g id="rescue-stairs-graphic">
                    <rect x="25" y="25" width="200" height="100" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
                    <line x1="25" y1="45" x2="225" y2="45" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="65" x2="225" y2="65" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="85" x2="225" y2="85" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="105" x2="225" y2="105" stroke="#64748b" stroke-width="1.5"/>
                    <text x="125" y="70" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">درج نازل (DOWN) ⬇</text>
                    
                    <rect x="25" y="155" width="200" height="100" fill="#1e293b" stroke="#475569" stroke-width="1.5"/>
                    <line x1="25" y1="175" x2="225" y2="175" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="195" x2="225" y2="195" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="215" x2="225" y2="215" stroke="#64748b" stroke-width="1.5"/>
                    <line x1="25" y1="235" x2="225" y2="235" stroke="#64748b" stroke-width="1.5"/>
                    <text x="125" y="200" fill="#cbd5e1" font-size="12" font-weight="bold" text-anchor="middle">درج صاعد (UP) ⬆</text>
                  </g>

                  <!-- Central Well & Handrails -->
                  <rect x="25" y="125" width="180" height="30" fill="#090d16" stroke="#334155"/>
                  <line x1="30" y1="130" x2="200" y2="130" stroke="#38bdf8" stroke-width="2.5"/>
                  <line x1="30" y1="150" x2="200" y2="150" stroke="#38bdf8" stroke-width="2.5"/>

                  <!-- Fire Door with Outward Swing -->
                  <g id="rescue-door">
                    <line x1="496" y1="110" x2="496" y2="190" stroke="#090d16" stroke-width="6"/>
                    <path d="M 496 110 A 80 80 0 0 0 416 190" fill="none" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                    <line x1="496" y1="110" x2="416" y2="190" stroke="#f59e0b" stroke-width="3"/>
                    <text x="445" y="145" fill="#fde68a" font-size="10" font-weight="bold">باب حريق 90سم</text>
                  </g>

                  <!-- Evacuation Flow Path (Orange Arrow) -->
                  <path d="M 450 170 Q 320 170 235 70" fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="6"/>
                  <polygon points="230,65 245,67 238,78" fill="#f59e0b"/>
                  <text x="340" y="160" fill="#fde68a" font-size="11" font-weight="bold">مسار إخلاء المشاة</text>

                  <!-- Wheelchair Rescue Refuge Space (76 x 122 cm) -->
                  <g id="rescue-refuge-space">
                    <rect id="rescue-space-box" x="250" y="30" width="85" height="95" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2.5" rx="5"/>
                    <circle cx="292" cy="65" r="18" fill="#047857" stroke="#10b981" stroke-width="2"/>
                    <text x="292" y="71" fill="#fff" font-size="16" text-anchor="middle" font-weight="bold">♿</text>
                    <rect x="255" y="90" width="75" height="20" rx="3" fill="#064e3b" stroke="#10b981"/>
                    <text x="292" y="104" fill="#a7f3d0" font-size="10" text-anchor="middle" font-weight="bold">76 × 122 سم</text>
                    
                    <!-- Emergency Intercom Device on Wall -->
                    <rect x="235" y="45" width="12" height="20" fill="#ef4444" stroke="#fff" rx="2"/>
                    <text x="241" y="58" fill="#fff" font-size="8" text-anchor="middle" font-weight="bold">SOS</text>
                  </g>

                  <!-- Dimension Callouts -->
                  <rect x="345" y="40" width="130" height="26" rx="5" fill="#1e1b4b" stroke="#38bdf8"/>
                  <text x="410" y="57" fill="#bae6fd" font-size="10.5" text-anchor="middle" font-weight="bold">فضاء محمي خارج مسار الهروب</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span id="rescue-verdict-note">✓ فضاء الكرسي المتحرك مؤمن بالكامل ولا يعترض حركة الإخلاء العامة.</span>
                <span class="text-rose-400 font-bold">كود م.ب.ع 202: بند 7-2</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 9: ACCESSIBLE STAIRS & DUAL HANDRAILS -->
      <div id="calc-sec-stairs" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-teal-500 font-black">9.</span>
              <span>محاكي السلالم المعمارية الميسرة والدرابزين المزدوج (Accessible Stairs & Handrails)</span>
            </h3>
            <p class="text-xs text-slate-500">هندسة القائمة والنائمة والأنوف المشطوفة والامتدادات الأفقية للدرابزين طبقاً لكود م.ب.ع 202 (الباب 3-3 و 3-5).</p>
          </div>
          <span class="text-[10px] bg-teal-50 dark:bg-teal-950/40 text-teal-700 dark:text-teal-300 font-bold px-2 py-0.5 rounded border border-teal-300">معادلة الراحة 2R+T</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <div class="flex justify-between items-center mb-1">
                <label class="font-bold text-slate-700 dark:text-slate-300">ارتفاع القائمة (Riser Height):</label>
                <span class="font-bold text-emerald-600 dark:text-emerald-400" id="stairs-riser-val">15 سم</span>
              </div>
              <input type="range" id="stairs-riser-slider" min="11" max="22" value="15" step="0.5" oninput="runStairsCalc()" class="w-full accent-teal-600">
              <div class="flex justify-between text-[10px] text-slate-400">
                <span>11 سم (مريح جداً)</span>
                <span>المثالي: 15-16 سم</span>
                <span>22 سم (شديد الانحدار ❌)</span>
              </div>
            </div>

            <div>
              <div class="flex justify-between items-center mb-1">
                <label class="font-bold text-slate-700 dark:text-slate-300">عرض النائمة (Tread Width):</label>
                <span class="font-bold text-teal-600 dark:text-teal-400" id="stairs-tread-val">30 سم</span>
              </div>
              <input type="range" id="stairs-tread-slider" min="24" max="36" value="30" step="1" oninput="runStairsCalc()" class="w-full accent-teal-600">
              <div class="flex justify-between text-[10px] text-slate-400">
                <span>24 سم (ضيق ومخالف ❌)</span>
                <span>الحد الأدنى: 28 سم</span>
                <span>36 سم (واسع ومريح ✅)</span>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">نوع وشكل أنف الدرجة (Stair Nosing):</label>
              <select id="stairs-nosing-type" onchange="runStairsCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="beveled" selected>أنف مشطوف بزاوية 60° ملساء (مطابق ويمنع التعثر ✅)</option>
                <option value="flush">أنف مستوٍ تماماً مع القائمة (Flush Nosing ✅)</option>
                <option value="abrupt">أنف بارز حاد ومعلق (مخالف للكود ويسبب التعثر ❌)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">عناصر السلامة الإلزامية:</label>
              <div class="space-y-1.5">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-stairs-extension" checked onchange="runStairsCalc()">
                  <span>امتداد أفقي للدرابزين 30 سم عند البداية والنهاية مع استدارة ناعمة</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-stairs-tactile" checked onchange="runStairsCalc()">
                  <span>شريط تحذير لمسي بنقاط بارزة (60 سم) قبل أول درجة وبعد آخر درجة</span>
                </label>
              </div>
            </div>

            <!-- Results Card -->
            <div class="p-3 bg-white dark:bg-slate-800 rounded-lg border border-slate-200 dark:border-slate-700 space-y-2">
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">معادلة راحة الدرج (2R + T):</span>
                <span class="font-bold text-slate-800 dark:text-slate-200" id="stairs-res-formula">60 سم (مثالي 60-64 سم)</span>
              </div>
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">ارتفاع الدرابزين المزدوج:</span>
                <span class="font-bold text-slate-800 dark:text-slate-200">85 سم (علوي) | 65 سم (سفلي)</span>
              </div>
              <div class="border-t border-slate-100 dark:border-slate-700 pt-2">
                <span class="text-slate-500 text-[10px] block">تقييم الكود العراقي م.ب.ع 202:</span>
                <div id="stairs-res-eval" class="text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5">مطابق تماماً ومريح للحركة اليومية</div>
              </div>
            </div>

            <!-- Export Buttons -->
            <div class="flex items-center gap-2 pt-1">
              <button onclick="exportToDXF('stairs')" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📐</span> <span>تصدير كاد (.DXF)</span>
              </button>
              <button onclick="exportTenderSpecs('stairs')" class="flex-1 bg-teal-700 hover:bg-teal-600 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📑</span> <span>كراسة المواصفات</span>
              </button>
            </div>
          </div>

          <!-- Visual SVG Simulator (Module 9) -->
          <div class="lg:col-span-7 space-y-2">
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center relative overflow-hidden">
              <div class="text-[11px] font-bold text-slate-300 mb-2 flex justify-between items-center">
                <span>مقطع رأسي هندسي تفاعلي: السلالم والدرابزين المزدوج (Elevation Section)</span>
                <span class="text-teal-400 font-mono text-[10px]">م.ب.ع 202: بند 3-3</span>
              </div>
              <div class="w-full overflow-x-auto flex justify-center">
                <svg id="stairs-svg" viewBox="0 0 520 280" class="w-full max-w-[500px] h-[260px] bg-slate-950 rounded-lg border border-slate-800">
                  <!-- Ground / Lower Landing -->
                  <line x1="20" y1="230" x2="160" y2="230" stroke="#475569" stroke-width="4"/>
                  
                  <!-- Tactile Warning Strip on Lower Landing (x: 50 to 140) -->
                  <rect id="stairs-tactile-rect" x="60" y="222" width="80" height="8" fill="#f59e0b" stroke="#d97706" rx="2"/>
                  <text id="stairs-tactile-text" x="100" y="214" fill="#fde68a" font-size="9" text-anchor="middle" font-weight="bold">بلاط تحذيري 60سم</text>

                  <!-- Steps Profile (3 steps) -->
                  <!-- Step 1: x160, y230 -> x160, y175 -> x260, y175 -->
                  <!-- Step 2: x260, y175 -> x260, y120 -> x360, y120 -->
                  <!-- Step 3 / Upper Landing: x360, y120 -> x360, y65 -> x490, y65 -->
                  <path id="stairs-steps-path" d="M 20 230 L 160 230 L 160 175 L 260 175 L 260 120 L 360 120 L 360 65 L 490 65" fill="none" stroke="#38bdf8" stroke-width="4"/>
                  
                  <!-- Step Hatch Solid Fill -->
                  <path d="M 160 230 L 160 175 L 260 175 L 260 120 L 360 120 L 360 65 L 490 65 L 490 230 Z" fill="#0f172a" fill-opacity="0.8"/>

                  <!-- Upper Landing Warning Strip -->
                  <rect x="375" y="57" width="80" height="8" fill="#f59e0b" stroke="#d97706" rx="2"/>

                  <!-- Dimension Callouts -->
                  <!-- Riser callout (Step 1) -->
                  <line x1="145" y1="230" x2="145" y2="175" stroke="#10b981" stroke-width="1.5"/>
                  <rect x="85" y="190" width="55" height="20" rx="3" fill="#064e3b" stroke="#10b981"/>
                  <text id="stairs-svg-riser-text" x="112" y="204" fill="#a7f3d0" font-size="10" text-anchor="middle" font-weight="bold">R: 15سم</text>

                  <!-- Tread callout (Step 1) -->
                  <line x1="160" y1="165" x2="260" y2="165" stroke="#10b981" stroke-width="1.5"/>
                  <rect x="182" y="140" width="55" height="20" rx="3" fill="#064e3b" stroke="#10b981"/>
                  <text id="stairs-svg-tread-text" x="210" y="154" fill="#a7f3d0" font-size="10" text-anchor="middle" font-weight="bold">T: 30سم</text>

                  <!-- Dual Handrails (Upper 85cm, Lower 65cm) with 30cm extensions -->
                  <!-- Handrail Posts -->
                  <line x1="160" y1="230" x2="160" y2="90" stroke="#64748b" stroke-width="3"/>
                  <line x1="260" y1="175" x2="260" y2="35" stroke="#64748b" stroke-width="3"/>
                  <line x1="360" y1="120" x2="360" y2="-20" stroke="#64748b" stroke-width="3"/>

                  <!-- Upper Handrail (85cm) -->
                  <path id="stairs-handrail-upper" d="M 120 145 L 160 145 L 360 35 L 430 35" fill="none" stroke="#2dd4bf" stroke-width="4.5" stroke-linecap="round"/>
                  <circle cx="120" cy="145" r="4" fill="#2dd4bf"/>
                  <circle cx="430" cy="35" r="4" fill="#2dd4bf"/>
                  <rect x="420" y="12" width="85" height="18" rx="3" fill="#134e4a" stroke="#2dd4bf"/>
                  <text x="462" y="25" fill="#99f6e4" font-size="9" text-anchor="middle" font-weight="bold">درابزين 85سم</text>

                  <!-- Lower Handrail (65cm) -->
                  <path id="stairs-handrail-lower" d="M 120 165 L 160 165 L 360 55 L 430 55" fill="none" stroke="#14b8a6" stroke-width="3.5" stroke-linecap="round"/>
                  <rect x="420" y="70" width="85" height="18" rx="3" fill="#134e4a" stroke="#14b8a6"/>
                  <text x="462" y="83" fill="#99f6e4" font-size="9" text-anchor="middle" font-weight="bold">سفلي 65سم للأطفال</text>

                  <!-- 30cm Extension Callout -->
                  <line x1="120" y1="135" x2="160" y2="135" stroke="#f59e0b" stroke-width="1.5" stroke-dasharray="2"/>
                  <text x="140" y="128" fill="#fde68a" font-size="8.5" text-anchor="middle" font-weight="bold">امتداد 30سم</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span id="stairs-verdict-note">✓ السلالم مجهزة بدرابزين مزدوج مستمر وأنف مشطوف يمنع التعثر.</span>
                <span class="text-teal-400 font-bold">كود م.ب.ع 202: بند 3-5</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- MODULE 10: AUDITORIUM, THEATER & STADIUM WHEELCHAIR SEATING -->
      <div id="calc-sec-theater" class="calc-section bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <h3 class="text-base font-bold text-slate-900 dark:text-slate-100 flex items-center gap-2">
              <span class="text-amber-500 font-black">10.</span>
              <span>حاسبة ومحاكي مقاعد المسارح والقاعات (Auditorium & Stadium Seating)</span>
            </h3>
            <p class="text-xs text-slate-500">احتساب مقاعد الكراسي المتحركة الإلزامية ومقاعد المرافقين المصاحبين وفق م.ب.ع 202 (الباب 6-4) و ADA Sec 221.</p>
          </div>
          <span class="text-[10px] bg-amber-50 dark:bg-amber-950/40 text-amber-700 dark:text-amber-300 font-bold px-2 py-0.5 rounded border border-amber-300">نسبة كودية إلزامية</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <div class="lg:col-span-5 space-y-4 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div>
              <div class="flex justify-between items-center mb-1">
                <label class="font-bold text-slate-700 dark:text-slate-300">سعة القاعة الإجمالية (Total Seating Capacity):</label>
                <span class="font-bold text-amber-600 dark:text-amber-400 text-sm" id="theater-cap-val">250 مقعداً</span>
              </div>
              <input type="range" id="theater-cap-slider" min="20" max="1500" value="250" step="10" oninput="runTheaterCalc()" class="w-full accent-amber-600">
              <div class="flex justify-between text-[10px] text-slate-400">
                <span>20 مقعد (قاعة صغيرة)</span>
                <span>300 مقعد (مدرج جامعي)</span>
                <span>1500 مقعد (مسرح كبير)</span>
              </div>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">شكل وطبيعة أرضية القاعة:</label>
              <select id="theater-floor-type" onchange="runTheaterCalc()" class="w-full px-3 py-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
                <option value="raked" selected>مدرج مائل / مسرح متدرج (Raked Floor مع خطوط رؤية علوية)</option>
                <option value="flat">أرضية مستوية (Flat Floor للمؤتمرات والقاعات متعددة الأغراض)</option>
              </select>
            </div>

            <div>
              <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">توزيع وتكامل المواقع في القاعة:</label>
              <div class="space-y-1.5">
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-theater-dispersed" checked onchange="runTheaterCalc()">
                  <span>توزيع مواقع الكراسي في أكثر من صف (أمامي ووسطي) وليس في الخلف فقط</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-theater-companion" checked onchange="runTheaterCalc()">
                  <span>مقعد مرافق مصاحب ملاصق لكل موقع كرسي متحرك (1:1 Companion Seat)</span>
                </label>
                <label class="flex items-center gap-2 cursor-pointer">
                  <input type="checkbox" id="chk-theater-aisle" checked onchange="runTheaterCalc()">
                  <span>توفير 1% مقاعد طرفية بمقابض قابلة للرفع (Aisle Transfer Seats)</span>
                </label>
              </div>
            </div>

            <!-- Code Calculations Breakdown Card -->
            <div class="p-3 bg-white dark:bg-slate-800 rounded-lg border border-slate-200 dark:border-slate-700 space-y-2">
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">مواقع الكراسي المتحركة الإلزامية:</span>
                <span class="font-bold text-blue-600 dark:text-blue-400 text-sm" id="theater-res-wheelchair">5 مواقع</span>
              </div>
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">مقاعد المرافقين المصاحبين (1:1):</span>
                <span class="font-bold text-purple-600 dark:text-purple-400" id="theater-res-companion">5 مقاعد</span>
              </div>
              <div class="flex justify-between items-center text-[11px]">
                <span class="text-slate-500">المقاعد الطرفية الميسرة (Aisle):</span>
                <span class="font-bold text-amber-600 dark:text-amber-400" id="theater-res-aisle">3 مقاعد</span>
              </div>
              <div class="border-t border-slate-100 dark:border-slate-700 pt-2">
                <span class="text-slate-500 text-[10px] block">القرار الهندسي للتراخيص:</span>
                <div id="theater-res-eval" class="text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5">مطابق تماماً لجدول 6-4 لكود م.ب.ع 202</div>
              </div>
            </div>

            <!-- Export Buttons -->
            <div class="flex items-center gap-2 pt-1">
              <button onclick="exportToDXF('theater')" class="flex-1 bg-slate-800 hover:bg-slate-700 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📐</span> <span>تصدير كاد (.DXF)</span>
              </button>
              <button onclick="exportTenderSpecs('theater')" class="flex-1 bg-amber-700 hover:bg-amber-600 text-white font-bold py-2 px-3 rounded-lg text-xs flex items-center justify-center gap-1.5 transition">
                <span>📑</span> <span>كراسة المواصفات</span>
              </button>
            </div>
          </div>

          <!-- Visual SVG Simulator (Module 10) -->
          <div class="lg:col-span-7 space-y-2">
            <div class="bg-slate-900 p-3 rounded-xl border border-slate-800 text-center relative overflow-hidden">
              <div class="text-[11px] font-bold text-slate-300 mb-2 flex justify-between items-center">
                <span>مسقط ومقطع تفاعلي: توزيع مقاعد الكراسي المتحركة وزوايا الرؤية (Sightlines)</span>
                <span class="text-amber-400 font-mono text-[10px]">م.ب.ع 202: بند 6-4</span>
              </div>
              <div class="w-full overflow-x-auto flex justify-center">
                <svg id="theater-svg" viewBox="0 0 520 280" class="w-full max-w-[500px] h-[260px] bg-slate-950 rounded-lg border border-slate-800">
                  <!-- Stage / Screen at Front (Top) -->
                  <rect x="110" y="15" width="300" height="28" fill="#1e293b" stroke="#f59e0b" stroke-width="2" rx="4"/>
                  <text x="260" y="33" fill="#fde68a" font-size="12" font-weight="black" text-anchor="middle">منصة المسرح والشاشة (STAGE / SCREEN) 🎬</text>

                  <!-- Standard Rows of Seats (Gray Dots/Bars) -->
                  <!-- Row 1 -->
                  <g fill="#334155">
                    <rect x="70" y="60" width="160" height="16" rx="3"/>
                    <rect x="290" y="60" width="160" height="16" rx="3"/>
                  </g>
                  <!-- Row 2 -->
                  <g fill="#334155">
                    <rect x="60" y="90" width="150" height="16" rx="3"/>
                    <rect x="310" y="90" width="150" height="16" rx="3"/>
                  </g>
                  <!-- Central Aisle -->
                  <line x1="260" y1="50" x2="260" y2="250" stroke="#475569" stroke-width="1.5" stroke-dasharray="3"/>
                  <text x="260" y="160" fill="#64748b" font-size="9" text-anchor="middle">ممر التوزيع 150سم</text>

                  <!-- Wheelchair Spaces (Row 3 - Prime Seating Tier) -->
                  <!-- Space 1 Left -->
                  <g id="theater-wc-1">
                    <rect x="110" y="125" width="55" height="38" fill="rgba(2, 132, 199, 0.3)" stroke="#0284c7" stroke-width="2" rx="4"/>
                    <text x="137" y="148" fill="#38bdf8" font-size="15" text-anchor="middle" font-weight="bold">♿</text>
                    <rect x="168" y="125" width="35" height="38" fill="#581c87" stroke="#a855f7" stroke-width="1.5" rx="4"/>
                    <text x="185" y="148" fill="#e9d5ff" font-size="11" text-anchor="middle" font-weight="bold">مرافق</text>
                  </g>

                  <!-- Space 2 Right -->
                  <g id="theater-wc-2">
                    <rect x="315" y="125" width="35" height="38" fill="#581c87" stroke="#a855f7" stroke-width="1.5" rx="4"/>
                    <text x="332" y="148" fill="#e9d5ff" font-size="11" text-anchor="middle" font-weight="bold">مرافق</text>
                    <rect x="355" y="125" width="55" height="38" fill="rgba(2, 132, 199, 0.3)" stroke="#0284c7" stroke-width="2" rx="4"/>
                    <text x="382" y="148" fill="#38bdf8" font-size="15" text-anchor="middle" font-weight="bold">♿</text>
                  </g>

                  <!-- Row 4 -->
                  <g fill="#334155">
                    <rect x="50" y="180" width="180" height="16" rx="3"/>
                    <rect x="290" y="180" width="180" height="16" rx="3"/>
                  </g>
                  <!-- Row 5 -->
                  <g fill="#334155">
                    <rect x="40" y="210" width="190" height="16" rx="3"/>
                    <rect x="290" y="210" width="190" height="16" rx="3"/>
                  </g>

                  <!-- Sightline Vector Ray (Blue dashed line toward stage) -->
                  <line x1="137" y1="125" x2="200" y2="43" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>
                  <line x1="382" y1="125" x2="320" y2="43" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4"/>

                  <!-- Dimension Badges -->
                  <rect x="85" y="245" width="140" height="22" rx="4" fill="#0c4a6e" stroke="#0284c7"/>
                  <text x="155" y="259" fill="#7dd3fc" font-size="9.5" text-anchor="middle" font-weight="bold">موقع كرسي 90 × 125 سم</text>

                  <rect x="295" y="245" width="140" height="22" rx="4" fill="#3b0764" stroke="#a855f7"/>
                  <text x="365" y="259" fill="#f3e8ff" font-size="9.5" text-anchor="middle" font-weight="bold">مقعد مرافق ملاصق (1:1)</text>
                </svg>
              </div>
              <div class="text-[11px] text-slate-300 mt-2 flex items-center justify-between">
                <span id="theater-verdict-note">✓ مواقع الكراسي موزعة هندسياً وتحقق زاوية رؤية مستمرة دون حجب.</span>
                <span class="text-amber-400 font-bold">كود م.ب.ع 202: بند 6-4</span>
              </div>
            </div>
          </div>
        </div>
      </div>
'''

    # Insert after calc-sec-reach closing div
    reach_end_marker = '      </div>\n\n    </section>'
    if reach_end_marker in html:
        html = html.replace(reach_end_marker, f'      </div>\n{modules_html}\n    </section>')
        print("✓ Injected Modules 8, 9, 10 into HTML layout")
    else:
        # try regex search
        pattern = r'(<div id="calc-sec-reach"[^>]*>[\s\S]*?<\/div>\s*<\/div>\s*)(<\/section>)'
        html = re.sub(pattern, lambda m: m.group(1) + modules_html + '\n    ' + m.group(2), html, count=1)
        print("✓ Injected Modules 8, 9, 10 into HTML layout via regex")

    # 4. Update switchCalcSubTab JavaScript function
    old_switch_fn = '''    // Sub-Tab Switcher
    function switchCalcSubTab(subtab) {
      const sections = ['ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach'];
      const buttons = ['all', 'ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach'];'''

    new_switch_fn = '''    // Sub-Tab Switcher
    function switchCalcSubTab(subtab) {
      const sections = ['ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach', 'rescue', 'stairs', 'theater'];
      const buttons = ['all', 'ramps', 'restroom', 'parking', 'doors', 'elevators', 'curb', 'reach', 'rescue', 'stairs', 'theater'];'''

    html = html.replace(old_switch_fn, new_switch_fn)
    print("✓ Updated switchCalcSubTab with 10 modules")

    # 5. Add JavaScript Calculation Functions for Modules 8, 9, 10
    new_js_functions = '''
    // --- MODULE 8: EMERGENCY RESCUE AREAS SIMULATOR ---
    function runRescueCalc() {
      const stairWidth = parseInt(document.getElementById('rescue-stair-width').value) || 150;
      const spaces = parseInt(document.querySelector('input[name="rescue-spaces"]:checked').value) || 1;
      const firewall = document.getElementById('chk-rescue-firewall').checked;
      const intercom = document.getElementById('chk-rescue-intercom').checked;
      const clearpath = document.getElementById('chk-rescue-clearpath').checked;

      const spaceWidth = spaces === 1 ? 76 : 152;
      const spaceDepth = 122;

      document.getElementById('rescue-res-dims').innerText = `${spaceWidth} × ${spaceDepth} سم (${spaces === 1 ? 'موقع فردي' : 'موقع مزدوج'})`;
      
      const pathRemaining = stairWidth;
      document.getElementById('rescue-res-path').innerText = `${pathRemaining} سم (${pathRemaining >= 120 ? 'كافٍ وسلس' : 'ضيق بحاجة لتوسيع'})`;

      const evalElem = document.getElementById('rescue-res-eval');
      const noteElem = document.getElementById('rescue-verdict-note');
      const box = document.getElementById('rescue-space-box');

      const isCompliant = firewall && intercom && clearpath && pathRemaining >= 120;

      if (isCompliant) {
        evalElem.innerText = 'معتمد بالفئة الذهبية - فضاء إنقاذ آمن مستوفٍ للكود';
        evalElem.className = 'text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5';
        if (noteElem) noteElem.innerText = '✓ فضاء الكرسي المتحرك مؤمن بالكامل ومجهز باتصال طوارئ ولا يعترض مسار الإخلاء.';
        if (box) {
          box.setAttribute('stroke', '#10b981');
          box.setAttribute('fill', 'rgba(16, 185, 129, 0.25)');
        }
      } else {
        let issues = [];
        if (!firewall) issues.push('غياب عزل الحريق 2 ساعة');
        if (!intercom) issues.push('غياب هاتف الطوارئ ثنائي الاتجاه');
        if (!clearpath) issues.push('تداخل الفضاء مع مسار هروب المشاة');
        evalElem.innerText = `مرفوض هندسياً: ${issues.join(' | ')}`;
        evalElem.className = 'text-sm font-black text-rose-600 dark:text-rose-400 mt-0.5';
        if (noteElem) noteElem.innerText = '❌ تحذير: فضاء الإنقاذ غير آمن وقد يتسبب في محاصرة ذوي الإعاقة أو إعاقة الإخلاء.';
        if (box) {
          box.setAttribute('stroke', '#ef4444');
          box.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
        }
      }
    }

    // --- MODULE 9: ACCESSIBLE STAIRS & DUAL HANDRAILS SIMULATOR ---
    function runStairsCalc() {
      const riser = parseFloat(document.getElementById('stairs-riser-slider').value) || 15;
      const tread = parseFloat(document.getElementById('stairs-tread-slider').value) || 30;
      const nosing = document.getElementById('stairs-nosing-type').value;
      const extension = document.getElementById('chk-stairs-extension').checked;
      const tactile = document.getElementById('chk-stairs-tactile').checked;

      document.getElementById('stairs-riser-val').innerText = `${riser} سم`;
      document.getElementById('stairs-tread-val').innerText = `${tread} سم`;

      // Comfort Formula: 2R + T
      const formulaVal = Math.round((2 * riser) + tread);
      document.getElementById('stairs-res-formula').innerText = `${formulaVal} سم (المثالي: 60 - 64 سم)`;

      const evalElem = document.getElementById('stairs-res-eval');
      const noteElem = document.getElementById('stairs-verdict-note');
      
      const riserOk = riser <= 18 && riser >= 12;
      const treadOk = tread >= 28;
      const nosingOk = nosing !== 'abrupt';
      const formulaOk = formulaVal >= 59 && formulaVal <= 65;

      const isCompliant = riserOk && treadOk && nosingOk && extension && tactile;

      if (isCompliant) {
        evalElem.innerText = `مطابق 100% لكود م.ب.ع 202 (2R+T=${formulaVal}سم - صعود مريح جداً)`;
        evalElem.className = 'text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5';
        if (noteElem) noteElem.innerText = '✓ السلالم مجهزة بدرابزين مزدوج مستمر وأنف مشطوف وبلاط تحذيري يمنع السقوط.';
      } else {
        let defects = [];
        if (!riserOk) defects.push(riser > 18 ? 'القائمة مرتفعة جداً' : 'القائمة منخفضة');
        if (!treadOk) defects.push('النائمة ضيقة (<28سم)');
        if (!nosingOk) defects.push('أنف الدرجة بارز ومعرقل');
        if (!extension) defects.push('غياب امتداد الدرابزين 30سم');
        if (!tactile) defects.push('غياب شريط التحذير اللمسي');
        evalElem.innerText = `ملاحظات: ${defects.join('، ')}`;
        evalElem.className = 'text-sm font-black text-amber-600 dark:text-amber-400 mt-0.5';
        if (noteElem) noteElem.innerText = '⚠️ يتطلب تصحيح أبعاد الدرجة وملحقات السلامة لتفادي حوادث السقوط والتعثر.';
      }

      // Update SVG elements
      const riserText = document.getElementById('stairs-svg-riser-text');
      const treadText = document.getElementById('stairs-svg-tread-text');
      if (riserText) riserText.textContent = `R: ${riser}سم`;
      if (treadText) treadText.textContent = `T: ${tread}سم`;

      const tactileRect = document.getElementById('stairs-tactile-rect');
      const tactileText = document.getElementById('stairs-tactile-text');
      if (tactileRect) tactileRect.style.display = tactile ? 'block' : 'none';
      if (tactileText) tactileText.style.display = tactile ? 'block' : 'none';
    }

    // --- MODULE 10: AUDITORIUM & THEATER SEATING CALCULATOR ---
    function runTheaterCalc() {
      const cap = parseInt(document.getElementById('theater-cap-slider').value) || 250;
      const floor = document.getElementById('theater-floor-type').value;
      const dispersed = document.getElementById('chk-theater-dispersed').checked;
      const companion = document.getElementById('chk-theater-companion').checked;
      const aisle = document.getElementById('chk-theater-aisle').checked;

      document.getElementById('theater-cap-val').innerText = `${cap} مقعداً`;

      // Code Table 221.2 calculation
      let reqSpaces = 1;
      if (cap <= 25) reqSpaces = 1;
      else if (cap <= 50) reqSpaces = 2;
      else if (cap <= 150) reqSpaces = 4;
      else if (cap <= 300) reqSpaces = 5;
      else if (cap <= 500) reqSpaces = 6;
      else reqSpaces = 6 + Math.ceil((cap - 500) / 150);

      const companionSpaces = companion ? reqSpaces : 0;
      const aisleSeats = Math.max(1, Math.round(cap * 0.01));

      document.getElementById('theater-res-wheelchair').innerText = `${reqSpaces} مواقع كراسي متحركة`;
      document.getElementById('theater-res-companion').innerText = `${companionSpaces} مقاعد مرافقين (1:1 ملاصق)`;
      document.getElementById('theater-res-aisle').innerText = `${aisleSeats} مقاعد بمقابض قابلة للطي`;

      const evalElem = document.getElementById('theater-res-eval');
      const noteElem = document.getElementById('theater-verdict-note');

      const isCompliant = dispersed && companion && aisle;

      if (isCompliant) {
        evalElem.innerText = `مطابق لكود م.ب.ع 202 (الباب 6-4) - مخصص ${reqSpaces} مواقع مدمجة`;
        evalElem.className = 'text-sm font-black text-emerald-700 dark:text-emerald-400 mt-0.5';
        if (noteElem) noteElem.innerText = '✓ مواقع الكراسي موزعة هندسياً في الصفوف المتميزة وتؤمن خط رؤية حر فوق الواقفين.';
      } else {
        evalElem.innerText = 'اعتماد جزئي مشروط - يلزم دمج المقاعد ومقاعد المرافقين بمحاذاة الكراسي';
        evalElem.className = 'text-sm font-black text-amber-600 dark:text-amber-400 mt-0.5';
        if (noteElem) noteElem.innerText = '⚠️ يمنع عزل مستخدمي الكراسي المتحركة في الصف الأخير فقط طبقاً للكود العراقي.';
      }
    }
'''

    # Insert JS functions right before exportToDXF
    dxf_marker = '    function exportToDXF(type) {'
    if dxf_marker in html:
        html = html.replace(dxf_marker, f'{new_js_functions}\n{dxf_marker}')
        print("✓ Injected JS Calculation Functions for Modules 8, 9, 10")
    else:
        print("Error: exportToDXF marker not found!")

    # 6. Update exportToDXF for rescue, stairs, theater
    old_dxf_tail = '''      } else {
        entities += dxfLine(0, 0, 1500, 0, 'DETAIL');
        entities += dxfLine(1500, 0, 1500, 1000, 'DETAIL');
      }'''

    new_dxf_tail = '''      } else if (type === 'rescue') {
        entities += dxfLine(0, 0, 2400, 0, 'FIRE_WALL');
        entities += dxfLine(2400, 0, 2400, 2000, 'FIRE_WALL');
        entities += dxfLine(2400, 2000, 0, 2000, 'FIRE_WALL');
        entities += dxfLine(0, 2000, 0, 0, 'FIRE_WALL');
        entities += dxfLine(300, 300, 1060, 300, 'REFUGE_SPACE_760x1220');
        entities += dxfLine(1060, 300, 1060, 1520, 'REFUGE_SPACE_760x1220');
        entities += dxfLine(1060, 1520, 300, 1520, 'REFUGE_SPACE_760x1220');
        entities += dxfLine(300, 1520, 300, 300, 'REFUGE_SPACE_760x1220');
        entities += dxfCircle(680, 910, 250, 'WHEELCHAIR_SYMBOL');
        entities += dxfText(300, 1600, 60, 'AREA OF RESCUE ASSISTANCE (760x1220MM)', 'ANNOTATION');
        entities += dxfText(1200, 1000, 70, 'EGRESS EVACUATION PATH (CLEAR >= 1200MM)', 'ANNOTATION');
      } else if (type === 'stairs') {
        const r = parseFloat(document.getElementById('stairs-riser-slider').value) || 15;
        const t = parseFloat(document.getElementById('stairs-tread-slider').value) || 30;
        let curX = 0, curY = 0;
        for (let s = 0; s < 5; s++) {
          entities += dxfLine(curX, curY, curX, curY + (r * 10), 'RISER');
          curY += (r * 10);
          entities += dxfLine(curX, curY, curX + (t * 10), curY, 'TREAD');
          curX += (t * 10);
        }
        entities += dxfLine(-300, 850, curX + 300, curY + 850, 'HANDRAIL_UPPER_850');
        entities += dxfLine(-300, 650, curX + 300, curY + 650, 'HANDRAIL_LOWER_650');
        entities += dxfText(100, curY + 1100, 70, `ACCESSIBLE STAIR SECTION (RISER ${r}CM, TREAD ${t}CM)`, 'TITLE');
      } else if (type === 'theater') {
        const cap = parseInt(document.getElementById('theater-cap-slider').value) || 250;
        entities += dxfLine(0, 0, 6000, 0, 'STAGE_FRONT');
        entities += dxfLine(6000, 0, 6000, 1500, 'STAGE_FRONT');
        entities += dxfLine(6000, 1500, 0, 1500, 'STAGE_FRONT');
        entities += dxfLine(0, 1500, 0, 0, 'STAGE_FRONT');
        entities += dxfLine(1000, 3000, 1900, 3000, 'WHEELCHAIR_SPACE_900x1250');
        entities += dxfLine(1900, 3000, 1900, 4250, 'WHEELCHAIR_SPACE_900x1250');
        entities += dxfLine(1900, 4250, 1000, 4250, 'WHEELCHAIR_SPACE_900x1250');
        entities += dxfLine(1000, 4250, 1000, 3000, 'WHEELCHAIR_SPACE_900x1250');
        entities += dxfCircle(1450, 3625, 300, 'WHEELCHAIR_SYMBOL');
        entities += dxfText(2000, 3625, 70, 'COMPANION SEAT (1:1 ADJACENT)', 'ANNOTATION');
      } else {
        entities += dxfLine(0, 0, 1500, 0, 'DETAIL');
        entities += dxfLine(1500, 0, 1500, 1000, 'DETAIL');
      }'''

    html = html.replace(old_dxf_tail, new_dxf_tail)
    print("✓ Extended exportToDXF with rescue, stairs, and theater support")

    # 7. Update exportTenderSpecs for rescue, stairs, theater
    old_specs_tail = '''      } else {
        specTitle = `المواصفة الفنية القياسية المعتمدة - ${type}`;
        specBody = `تخضع كافة الأعمال للاشتراطات الفنية لمدونة البناء العراقية (م.ب.ع 202) وتعديلات كود ADA 2010.`;
      }'''

    new_specs_tail = '''      } else if (type === 'rescue') {
        specTitle = 'المواصفة الفنية لفضاءات الإنقاذ والإخلاء الآمن في الأدراج (Areas of Rescue Assistance)';
        specBody = `### مواصفة البند (C-202-RESCUE):
1. **الفضاء المعماري:** يجب توفير فضاء انتظار آمن ومستقل لمستخدمي الكراسي المتحركة داخل بسطة بيت الدرج أو ردهة مهرب الحريق بأبعاد صافية لا تقل عن 76 × 122 سم لكل كرسي.
2. **عدم إعاقة مسار الهروب (Zero Encroachment):** يمنع منعاً باتاً أن يتداخل فضاء الكرسي المتحرك أو قوس فتح باب الحريق مع عرض مسار هروب المشاة الإلزامي (عرض المهرب الصافي لا يقل عن 120 سم).
3. **مقاومة الحريق والدخان:** عزل بيت الدرج بجدران وأبواب مانعة لانتشار النيران والدخان بتصنيف مقاومة حريق لا يقل عن ساعتين (2 Hours Fire-Rated Enclosure)، مع تزويد بيت الدرج بنظام ضغط هواء ميكانيكي إيجابي (Positive Air Pressurization) لمنع دخول الدخان السام.
4. **نظام الاتصال والإنذار ثنائي الاتجاه:** تركيب جهاز اتصال صوتي داخلي مرئي ومسموع (Two-Way Emergency Communication System) مربوط مباشرة مع غرفة التحكم المركزية للمبنى ومركز الدفاع المدني، بارتفاع تشغيل 90 - 120 سم، مزود بزر استدعاء SOS وضوء إشارة وصول النجدة.`;
      } else if (type === 'stairs') {
        specTitle = 'المواصفة الفنية للسلالم المعمارية الميسرة والدرابزين المزدوج';
        specBody = `### مواصفة البند (C-202-STAIRS):
1. **أبعاد الدرجات الهندسية:** يجب أن يكون ارتفاع القائمة (Riser) منتظماً تماماً بين 14 و 17 سم (الحد الأقصى المطلق 18 سم)، وعرض النائمة (Tread) لا يقل عن 28 إلى 30 سم، مع الالتزام الصارم بمعادلة راحة الدرج: 2R + T = 60 إلى 64 سم.
2. **أنف الدرجة (Nosings):** يجب أن تكون أنوف الدرجات مشطوفة بزاوية 60° ملساء أو مستوية تماماً مع القائمة (Flush)، ويحظر حظراً تاماً استخدام الأنوف البارزة المعلقة الحادة لتفادي تعثر مشط القدم أثناء الصعود.
3. **الدرابزين المزدوج المستمر:** تثبيت درابزين مزدوج مستمر على كلا جانبي الدرج بدون انقطاع عند البسطات؛ الماسورة العليا بارتفاع 85 - 90 سم، والماسورة السفلى بارتفاع 65 - 70 سم، بقطر دائري أملس 38 - 45 ملم، مع امتداد أفقي بطول 30 سم عند بداية الدرج ونهايته ينتهي باستدارة كروية نحو الجدار أو الأرض.
4. **شريط التحذير اللمسي:** تركيب شريط بلاط تحذيري بنقاط بارزة (Tactile Blister Pavers) بعمق 60 سم وبلون متباين (أصفر عاكس) قبل أول درجة في الأعلى والأسفل لتنبيه المكفوفين وضعاف البصر بوجود درج.`;
      } else if (type === 'theater') {
        specTitle = 'المواصفة الفنية لمقاعد الكراسي المتحركة في المسارح والقاعات والمدرجات';
        specBody = `### مواصفة البند (C-202-THEATER):
1. **النسبة الإلزامية للمقاعد:** تخصيص مواقع كراسي متحركة طبقاً للجدول القياسي 6-4 لكود م.ب.ع 202 (مثال: 5 مواقع لقاعة 300 مقعد، 6 مواقع لقاعة 500 مقعد، مضافاً إليها موقع لكل 150 مقعداً إضافياً).
2. **أبعاد موقع الكرسي:** أبعاد الفضاء الصافي لموقع الكرسي الواحد 90 سم عرضاً × 125 سم عمقاً للاقتراب الأمامي (أو 150 سم للاقتراب الجانبي)، بأرضية مستوية تماماً بميل تصريف لا يتجاوز 1:50.
3. **مقاعد المرافقين المصاحبين (1:1 Companion Seats):** توفير مقعد اعتيادي ملاصق في نفس الصف ونفس المستوى لكل موقع كرسي متحرك للمرافقين والأسرة.
4. **التوزيع الأفقي والرأسي وخطوط الرؤية (Lines of Sight):** يجب توزيع مواقع الكراسي في مختلف مناطق القاعة (الصفوف الأمامية والوسطى) وعدم عزلها في الصف الأخير فقط، مع ضمان خط رؤية مريح وغير محجوب فوق رؤوس المشاهدين الجالسين والواقفين (Sightlines Over Standing Spectators).
5. **المقاعد الطرفية الميسرة (Aisle Seats):** تخصيص ما لا يقل عن 1% من مقاعد القاعة على الأطراف بمقابض أذرع قابلة للرفع لتسهيل انتقال كبار السن ومستخدمي العكازات.`;
      } else {
        specTitle = `المواصفة الفنية القياسية المعتمدة - ${type}`;
        specBody = `تخضع كافة الأعمال للاشتراطات الفنية لمدونة البناء العراقية (م.ب.ع 202) وتعديلات كود ADA 2010.`;
      }'''

    html = html.replace(old_specs_tail, new_specs_tail)
    print("✓ Extended exportTenderSpecs with rescue, stairs, and theater specifications")

    # 8. Add onLoad initialization for rescue, stairs, theater
    old_onload = '''      if (typeof runCurbCalc === 'function') runCurbCalc();
      if (typeof runReachCalc === 'function') runReachCalc();'''

    new_onload = '''      if (typeof runCurbCalc === 'function') runCurbCalc();
      if (typeof runReachCalc === 'function') runReachCalc();
      if (typeof runRescueCalc === 'function') runRescueCalc();
      if (typeof runStairsCalc === 'function') runStairsCalc();
      if (typeof runTheaterCalc === 'function') runTheaterCalc();'''

    html = html.replace(old_onload, new_onload)
    print("✓ Added onload initialization for 3 new simulators")

    # Write to iraqi_accessibility_platform.html and index.html
    with open('iraqi_accessibility_platform.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Successfully saved changes to iraqi_accessibility_platform.html and index.html")

    return True

if __name__ == '__main__':
    build_expansion()
