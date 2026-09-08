#!/usr/bin/env python3
"""
build_real_gis_map.py
Injects a REAL, professional, interactive GIS map into Tab 1 of the platform:
- Integrates Leaflet.js with CartoDB Dark Matter, Streets, and Esri Satellite layers.
- Uses official Iraq ADM1 GeoJSON boundaries for all 18 governorates.
- Dynamic color-coding by compliance rate (م.ب.ع 202).
- Interactive hover tooltips and rich click popups with ♿ municipal pins.
- Region filtering (Central, South, North, West) with smooth camera transitions.
- Synchronized with Governorate Analytics Card.
"""

import os
import json
import re

def build_real_gis():
    print("=" * 70)
    print("BUILDING REAL INTERACTIVE GIS MAP (LEAFLET.JS) FOR IRAQ")
    print("=" * 70)

    # 1. Load minified GeoJSON
    with open('scratch/iraq_adm1_minified.json', 'r', encoding='utf-8') as f:
        min_geojson = f.read()
    print(f"✓ Loaded minified GeoJSON: {len(min_geojson)} bytes")

    # 2. Read target HTML
    with open('iraqi_accessibility_platform.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 3. Add Leaflet CSS/JS to <head> if not present
    leaflet_head = '''  <!-- Leaflet.js Real Interactive GIS Map Engine -->
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
  <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
  <style>
    /* Leaflet Real GIS Map Styling */
    .leaflet-container {
      font-family: inherit;
      background: #090d16;
    }
    .gis-tooltip {
      background: rgba(15, 23, 42, 0.94) !important;
      border: 1px solid #0284c7 !important;
      color: #f8fafc !important;
      font-weight: 700 !important;
      font-size: 12px !important;
      border-radius: 8px !important;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5) !important;
      direction: rtl !important;
      text-align: right !important;
      padding: 6px 10px !important;
    }
    .gis-tooltip::before {
      border-top-color: rgba(15, 23, 42, 0.94) !important;
    }
    .leaflet-popup-content-wrapper {
      background: rgba(15, 23, 42, 0.96) !important;
      color: #f8fafc !important;
      border-radius: 12px !important;
      border: 1px solid #38bdf8 !important;
      box-shadow: 0 10px 25px rgba(0,0,0,0.6) !important;
      direction: rtl !important;
      text-align: right !important;
    }
    .leaflet-popup-tip {
      background: rgba(15, 23, 42, 0.96) !important;
    }
    .custom-gov-pin {
      display: flex !important;
      align-items: center !important;
      justify-content: center !important;
    }
    .custom-gov-pin div {
      animation: pulse-ring 2.5s cubic-bezier(0.45, 0, 0.55, 1) infinite;
    }
    @keyframes pulse-ring {
      0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
      70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
      100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
    }
  </style>'''

    if 'leaflet@1.9.4' not in html:
        insert_marker = '<script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.min.js"></script>'
        if insert_marker in html:
            html = html.replace(insert_marker, insert_marker + '\n' + leaflet_head)
            print("✓ Injected Leaflet CSS and JS into <head>")
        else:
            print("❌ Head insert marker not found!")
            return False
    else:
        print("✓ Leaflet already present in <head>")

    # 4. Generate the Real GIS HTML Section
    real_gis_html = '''      <!-- NATIONAL GIS ACCESSIBILITY & GOVERNORATES SURVEILLANCE -->
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

    # Replace old GIS block in Tab 1
    gis_start_marker = '      <!-- NATIONAL GIS ACCESSIBILITY & GOVERNORATES SURVEILLANCE -->'
    gis_end_marker = '    </section>'
    p1 = html.find(gis_start_marker)
    p2 = html.find(gis_end_marker, p1)
    if p1 != -1 and p2 != -1:
        html = html[:p1] + real_gis_html + '\n' + html[p2:]
        print("✓ Replaced schematic SVG with Real Leaflet GIS container in Tab 1")
    else:
        print("❌ Could not locate GIS section in Tab 1")
        return False

    # 5. Inject Leaflet JS logic into <script>
    gis_js_code = f'''
    // =========================================================================
    // REAL INTERACTIVE GIS MAP ENGINE FOR IRAQ (LEAFLET.JS)
    // =========================================================================

    const iraqGeoData = {min_geojson};

    const govCenters = {{
      'بغداد': [33.3152, 44.3661],
      'البصرة': [30.5081, 47.7835],
      'نينوى': [36.3438, 43.1340],
      'أربيل': [36.1901, 44.0091],
      'السليمانية': [35.5650, 45.4330],
      'دهوك': [36.8679, 42.9885],
      'كركوك': [35.4681, 44.3922],
      'صلاح الدين': [34.6060, 43.6793],
      'ديالى': [33.7489, 44.6444],
      'الأنبار': [33.4233, 43.2974],
      'بابل': [32.4683, 44.4305],
      'كربلاء المقدسة': [32.6160, 44.0249],
      'النجف الأشرف': [32.0259, 44.3463],
      'واسط': [32.5126, 45.8197],
      'الديوانية': [31.9929, 44.9254],
      'ميسان': [31.8415, 47.1448],
      'ذي قار': [31.0580, 46.2573],
      'المثنى': [31.3129, 45.2804]
    }};

    window.govCenters = govCenters;
    window.iraqMap = null;
    window.mapLayers = {{}};
    window.iraqGeoJsonLayer = null;
    window.markersLayerGroup = null;

    function getGovColor(rate) {{
      if (rate >= 80) return '#10b981';
      if (rate >= 70) return '#0284c7';
      if (rate >= 60) return '#f59e0b';
      return '#ef4444';
    }}

    function initIraqGISMap() {{
      const mapContainer = document.getElementById('iraq-leaflet-map');
      if (!mapContainer || window.iraqMap) return;
      if (typeof L === 'undefined') {{
        console.warn('Leaflet library is loading or unavailable');
        setTimeout(initIraqGISMap, 300);
        return;
      }}

      // 1. Create Leaflet map centered on Iraq
      window.iraqMap = L.map('iraq-leaflet-map', {{
        center: [33.2, 44.0],
        zoom: 6,
        minZoom: 5,
        maxZoom: 14,
        zoomControl: true,
        attributionControl: false
      }});

      // 2. Base Tile Layers
      window.mapLayers = {{
        dark: L.tileLayer('https://{{s}}.basemaps.cartocdn.com/dark_all/{{z}}/{{x}}/{{y}}{{r}}.png', {{
          maxZoom: 19,
          subdomains: 'abcd'
        }}),
        streets: L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
          maxZoom: 19
        }}),
        satellite: L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{{z}}/{{y}}/{{x}}', {{
          maxZoom: 19
        }})
      }};

      // Default to Dark GIS Layer
      window.mapLayers.dark.addTo(window.iraqMap);

      // 3. Add Iraq Official Governorates GeoJSON Layer
      if (typeof iraqGeoData !== 'undefined') {{
        window.iraqGeoJsonLayer = L.geoJSON(iraqGeoData, {{
          style: function(feature) {{
            const name = feature.properties.name_ar;
            const data = govData[name] || {{ rate: 60 }};
            return {{
              fillColor: getGovColor(data.rate),
              weight: 2,
              opacity: 0.9,
              color: '#38bdf8',
              fillOpacity: 0.55
            }};
          }},
          onEachFeature: function(feature, layer) {{
            const name = feature.properties.name_ar;
            const data = govData[name] || {{ rate: 0, status: 'تحت التدقيق' }};

            layer.bindTooltip(`
              <div style="direction: rtl; text-align: right;">
                <strong style="font-size: 13px;">${{name}}</strong><br/>
                <span style="color: ${{getGovColor(data.rate)}}; font-weight: bold;">نسبة الامتثال: ${{data.rate}}%</span>
              </div>
            `, {{
              direction: 'center',
              permanent: false,
              className: 'gis-tooltip'
            }});

            layer.on({{
              mouseover: function(e) {{
                const l = e.target;
                l.setStyle({{
                  weight: 3.5,
                  color: '#facc15',
                  fillOpacity: 0.8
                }});
                l.bringToFront();
              }},
              mouseout: function(e) {{
                if (window.activeGov === name) {{
                  e.target.setStyle({{
                    weight: 3.5,
                    color: '#facc15',
                    fillOpacity: 0.8
                  }});
                }} else {{
                  window.iraqGeoJsonLayer.resetStyle(e.target);
                }}
              }},
              click: function(e) {{
                selectGov(name);
              }}
            }});
          }}
        }}).addTo(window.iraqMap);
      }}

      // 4. Add Municipal Headquarters Pins with Pulsing Badges
      window.markersLayerGroup = L.layerGroup().addTo(window.iraqMap);
      for (const [govName, coords] of Object.entries(govCenters)) {{
        const d = govData[govName] || {{ rate: 60, status: 'لجنة مفعلة' }};
        const color = getGovColor(d.rate);

        const customIcon = L.divIcon({{
          className: 'custom-gov-pin',
          html: `
            <div style="background-color: ${{color}}; width: 26px; height: 26px; border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: 900; font-size: 13px; box-shadow: 0 0 10px ${{color}}, 0 2px 5px rgba(0,0,0,0.6); border: 2px solid #ffffff; cursor: pointer;">
              ♿
            </div>
          `,
          iconSize: [26, 26],
          iconAnchor: [13, 13],
          popupAnchor: [0, -13]
        }});

        const marker = L.marker(coords, {{ icon: customIcon }});
        marker.bindPopup(`
          <div style="direction: rtl; text-align: right; font-family: system-ui, -apple-system, sans-serif; min-width: 190px; padding: 4px;">
            <div style="font-weight: 800; font-size: 14px; margin-bottom: 4px; color: #38bdf8;">محافظة ${{govName}}</div>
            <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px; border-bottom: 1px solid #334155; padding-bottom: 4px;">
              <span style="color: #94a3b8;">نسبة الامتثال:</span>
              <strong style="color: ${{color}}; font-size: 13px;">${{d.rate}}%</strong>
            </div>
            <div style="font-size: 11px; color: #cbd5e1; margin-bottom: 8px;">
              الحالة: <strong>${{d.status}}</strong>
            </div>
            <button onclick="selectGov('${{govName}}')" style="background: #059669; color: white; border: none; padding: 5px 10px; border-radius: 8px; font-size: 11px; width: 100%; cursor: pointer; font-weight: bold;">عرض السجل البلدي الكامل</button>
          </div>
        `);

        marker.on('click', () => {{
          selectGov(govName);
        }});

        window.markersLayerGroup.addLayer(marker);
      }}

      // Initial Highlight
      selectGov('بغداد');
    }}

    function setMapBaseLayer(layerType) {{
      if (!window.iraqMap || !window.mapLayers) return;
      
      Object.values(window.mapLayers).forEach(l => {{
        if (window.iraqMap.hasLayer(l)) window.iraqMap.removeLayer(l);
      }});
      
      if (window.mapLayers[layerType]) {{
        window.iraqMap.addLayer(window.mapLayers[layerType]);
        if (window.iraqGeoJsonLayer) window.iraqGeoJsonLayer.bringToFront();
        if (window.markersLayerGroup) window.markersLayerGroup.bringToFront();
      }}

      ['dark', 'streets', 'satellite'].forEach(t => {{
        const btn = document.getElementById('btn-layer-' + t);
        if (btn) {{
          if (t === layerType) {{
            btn.className = 'px-2 py-1 rounded-lg bg-emerald-600 text-white font-bold transition';
          }} else {{
            btn.className = 'px-2 py-1 rounded-lg bg-slate-800 text-slate-300 hover:text-white transition';
          }}
        }}
      }});
    }}

    function resetIraqMap() {{
      if (window.iraqMap) {{
        window.iraqMap.flyTo([33.2, 44.0], 6);
        filterGovRegion('all');
        selectGov('بغداد');
      }}
    }}
