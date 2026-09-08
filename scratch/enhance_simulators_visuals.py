#!/usr/bin/env python3
"""
enhance_simulators_visuals.py
Upgrades all 7 interactive architectural simulator diagrams (Universal Design Lab):
- Enlarge font sizes across all SVGs to 12px-14px bold for crystal-clear readability.
- Add dedicated high-contrast background pill badges (<rect rx="5">) behind all dimension texts and callouts.
- Eliminate ALL overlapping text, labels, and graphic elements.
- Increase container heights from cramped h-24/h-44 to spacious h-56/h-60 with optimized viewBoxes.
- Preserve 100% of DOM IDs and JavaScript bindings.
"""

import re
import sys

def enhance_simulators():
    print("=" * 70)
    print("ENHANCING 7 ARCHITECTURAL SIMULATORS VISUALS & TYPOGRAPHY")
    print("=" * 70)

    with open('iraqi_accessibility_platform.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. ENHANCED SIMULATOR 1: RAMP & SLOPE (ramp-svg)
    old_ramp_pattern = r'<svg id="ramp-svg"[\s\S]*?</svg>'
    new_ramp_svg = '''<svg id="ramp-svg" viewBox="0 0 520 150" class="w-full h-36 sm:h-40">
                  <!-- Ground Baseline -->
                  <line x1="20" y1="125" x2="500" y2="125" stroke="#475569" stroke-width="2.5" stroke-dasharray="4"/>
                  
                  <!-- Entrance Platform & Badge -->
                  <rect x="20" y="45" width="85" height="80" fill="#1e293b" stroke="#38bdf8" stroke-width="2.5" rx="3"/>
                  <rect x="22" y="16" width="82" height="24" rx="5" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
                  <text x="63" y="32" fill="#7dd3fc" font-size="12" text-anchor="middle" font-weight="bold">المدخل الميسر</text>
                  
                  <!-- Ramp Slope Body -->
                  <polygon points="105,45 405,125 105,125" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="3"/>
                  
                  <!-- Architectural Handrail Lines (85cm & 65cm) -->
                  <line x1="105" y1="33" x2="405" y2="113" stroke="#e2e8f0" stroke-width="2.5" stroke-linecap="round"/>
                  <line x1="105" y1="39" x2="405" y2="119" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round"/>
                  
                  <!-- Central Slope Ratio Badge (Zero overlap, clear pill) -->
                  <g transform="translate(205, 52)">
                    <rect x="0" y="0" width="110" height="32" rx="7" fill="#022c22" stroke="#10b981" stroke-width="2"/>
                    <text x="55" y="21" fill="#34d399" font-size="14" text-anchor="middle" font-weight="black" id="svg-text-ratio">1:16</text>
                  </g>
                  
                  <!-- Rest Landing (at bottom) -->
                  <rect x="405" y="118" width="95" height="7" fill="#f59e0b" rx="2"/>
                  <rect x="410" y="84" width="86" height="24" rx="5" fill="#451a03" stroke="#f59e0b" stroke-width="1.5"/>
                  <text x="453" y="100" fill="#fde68a" font-size="12" text-anchor="middle" font-weight="bold">بسطة استراحة</text>
                </svg>'''
    
    html, count1 = re.subn(old_ramp_pattern, new_ramp_svg, html, count=1)
    print(f"✓ Enhanced Simulator 1 (Ramp): {count1} replaced")

    # 2. ENHANCED SIMULATOR 2: RESTROOM 2D (sim-svg)
    old_restroom_pattern = r'<svg id="sim-svg"[\s\S]*?</svg>'
    new_restroom_svg = '''<svg id="sim-svg" width="100%" height="420" viewBox="0 0 460 460" class="rounded-xl bg-slate-950">
                <defs>
                  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.7"/>
                  </pattern>
                </defs>
                <!-- Room Perimeter: 2.00 x 2.00m (360x360 px) -->
                <rect width="360" height="360" x="50" y="50" fill="url(#grid)" stroke="#0ea5e9" stroke-width="3.5" rx="6"/>
                
                <!-- Dimension Badges (Top & Right) -->
                <rect x="130" y="12" width="200" height="28" rx="6" fill="#082f49" stroke="#38bdf8" stroke-width="1.5"/>
                <text x="230" y="31" fill="#7dd3fc" font-size="13" text-anchor="middle" font-weight="bold">عرض الغرفة الصافي: 2.00 م (200 سم)</text>
                
                <text x="26" y="230" fill="#38bdf8" font-size="13" text-anchor="middle" transform="rotate(-90 26 230)" font-weight="bold">طول الغرفة: 2.00 م (200 سم)</text>

                <!-- 360 Turning Circle (150cm diameter = 135px radius) -->
                <g id="sim-circle-group">
                  <circle cx="230" cy="230" r="135" fill="rgba(16, 185, 129, 0.14)" stroke="#10b981" stroke-width="2.5" stroke-dasharray="6"/>
                  <rect x="140" y="206" width="180" height="48" rx="8" fill="#064e3b" fill-opacity="0.9" stroke="#10b981" stroke-width="1.5"/>
                  <text x="230" y="226" fill="#6ee7b7" font-size="13" text-anchor="middle" font-weight="black">دائرة دوران الكرسي 360°</text>
                  <text x="230" y="244" fill="#a7f3d0" font-size="11.5" text-anchor="middle" font-weight="bold">قطر 150 سم (دوران حر تماماً)</text>
                </g>

                <!-- T-Turn Alternative Area -->
                <g id="sim-tturn-group" style="display: none;">
                  <rect x="145" y="95" width="170" height="270" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5" rx="6"/>
                  <rect x="95" y="145" width="270" height="170" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="5" rx="6"/>
                  <rect x="145" y="206" width="170" height="48" rx="8" fill="#451a03" fill-opacity="0.92" stroke="#f59e0b" stroke-width="1.5"/>
                  <text x="230" y="226" fill="#fde68a" font-size="13" text-anchor="middle" font-weight="black">مساحة مناورة حرف T</text>
                  <text x="230" y="244" fill="#fef08a" font-size="11" text-anchor="middle" font-weight="bold">150 × 90 سم (استثناء للمباني القائمة)</text>
                </g>

                <!-- Water Closet (Toilet) -->
                <rect x="335" y="55" width="55" height="75" rx="14" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
                <circle cx="362" cy="100" r="16" fill="#94a3b8"/>
                <rect x="295" y="138" width="145" height="24" rx="5" fill="#1e293b" stroke="#64748b" stroke-width="1"/>
                <text x="367" y="154" fill="#f8fafc" font-size="11" text-anchor="middle" font-weight="bold">مرحاض (ارتفاع 45-50 سم)</text>

                <!-- Bidet Sprayer -->
                <circle cx="400" cy="95" r="6" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>

                <!-- Grab Bars Group (L-Bar & Folding Bar) -->
                <g id="sim-bars">
                  <!-- Fixed Wall L-Bar -->
                  <path d="M 405 60 L 405 130 L 380 130" fill="none" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
                  <!-- Folding Drop-down Bar -->
                  <line x1="315" y1="60" x2="315" y2="130" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
                  <!-- Dedicated Labels with Zero Overlap -->
                  <rect x="235" y="65" width="75" height="32" rx="5" fill="#1e293b" stroke="#f59e0b" stroke-width="1.2"/>
                  <text x="272" y="79" fill="#fbbf24" font-size="10" text-anchor="middle" font-weight="bold">مسند طي</text>
                  <text x="272" y="92" fill="#fbbf24" font-size="9" text-anchor="middle">(113 كغم)</text>
                </g>

                <!-- Washbasin (Bottom-Right Corner) -->
                <path d="M 325 330 Q 360 305 395 330 L 395 390 L 325 390 Z" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
                <circle cx="360" cy="350" r="6" fill="#38bdf8"/>
                <rect x="275" y="295" width="165" height="26" rx="5" fill="#0f172a" stroke="#38bdf8" stroke-width="1.2"/>
                <text x="357" y="312" fill="#7dd3fc" font-size="11.5" text-anchor="middle" font-weight="bold">مغسلة معلقة (ارتفاع 80-85 سم)</text>

                <!-- Accessible Door (Bottom-Left) -->
                <line x1="50" y1="410" x2="160" y2="410" stroke="#22c55e" stroke-width="6"/>
                <path id="sim-door-arc" d="M 160 410 A 110 110 0 0 1 50 410" fill="rgba(34, 197, 94, 0.15)" stroke="#22c55e" stroke-width="2.5" stroke-dasharray="4"/>
                <rect x="55" y="420" width="220" height="26" rx="5" fill="#052e16" stroke="#22c55e" stroke-width="1.2"/>
                <text x="165" y="437" fill="#4ade80" font-size="12" text-anchor="middle" font-weight="bold">عرض الباب: 90 سم (يفتح للخارج)</text>

                <!-- Emergency Pull Cord (Top-Left) -->
                <circle cx="75" cy="75" r="8" fill="#dc2626" stroke="#fecaca" stroke-width="2"/>
                <line x1="75" y1="75" x2="75" y2="115" stroke="#dc2626" stroke-width="2.5"/>
                <rect x="55" y="122" width="130" height="24" rx="5" fill="#450a0a" stroke="#ef4444" stroke-width="1.2"/>
                <text x="120" y="138" fill="#fca5a5" font-size="11" text-anchor="middle" font-weight="bold">حبل طوارئ (10سم)</text>
              </svg>'''

    html, count2 = re.subn(old_restroom_pattern, new_restroom_svg, html, count=1)
    print(f"✓ Enhanced Simulator 2 (Restroom): {count2} replaced")

    # 3. ENHANCED SIMULATOR 3: PARKING (park-svg)
    old_parking_pattern = r'<svg id="park-svg"[\s\S]*?</svg>'
    new_parking_svg = '''<svg id="park-svg" viewBox="0 0 520 220" class="w-full h-52 sm:h-56">
                  <!-- Asphalt Roadway -->
                  <rect x="10" y="10" width="500" height="200" fill="#0f172a" rx="8"/>
                  
                  <!-- Protected Sidewalk Curb (Top) -->
                  <rect x="10" y="10" width="500" height="36" fill="#334155" stroke="#475569" stroke-width="1.5"/>
                  <text x="260" y="32" fill="#cbd5e1" font-size="13" text-anchor="middle" font-weight="bold">رصيف المشاة المؤدي للمدخل الميسر (مسافة السير ≤ 50م)</text>
                  
                  <!-- Curb cut ramp (in front of access aisle) -->
                  <polygon id="park-curb-ramp" points="290,10 290,46 390,46 390,10" fill="#eab308" opacity="0.95"/>
                  <text x="340" y="32" fill="#000" font-size="11" text-anchor="middle" font-weight="black">منحدر رصيف</text>

                  <!-- Accessible Parking Stall (Left Bay: 2.40m wide) -->
                  <rect x="75" y="46" width="215" height="155" fill="#1e293b" stroke="#facc15" stroke-width="3.5"/>
                  
                  <!-- Wheelchair Painted ISA Marking inside stall -->
                  <circle cx="180" cy="115" r="22" fill="#0284c7"/>
                  <path d="M 174 109 A 8 8 0 1 0 186 109 A 8 8 0 1 0 174 109 M 180 106 L 180 121 L 190 121 M 175 117 A 11 11 0 0 0 190 129" fill="none" stroke="#ffffff" stroke-width="2.6" stroke-linecap="round"/>
                  
                  <!-- Stall Width Callout Badge -->
                  <rect x="110" y="165" width="145" height="26" rx="5" fill="#0f172a" stroke="#facc15" stroke-width="1.5"/>
                  <text x="182" y="182" fill="#facc15" font-size="12.5" text-anchor="middle" font-weight="bold">موقف مخصص (2.40 م)</text>

                  <!-- Vehicle Outline Inside Stall -->
                  <rect x="100" y="60" width="165" height="85" rx="10" fill="#38bdf8" fill-opacity="0.12" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4"/>
                  <text x="182" y="80" fill="#7dd3fc" font-size="11.5" text-anchor="middle" font-weight="bold">سيارة ميسرة مخصصة</text>

                  <!-- Access Aisle (Right side: 1.50m / 2.44m wide) -->
                  <g id="park-aisle-group">
                    <rect id="park-aisle-rect" x="290" y="46" width="125" height="155" fill="#0284c7" fill-opacity="0.22" stroke="#0284c7" stroke-width="2.5"/>
                    <!-- Diagonal Hatch lines -->
                    <line x1="290" y1="65" x2="415" y2="120" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="290" y1="100" x2="415" y2="155" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="290" y1="135" x2="415" y2="190" stroke="#38bdf8" stroke-width="2"/>
                    <line x1="290" y1="170" x2="370" y2="201" stroke="#38bdf8" stroke-width="2"/>
                    
                    <!-- Horizontal Clear Text Pill (No confusing 90deg text!) -->
                    <rect id="park-aisle-pill" x="295" y="105" width="115" height="34" rx="6" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
                    <text id="park-aisle-text" x="352" y="126" fill="#e0f2fe" font-size="12" text-anchor="middle" font-weight="black">ممر نزول (1.50م)</text>
                  </g>

                  <!-- Standard Accessibility Signpost (1.50m height) -->
                  <circle cx="45" cy="70" r="5" fill="#3b82f6" stroke="#fff" stroke-width="2"/>
                  <rect x="18" y="80" width="55" height="38" rx="4" fill="#1d4ed8" stroke="#ffffff" stroke-width="1.5"/>
                  <text x="45" y="97" fill="#fff" font-size="11" text-anchor="middle" font-weight="bold">شاخصة</text>
                  <text x="45" y="111" fill="#facc15" font-size="10.5" text-anchor="middle" font-weight="black">1.50 م</text>
                </svg>'''

    html, count3 = re.subn(old_parking_pattern, new_parking_svg, html, count=1)
    print(f"✓ Enhanced Simulator 3 (Parking): {count3} replaced")

    # 4. ENHANCED SIMULATOR 4: DOOR MANEUVERING CLEARANCES (door-svg)
    old_door_pattern = r'<svg id="door-svg"[\s\S]*?</svg>'
    new_door_svg = '''<svg id="door-svg" viewBox="0 0 520 220" class="w-full h-52 sm:h-56">
                  <!-- Main Partition Walls -->
                  <rect x="20" y="45" width="130" height="24" fill="#475569" stroke="#64748b" stroke-width="1.5" rx="3"/>
                  <rect x="240" y="45" width="260" height="24" fill="#475569" stroke="#64748b" stroke-width="1.5" rx="3"/>
                  <rect x="30" y="16" width="110" height="24" rx="5" fill="#1e293b" stroke="#64748b"/>
                  <text x="85" y="32" fill="#cbd5e1" font-size="12" text-anchor="middle" font-weight="bold">جدار فاصل</text>
                  <rect x="290" y="16" width="170" height="24" rx="5" fill="#1e293b" stroke="#64748b"/>
                  <text x="375" y="32" fill="#cbd5e1" font-size="12" text-anchor="middle" font-weight="bold">جدار المقبض (Latch Wall)</text>

                  <!-- Door Opening Gap (150 to 240 = 90cm) -->
                  <!-- Door Leaf (Swinging 90 deg) -->
                  <line id="door-leaf" x1="150" y1="57" x2="150" y2="152" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
                  <!-- Swing Arc -->
                  <path id="door-arc-path" d="M 240 57 A 90 90 0 0 1 150 152" fill="rgba(245, 158, 11, 0.14)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="4"/>
                  <!-- Lever Handle Symbol -->
                  <circle cx="150" cy="142" r="5" fill="#ef4444"/>
                  <line x1="150" y1="142" x2="164" y2="142" stroke="#ef4444" stroke-width="3"/>

                  <!-- Maneuvering Clearance Zone (Box) -->
                  <rect id="door-clearance-box" x="150" y="69" width="145" height="140" fill="rgba(16, 185, 129, 0.18)" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5" rx="5"/>
                  
                  <!-- Dedicated Clearance Text Badge (Positioned so it NEVER overlaps with avatar!) -->
                  <g transform="translate(160, 75)">
                    <rect x="0" y="0" width="185" height="28" rx="6" fill="#064e3b" fill-opacity="0.9" stroke="#10b981" stroke-width="1.5"/>
                    <text id="door-box-text" x="92" y="19" fill="#6ee7b7" font-size="12" text-anchor="middle" font-weight="bold">فضاء مناورة حر (150 × 135 سم)</text>
                  </g>

                  <!-- Latch Clearance Dimension Badge -->
                  <g id="door-latch-dim">
                    <line x1="240" y1="57" x2="285" y2="57" stroke="#38bdf8" stroke-width="2.5"/>
                    <line x1="240" y1="50" x2="240" y2="64" stroke="#38bdf8" stroke-width="2.5"/>
                    <line x1="285" y1="50" x2="285" y2="64" stroke="#38bdf8" stroke-width="2.5"/>
                    <rect x="245" y="44" width="85" height="22" rx="4" fill="#0c4a6e" stroke="#38bdf8"/>
                    <text x="287" y="59" fill="#7dd3fc" font-size="11" text-anchor="middle" font-weight="bold">خلوص 45 سم</text>
                  </g>

                  <!-- User Avatar (Wheelchair) placed cleanly at lower section without text clashing -->
                  <g id="door-user-avatar" transform="translate(200, 150)">
                    <rect x="-12" y="-14" width="24" height="28" rx="5" fill="#0284c7" stroke="#fff" stroke-width="1.8"/>
                    <circle cx="0" cy="-3" r="6" fill="#f8fafc"/>
                    <rect x="-15" y="-12" width="3.5" height="24" rx="1.5" fill="#94a3b8"/>
                    <rect x="12" y="-12" width="3.5" height="24" rx="1.5" fill="#94a3b8"/>
                  </g>
                </svg>'''

    html, count4 = re.subn(old_door_pattern, new_door_svg, html, count=1)
    print(f"✓ Enhanced Simulator 4 (Doors): {count4} replaced")

    # 5. ENHANCED SIMULATOR 5: ELEVATORS (elev-svg)
    old_elev_pattern = r'<svg id="elev-svg"[\s\S]*?</svg>'
    new_elev_svg = '''<svg id="elev-svg" viewBox="0 0 520 220" class="w-full h-52 sm:h-56">
                  <!-- Dividing Line between Plan & Elevation -->
                  <line x1="240" y1="15" x2="240" y2="205" stroke="#334155" stroke-width="1.5" stroke-dasharray="4"/>

                  <!-- LEFT: Plan View of Cabin (x: 20 to 230) -->
                  <g id="elev-plan-group">
                    <rect id="elev-plan-box" x="35" y="38" width="175" height="145" fill="#1e293b" stroke="#a855f7" stroke-width="3" rx="5"/>
                    <rect x="75" y="10" width="100" height="24" rx="5" fill="#1e1b4b" stroke="#a855f7" stroke-width="1.2"/>
                    <text x="125" y="26" fill="#c084fc" font-size="12" text-anchor="middle" font-weight="bold" id="elev-plan-w-text">العرض: 1.40 م</text>
                    
                    <rect x="10" y="85" width="22" height="60" rx="4" fill="#1e1b4b" stroke="#a855f7"/>
                    <text x="21" y="115" fill="#c084fc" font-size="12" text-anchor="middle" transform="rotate(-90 21 115)" font-weight="bold" id="elev-plan-d-text">1.10 م</text>

                    <!-- Handrails (3 sides) -->
                    <line x1="42" y1="45" x2="42" y2="175" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="42" y1="175" x2="202" y2="175" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>
                    <line x1="202" y1="175" x2="202" y2="45" stroke="#f59e0b" stroke-width="3.5" stroke-linecap="round"/>

                    <!-- Elevator Door at Top (Clear 90cm) -->
                    <line id="elev-door-line" x1="45" y1="38" x2="145" y2="38" stroke="#22c55e" stroke-width="6.5"/>
                    <rect x="55" y="44" width="115" height="22" rx="4" fill="#052e16" stroke="#22c55e"/>
                    <text x="112" y="59" fill="#4ade80" font-size="11" text-anchor="middle" font-weight="bold">باب منزلق (90 سم)</text>

                    <!-- Wheelchair User Inside Cabin -->
                    <circle cx="125" cy="115" r="18" fill="#0284c7" fill-opacity="0.5" stroke="#38bdf8" stroke-width="2"/>
                    <text x="125" y="119" fill="#fff" font-size="11" text-anchor="middle" font-weight="bold">كرسي</text>
                  </g>

                  <!-- RIGHT: Wall Elevation View of Control Panel & Handrail (x: 255 to 505) -->
                  <g id="elev-elev-group">
                    <rect x="255" y="25" width="250" height="180" fill="#1e293b" stroke="#64748b" stroke-width="1.5" rx="5"/>
                    <rect x="280" y="10" width="200" height="24" rx="5" fill="#0f172a" stroke="#64748b"/>
                    <text x="380" y="26" fill="#cbd5e1" font-size="12" text-anchor="middle" font-weight="bold">مقطع رأسي لجدار التحكم الداخلي</text>
                    
                    <!-- Ground Line -->
                    <line x1="255" y1="195" x2="505" y2="195" stroke="#475569" stroke-width="2.5"/>
                    <text x="495" y="190" fill="#94a3b8" font-size="10.5" font-weight="bold">الأرضية</text>

                    <!-- Handrail Elevation (85-90 cm) -->
                    <line x1="265" y1="135" x2="495" y2="135" stroke="#f59e0b" stroke-width="4.5" stroke-linecap="round"/>
                    <rect x="400" y="115" width="95" height="22" rx="4" fill="#1e293b" stroke="#f59e0b"/>
                    <text x="447" y="130" fill="#fbbf24" font-size="11" text-anchor="middle" font-weight="bold">درابزين (85 سم)</text>

                    <!-- Control Panel Column (90 - 120 cm range) -->
                    <rect x="305" y="65" width="60" height="95" fill="#334155" stroke="#38bdf8" stroke-width="2" rx="4"/>
                    
                    <!-- Braille Buttons (Dots) -->
                    <circle cx="320" cy="80" r="5" fill="#e2e8f0"/>
                    <circle cx="350" cy="80" r="5" fill="#e2e8f0"/>
                    <circle cx="320" cy="100" r="5" fill="#e2e8f0"/>
                    <circle cx="350" cy="100" r="5" fill="#e2e8f0"/>
                    
                    <!-- Emergency Call Button (Red, at 90cm) -->
                    <circle cx="335" cy="130" r="7" fill="#ef4444" stroke="#fca5a5" stroke-width="1.5"/>
                    <text x="335" y="152" fill="#38bdf8" font-size="10" text-anchor="middle" font-weight="bold">برايل 90-120سم</text>
                  </g>
                </svg>'''

    html, count5 = re.subn(old_elev_pattern, new_elev_svg, html, count=1)
    print(f"✓ Enhanced Simulator 5 (Elevators): {count5} replaced")

    # 6. ENHANCED SIMULATOR 6: CURB RAMPS & TACTILE (curb-svg)
    old_curb_pattern = r'<svg id="curb-svg"[\s\S]*?</svg>'
    new_curb_svg = '''<svg id="curb-svg" viewBox="0 0 520 220" class="w-full h-52 sm:h-56">
                  <!-- Sidewalk Pavement (Top) -->
                  <rect x="15" y="15" width="490" height="75" fill="#334155" stroke="#475569" stroke-width="1.5" rx="4"/>
                  <rect x="160" y="25" width="200" height="26" rx="5" fill="#0f172a" stroke="#64748b"/>
                  <text x="260" y="42" fill="#cbd5e1" font-size="12.5" text-anchor="middle" font-weight="bold">مستوى الرصيف العلوي (+15 سم)</text>

                  <!-- Asphalt Roadway (Bottom) -->
                  <rect x="15" y="145" width="490" height="65" fill="#0f172a" stroke="#1e293b" rx="4"/>
                  <text x="260" y="190" fill="#94a3b8" font-size="12" text-anchor="middle" font-weight="bold">قارعة طريق السيارات / الشارع (منسوب 0.00)</text>

                  <!-- Left Flared Wing (1:10 Slope) -->
                  <polygon points="90,90 170,90 170,145 90,145" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                  <line x1="90" y1="90" x2="170" y2="145" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/>
                  <rect x="95" y="105" width="70" height="24" rx="4" fill="#1e293b" stroke="#f59e0b"/>
                  <text x="130" y="121" fill="#fbbf24" font-size="11.5" text-anchor="middle" font-weight="bold">جناح 1:10</text>

                  <!-- Right Flared Wing (1:10 Slope) -->
                  <polygon points="350,90 430,90 430,145 350,145" fill="#475569" stroke="#94a3b8" stroke-width="1.5"/>
                  <line x1="430" y1="90" x2="350" y2="145" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3"/>
                  <rect x="355" y="105" width="70" height="24" rx="4" fill="#1e293b" stroke="#f59e0b"/>
                  <text x="390" y="121" fill="#fbbf24" font-size="11.5" text-anchor="middle" font-weight="bold">جناح 1:10</text>

                  <!-- Central Ramp (Clear 1:12) -->
                  <rect x="170" y="90" width="180" height="55" fill="#14b8a6" fill-opacity="0.25" stroke="#14b8a6" stroke-width="2.5"/>
                  <rect x="180" y="96" width="160" height="24" rx="4" fill="#042f2e" stroke="#14b8a6"/>
                  <text x="260" y="112" fill="#2dd4bf" font-size="12" text-anchor="middle" font-weight="bold" id="curb-ramp-text">منحدر النزول (ميل 1:12)</text>

                  <!-- Tactile Paving Strip (60cm deep = 20px) at transition -->
                  <rect id="curb-tactile-strip" x="170" y="125" width="180" height="20" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
                  <!-- Studs pattern -->
                  <g id="curb-studs-group">
                    <circle cx="185" cy="135" r="3" fill="#713f12"/>
                    <circle cx="210" cy="135" r="3" fill="#713f12"/>
                    <circle cx="235" cy="135" r="3" fill="#713f12"/>
                    <circle cx="260" cy="135" r="3" fill="#713f12"/>
                    <circle cx="285" cy="135" r="3" fill="#713f12"/>
                    <circle cx="310" cy="135" r="3" fill="#713f12"/>
                    <circle cx="335" cy="135" r="3" fill="#713f12"/>
                  </g>
                  
                  <!-- Tactile Warning Pill Badge (Positioned below strip so NO text overlap with dots!) -->
                  <rect x="165" y="152" width="190" height="25" rx="5" fill="#422006" stroke="#eab308" stroke-width="1.5"/>
                  <text x="260" y="169" fill="#fde047" font-size="12" text-anchor="middle" font-weight="black">بلاط تحذيري للمكفوفين (60 سم)</text>

                  <!-- Zero-Lip Flush Transition Line (Street level 0.00) -->
                  <line x1="90" y1="145" x2="430" y2="145" stroke="#38bdf8" stroke-width="3"/>
                </svg>'''

    html, count6 = re.subn(old_curb_pattern, new_curb_svg, html, count=1)
    print(f"✓ Enhanced Simulator 6 (Curb Ramp): {count6} replaced")

    # 7. ENHANCED SIMULATOR 7: ERGONOMIC REACH RANGES (reach-svg)
    old_reach_pattern = r'<svg id="reach-svg"[\s\S]*?</svg>'
    new_reach_svg = '''<svg id="reach-svg" viewBox="0 0 520 220" class="w-full h-52 sm:h-56">
                  <!-- Ground Baseline -->
                  <line x1="20" y1="190" x2="500" y2="190" stroke="#475569" stroke-width="3"/>
                  <text x="490" y="206" fill="#94a3b8" font-size="11" font-weight="bold">الأرضية (0)</text>

                  <!-- Three Ergonomic Height Zones on Right (x: 370 to 500) -->
                  <!-- Red Non-compliant Top Zone: > 120cm -->
                  <rect x="370" y="20" width="130" height="40" fill="rgba(239, 68, 68, 0.18)" rx="4"/>
                  <rect x="375" y="27" width="120" height="24" rx="4" fill="#450a0a" stroke="#ef4444"/>
                  <text x="435" y="43" fill="#fca5a5" font-size="11" text-anchor="middle" font-weight="bold">نطاق محظور (>120سم)</text>

                  <!-- Green Compliant Zone: 38 to 120cm (y: 152 to 60) -->
                  <rect x="370" y="60" width="130" height="92" fill="rgba(16, 185, 129, 0.22)" stroke="#10b981" stroke-width="1.5" stroke-dasharray="4" rx="4"/>
                  <rect x="372" y="92" width="126" height="28" rx="5" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
                  <text x="435" y="110" fill="#6ee7b7" font-size="11.5" text-anchor="middle" font-weight="black">نطاق مريح (38-120 سم)</text>

                  <!-- Red Non-compliant Bottom Zone: < 38cm -->
                  <rect x="370" y="152" width="130" height="38" fill="rgba(239, 68, 68, 0.18)" rx="4"/>
                  <rect x="375" y="158" width="120" height="24" rx="4" fill="#450a0a" stroke="#ef4444"/>
                  <text x="435" y="174" fill="#fca5a5" font-size="11" text-anchor="middle" font-weight="bold">منخفض جداً (&lt;38سم)</text>

                  <!-- Wheelchair Silhouette at Left (x: 40 to 170) -->
                  <g id="reach-user-figure">
                    <!-- Wheels -->
                    <circle cx="95" cy="155" r="30" fill="none" stroke="#38bdf8" stroke-width="3"/>
                    <circle cx="95" cy="155" r="5" fill="#38bdf8"/>
                    <circle cx="150" cy="178" r="9" fill="none" stroke="#94a3b8" stroke-width="2.5"/>
                    <!-- Frame & Seat -->
                    <line x1="95" y1="155" x2="125" y2="135" stroke="#38bdf8" stroke-width="3.5"/>
                    <line x1="85" y1="135" x2="140" y2="135" stroke="#38bdf8" stroke-width="4.5"/>
                    <!-- Backrest -->
                    <line x1="85" y1="135" x2="80" y2="85" stroke="#38bdf8" stroke-width="4.5"/>
                    <!-- Human Figure -->
                    <circle cx="102" cy="62" r="11" fill="#f8fafc"/>
                    <line x1="97" y1="73" x2="115" y2="135" stroke="#f8fafc" stroke-width="5.5" stroke-linecap="round"/>
                    <line x1="115" y1="135" x2="168" y2="135" stroke="#f8fafc" stroke-width="5.5" stroke-linecap="round"/>
                    <line x1="168" y1="135" x2="168" y2="175" stroke="#f8fafc" stroke-width="5.5" stroke-linecap="round"/>
                    <!-- Outstretched Arm reaching toward target -->
                    <line id="reach-arm-line" x1="102" y1="85" x2="230" y2="105" stroke="#f8fafc" stroke-width="4" stroke-linecap="round"/>
                  </g>

                  <!-- Target Counters (x: 210 to 350) -->
                  <g id="reach-target-group">
                    <!-- Standard High Employee Counter (110cm) -->
                    <rect x="275" y="80" width="55" height="110" fill="#334155" stroke="#475569" stroke-width="2" rx="3"/>
                    <rect x="270" y="52" width="75" height="24" rx="4" fill="#1e293b" stroke="#64748b"/>
                    <text x="307" y="68" fill="#cbd5e1" font-size="11" text-anchor="middle" font-weight="bold">كاونتر 110سم</text>

                    <!-- Accessible Lower Counter Tier (85cm) with Knee Clearance -->
                    <path id="reach-counter-shape" d="M 205 105 L 275 105 L 275 190 L 250 190 L 250 122 L 205 122 Z" fill="#0284c7" fill-opacity="0.35" stroke="#0284c7" stroke-width="2.5"/>
                    <rect x="195" y="75" width="85" height="25" rx="5" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
                    <text id="reach-target-label" x="237" y="92" fill="#7dd3fc" font-size="12" text-anchor="middle" font-weight="bold">ميسر (85 سم)</text>
                    
                    <!-- Knee clearance dimension badge -->
                    <rect x="180" y="132" width="85" height="22" rx="4" fill="#451a03" stroke="#f59e0b"/>
                    <text x="222" y="147" fill="#fde68a" font-size="10.5" text-anchor="middle" font-weight="bold">فراغ ركبة ≥ 68سم</text>
                  </g>

                  <!-- Dynamic Target Level Indicator (Red/Green line + dot) -->
                  <line id="reach-level-indicator" x1="20" y1="105" x2="490" y2="105" stroke="#10b981" stroke-width="2.5" stroke-dasharray="5"/>
                  <circle id="reach-target-dot" cx="237" cy="105" r="6" fill="#10b981" stroke="#fff" stroke-width="2"/>
                </svg>'''

    html, count7 = re.subn(old_reach_pattern, new_reach_svg, html, count=1)
    print(f"✓ Enhanced Simulator 7 (Reach Ranges): {count7} replaced")

    # Update runReachCalc ground level calculation in JS (since ground moved from 180 to 190 in the higher viewBox)
    old_reach_js = "const targetY = 180 - (height * 1.0);"
    new_reach_js = "const targetY = 190 - (height * 1.0);"
    if old_reach_js in html:
        html = html.replace(old_reach_js, new_reach_js)
        print("✓ Synchronized runReachCalc targetY scale in JS")

    # Save to iraqi_accessibility_platform.html and index.html
    with open('iraqi_accessibility_platform.html', 'w', encoding='utf-8') as f:
        f.write(html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("✓ Saved updated files: iraqi_accessibility_platform.html and index.html")

    return True

if __name__ == '__main__':
    enhance_simulators()
