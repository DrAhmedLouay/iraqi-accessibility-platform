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
              <span class="text-2xl">🗺️</span>
              <div>
                <h3 class="text-base sm:text-lg font-black text-slate-900 dark:text-slate-100 flex items-center gap-2">
                  <span>الخارطة الجغرافية الوطنية التفاعلية لمباني العراق (GIS Accessibility Map)</span>
                  <span class="text-xs bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 px-2.5 py-0.5 rounded-full font-bold border border-emerald-300 dark:border-emerald-800 flex items-center gap-1">
                    <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
                    نظام GIS حقيقي مباشر
                  </span>
                </h3>
                <p class="text-xs text-slate-500 mt-0.5">رصد جغرافي حقيقي لنسب الامتثال والجاهزية عبر محافظات العراق الـ 18 مستند إلى بيانات مكانية وقمرية حية.</p>
              </div>
            </div>
          </div>
          <!-- Regional Filter Buttons -->
          <div class="flex flex-wrap items-center gap-1.5 text-xs">
            <span class="text-slate-400 font-bold text-[11px] ml-1">تصفية حسب الإقليم:</span>
            <button onclick="filterGovRegion('all')" id="btn-reg-all" class="px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold transition">كل المحافظات (18)</button>
            <button onclick="filterGovRegion('center')" id="btn-reg-center" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">بغداد والوسط</button>
            <button onclick="filterGovRegion('south')" id="btn-reg-south" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الجنوب</button>
            <button onclick="filterGovRegion('north')" id="btn-reg-north" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الشمال وكردستان</button>
            <button onclick="filterGovRegion('west')" id="btn-reg-west" class="px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition">الأنبار وغرب العراق</button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Real Interactive GIS Map (Leaflet.js) -->
          <div class="lg:col-span-7 bg-slate-950 rounded-2xl p-4 border border-slate-800 flex flex-col relative overflow-hidden shadow-lg">
            <div class="w-full flex flex-wrap justify-between items-center text-xs text-slate-400 mb-3 pb-2 border-b border-slate-800 gap-2">
              <div class="flex items-center gap-2">
                <span class="text-slate-300 font-bold">المحافظة النشطة:</span>
                <span id="gis-selected-gov" class="text-emerald-400 font-black text-sm">بغداد (العاصمة)</span>
              </div>
              
              <!-- Map Layer Switcher Buttons -->
              <div class="flex items-center gap-1 text-[11px]">
                <button onclick="setMapBaseLayer('dark')" id="btn-layer-dark" class="px-2 py-1 rounded-lg bg-emerald-600 text-white font-bold transition">🌙 مظلمة GIS</button>
                <button onclick="setMapBaseLayer('streets')" id="btn-layer-streets" class="px-2 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition">☀️ شوارع</button>
                <button onclick="setMapBaseLayer('satellite')" id="btn-layer-satellite" class="px-2 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition">🛰️ قمر صناعي</button>
                <button onclick="resetIraqMap()" class="px-2 py-1 rounded-lg bg-slate-800 text-sky-400 hover:bg-slate-700 font-bold transition" title="إعادة ضبط الرؤية">🔄 إعادة ضبط</button>
              </div>
            </div>

            <!-- Leaflet Interactive Map Container -->
            <div id="iraq-leaflet-map" style="width: 100%; height: 430px; min-height: 430px; border-radius: 12px; z-index: 10;" class="shadow-inner relative"></div>

            <!-- Map Legend / Heatmap Indicator -->
            <div class="mt-3 flex flex-wrap items-center justify-between gap-2 text-[11px] text-slate-400 bg-slate-900/90 px-3.5 py-2.5 rounded-xl border border-slate-800">
              <span class="font-bold text-slate-200">مؤشر الامتثال الجغرافي:</span>
              <div class="flex flex-wrap items-center gap-3">
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-emerald-500 inline-block shadow-sm shadow-emerald-500/50"></span> ≥ 80% (متقدم)</span>
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-sky-500 inline-block shadow-sm shadow-sky-500/50"></span> 70-79% (لجنة مفعلة)</span>
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-amber-500 inline-block shadow-sm shadow-amber-500/50"></span> 60-69% (قيد التأهيل)</span>
                <span class="flex items-center gap-1.5"><span class="w-3 h-3 rounded-full bg-rose-500 inline-block shadow-sm shadow-rose-500/50"></span> &lt; 60% (تدخل عاجل)</span>
              </div>
            </div>
          </div>

          <!-- Governorate Readiness & Analytics Card -->
          <div class="lg:col-span-5 bg-slate-50 dark:bg-slate-900 rounded-2xl p-5 border border-slate-200 dark:border-slate-800 space-y-4">
            <div class="flex justify-between items-start border-b border-slate-200 dark:border-slate-800 pb-3">
              <div>
                <span class="text-[10px] text-slate-500 font-bold uppercase tracking-wider">سجل المحافظة واللجنة البلدية</span>
                <h4 id="gov-card-title" class="text-lg font-black text-slate-900 dark:text-slate-100">أمانة بغداد</h4>
              </div>
              <span id="gov-card-status" class="text-xs bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 px-2.5 py-1 rounded-full font-bold">لجنة فحص مفعلة</span>
            </div>

            <div class="bg-white dark:bg-slate-800/80 rounded-xl p-3.5 border border-slate-200 dark:border-slate-700/60">
              <div class="text-xs text-slate-500 font-medium">معدل الامتثال الكلي للمحافظة (م.ب.ع 202)</div>
              <div class="flex items-baseline gap-2 mt-1">
                <span id="gov-card-rate" class="text-3xl font-black text-emerald-600 dark:text-emerald-400">76.4%</span>
                <span class="text-xs text-slate-500">من إجمالي المباني الحكومية والخدمية</span>
              </div>
              <div class="w-full bg-slate-200 dark:bg-slate-700 h-2 rounded-full mt-2 overflow-hidden">
                <div class="bg-emerald-500 h-2 rounded-full transition-all duration-500" style="width: 76.4%"></div>
              </div>
            </div>

            <div class="grid grid-cols-3 gap-2 text-center text-xs">
              <div class="p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
                <div class="text-slate-400 text-[10px]">المباني المفحوصة</div>
                <div id="gov-stat-total" class="text-base font-bold text-slate-800 dark:text-slate-200 mt-0.5">142 مبنى</div>
              </div>
              <div class="p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
                <div class="text-slate-400 text-[10px]">معتمدة ومطابقة</div>
                <div id="gov-stat-pass" class="text-base font-bold text-emerald-600 mt-0.5">89 مبنى</div>
              </div>
              <div class="p-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700">
                <div class="text-slate-400 text-[10px]">قيد التحوير</div>
                <div id="gov-stat-retro" class="text-base font-bold text-amber-600 mt-0.5">53 مبنى</div>
              </div>
            </div>

            <div>
              <div class="text-xs font-bold text-slate-700 dark:text-slate-300 mb-2">أبرز مشاريع ومباني المحافظة المسجلة:</div>
              <div id="gov-projects-list" class="space-y-1.5 text-xs">
                <!-- Injected via JS -->
              </div>
            </div>

            <div class="pt-2 border-t border-slate-200 dark:border-slate-800 flex justify-between items-center">
              <span class="text-[10px] text-slate-500">نظام الرقابة البلدية المركزي 2026</span>
              <div class="flex gap-2">
                <button onclick="exportGovReport()" class="text-xs bg-slate-200 dark:bg-slate-800 hover:bg-slate-300 text-slate-700 dark:text-slate-300 font-bold px-3 py-1.5 rounded-lg transition">📄 تصدير تقرير المحافظة</button>
              </div>
            </div>
          </div>
        </div>
      </div>'''