'''

    # Now replace old selectGov and filterGovRegion functions
    old_gov_js_pattern = r'const govData = \{[\s\S]*?function exportGovReport\(\) \{'
    
    # We want to keep govData and exportGovReport, but update selectGov and filterGovRegion
    # Let's inspect where selectGov starts
    select_gov_code = '''
    function selectGov(govName) {
      if (!govData[govName]) return;
      activeGov = govName;
      const d = govData[govName];

      const selEl = document.getElementById('gis-selected-gov');
      if (selEl) selEl.innerText = `${govName}`;
      const titleEl = document.getElementById('gov-card-title');
      if (titleEl) titleEl.innerText = `محافظة ${govName}`;
      const statusEl = document.getElementById('gov-card-status');
      if (statusEl) statusEl.innerText = d.status;
      const rateEl = document.getElementById('gov-card-rate');
      if (rateEl) rateEl.innerText = `${d.rate}%`;
      const totEl = document.getElementById('gov-stat-total');
      if (totEl) totEl.innerText = `${d.total} مبنى`;
      const passEl = document.getElementById('gov-stat-pass');
      if (passEl) passEl.innerText = `${d.pass} مبنى`;
      const retroEl = document.getElementById('gov-stat-retro');
      if (retroEl) retroEl.innerText = `${d.retro} مبنى`;

      const list = document.getElementById('gov-projects-list');
      if (list) {
        list.innerHTML = d.projects.map(p => `
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex justify-between items-center text-xs">
            <span class="text-slate-800 dark:text-slate-200 font-medium">🏛️ ${p}</span>
            <span class="text-[10px] text-emerald-600 dark:text-emerald-400 font-bold bg-emerald-50 dark:bg-emerald-950/40 px-2 py-0.5 rounded">مفحوص</span>
          </div>
        `).join('');
      }

      // Highlight corresponding GeoJSON polygon on Leaflet Map
      if (window.iraqGeoJsonLayer) {
        window.iraqGeoJsonLayer.eachLayer(layer => {
          const pName = layer.feature.properties.name_ar;
          if (pName === govName) {
            layer.setStyle({
              weight: 3.5,
              color: '#facc15',
              fillOpacity: 0.8
            });
            layer.bringToFront();
          } else {
            const pData = govData[pName] || { rate: 60 };
            layer.setStyle({
              weight: 1.8,
              color: '#38bdf8',
              fillColor: getGovColor(pData.rate),
              fillOpacity: 0.55
            });
          }
        });
      }

      // Pan to governorate municipal center smoothly
      if (window.govCenters && window.govCenters[govName] && window.iraqMap) {
        const coords = window.govCenters[govName];
        window.iraqMap.panTo(coords, { animate: true, duration: 0.8 });
      }
    }

    function filterGovRegion(region) {
      ['all', 'center', 'south', 'north', 'west'].forEach(r => {
        const btn = document.getElementById('btn-reg-' + r);
        if (btn) {
          btn.className = (r === region)
            ? 'px-2.5 py-1 rounded-lg bg-emerald-600 text-white font-bold transition'
            : 'px-2.5 py-1 rounded-lg bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:bg-slate-200 transition';
        }
      });

      if (!window.iraqMap) return;

      if (region === 'all') {
        window.iraqMap.flyTo([33.2, 44.0], 6, { duration: 1.2 });
      } else if (region === 'center') {
        window.iraqMap.flyTo([32.9, 44.5], 7, { duration: 1.2 });
      } else if (region === 'south') {
        window.iraqMap.flyTo([31.0, 46.5], 7, { duration: 1.2 });
      } else if (region === 'north') {
        window.iraqMap.flyTo([36.2, 44.0], 7.2, { duration: 1.2 });
      } else if (region === 'west') {
        window.iraqMap.flyTo([33.2, 42.5], 6.8, { duration: 1.2 });
      }
    }'''

    # Replace selectGov & filterGovRegion in JS
    old_fn_start = html.find('function selectGov(govName) {')
    old_fn_end = html.find('function exportGovReport() {')
    if old_fn_start != -1 and old_fn_end != -1:
        html = html[:old_fn_start] + select_gov_code + '\n\n    ' + html[old_fn_end:]
        print("✓ Replaced selectGov and filterGovRegion with Leaflet-connected versions")
    else:
        print("❌ Could not locate selectGov in JS")
        return False

    # Insert gis_js_code right before `const govData = {`
    gov_data_pos = html.find('const govData = {')
    if gov_data_pos != -1:
        html = html[:gov_data_pos] + gis_js_code + '\n\n    ' + html[gov_data_pos:]
        print("✓ Injected Real GIS Map Engine code into <script>")
    else:
        print("❌ Could not locate govData in JS")
        return False

    # Also update switchTab to invalidateSize on dashboard tab
    switch_tab_pos = html.find("if (targetSection) targetSection.classList.remove('hidden');")
    if switch_tab_pos != -1 and "window.iraqMap.invalidateSize()" not in html:
        invalidate_code = """if (targetSection) targetSection.classList.remove('hidden');
      if (tabId === 'dashboard' && window.iraqMap) {
        setTimeout(() => { window.iraqMap.invalidateSize(); }, 200);
      }"""
        html = html.replace("if (targetSection) targetSection.classList.remove('hidden');", invalidate_code)
        print("✓ Added map.invalidateSize() to switchTab('dashboard')")

    # In window.onload, ensure initIraqGISMap is called
    if 'initIraqGISMap();' not in html:
        onload_marker = "if (typeof selectGov === 'function') selectGov('بغداد');"
        if onload_marker in html:
            html = html.replace(onload_marker, "if (typeof initIraqGISMap === 'function') initIraqGISMap();\n      " + onload_marker)
            print("✓ Injected initIraqGISMap() into window.onload")

    # Save to iraqi_accessibility_platform.html and index.html
    with open('iraqi_accessibility_platform.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Saved updated files: iraqi_accessibility_platform.html and index.html")

    return True

if __name__ == '__main__':
    build_real_gis()
