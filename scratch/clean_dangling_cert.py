#!/usr/bin/env python3
import sys

FILES = [
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html',
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html'
]

dangling_target = """    function openOfficialCertFromAudit(source) {
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
    }"""

clean_replacement = """    function openOfficialCertFromAudit(source) {
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

    function copyCertShareLink() {
      const qrIdElem = document.getElementById('cert-qr-id');
      const serial = qrIdElem ? qrIdElem.innerText : 'IRQ-ACC-2026';
      navigator.clipboard.writeText(`https://drahmedlouay.github.io/iraqi-accessibility-platform/?verify=${serial}`);
      alert("تم نسخ رابط التحقق من الشهادة بنجاح!");
    }"""

for fpath in FILES:
    print(f"Cleaning: {fpath}")
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if dangling_target in content:
        content = content.replace(dangling_target, clean_replacement)
        print("  ✓ Removed dangling snippet successfully")
    else:
        print("  ⚠️ Target exact match not found, checking with regex...")
        # fallback search
        start_idx = content.find("function openOfficialCertFromAudit(source) {")
        end_idx = content.find("function openCertVerifierModal()", start_idx)
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + clean_replacement + "\n\n    " + content[end_idx:]
            print("  ✓ Cleaned up section via range replacement")
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Saved {fpath}")

print("Clean up finished!")
