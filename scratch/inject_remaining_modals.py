#!/usr/bin/env python3
"""
inject_remaining_modals.py
Injects cert-verifier-modal, hotkeys-modal, ai-chat-btn, and ai-chat-drawer
into iraqi_accessibility_platform.html and index.html, and wires up openOfficialCertFromAudit.
"""

import sys
import re

FILES = [
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html',
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html'
]

MODALS_HTML = """
  <!-- 🔍 MUNICIPAL QR VERIFICATION PORTAL MODAL (TRACK 2) -->
  <div id="cert-verifier-modal" class="no-print fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full border border-slate-300 dark:border-slate-700 p-6 space-y-4 shadow-2xl relative text-slate-800 dark:text-slate-100">
      <button onclick="closeCertVerifierModal()" class="absolute top-4 left-4 w-7 h-7 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 font-black flex items-center justify-center">✕</button>
      <div class="flex items-center gap-2 border-b border-slate-200 dark:border-slate-800 pb-3">
        <span class="text-xl">🔍</span>
        <div>
          <h3 class="font-bold text-sm">بوابة التحقق من تراخيص كود الوصول الشامل</h3>
          <p class="text-[11px] text-slate-500">أدخل رقم السجل الرقمي للشهادة للتأكد من مطابقتها الرسمية</p>
        </div>
      </div>
      <div>
        <label class="block text-xs font-bold text-slate-700 dark:text-slate-300 mb-1">رقم السجل الرقمي (Certificate ID):</label>
        <div class="flex gap-1.5">
          <input type="text" id="input-verify-id" placeholder="IRQ-ACC-2026-..." class="flex-1 p-2 rounded-lg border border-slate-300 dark:border-slate-700 text-xs font-mono font-bold bg-white dark:bg-slate-800">
          <button onclick="runCertificateVerification()" class="px-4 py-2 rounded-lg bg-teal-700 hover:bg-teal-600 text-white font-bold text-xs transition">فحص</button>
        </div>
      </div>
      <div id="verify-result-box" class="hidden p-3 rounded-xl bg-emerald-50 dark:bg-emerald-950/40 border border-emerald-300 dark:border-emerald-800 text-xs space-y-1">
        <div class="font-bold text-emerald-800 dark:text-emerald-300 flex items-center gap-1">
          <span>✅</span> <span>شهادة ترخيص رسمية معتمدة وسارية</span>
        </div>
        <div id="verify-details-text" class="text-slate-600 dark:text-slate-300 text-[11px]">
          المبنى الحكومي النموذجي | امتثال 96% (الدرجة البلاتينية) | مسجل رسمياً في سجلات جمهورية العراق.
        </div>
      </div>
    </div>
  </div>

  <!-- ⌨️ KEYBOARD SHORTCUTS HELPER MODAL (TRACK 5) -->
  <div id="hotkeys-modal" class="no-print fixed inset-0 bg-slate-950/80 backdrop-blur-md z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-white dark:bg-slate-900 rounded-2xl max-w-md w-full border border-slate-300 dark:border-slate-700 p-6 space-y-4 shadow-2xl relative text-slate-800 dark:text-slate-100">
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

for fpath in FILES:
    print(f"Processing: {fpath}")
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject modals if not present
    if 'id="cert-verifier-modal"' not in content:
        content = content.replace('</body>', MODALS_HTML + "\n</body>", 1)
        print("  ✓ Injected missing modals into HTML")

    # Wire up openOfficialCertFromAudit to call openCertificateModal
    cert_connector_code = """
    function openOfficialCertFromAudit(source) {
      if (typeof openCertificateModal === 'function') {
        openCertificateModal();
      } else {
        const cert = document.getElementById('cert-modal');
        if (cert) cert.classList.remove('hidden');
      }
    }
    function closeCertModal() {
      if (typeof closeCertificateModal === 'function') {
        closeCertificateModal();
      } else {
        const cert = document.getElementById('cert-modal');
        if (cert) cert.classList.add('hidden');
      }
    }
"""
    if 'function openOfficialCertFromAudit' in content:
        # replace existing stub with full connector
        content = re.sub(r'function openOfficialCertFromAudit\(source\) \{[\s\S]*?\}', cert_connector_code.strip(), content)
        print("  ✓ Wired openOfficialCertFromAudit to openCertificateModal")

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Completed: {fpath}\n")

print("All modals and functions cleanly integrated!")
