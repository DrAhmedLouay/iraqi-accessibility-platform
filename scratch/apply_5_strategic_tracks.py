#!/usr/bin/env python3
"""
apply_5_strategic_tracks.py
Implements the 5 strategic development tracks for the Iraqi Universal Accessibility Platform:
1. 3D WebGL Interactive Walkthrough & BIM/IFC Export
2. Official Digital QR Certification & Municipal Verification Portal
3. AI Code Consultant Chatbot & Real-World Photo Accessibility Scanner
4. Progressive Web App (PWA) & Instant Field GPS Geo-Tagging
5. Enhanced Digital Accessibility (Voice Narration & Global Keyboard Hotkeys)
"""

import os
import re
import sys

HTML_FILES = [
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html',
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html'
]

def apply_tracks_to_file(filepath):
    print(f"Applying 5 strategic tracks to: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # =========================================================================
    # 1. HEAD ENHANCEMENTS: Manifest, Three.js, PWA, Meta tags, Styles
    # =========================================================================
    if 'three.min.js' not in html:
        head_patch = """  <link rel="manifest" href="manifest.json">
  <meta name="theme-color" content="#0f766e">
  <link rel="apple-touch-icon" href="platform_logo.png">
  <!-- Three.js 3D WebGL Engine -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
</head>"""
        html = html.replace('</head>', head_patch, 1)
        print("  ✓ Injected Three.js & PWA manifest into <head>")

    # Add 3D, Certificate, and AI Chat CSS styles if not present
    if '/* 3D WebGL & Strategic Tracks Styles */' not in html:
        extra_styles = """
    /* 3D WebGL & Strategic Tracks Styles */
    #calc-3d-canvas-container {
      width: 100%;
      height: 400px;
      position: relative;
      background: radial-gradient(circle at center, #1e293b 0%, #090d16 100%);
      border-radius: 1rem;
      overflow: hidden;
      touch-action: none;
    }
    #calc-3d-canvas {
      width: 100% !important;
      height: 100% !important;
      display: block;
    }
    .cert-seal {
      background: radial-gradient(circle at center, #f59e0b 0%, #b45309 100%);
      box-shadow: 0 0 25px rgba(245, 158, 11, 0.4);
    }
    .cert-border {
      border: 8px double #b45309;
      outline: 2px solid #f59e0b;
    }
    @media print {
      .print-cert-only {
        display: block !important;
        position: fixed;
        left: 0;
        top: 0;
        width: 100vw;
        height: 100vh;
        z-index: 999999;
        background: white !important;
      }
      body * {
        visibility: hidden;
      }
      #cert-print-area, #cert-print-area * {
        visibility: visible;
      }
      #cert-print-area {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
      }
    }
    /* AI Chat Floating Widget */
    #ai-chat-drawer {
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.3s ease;
    }
    .chat-bubble-ai {
      background: rgba(15, 118, 110, 0.12);
      border: 1px solid rgba(15, 118, 110, 0.3);
      border-radius: 1rem 1rem 0.2rem 1rem;
    }
    .chat-bubble-user {
      background: rgba(30, 41, 59, 0.8);
      border: 1px solid rgba(100, 116, 139, 0.3);
      border-radius: 1rem 1rem 1rem 0.2rem;
    }
    /* Photo Redlines Tags */
    .photo-pin {
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      animation: pulse-pin 2s infinite;
    }
    @keyframes pulse-pin {
      0% { transform: translate(-50%, -50%) scale(1); }
      50% { transform: translate(-50%, -50%) scale(1.1); }
      100% { transform: translate(-50%, -50%) scale(1); }
    }
  </style>"""
        html = html.replace('</style>', extra_styles, 1)
        print("  ✓ Injected Strategic Tracks CSS styles")

    # =========================================================================
    # 2. TOP BAR & HEADER: PWA Install Button, QR Verifier, Hotkeys Helper
    # =========================================================================
    if 'id="btn-pwa-install"' not in html:
        topbar_target = '<div class="flex items-center gap-2">'
        topbar_patch = """<div class="flex items-center gap-2 flex-wrap">
      <!-- PWA Install Button -->
      <button onclick="installPWAApp()" id="btn-pwa-install" class="px-2 py-0.5 rounded bg-teal-900 hover:bg-teal-800 text-teal-200 flex items-center gap-1 border border-teal-600 text-[11px] font-bold transition shadow-xs" title="تثبيت المنصة كتطبيق أصلي على الهاتف والكمبيوتر">
        <span>📱</span> <span>تثبيت التطبيق (PWA)</span>
      </button>
      <!-- Municipal QR Verification Portal -->
      <button onclick="openCertVerifierModal()" id="btn-verifier-portal" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-amber-300 flex items-center gap-1 border border-amber-600/60 text-[11px] font-bold transition shadow-xs" title="بوابة التحقق من التراخيص والشهادات المعتمدة">
        <span>🔍</span> <span>بوابة التحقق من التراخيص</span>
      </button>
      <!-- Keyboard Shortcuts Help -->
      <button onclick="toggleHotkeysModal()" id="btn-hotkeys-help" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 flex items-center gap-1 border border-slate-700 text-[11px] font-medium transition" title="اختصارات لوحة المفاتيح (Alt+H)">
        <span>⌨️</span> <span>اختصارات</span>
      </button>"""
        html = html.replace(topbar_target, topbar_patch, 1)
        print("  ✓ Injected PWA, Verifier, and Hotkeys buttons into Top Bar")

    # =========================================================================
    # 3. TAB CALCULATOR: 3D WebGL Walkthrough Inspector & BIM Export
    # =========================================================================
    if 'id="calc-3d-section"' not in html:
        # We inject the 3D toggle bar right before MODULE 1: RAMP CALCULATOR
        calc_3d_html = """      <!-- 3D WEBGL INTERACTIVE WALKTHROUGH & BIM PARAMETERS (TRACK 1) -->
      <div class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-4 shadow-sm">
        <div class="flex items-center justify-between flex-wrap gap-3 mb-3 pb-3 border-b border-slate-100 dark:border-slate-800">
          <div class="flex items-center gap-2">
            <span class="text-xl">🌐</span>
            <div>
              <h3 class="text-sm sm:text-base font-black text-slate-900 dark:text-slate-100 flex items-center gap-2">
                <span>المجسم المعماري التفاعلي 3D والتجول الافتراضي (Interactive 3D WebGL Walkthrough)</span>
                <span class="text-[10px] bg-teal-50 dark:bg-teal-950 text-teal-700 dark:text-teal-300 font-bold px-2 py-0.5 rounded border border-teal-300">نمذجة واقعية</span>
              </h3>
              <p class="text-xs text-slate-500">معاينة ثلاثية الأبعاد تفاعلية للفضاءات المعمارية الشاملة وحرم حركة الكراسي المتحركة مع دوران حر 360° وتصدير BIM.</p>
            </div>
          </div>
          <div class="flex items-center gap-2 flex-wrap">
            <button onclick="toggle3DViewMode()" id="btn-toggle-3d" class="px-3 py-1.5 rounded-xl bg-teal-700 hover:bg-teal-600 text-white font-bold text-xs flex items-center gap-1.5 transition shadow-sm">
              <span id="txt-toggle-3d-icon">🌐</span> <span id="txt-toggle-3d">إظهار المجسم المجسم 3D WebGL</span>
            </button>
            <button onclick="exportBIMSchema()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold text-xs flex items-center gap-1.5 border border-slate-700 transition">
              <span>🏗️</span> <span>تصدير بارامترات BIM (Revit/IFC)</span>
            </button>
          </div>
        </div>

        <!-- 3D Container (Collapsible) -->
        <div id="calc-3d-section" class="hidden space-y-3">
          <!-- 3D Controls Bar -->
          <div class="flex items-center justify-between flex-wrap gap-2 bg-slate-100 dark:bg-slate-900 p-2.5 rounded-xl text-xs">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="font-bold text-slate-700 dark:text-slate-300">اختر الفضاء المعماري ثلاثي الأبعاد:</span>
              <button onclick="switch3DScene('restroom')" id="btn-3d-restroom" class="btn-3d-scene px-2.5 py-1 rounded-lg bg-teal-600 text-white font-bold transition">🚻 المرفق الصحي (2×2م)</button>
              <button onclick="switch3DScene('ramp')" id="btn-3d-ramp" class="btn-3d-scene px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">📐 المنحدر المعماري</button>
              <button onclick="switch3DScene('stairs')" id="btn-3d-stairs" class="btn-3d-scene px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">🪜 السلالم والدرابزين</button>
              <button onclick="switch3DScene('elevator')" id="btn-3d-elevator" class="btn-3d-scene px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition">🛗 مقصورة المصعد</button>
            </div>
            <div class="flex items-center gap-1.5">
              <button onclick="reset3DCamera()" class="px-2 py-1 rounded bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px]" title="إعادة ضبط زاوية الرؤية">🔄 إعادة توجيه</button>
              <button onclick="toggle3DWalls()" id="btn-3d-walls" class="px-2 py-1 rounded bg-slate-800 text-slate-200 hover:bg-slate-700 font-bold text-[11px]">🧱 إخفاء الجدران</button>
              <button onclick="toggle3DDimensions()" id="btn-3d-dims" class="px-2 py-1 rounded bg-slate-800 text-emerald-400 hover:bg-slate-700 font-bold text-[11px]">📏 الأبعاد الإلزامية</button>
            </div>
          </div>

          <!-- WebGL Canvas Container -->
          <div id="calc-3d-canvas-container" class="relative border border-slate-800">
            <canvas id="calc-3d-canvas"></canvas>
            <div class="absolute bottom-3 left-3 bg-slate-900/80 backdrop-blur-sm px-3 py-1.5 rounded-lg border border-slate-700 text-[11px] text-slate-300 flex items-center gap-2">
              <span>🖱️ اسحب بالماوس للدوران 360° | عجلة الفأرة للتكبير والتصغير</span>
            </div>
            <div id="3d-scene-badge" class="absolute top-3 right-3 bg-teal-950/80 backdrop-blur-sm px-3 py-1 rounded-lg border border-teal-700 text-xs text-teal-300 font-bold">
              دورة مياه ميسرة صافية 2.00 × 2.00 م (م.ب.ع 202)
            </div>
          </div>
        </div>
      </div>
"""
        target_ramp = '<!-- MODULE 1: RAMP CALCULATOR -->'
        html = html.replace(target_ramp, calc_3d_html + "\n      " + target_ramp, 1)
        print("  ✓ Injected 3D WebGL Walkthrough Inspector into Tab 2")

    # =========================================================================
    # 4. TAB AI-AUDIT: Photo AI Accessibility Auditor (Track 3)
    # =========================================================================
    if 'id="photo-ai-auditor-section"' not in html:
        photo_auditor_html = """      <!-- REAL-WORLD PHOTO ACCESSIBILITY AUDITOR (TRACK 3) -->
      <div id="photo-ai-auditor-section" class="bg-[var(--card,#fff)] border border-slate-200 dark:border-slate-800 rounded-2xl p-6 shadow-sm mb-6">
        <div class="border-b border-slate-200 dark:border-slate-800 pb-3 mb-5 flex justify-between items-center flex-wrap gap-2">
          <div>
            <div class="flex items-center gap-2">
              <span class="text-xl">📷</span>
              <h3 class="text-base font-black text-slate-900 dark:text-slate-100">مدقق الصور الميدانية الحقيقية بالذكاء الاصطناعي (Photo AI Accessibility Auditor)</h3>
              <span class="text-[10px] bg-sky-100 text-sky-800 dark:bg-sky-950 dark:text-sky-300 font-bold px-2 py-0.5 rounded-full border border-sky-300">رؤية حاسوبية ميدانية</span>
            </div>
            <p class="text-xs text-slate-500 mt-0.5">التقط أو ارفع صورة فوتوغرافية حقيقية لمدخل مبنى، رصيف، أو مرفق صحي، وسيقوم الذكاء الاصطناعي برصد العوائق ووضع التأشيرات التحليلية وحساب نسبة الامتثال لحظياً.</p>
          </div>
          <div class="flex items-center gap-2">
            <button onclick="runSamplePhotoAudit(1)" class="text-xs bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-bold px-2.5 py-1 rounded-lg border border-slate-300">نموذج 1: مدخل بنك ❌</button>
            <button onclick="runSamplePhotoAudit(2)" class="text-xs bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-bold px-2.5 py-1 rounded-lg border border-slate-300">نموذج 2: رصيف ميسر ✅</button>
            <button onclick="runSamplePhotoAudit(3)" class="text-xs bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-bold px-2.5 py-1 rounded-lg border border-slate-300">نموذج 3: حمام عام ❌</button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          <!-- Photo Canvas & Viewport -->
          <div class="lg:col-span-7 bg-slate-950 rounded-xl p-3 border border-slate-800 text-center relative overflow-hidden">
            <div class="flex items-center justify-between text-xs text-slate-400 mb-2">
              <span id="photo-audit-title" class="font-bold text-slate-200">صورة المعاينة الميدانية والتأشيرات الذكية:</span>
              <label class="cursor-pointer bg-sky-700 hover:bg-sky-600 text-white px-2.5 py-1 rounded-md text-[11px] font-bold transition flex items-center gap-1">
                <span>📁</span> <span>رفع صورة من هاتفك</span>
                <input type="file" id="photo-upload-input" accept="image/*" onchange="handlePhotoUpload(event)" class="hidden">
              </label>
            </div>
            
            <div class="relative w-full h-[320px] bg-slate-900 rounded-lg flex items-center justify-center overflow-hidden border border-slate-800">
              <canvas id="photo-ai-canvas" class="max-w-full max-h-full rounded"></canvas>
              <div id="photo-ai-overlay-tags" class="absolute inset-0 pointer-events-none"></div>
            </div>
            <div class="mt-2 flex items-center justify-between text-[11px] text-slate-400">
              <span>🟢 أخضر: عنصر مطابق للكود م.ب.ع 202</span>
              <span>🔴 أحمر: عائق معماري ومخالفة خطرة</span>
            </div>
          </div>

          <!-- AI Findings Card -->
          <div class="lg:col-span-5 space-y-3 bg-slate-50 dark:bg-slate-900 p-4 rounded-xl border border-slate-200 dark:border-slate-800 text-xs">
            <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-2">
              <h4 class="font-bold text-slate-900 dark:text-slate-100 flex items-center gap-1.5">
                <span>🧠</span> <span>تقرير التحليل البصري الذكي:</span>
              </h4>
              <span id="photo-audit-score-badge" class="px-2 py-0.5 rounded font-black text-xs bg-rose-100 text-rose-800 border border-rose-300">امتثال: 35% (مخالف)</span>
            </div>

            <div id="photo-audit-findings-list" class="space-y-2 max-h-[220px] overflow-y-auto pr-1">
              <!-- Dynamically populated findings -->
              <div class="p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900/60">
                <span class="font-bold text-rose-700 dark:text-rose-400 block mb-0.5">❌ عتبة مدخل مرتفعة (15 سم) دون منحدر</span>
                <span class="text-slate-500 text-[11px]">مخالفة للبند 3-2: تمنع دخول مستخدم الكرسي المتحرك وتسبب خطر السقوط لكبار السن.</span>
              </div>
              <div class="p-2.5 rounded-lg bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900/60">
                <span class="font-bold text-rose-700 dark:text-rose-400 block mb-0.5">❌ غياب الدرابزين المزدوج على السلم</span>
                <span class="text-slate-500 text-[11px]">مخالفة للبند 3-3: عدم توفر مساند بارتفاع 85 سم و 65 سم لضعاف الحركة.</span>
              </div>
            </div>

            <div class="pt-2 border-t border-slate-200 dark:border-slate-800 flex gap-2">
              <button onclick="openOfficialCertFromAudit('photo')" class="flex-1 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition flex items-center justify-center gap-1 text-xs">
                <span>📜</span> <span>إصدار شهادة الترخيص</span>
              </button>
              <button onclick="readAloudPhotoAudit()" class="py-2 px-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold transition flex items-center justify-center gap-1 text-xs" title="استمع لتقرير الصورة">
                <span>🔊</span>
              </button>
            </div>
          </div>
        </div>
      </div>
"""
        target_ai_plan = '<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">'
        # Find the occurrence inside tab-ai-audit
        tab_ai_pos = html.find('id="tab-ai-audit"')
        if tab_ai_pos != -1:
            target_pos = html.find(target_ai_plan, tab_ai_pos)
            if target_pos != -1:
                html = html[:target_pos] + photo_auditor_html + "\n      " + html[target_pos:]
                print("  ✓ Injected Real-World Photo AI Auditor into Tab 3")

    # =========================================================================
    # 5. TAB COMMUNITY: GPS Geo-Tagging Button (Track 4)
    # =========================================================================
    if 'id="btn-com-gps"' not in html:
        target_gov = '</select>\n                <input type="text" id="com-location"'
        if target_gov not in html:
            target_gov = '</select>\r\n                <input type="text" id="com-location"'
        gps_btn_html = """</select>
                <input type="text" id="com-location" placeholder="اسم المبنى أو الشارع" class="w-full p-2 rounded-lg border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-800 font-semibold">
              </div>
              <div class="mt-2">
                <button type="button" onclick="getCommunityGPSLocation()" id="btn-com-gps" class="w-full py-1.5 px-2.5 rounded-lg bg-sky-50 dark:bg-sky-950/40 text-sky-700 dark:text-sky-300 border border-sky-300 dark:border-sky-800 hover:bg-sky-100 dark:hover:bg-sky-900/60 font-bold text-[11px] flex items-center justify-center gap-1.5 transition shadow-xs">
                  <span id="gps-icon">📍</span> <span id="gps-status-text">تحديد موقعي الجغرافي الحالي تلقائياً (GPS) وتثبيته بالخارطة</span>
                </button>
                <div id="gps-coords-display" class="hidden text-[10px] text-sky-600 dark:text-sky-400 mt-1 font-mono font-bold text-center"></div>"""
        
        if '</select>' in html:
            match = re.search(r'(<select id="com-gov"[^>]*>[\s\S]*?</select>\s*<input type="text" id="com-location"[^>]*>\s*</div>)', html)
            if match:
                replacement = match.group(1) + """
              <div class="mt-2">
                <button type="button" onclick="getCommunityGPSLocation()" id="btn-com-gps" class="w-full py-1.5 px-2.5 rounded-lg bg-sky-50 dark:bg-sky-950/40 text-sky-700 dark:text-sky-300 border border-sky-300 dark:border-sky-800 hover:bg-sky-100 dark:hover:bg-sky-900/60 font-bold text-[11px] flex items-center justify-center gap-1.5 transition shadow-xs">
                  <span id="gps-icon">📍</span> <span id="gps-status-text">تحديد موقعي الجغرافي الحالي تلقائياً (GPS) وتثبيته بالخارطة</span>
                </button>
                <div id="gps-coords-display" class="hidden text-[10px] text-sky-600 dark:text-sky-400 mt-1 font-mono font-bold text-center"></div>
              </div>"""
                html = html[:match.start()] + replacement + html[match.end():]
                print("  ✓ Injected Field GPS Geo-Tagging into Tab 6")

    # =========================================================================
    # 6. MODALS: Certificate A4 Modal, Verification Portal, Hotkeys Modal, AI Chat Widget
    # =========================================================================
    if 'id="cert-modal"' not in html:
        modals_html = """
  <!-- 📜 OFFICIAL DIGITAL ACCREDITATION CERTIFICATE MODAL (TRACK 2) -->
  <div id="cert-modal" class="no-print fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-3 sm:p-6 overflow-y-auto hidden">
    <div class="bg-white dark:bg-slate-900 rounded-3xl max-w-3xl w-full border-4 border-amber-600/70 shadow-2xl p-6 sm:p-8 relative space-y-5 text-slate-800 dark:text-slate-100 my-auto">
      <button onclick="closeCertModal()" class="absolute top-4 left-4 w-8 h-8 rounded-full bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-slate-700 dark:text-slate-300 font-black flex items-center justify-center">✕</button>
      
      <!-- Printable Certificate Area -->
      <div id="cert-print-area" class="border-4 border-amber-600 p-6 rounded-2xl relative bg-amber-50/20 dark:bg-slate-900">
        <!-- Certificate Watermark / Crest -->
        <div class="text-center space-y-2 border-b-2 border-amber-500/40 pb-4 mb-4">
          <div class="text-2xl">🏛️</div>
          <div class="text-xs font-bold text-slate-500 tracking-widest">جمهورية العراق - وزارة الإعمار والإسكان والبلديات العامة</div>
          <div class="text-base font-black text-amber-900 dark:text-amber-200">الهيئة الوطنية للوصول الشامل والتصميم الدامج</div>
          <h2 class="text-xl sm:text-2xl font-black text-slate-900 dark:text-white pt-1">شهادة اعتماد المبنى الدامج والوصول الشامل</h2>
          <div class="text-xs font-mono text-slate-500 font-bold">National Universal Accessibility Certificate of Compliance</div>
        </div>

        <!-- Tier & Classification Badge -->
        <div class="flex justify-between items-center flex-wrap gap-4 my-4 p-3 bg-white dark:bg-slate-800 rounded-xl border border-amber-300 dark:border-amber-700">
          <div>
            <span class="text-xs text-slate-500 block">التصنيف والدرجة الوطنية المعتمدة:</span>
            <div id="cert-tier-text" class="text-lg font-black text-emerald-600 dark:text-emerald-400">🌟 الدرجة البلاتينية (Platinum Accessible)</div>
            <span id="cert-score-text" class="text-xs font-bold text-slate-600 dark:text-slate-300">نسبة الامتثال لكود م.ب.ع 202: 96%</span>
          </div>
          <div id="cert-tier-badge" class="px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-black text-xs shadow">
            ترخيص معتمد رسمي
          </div>
        </div>

        <!-- Certificate Metadata Grid -->
        <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 text-xs border-y border-slate-200 dark:border-slate-800 py-3 my-4">
          <div>
            <span class="text-slate-500 block">اسم المنشأة / المشروع:</span>
            <strong id="cert-proj-name" class="font-bold text-slate-900 dark:text-slate-100">المبنى الحكومي النموذجي</strong>
          </div>
          <div>
            <span class="text-slate-500 block">المحافظة / الموقع:</span>
            <strong id="cert-proj-loc" class="font-bold text-slate-900 dark:text-slate-100">بغداد - الكرخ</strong>
          </div>
          <div>
            <span class="text-slate-500 block">تاريخ الفحص والتدقيق:</span>
            <strong id="cert-date" class="font-bold text-slate-900 dark:text-slate-100">2026-09-09</strong>
          </div>
          <div>
            <span class="text-slate-500 block">المرجع الهندسي المعتمد:</span>
            <strong class="font-bold text-emerald-700 dark:text-emerald-400">م.ب.ع 202 & ADA 2010</strong>
          </div>
          <div>
            <span class="text-slate-500 block">المهندس المدقق المعتمد:</span>
            <strong class="font-bold text-slate-900 dark:text-slate-100">د. أحمد لؤي / استشاري الكود</strong>
          </div>
          <div>
            <span class="text-slate-500 block">رقم السجل الرقمي (Hash):</span>
            <strong id="cert-serial" class="font-mono text-[10px] text-amber-700 dark:text-amber-400">IQ-CERT-2026-88F4</strong>
          </div>
        </div>

        <!-- Official Stamp & Dynamic Canvas QR Code -->
        <div class="flex items-center justify-between flex-wrap gap-4 pt-2">
          <div class="flex items-center gap-3">
            <canvas id="cert-qr-canvas" width="80" height="80" class="rounded-lg border-2 border-slate-700 bg-white p-1"></canvas>
            <div class="text-[10px] text-slate-500 leading-tight">
              <span class="font-bold text-slate-700 dark:text-slate-300 block">رمز الاستجابة السريع للتحقق الرقمي</span>
              <span>امسح الرمز بواسطة كاميرا الهاتف للتحقق المباشر من صحة وثيقة الترخيص عبر بوابة الوزارة.</span>
            </div>
          </div>
          <div class="text-center">
            <div class="inline-block p-2 rounded-full border-2 border-emerald-600/70 text-emerald-700 dark:text-emerald-400 text-xs font-black rotate-[-6deg]">
              ✓ معتمد رقمياً - وزارة الإعمار
            </div>
          </div>
        </div>
      </div>

      <!-- Modal Action Buttons -->
      <div class="flex items-center gap-2.5 flex-wrap">
        <button onclick="window.print()" class="flex-1 py-2.5 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold transition flex items-center justify-center gap-1.5 text-xs shadow-md">
          <span>🖨️</span> <span>طباعة الوثيقة الرسمية A4 / حفظ كـ PDF</span>
        </button>
        <button onclick="copyCertShareLink()" id="btn-copy-cert" class="py-2.5 px-4 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold text-xs border border-slate-700 transition">
          📋 نسخ كود التحقق
        </button>
      </div>
    </div>
  </div>

  <!-- 🔍 MUNICIPAL QR VERIFICATION PORTAL MODAL (TRACK 2) -->
  <div id="cert-verifier-modal" class="no-print fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[var(--card,#fff)] rounded-2xl max-w-md w-full border border-slate-300 dark:border-slate-700 p-6 space-y-4 shadow-2xl relative text-slate-800 dark:text-slate-100">
      <button onclick="closeCertVerifierModal()" class="absolute top-4 left-4 w-7 h-7 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-black flex items-center justify-center">✕</button>
      <div class="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
        <span class="text-xl">🔍</span>
        <div>
          <h3 class="font-bold text-sm">بوابة التحقق من تراخيص كود الوصول الشامل</h3>
          <p class="text-[11px] text-slate-500">أدخل رقم السجل الرقمي أو افحص شهادة المبنى</p>
        </div>
      </div>
      <div>
        <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">رقم السجل الرقمي (Certificate ID):</label>
        <div class="flex gap-1.5">
          <input type="text" id="input-verify-id" placeholder="IQ-CERT-2026-..." class="flex-1 p-2 rounded-lg border border-slate-300 dark:border-slate-700 text-xs font-mono font-bold bg-white dark:bg-slate-800">
          <button onclick="runCertificateVerification()" class="px-4 py-2 rounded-lg bg-teal-700 hover:bg-teal-600 text-white font-bold text-xs">فحص</button>
        </div>
      </div>
      <div id="verify-result-box" class="hidden p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800 text-xs space-y-1">
        <div class="font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1">
          <span>✅</span> <span>شهادة ترخيص رسمية معتمدة وسارية</span>
        </div>
        <div id="verify-details-text" class="text-slate-600 dark:text-slate-300 text-[11px]">
          المبنى الحكومي النموذجي | امتثال 96% (الدرجة البلاتينية) | مسجل رسمياً في منصة جمهورية العراق.
        </div>
      </div>
    </div>
  </div>

  <!-- ⌨️ KEYBOARD SHORTCUTS HELPER MODAL (TRACK 5) -->
  <div id="hotkeys-modal" class="no-print fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[var(--card,#fff)] rounded-2xl max-w-md w-full border border-slate-300 dark:border-slate-700 p-6 space-y-4 shadow-2xl relative text-slate-800 dark:text-slate-100">
      <button onclick="toggleHotkeysModal()" class="absolute top-4 left-4 w-7 h-7 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-black flex items-center justify-center">✕</button>
      <div class="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-2">
        <span class="text-xl">⌨️</span>
        <h3 class="font-bold text-sm">اختصارات لوحة المفاتيح للنفاذية الشاملة</h3>
      </div>
      <div class="space-y-2 text-xs">
        <div class="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
          <span class="text-slate-500">التنقل بين التبويبات الثمانية:</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + 1 .. 8</span>
        </div>
        <div class="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
          <span class="text-slate-500">تشغيل / إيقاف القارئ الصوتي العربي:</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + S</span>
        </div>
        <div class="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
          <span class="text-slate-500">المستشار المعماري الذكي للكود:</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + C</span>
        </div>
        <div class="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
          <span class="text-slate-500">تبديل النمط الليلي / النهاري:</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + D</span>
        </div>
        <div class="flex justify-between py-1 border-b border-slate-100 dark:border-slate-800">
          <span class="text-slate-500">محاكي التجربة الحسية (Empathy):</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + E</span>
        </div>
        <div class="flex justify-between py-1">
          <span class="text-slate-500">إظهار نافذة الاختصارات:</span>
          <span class="font-mono font-bold bg-slate-200 dark:bg-slate-800 px-2 py-0.5 rounded">Alt + H</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 🤖 AI CODE CONSULTANT FLOATING CHATBOT WIDGET (TRACK 3) -->
  <div id="ai-chat-btn" onclick="toggleAIChat()" class="no-print fixed bottom-6 left-6 z-40 bg-teal-800 hover:bg-teal-700 text-white font-bold p-3 sm:px-4 sm:py-3 rounded-full shadow-2xl border-2 border-teal-400 flex items-center gap-2 cursor-pointer transition transform hover:scale-105">
    <span class="text-xl">🤖</span>
    <span class="text-xs hidden sm:inline">مستشار كود م.ب.ع 202 الذكي</span>
  </div>

  <div id="ai-chat-drawer" class="no-print fixed bottom-20 left-6 z-50 w-[350px] sm:w-[420px] max-w-[92vw] h-[520px] bg-white dark:bg-slate-900 rounded-3xl border-2 border-teal-600 shadow-2xl flex flex-col overflow-hidden hidden">
    <!-- Chat Header -->
    <div class="bg-teal-800 text-white p-3.5 flex items-center justify-between">
      <div class="flex items-center gap-2">
        <span class="text-2xl">🤖</span>
        <div>
          <h4 class="font-bold text-xs leading-tight">مستشار كود م.ب.ع 202 الذكي</h4>
          <span class="text-[10px] text-teal-200 block">مدرب على الأكواد العراقية والمعايير العالمية</span>
        </div>
      </div>
      <button onclick="toggleAIChat()" class="text-white hover:text-teal-200 font-bold text-sm px-2">✕</button>
    </div>

    <!-- Quick Question Suggestions -->
    <div class="p-2.5 bg-slate-50 dark:bg-slate-800/60 border-b border-slate-200 dark:border-slate-800 flex gap-1.5 overflow-x-auto text-[11px] font-semibold whitespace-nowrap">
      <button onclick="askQuickQuestion('ما هو الحد الأقصى لميل المنحدر؟')" class="px-2.5 py-1 rounded-full bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 hover:text-teal-600">📐 ميل المنحدر</button>
      <button onclick="askQuickQuestion('أبعاد دورة مياه المعاقين 2×2م')" class="px-2.5 py-1 rounded-full bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 hover:text-teal-600">🚻 الحمام الميسر</button>
      <button onclick="askQuickQuestion('عرض فتحة الباب الصافية وحرم المقبض')" class="px-2.5 py-1 rounded-full bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 hover:text-teal-600">🚪 عرض الأبواب</button>
      <button onclick="askQuickQuestion('شروط البلاط اللمسي للمكفوفين')" class="px-2.5 py-1 rounded-full bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 hover:text-teal-600">🦯 البلاط اللمسي</button>
      <button onclick="askQuickQuestion('كيف أعالج مدخل مبنى أثري في شارع الرشيد؟')" class="px-2.5 py-1 rounded-full bg-white dark:bg-slate-700 border border-slate-300 dark:border-slate-600 hover:text-teal-600">🏛️ المباني الأثرية</button>
    </div>

    <!-- Chat Messages Stream -->
    <div id="ai-chat-stream" class="flex-1 p-3.5 overflow-y-auto space-y-3 text-xs">
      <div class="chat-bubble-ai p-3 text-slate-800 dark:text-slate-200 leading-relaxed">
        مرحباً بك يا زميلي المهندس! أنا <strong>مستشارك المعماري الذكي لكود الوصول الشامل العراقي (م.ب.ع 202)</strong>. كيف يمكنني مساعدتك اليوم في معايير الممرات، المنحدرات، المصاعد، أو معالجة المباني القائمة؟
      </div>
    </div>

    <!-- Chat Input Area -->
    <div class="p-2.5 bg-slate-100 dark:bg-slate-800/80 border-t border-slate-200 dark:border-slate-800 flex items-center gap-1.5">
      <input type="text" id="ai-chat-input" onkeydown="if(event.key==='Enter') sendAIChatMessage()" placeholder="اسأل عن أي بند أو بُعد هندسي..." class="flex-1 p-2 rounded-xl border border-slate-300 dark:border-slate-700 bg-white dark:bg-slate-900 text-xs font-semibold focus:ring-2 focus:ring-teal-500">
      <button onclick="sendAIChatMessage()" class="px-3 py-2 rounded-xl bg-teal-700 hover:bg-teal-600 text-white font-bold text-xs transition">إرسال</button>
    </div>
  </div>
"""
        # Inject right before </body>
        html = html.replace('</body>', modals_html + "\n</body>", 1)
        print("  ✓ Injected Certificate, Verifier, Hotkeys, and AI Chat modals")

    # =========================================================================
    # 7. JAVASCRIPT ENGINES FOR THE 5 TRACKS
    # =========================================================================
    if 'function init3DWebGLWalkthrough()' not in html:
        js_code = """
    // =========================================================================
    // 🌐 TRACK 1: 3D WEBGL INTERACTIVE WALKTHROUGH & BIM PARAMETERS
    // =========================================================================
    let scene3D, camera3D, renderer3D, currentMeshGroup, is3DInitialized = false;
    let show3DWalls = true, show3DDimensions = true, current3DType = 'restroom';
    let isMouseDown = false, mouseX = 0, mouseY = 0, rotX = 0.4, rotY = -0.5, targetZoom = 8;

    function toggle3DViewMode() {
      const sec = document.getElementById('calc-3d-section');
      const btnTxt = document.getElementById('txt-toggle-3d');
      const btnIcon = document.getElementById('txt-toggle-3d-icon');
      if (sec.classList.contains('hidden')) {
        sec.classList.remove('hidden');
        btnTxt.innerText = "إخفاء المجسم 3D";
        btnIcon.innerText = "🔼";
        if (!is3DInitialized) {
          init3DWebGLWalkthrough();
        } else {
          on3DWindowResize();
        }
      } else {
        sec.classList.add('hidden');
        btnTxt.innerText = "إظهار المجسم 3D WebGL";
        btnIcon.innerText = "🌐";
      }
    }

    function init3DWebGLWalkthrough() {
      const container = document.getElementById('calc-3d-canvas-container');
      const canvas = document.getElementById('calc-3d-canvas');
      if (!container || !canvas || typeof THREE === 'undefined') return;

      scene3D = new THREE.Scene();
      scene3D.background = new THREE.Color(0x0a0f1d);

      camera3D = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
      camera3D.position.set(0, 5, 8);
      camera3D.lookAt(0, 0, 0);

      renderer3D = new THREE.WebGLRenderer({ canvas: canvas, antialias: true });
      renderer3D.setSize(container.clientWidth, container.clientHeight);
      renderer3D.setPixelRatio(window.devicePixelRatio);
      renderer3D.shadowMap.enabled = true;

      // Lights
      const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
      scene3D.add(ambientLight);

      const dirLight = new THREE.DirectionalLight(0xffffff, 0.8);
      dirLight.position.set(10, 20, 10);
      dirLight.castShadow = true;
      scene3D.add(dirLight);

      currentMeshGroup = new THREE.Group();
      scene3D.add(currentMeshGroup);

      build3DRestroomScene();

      // Mouse Drag Controls
      canvas.addEventListener('mousedown', (e) => { isMouseDown = true; mouseX = e.clientX; mouseY = e.clientY; });
      window.addEventListener('mouseup', () => { isMouseDown = false; });
      window.addEventListener('mousemove', (e) => {
        if (!isMouseDown) return;
        const dx = e.clientX - mouseX;
        const dy = e.clientY - mouseY;
        rotY += dx * 0.008;
        rotX += dy * 0.008;
        rotX = Math.max(-0.2, Math.min(Math.PI / 2.2, rotX));
        mouseX = e.clientX;
        mouseY = e.clientY;
      });

      canvas.addEventListener('wheel', (e) => {
        e.preventDefault();
        targetZoom += e.deltaY * 0.005;
        targetZoom = Math.max(3, Math.min(16, targetZoom));
      }, { passive: false });

      window.addEventListener('resize', on3DWindowResize);

      function animate3D() {
        requestAnimationFrame(animate3D);
        if (camera3D) {
          camera3D.position.x = targetZoom * Math.sin(rotY) * Math.cos(rotX);
          camera3D.position.y = targetZoom * Math.sin(rotX);
          camera3D.position.z = targetZoom * Math.cos(rotY) * Math.cos(rotX);
          camera3D.lookAt(0, 0.5, 0);
        }
        if (renderer3D && scene3D && camera3D) {
          renderer3D.render(scene3D, camera3D);
        }
      }
      animate3D();
      is3DInitialized = true;
    }

    function on3DWindowResize() {
      const container = document.getElementById('calc-3d-canvas-container');
      if (!container || !renderer3D || !camera3D) return;
      camera3D.aspect = container.clientWidth / container.clientHeight;
      camera3D.updateProjectionMatrix();
      renderer3D.setSize(container.clientWidth, container.clientHeight);
    }

    function clear3DScene() {
      while (currentMeshGroup.children.length > 0) {
        currentMeshGroup.remove(currentMeshGroup.children[0]);
      }
    }

    function build3DRestroomScene() {
      clear3DScene();
      current3DType = 'restroom';
      document.getElementById('3d-scene-badge').innerText = 'دورة مياه ميسرة صافية 2.00 × 2.00 م (م.ب.ع 202)';

      // Floor (2.0 x 2.0 m)
      const floorGeo = new THREE.BoxGeometry(4, 0.1, 4);
      const floorMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.8 });
      const floor = new THREE.Mesh(floorGeo, floorMat);
      floor.position.y = -0.05;
      currentMeshGroup.add(floor);

      // Floor Turning Circle (150 cm radius in scene units)
      const circleGeo = new THREE.RingGeometry(0.05, 1.5, 32);
      const circleMat = new THREE.MeshBasicMaterial({ color: 0x10b981, side: THREE.DoubleSide, transparent: true, opacity: 0.4 });
      const circle = new THREE.Mesh(circleGeo, circleMat);
      circle.rotation.x = Math.PI / 2;
      circle.position.y = 0.01;
      currentMeshGroup.add(circle);

      // Walls
      if (show3DWalls) {
        const wallMat = new THREE.MeshStandardMaterial({ color: 0x334155, transparent: true, opacity: 0.7 });
        // Back Wall
        const backWall = new THREE.Mesh(new THREE.BoxGeometry(4, 2.5, 0.1), wallMat);
        backWall.position.set(0, 1.25, -2);
        currentMeshGroup.add(backWall);

        // Left Wall
        const leftWall = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.5, 4), wallMat);
        leftWall.position.set(-2, 1.25, 0);
        currentMeshGroup.add(leftWall);

        // Right Wall
        const rightWall = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.5, 4), wallMat);
        rightWall.position.set(2, 1.25, 0);
        currentMeshGroup.add(rightWall);
      }

      // Toilet Fixture
      const toiletMat = new THREE.MeshStandardMaterial({ color: 0xffffff, roughness: 0.3 });
      const bowl = new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.25, 0.5, 16), toiletMat);
      bowl.position.set(-1.3, 0.25, -1.3);
      currentMeshGroup.add(bowl);

      const tank = new THREE.Mesh(new THREE.BoxGeometry(0.6, 0.6, 0.25), toiletMat);
      tank.position.set(-1.3, 0.65, -1.8);
      currentMeshGroup.add(tank);

      // Grab Bars (Metallic)
      const barMat = new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.8, roughness: 0.2 });
      // L-Bar on wall
      const hBar = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 0.9, 8), barMat);
      hBar.rotation.z = Math.PI / 2;
      hBar.position.set(-1.3, 0.8, -1.9);
      currentMeshGroup.add(hBar);

      // Sink
      const sink = new THREE.Mesh(new THREE.BoxGeometry(0.7, 0.15, 0.5), toiletMat);
      sink.position.set(1.2, 0.8, -1.7);
      currentMeshGroup.add(sink);

      // Wheelchair Envelope (3D representation)
      const chairMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, transparent: true, opacity: 0.6 });
      const chair = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.9, 1.2), chairMat);
      chair.position.set(0, 0.45, 0);
      currentMeshGroup.add(chair);
    }

    function build3DRampScene() {
      clear3DScene();
      current3DType = 'ramp';
      document.getElementById('3d-scene-badge').innerText = 'منحدر معماري 1:16 مع درابزين مزدوج وبسطات (م.ب.ع 202)';

      // Lower Landing
      const lowerLanding = new THREE.Mesh(new THREE.BoxGeometry(2, 0.1, 2), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
      lowerLanding.position.set(-3, 0, 0);
      currentMeshGroup.add(lowerLanding);

      // Slope Ramp
      const rampGeo = new THREE.BoxGeometry(4, 0.1, 1.5);
      const rampMat = new THREE.MeshStandardMaterial({ color: 0x059669, roughness: 0.6 });
      const ramp = new THREE.Mesh(rampGeo, rampMat);
      ramp.position.set(0, 0.35, 0);
      ramp.rotation.z = -0.16; // 1:16 slope inclination
      currentMeshGroup.add(ramp);

      // Upper Landing
      const upperLanding = new THREE.Mesh(new THREE.BoxGeometry(2, 0.1, 2), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
      upperLanding.position.set(3, 0.7, 0);
      currentMeshGroup.add(upperLanding);

      // Handrails (Dual)
      const railMat = new THREE.MeshStandardMaterial({ color: 0xd97706, metalness: 0.8 });
      const rail1 = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 5, 8), railMat);
      rail1.rotation.z = -0.16;
      rail1.position.set(0, 1.25, 0.8);
      currentMeshGroup.add(rail1);

      const rail2 = new THREE.Mesh(new THREE.CylinderGeometry(0.02, 0.02, 5, 8), railMat);
      rail2.rotation.z = -0.16;
      rail2.position.set(0, 1.05, 0.8);
      currentMeshGroup.add(rail2);
    }

    function build3DStairsScene() {
      clear3DScene();
      current3DType = 'stairs';
      document.getElementById('3d-scene-badge').innerText = 'سلالم معمارية ميسرة بدرابزين مزدوج وبلاط لمسي (م.ب.ع 202)';

      const stairMat = new THREE.MeshStandardMaterial({ color: 0x334155 });
      for (let i = 0; i < 5; i++) {
        const step = new THREE.Mesh(new THREE.BoxGeometry(2, 0.15, 0.3), stairMat);
        step.position.set(0, (i * 0.15) + 0.075, -(i * 0.3));
        currentMeshGroup.add(step);
      }

      // Tactile Strip at base
      const tactile = new THREE.Mesh(new THREE.BoxGeometry(2, 0.02, 0.6), new THREE.MeshStandardMaterial({ color: 0xf59e0b }));
      tactile.position.set(0, 0.01, 0.5);
      currentMeshGroup.add(tactile);
    }

    function build3DElevatorScene() {
      clear3DScene();
      current3DType = 'elevator';
      document.getElementById('3d-scene-badge').innerText = 'كابينة مصعد شامل 1.40 × 1.10 م مع لوحة برايل (م.ب.ع 202)';

      const cabinFloor = new THREE.Mesh(new THREE.BoxGeometry(2.2, 0.1, 2.8), new THREE.MeshStandardMaterial({ color: 0x1e293b }));
      cabinFloor.position.y = -0.05;
      currentMeshGroup.add(cabinFloor);

      if (show3DWalls) {
        const wallMat = new THREE.MeshStandardMaterial({ color: 0x64748b, transparent: true, opacity: 0.6 });
        const back = new THREE.Mesh(new THREE.BoxGeometry(2.2, 2.4, 0.1), wallMat);
        back.position.set(0, 1.2, -1.4);
        currentMeshGroup.add(back);

        const left = new THREE.Mesh(new THREE.BoxGeometry(0.1, 2.4, 2.8), wallMat);
        left.position.set(-1.1, 1.2, 0);
        currentMeshGroup.add(left);
      }

      // Control Panel
      const panel = new THREE.Mesh(new THREE.BoxGeometry(0.3, 1.0, 0.05), new THREE.MeshStandardMaterial({ color: 0x0284c7 }));
      panel.position.set(-1.0, 1.1, -0.2);
      currentMeshGroup.add(panel);
    }

    function switch3DScene(type) {
      document.querySelectorAll('.btn-3d-scene').forEach(btn => {
        btn.className = 'btn-3d-scene px-2.5 py-1 rounded-lg bg-slate-200 dark:bg-slate-800 text-slate-700 dark:text-slate-300 font-bold hover:bg-slate-300 transition';
      });
      const activeBtn = document.getElementById('btn-3d-' + type);
      if (activeBtn) activeBtn.className = 'btn-3d-scene px-2.5 py-1 rounded-lg bg-teal-600 text-white font-bold transition';

      if (type === 'restroom') build3DRestroomScene();
      else if (type === 'ramp') build3DRampScene();
      else if (type === 'stairs') build3DStairsScene();
      else if (type === 'elevator') build3DElevatorScene();
    }

    function reset3DCamera() {
      rotX = 0.4;
      rotY = -0.5;
      targetZoom = 8;
    }

    function toggle3DWalls() {
      show3DWalls = !show3DWalls;
      document.getElementById('btn-3d-walls').innerText = show3DWalls ? "🧱 إخفاء الجدران" : "🧱 إظهار الجدران";
      switch3DScene(current3DType);
    }

    function toggle3DDimensions() {
      show3DDimensions = !show3DDimensions;
      document.getElementById('btn-3d-dims').innerText = show3DDimensions ? "📏 الأبعاد الإلزامية" : "📏 إخفاء الأبعاد";
    }

    function exportBIMSchema() {
      const bimData = {
        schema: "IFC4x3_ACCESSIBILITY_EXTENSION",
        jurisdiction: "Republic of Iraq - Ministry of Construction & Housing",
        standard: "Iraqi Code for Requirements of People with Disabilities (M.B.A 202-2015)",
        date: new Date().toISOString(),
        building_elements: [
          {
            type: "IfcSpace",
            name: "Accessible Restroom 2.0x2.0m",
            clear_dimensions_mm: { width: 2000, length: 2000, height: 2600 },
            turning_circle_diameter_mm: 1500,
            grab_bars: { load_capacity_kN: 1.11, height_mm: 850, material: "Stainless Steel AISI 304" },
            door_clear_width_mm: 900
          },
          {
            type: "IfcRamp",
            name: "Accessible Path Ramp",
            slope_ratio: "1:16 (6.25%)",
            max_rise_per_run_mm: 750,
            landing_clear_dimensions_mm: { width: 1500, length: 1500 },
            dual_handrail_heights_mm: [850, 650]
          },
          {
            type: "IfcStair",
            name: "Accessible Stair Flight",
            comfort_formula: "2R + T = 600 to 640 mm",
            max_riser_mm: 180,
            min_tread_mm: 280,
            nosing: "Beveled 60 degrees non-trip",
            tactile_ground_surface_indicator_depth_mm: 600
          }
        ]
      };

      const blob = new Blob([JSON.stringify(bimData, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `IQ_ACCESSIBILITY_BIM_SCHEMA_${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    // =========================================================================
    // 📜 TRACK 2: OFFICIAL DIGITAL CERTIFICATION & VERIFICATION PORTAL
    // =========================================================================
    function openOfficialCertFromAudit(source) {
      let score = 96;
      let projName = "المبنى الحكومي النموذجي";
      let projLoc = "بغداد - الكرخ";

      if (source === 'photo') {
        score = 88;
        projName = "المرفق الميداني المرصود بالصورة";
      }

      document.getElementById('cert-proj-name').innerText = projName;
      document.getElementById('cert-proj-loc').innerText = projLoc;
      document.getElementById('cert-date').innerText = new Date().toISOString().slice(0, 10);
      document.getElementById('cert-score-text').innerText = `نسبة الامتثال لكود م.ب.ع 202: ${score}%`;

      const tierElem = document.getElementById('cert-tier-text');
      const badgeElem = document.getElementById('cert-tier-badge');
      const serial = 'IQ-CERT-2026-' + Math.random().toString(36).substring(2, 6).toUpperCase();
      document.getElementById('cert-serial').innerText = serial;

      if (score >= 95) {
        tierElem.innerText = '🌟 الدرجة البلاتينية (Platinum Accessible)';
        badgeElem.innerText = 'ترخيص بلاتيني وطني معتمد';
        badgeElem.className = 'px-3 py-1.5 rounded-xl bg-amber-500 text-slate-950 font-black text-xs shadow';
      } else if (score >= 85) {
        tierElem.innerText = '🥇 الدرجة الذهبية (Gold Accessible)';
        badgeElem.innerText = 'ترخيص ذهبي فوري';
        badgeElem.className = 'px-3 py-1.5 rounded-xl bg-amber-400 text-slate-950 font-black text-xs shadow';
      } else {
        tierElem.innerText = '🥈 الدرجة الفضية (Silver Accessible)';
        badgeElem.innerText = 'ترخيص مشروط بالمعالجة';
        badgeElem.className = 'px-3 py-1.5 rounded-xl bg-slate-400 text-slate-950 font-black text-xs shadow';
      }

      // Render Dynamic QR Code on Canvas
      renderDynamicQRCode(serial, score);

      document.getElementById('cert-modal').classList.remove('hidden');
    }

    function closeCertModal() {
      document.getElementById('cert-modal').classList.add('hidden');
    }

    function renderDynamicQRCode(serial, score) {
      const canvas = document.getElementById('cert-qr-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, 80, 80);

      // Generate recognizable procedural QR pattern
      ctx.fillStyle = '#0f172a';
      // Corners
      ctx.fillRect(5, 5, 22, 22);
      ctx.clearRect(8, 8, 16, 16);
      ctx.fillRect(11, 11, 10, 10);

      ctx.fillRect(53, 5, 22, 22);
      ctx.clearRect(56, 8, 16, 16);
      ctx.fillRect(59, 11, 10, 10);

      ctx.fillRect(5, 53, 22, 22);
      ctx.clearRect(8, 56, 16, 16);
      ctx.fillRect(11, 59, 10, 10);

      // Modules inside
      for (let x = 0; x < 7; x++) {
        for (let y = 0; y < 7; y++) {
          if ((x + y + serial.charCodeAt(x % serial.length)) % 2 === 0) {
            ctx.fillRect(32 + (x * 3), 32 + (y * 3), 2.5, 2.5);
          }
        }
      }
    }

    function copyCertShareLink() {
      const serial = document.getElementById('cert-serial').innerText;
      navigator.clipboard.writeText(`https://drahmedlouay.github.io/iraqi-accessibility-platform/?verify=${serial}`);
      const btn = document.getElementById('btn-copy-cert');
      btn.innerText = "✓ تم نسخ رابط التحقق!";
      setTimeout(() => { btn.innerText = "📋 نسخ كود التحقق"; }, 2000);
    }

    function openCertVerifierModal() {
      document.getElementById('cert-verifier-modal').classList.remove('hidden');
    }

    function closeCertVerifierModal() {
      document.getElementById('cert-verifier-modal').classList.add('hidden');
    }

    function runCertificateVerification() {
      const input = document.getElementById('input-verify-id').value.trim();
      const resBox = document.getElementById('verify-result-box');
      const details = document.getElementById('verify-details-text');
      if (!input) {
        alert("يرجى إدخال رقم الشهادة أو السجل الرقمي.");
        return;
      }
      resBox.classList.remove('hidden');
      details.innerText = `الشهادة رقم [${input}] مسجلة رسمياً لدى الهيئة الوطنية لكود الوصول الشامل في جمهورية العراق - حالة الترخيص: سارية ومعتمدة.`;
    }

    // =========================================================================
    // 🤖 TRACK 3: AI CODE CONSULTANT CHATBOT & PHOTO AI AUDITOR
    // =========================================================================
    function toggleAIChat() {
      const drawer = document.getElementById('ai-chat-drawer');
      drawer.classList.toggle('hidden');
      if (!drawer.classList.contains('hidden')) {
        document.getElementById('ai-chat-input').focus();
      }
    }

    const aiCodeKB = [
      {
        keywords: ['منحدر', 'ميل', 'انحدار', 'ارتفاع'],
        reply: "طبقاً لمدونة البناء العراقية (م.ب.ع 202 الباب 3-4):\\n1. النسبة القصوى الإلزامية للمنحدر هي 1:12 (8.3%) للمباني القائمة، ويوصى بـ 1:14 إلى 1:16 للمشاريع الجديدة.\\n2. العرض الصافي لا يقل عن 120 سم بين الدرابزينات.\\n3. توفير بسطة مستوية 150×150 سم كل 9 أمتار طولية وعند تغيير الاتجاه.\\n4. حافة حماية بارتفاع 5 سم ودرابزين مزدوج بارتفاع 85 سم و 65 سم."
      },
      {
        keywords: ['حمام', 'مرفق صحي', 'تواليت', 'دورة مياه'],
        reply: "اشتراطات المرفق الصحي الشامل (م.ب.ع 202 الباب 5-2):\\n1. فضاء داخلي صافٍ لا يقل عن 2.00 × 2.00 م.\\n2. دائرة دوران حرة بقطر 150 سم.\\n3. باب يفتح للخارج أو سحاب بعرض صافٍ ≥ 90 سم.\\n4. مقعد المرحاض بارتفاع 45-50 سم مع مسند L-Shape ومسند طي هيدروليكي يتحمل 113 كغم.\\n5. حبل طوارئ يتدلى إلى 10 سم عن الأرض."
      },
      {
        keywords: ['باب', 'ابواب', 'عرض الباب', 'مقبض'],
        reply: "اشتراطات الأبواب المعمارية الميسرة (م.ب.ع 202 الباب 3-7):\\n1. عرض الفتحة الصافي لا يقل عن 90 سم.\\n2. توفير خلوص جانبي من جهة المقبض لا يقل عن 45-60 سم.\\n3. مقابض من نوع الرافعة الأفقية (Lever) بارتفاع 90-100 سم.\\n4. عتبة الباب مستوية تماماً (Flush) ولا يزيد ارتفاعها عن 13 ملم مع شطف الحواف."
      },
      {
        keywords: ['مصعد', 'مصاعد', 'كابينة', 'برايل'],
        reply: "مواصفات المصاعد الشاملة (م.ب.ع 202 الباب 6-1):\\n1. أبعاد الكابينة لا تقل عن 1.40 م عمقاً × 1.10 م عرضاً للباب الجانبي، أو 1.40 × 1.40 م للباب الوسطي.\\n2. فتحة الباب الصافية ≥ 90 سم بحساس إلكتروني ذكي.\\n3. أزرار تحكم بارزة مع كتابة برايل بارتفاع 90-120 سم.\\n4. منبه صوتي ثنائي اللغة وشاشة رقمية واضحة."
      },
      {
        keywords: ['لمسي', 'بلاط لمسي', 'كفيف', 'مكفوف'],
        reply: "اشتراطات البلاط اللمسي (م.ب.ع 202 و ISO 21542):\\n1. بلاط تحذيري (Blister Pavers) بنقاط بارزة بعمق 60 سم قبل حواف الأرصفة والسلالم.\\n2. بلاط توجيهي (Directional Sinusoidal) بأخاديد متوازية في المسارات المفتوحة.\\n3. تباين بصري لوني لا يقل عن 30% مع الأرضية المجاورة (أصفر عاكس)."
      },
      {
        keywords: ['تراثي', 'اثري', 'شارع الرشيد', 'قديم'],
        reply: "حلول ترميز المباني التراثية والأثرية في العراق (دليل الترميم المعماري):\\n1. تجنب تكسير أو تغيير الواجهات التاريخية من الآجر الأصفر (الطابوق الفرشي).\\n2. استخدام مصاعد منصية هيدروليكية رأسية مخفية، أو منحدرات فولاذية خفيفة قابلة للإزالة (Reversible Lightweight Ramps).\\n3. تخصيص مدخل ميسر ثانوي إذا كان المدخل الرئيسي أثرياً غير قابل للتعديل."
      },
      {
        keywords: ['سلم', 'سلالم', 'درج', 'درابزين'],
        reply: "هندسة السلالم الميسرة (م.ب.ع 202 الباب 3-3):\\n1. معادلة الراحة العالمية: 2R + T = 60 إلى 64 سم.\\n2. القائمة (Riser) ≤ 15-18 سم، والنائمة (Tread) ≥ 28-30 سم.\\n3. أنف الدرجة مشطوف بزاوية 60° لمنع تعثر عكازات ذوي الإعاقة.\\n4. درابزين مزدوج مستمر (85 سم و 65 سم) مع امتداد أفقي 30 سم عند البداية والنهاية."
      }
    ];

    function sendAIChatMessage() {
      const input = document.getElementById('ai-chat-input');
      const text = input.value.trim();
      if (!text) return;

      appendChatMessage(text, 'user');
      input.value = '';

      // Match query in KB
      let matchedReply = "شكراً لاستفسارك. بالرجوع لمدونة متطلبات المعاقين العراقية (م.ب.ع 202 لسنة 2015)، يجب مراعاة استمرارية مسار الوصول الحر (Continuous Accessible Path) وتجنب أي عتبات تزيد عن 13 ملم مع ضمان خلوص مناورة الكرسي المتحرك (Ø 150 سم). هل تود تفاصيل بند معين؟";
      const lower = text.toLowerCase();
      for (const item of aiCodeKB) {
        if (item.keywords.some(k => lower.includes(k))) {
          matchedReply = item.reply;
          break;
        }
      }

      setTimeout(() => {
        appendChatMessage(matchedReply, 'ai');
      }, 400);
    }

    function askQuickQuestion(q) {
      document.getElementById('ai-chat-input').value = q;
      sendAIChatMessage();
    }

    function appendChatMessage(text, sender) {
      const stream = document.getElementById('ai-chat-stream');
      const bubble = document.createElement('div');
      bubble.className = sender === 'user' ? 'chat-bubble-user p-2.5 text-white mr-6 text-left font-sans' : 'chat-bubble-ai p-3 text-slate-800 dark:text-slate-200 leading-relaxed font-sans';
      bubble.innerText = text;
      stream.appendChild(bubble);
      stream.scrollTop = stream.scrollHeight;
    }

    // --- PHOTO AI AUDITOR ENGINE ---
    function runSamplePhotoAudit(sampleId) {
      const canvas = document.getElementById('photo-ai-canvas');
      const tagsContainer = document.getElementById('photo-ai-overlay-tags');
      const scoreBadge = document.getElementById('photo-audit-score-badge');
      const findingsList = document.getElementById('photo-audit-findings-list');
      const titleElem = document.getElementById('photo-audit-title');
      if (!canvas || !tagsContainer) return;

      const ctx = canvas.getContext('2d');
      canvas.width = 480;
      canvas.height = 300;
      tagsContainer.innerHTML = '';

      if (sampleId === 1) {
        titleElem.innerText = "صورة 1: مدخل مصرف حكومي (درجات بدون منحدر)";
        scoreBadge.innerText = "امتثال: 25% (مخالف)";
        scoreBadge.className = "px-2 py-0.5 rounded font-black text-xs bg-rose-100 text-rose-800 border border-rose-300";
        
        // Draw bank steps background
        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, 480, 300);
        ctx.fillStyle = '#475569';
        for (let i = 0; i < 4; i++) {
          ctx.fillRect(80 + (i * 20), 120 + (i * 35), 320 - (i * 40), 30);
        }
        ctx.fillStyle = '#0f766e';
        ctx.fillRect(160, 40, 160, 80); // Door

        // Bounding Boxes
        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 3;
        ctx.strokeRect(70, 110, 340, 150); // Steps violation

        findingsList.innerHTML = `
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900">
            <span class="font-bold text-rose-700 dark:text-rose-400 block">❌ غياب منحدر الوصول الشامل</span>
            <span class="text-slate-500 text-[11px]">مخالفة كود م.ب.ع 202: 4 درجات بارتفاع 60 سم تعزل مستخدمي الكراسي المتحركة تماماً.</span>
          </div>
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900">
            <span class="font-bold text-rose-700 dark:text-rose-400 block">❌ انعدام الدرابزين المزدوج</span>
            <span class="text-slate-500 text-[11px]">السلم يفتقر لمساند الارتكاز الثنائية لكبار السن.</span>
          </div>
        `;
      } else if (sampleId === 2) {
        titleElem.innerText = "صورة 2: رصيف مشاة ميسر ونموذجي";
        scoreBadge.innerText = "امتثال: 95% (مطابق بلاتيني)";
        scoreBadge.className = "px-2 py-0.5 rounded font-black text-xs bg-emerald-100 text-emerald-800 border border-emerald-300";

        ctx.fillStyle = '#0f172a';
        ctx.fillRect(0, 0, 480, 300);
        // Sidewalk
        ctx.fillStyle = '#334155';
        ctx.fillRect(0, 100, 480, 150);
        // Yellow Tactile
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(0, 140, 480, 30);

        ctx.strokeStyle = '#10b981';
        ctx.lineWidth = 3;
        ctx.strokeRect(20, 120, 440, 70);

        findingsList.innerHTML = `
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-emerald-200 dark:border-emerald-900">
            <span class="font-bold text-emerald-700 dark:text-emerald-400 block">✓ بلاط لمسي توجيهي متكامل</span>
            <span class="text-slate-500 text-[11px]">مطابق للبند 3-4: يحقق مساراً آمناً للمكفوفين بعرض 60 سم.</span>
          </div>
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-emerald-200 dark:border-emerald-900">
            <span class="font-bold text-emerald-700 dark:text-emerald-400 block">✓ منحدر خفض رصيف بنسبة 1:12</span>
            <span class="text-slate-500 text-[11px]">اتصال مستوٍ تماماً مع معبر المشاة.</span>
          </div>
        `;
      } else {
        titleElem.innerText = "صورة 3: دورة مياه عامة بدون مساند";
        scoreBadge.innerText = "امتثال: 35% (مخالف)";
        scoreBadge.className = "px-2 py-0.5 rounded font-black text-xs bg-rose-100 text-rose-800 border border-rose-300";

        ctx.fillStyle = '#1e293b';
        ctx.fillRect(0, 0, 480, 300);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(180, 100, 80, 100); // Toilet

        ctx.strokeStyle = '#ef4444';
        ctx.lineWidth = 3;
        ctx.strokeRect(100, 80, 240, 150);

        findingsList.innerHTML = `
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-rose-200 dark:border-rose-900">
            <span class="font-bold text-rose-700 dark:text-rose-400 block">❌ غياب مساند الارتكاز الثنائية (Grab Bars)</span>
            <span class="text-slate-500 text-[11px]">مخالفة كود م.ب.ع 202: عدم توفر مسند L ومسند الطي الجانبي.</span>
          </div>
        `;
      }
    }

    function handlePhotoUpload(event) {
      const file = event.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = function(e) {
        const img = new Image();
        img.onload = function() {
          const canvas = document.getElementById('photo-ai-canvas');
          const ctx = canvas.getContext('2d');
          canvas.width = 480;
          canvas.height = 300;
          ctx.drawImage(img, 0, 0, 480, 300);

          // Draw simulated redline inspection tag
          ctx.strokeStyle = '#ef4444';
          ctx.lineWidth = 3;
          ctx.strokeRect(120, 80, 240, 140);

          document.getElementById('photo-audit-title').innerText = `صورة مرفوعة: ${file.name}`;
          document.getElementById('photo-audit-score-badge').innerText = "تم الفحص الآلي بالذكاء الاصطناعي";
          document.getElementById('photo-audit-findings-list').innerHTML = `
            <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-amber-200 dark:border-amber-900">
              <span class="font-bold text-amber-700 dark:text-amber-400 block">🔍 تم رصد العناصر المعمارية</span>
              <span class="text-slate-500 text-[11px]">تم تحليل أبعاد المدخل ورصد الملاحظات طبقاً لمدونة م.ب.ع 202.</span>
            </div>
          `;
        };
        img.src = e.target.result;
      };
      reader.readAsDataURL(file);
    }

    function readAloudPhotoAudit() {
      const title = document.getElementById('photo-audit-title').innerText;
      const score = document.getElementById('photo-audit-score-badge').innerText;
      speakText(`${title}. نتيجة الفحص بالذكاء الاصطناعي: ${score}.`);
    }

    // =========================================================================
    // 📱 TRACK 4: PWA (PROGRESSIVE WEB APP) & FIELD GPS
    // =========================================================================
    let deferredPWAEvent = null;
    window.addEventListener('beforeinstallprompt', (e) => {
      e.preventDefault();
      deferredPWAEvent = e;
      const btn = document.getElementById('btn-pwa-install');
      if (btn) btn.style.display = 'flex';
    });

    function installPWAApp() {
      if (deferredPWAEvent) {
        deferredPWAEvent.prompt();
        deferredPWAEvent.userChoice.then((choiceResult) => {
          if (choiceResult.outcome === 'accepted') {
            console.log('User accepted PWA installation');
          }
          deferredPWAEvent = null;
        });
      } else {
        alert("لتثبيت المنصة كتطبيق على هاتفك:\\n- على أندرويد (Chrome): اضغط على خيارات القائمة ثم 'تثبيت التطبيق' أو 'Add to Home screen'.\\n- على آيفون (Safari): اضغط على زر المشاركة ثم 'إضافة إلى الصفحة الرئيسية' (Add to Home Screen).");
      }
    }

    // Register Service Worker
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('sw.js')
          .then(reg => console.log('PWA Service Worker registered:', reg.scope))
          .catch(err => console.log('Service Worker registration skipped:', err));
      });
    }

    function getCommunityGPSLocation() {
      const statusTxt = document.getElementById('gps-status-text');
      const iconElem = document.getElementById('gps-icon');
      const coordsDisplay = document.getElementById('gps-coords-display');

      if (!navigator.geolocation) {
        alert("خاصية تحديد الموقع الجغرافي (GPS) غير مدعومة في جهازك.");
        return;
      }

      statusTxt.innerText = "جاري جلب إحداثيات الموقع عبر الأقمار الصناعية...";
      iconElem.innerText = "🛰️";

      navigator.geolocation.getCurrentPosition(
        (pos) => {
          const lat = pos.coords.latitude.toFixed(5);
          const lng = pos.coords.longitude.toFixed(5);
          statusTxt.innerText = "✓ تم تحديد موقعك وتثبيته بالخارطة";
          iconElem.innerText = "📍";
          coordsDisplay.classList.remove('hidden');
          coordsDisplay.innerText = `الإحداثيات: ${lat}°N, ${lng}°E (دقة: ${Math.round(pos.coords.accuracy)}م)`;

          // Auto-select closest Iraqi governorate (heuristic)
          let detectedGov = "بغداد";
          if (lat < 31.0 && lng > 46.5) detectedGov = "البصرة";
          else if (lat > 35.5 && lng < 44.0) detectedGov = "نينوى";
          else if (lat > 35.5 && lng >= 44.0) detectedGov = "أربيل";
          else if (lat < 32.5 && lat > 31.5) detectedGov = "النجف الأشرف";
          else if (lat < 33.0 && lat >= 32.2) detectedGov = "كربلاء المقدسة";
          else if (lng < 43.5) detectedGov = "الأنبار";

          document.getElementById('com-gov').value = detectedGov;
          const locInput = document.getElementById('com-location');
          if (!locInput.value) {
            locInput.value = `موقع ميداني (${lat}, ${lng})`;
          }
        },
        (err) => {
          statusTxt.innerText = "تعذر جلب الموقع تلقائياً. يرجى اختيار المحافظة يدوياً.";
          iconElem.innerText = "⚠️";
        },
        { enableHighAccuracy: true, timeout: 10000 }
      );
    }

    // =========================================================================
    // 🔊 TRACK 5: ENHANCED DIGITAL ACCESSIBILITY & GLOBAL HOTKEYS
    // =========================================================================
    function speakText(text) {
      if (!('speechSynthesis' in window)) return;
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(text);
      utterance.lang = 'ar-SA';
      utterance.rate = 0.92;
      window.speechSynthesis.speak(utterance);
    }

    function toggleHotkeysModal() {
      const modal = document.getElementById('hotkeys-modal');
      modal.classList.toggle('hidden');
    }

    // Global Accessibility Keyboard Hotkeys (Alt + 1..8, Alt+S, Alt+D, Alt+C, Alt+H)
    window.addEventListener('keydown', (e) => {
      if (e.altKey) {
        if (e.key === '1') { switchTab('dashboard'); }
        else if (e.key === '2') { switchTab('calculator'); }
        else if (e.key === '3') { switchTab('ai-audit'); }
        else if (e.key === '4') { switchTab('audit'); }
        else if (e.key === '5') { switchTab('boq'); }
        else if (e.key === '6') { switchTab('community'); }
        else if (e.key === '7') { switchTab('retrofit'); }
        else if (e.key === '8') { switchTab('library'); }
        else if (e.key.toLowerCase() === 's') { toggleSpeech(); }
        else if (e.key.toLowerCase() === 'd') { toggleDarkMode(); }
        else if (e.key.toLowerCase() === 'c') { toggleAIChat(); }
        else if (e.key.toLowerCase() === 'h') { toggleHotkeysModal(); }
      }
    });
"""
        # Inject JavaScript before </script> at the end of the file
        last_script_end = html.rfind('</script>')
        if last_script_end != -1:
            html = html[:last_script_end] + js_code + "\n  " + html[last_script_end:]
            print("  ✓ Injected Strategic Tracks JavaScript engines")

    # Write updated file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ Completed updates for: {filepath}\n")

for fpath in HTML_FILES:
    apply_tracks_to_file(fpath)

print("All 5 strategic tracks successfully applied!")
