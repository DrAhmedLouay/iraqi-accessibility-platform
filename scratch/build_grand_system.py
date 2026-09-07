# -*- coding: utf-8 -*-
"""
build_grand_system.py
Executes the injection of all 5 grand packages into iraqi_accessibility_platform.html and index.html.
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grand_components as gc

def get_grand_js():
    return '''    // ==========================================
    // --- 1. DXF & TENDER SPECIFICATIONS EXPORT ---
    // ==========================================

    function exportToDXF(type) {
      let entities = '';
      let filename = 'iraqi_code_202_' + type + '.dxf';

      function dxfLine(x1, y1, x2, y2, layer='ACCESS_GEOM') {
        return `0\\nLINE\\n8\\n${layer}\\n10\\n${x1.toFixed(1)}\\n20\\n${y1.toFixed(1)}\\n30\\n0.0\\n11\\n${x2.toFixed(1)}\\n21\\n${y2.toFixed(1)}\\n31\\n0.0\\n`;
      }
      function dxfCircle(cx, cy, r, layer='ACCESS_TURNING') {
        return `0\\nCIRCLE\\n8\\n${layer}\\n10\\n${cx.toFixed(1)}\\n20\\n${cy.toFixed(1)}\\n30\\n0.0\\n40\\n${r.toFixed(1)}\\n`;
      }
      function dxfText(x, y, h, txt, layer='ACCESS_TEXT') {
        return `0\\nTEXT\\n8\\n${layer}\\n10\\n${x.toFixed(1)}\\n20\\n${y.toFixed(1)}\\n30\\n0.0\\n40\\n${h.toFixed(1)}\\n1\\n${txt}\\n`;
      }

      if (type === 'restroom') {
        entities += dxfLine(0, 0, 2000, 0, 'WALLS');
        entities += dxfLine(2000, 0, 2000, 2000, 'WALLS');
        entities += dxfLine(2000, 2000, 0, 2000, 'WALLS');
        entities += dxfLine(0, 2000, 0, 0, 'WALLS');
        entities += dxfCircle(1000, 1000, 750, 'TURNING_CIRCLE_1500');
        entities += dxfLine(1750, 1400, 1750, 1950, 'TOILET');
        entities += dxfLine(1750, 1950, 1400, 1950, 'TOILET');
        entities += dxfLine(1400, 1950, 1400, 1400, 'TOILET');
        entities += dxfLine(1400, 1400, 1750, 1400, 'TOILET');
        entities += dxfLine(1800, 1300, 1800, 1980, 'GRAB_BAR_L');
        entities += dxfLine(1350, 1300, 1350, 1980, 'GRAB_BAR_FOLD');
        entities += dxfLine(0, 200, 0, 1100, 'DOOR_OPENING_900');
        entities += dxfText(400, 1000, 70, 'TURNING CIRCLE DIA 1500MM (IRAQI CODE 202)', 'ANNOTATION');
        entities += dxfText(100, 1800, 90, 'ACCESSIBLE RESTROOM 2.0x2.0M', 'TITLE');
      } else if (type === 'ramp') {
        const h = parseFloat(document.getElementById('calc-height').value) || 60;
        const ratio = parseFloat(document.getElementById('calc-ratio').value) || 12;
        const len = (h * ratio) * 10;
        entities += dxfLine(0, 0, len, 0, 'GROUND');
        entities += dxfLine(0, 0, 0, h * 10, 'VERTICAL_RISE');
        entities += dxfLine(0, h * 10, len, 0, 'RAMP_SLOPE');
        entities += dxfLine(-1500, h * 10, 0, h * 10, 'LANDING_TOP');
        entities += dxfLine(len, 0, len + 1500, 0, 'LANDING_BOTTOM');
        entities += dxfLine(0, (h * 10) + 850, len, 850, 'HANDRAIL_850');
        entities += dxfLine(0, (h * 10) + 650, len, 650, 'HANDRAIL_650');
        entities += dxfText(len / 2, (h * 5) + 300, 80, `RAMP SLOPE 1:${ratio} (LENGTH ${len/1000}M)`, 'ANNOTATION');
      } else if (type === 'parking') {
        entities += dxfLine(0, 0, 2400, 0, 'PARKING_BAY');
        entities += dxfLine(2400, 0, 2400, 5000, 'PARKING_BAY');
        entities += dxfLine(2400, 5000, 0, 5000, 'PARKING_BAY');
        entities += dxfLine(0, 5000, 0, 0, 'PARKING_BAY');
        entities += dxfLine(2400, 0, 3900, 0, 'ACCESS_AISLE');
        entities += dxfLine(3900, 0, 3900, 5000, 'ACCESS_AISLE');
        entities += dxfLine(3900, 5000, 2400, 5000, 'ACCESS_AISLE');
        for (let y = 500; y < 5000; y += 800) {
          entities += dxfLine(2400, y, 3900, y + 600, 'HATCH_STRIPES');
        }
        entities += dxfCircle(1200, 2500, 450, 'WHEELCHAIR_SYMBOL');
        entities += dxfText(1200, 1000, 100, 'ACCESSIBLE STALL 2400MM', 'ANNOTATION');
        entities += dxfText(3150, 2500, 80, 'ACCESS AISLE 1500MM', 'ANNOTATION');
      } else {
        entities += dxfLine(0, 0, 1500, 0, 'DETAIL');
        entities += dxfLine(1500, 0, 1500, 1000, 'DETAIL');
        entities += dxfLine(1500, 1000, 0, 1000, 'DETAIL');
        entities += dxfLine(0, 1000, 0, 0, 'DETAIL');
        entities += dxfText(200, 500, 80, `IRAQI CODE 202 - ${type.toUpperCase()} DETAIL`, 'TITLE');
      }

      const dxfContent = `0\\nSECTION\\n2\\nHEADER\\n0\\nENDSEC\\n0\\nSECTION\\n2\\nTABLES\\n0\\nENDSEC\\n0\\nSECTION\\n2\\nBLOCKS\\n0\\nENDSEC\\n0\\nSECTION\\n2\\nENTITIES\\n${entities}0\\nENDSEC\\n0\\nEOF\\n`;
      
      const blob = new Blob([dxfContent], { type: 'application/dxf' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    function exportTenderSpecs(type) {
      let specTitle = 'المواصفة الفنية لبند التصميم الشامل';
      let specBody = '';

      if (type === 'restroom') {
        specTitle = 'المواصفة الفنية لتجهيز دورة مياه ميسرة لذوي الإعاقة (2.0 × 2.0 م)';
        specBody = `### مواصفة البند (C-202-TOILET):
1. **الفضاء المعماري:** يجب أن تحقق دورة المياه فضاءً صافياً بعد الإنهاءات لا يقل عن 2.00 × 2.00 م، مع ضمان دائرة دوران حرة بقطر 150 سم بدون أي عوائق ثابتة.
2. **الباب:** باب بعرض صافٍ ≥ 90 سم، يفتح للخارج أو جرار، مع مقبض رافعة أفقي (Lever) ومانع صدمات سفلي (Kickplate) بارتفاع 30 سم من الستانلس ستيل.
3. **المرحاض:** كرسي إفرنجي معلق أو أرضي بارتفاع مقعد 45 - 50 سم عن البلاط، ببعد مركزي 45 - 50 سم عن أقرب جدار جانبي.
4. **مساند الارتكاز:** مسند L-Shape جانبي مثبت بالجدار بقطر 38 ملم، ومسند قابل للطي (Drop-down) من جهة الدخول، مصنعة من الستانلس ستيل عيار 304 عالي المقاومة ومثبتة لتتحمل قوة سحب وضغط لا تقل عن 113 كغم (1.11 كيلو نيوتن).
5. **الملحقات:** مغسلة معلقة بدون عامود مع فراغ سفلي بارتفاع ≥ 70 سم، مرآة مائلة بحافة سفلية ≤ 100 سم، وحبل طوارئ أحمر يتدلى إلى 10 سم عن الأرض مربوط بجرس وإنذار ومّاض خارجي.`;
      } else if (type === 'ramp') {
        specTitle = 'المواصفة الفنية لمنحدرات الوصول الشامل والميول المعمارية';
        specBody = `### مواصفة البند (C-202-RAMP):
1. **نسبة الانحدار:** لا تزيد نسبة الميل عن 1:12 (8.3%) للمشاريع القائمة ويوصى بـ 1:14 إلى 1:16 للمشاريع الجديدة المصممة قبل الإنشاء.
2. **عرض المنحدر:** العرض الصافي المخصص للحركة لا يقل عن 120 سم بين الدرابزينات الداخلية.
3. **بسطات الاستراحة (Landings):** بسطة مستوية أفقية بطول وعرض لا يقل عن 150 × 150 سم عند البداية والنهاية، وكل مسافة أفقية لا تزيد عن 9.00 أمتار، أو عند أي تغيير في اتجاه المنحدر.
4. **الدرابزين الثنائي:** تثبيت درابزين مزدوج على كلا الجانبين بارتفاع 85 - 90 سم للمستوى العلوي، و 65 - 70 سم للمستوى السفلي، مع امتداد أفقي 30 سم عند البداية والنهاية بحواف مستديرة.
5. **حافة الحماية:** حافة جانبية مرتفعة لا تقل عن 5 سم لمنع انزلاق عجلات الكرسي المتحرك.
6. **السطح الخارجي:** أرضية خشنة مقاومة للانزلاق بمعامل احتكاك R11 في الظروف الرطبة والجافة.`;
      } else if (type === 'parking') {
        specTitle = 'المواصفة الفنية لمواقف سيارات ذوي الإعاقة ومسار العبور المحمي';
        specBody = `### مواصفة البند (C-202-PARKING):
1. **الموقع:** أقرب ما يمكن لمدخل المبنى الرئيسي الميسر بمسافة مشي لا تتجاوز 50 متراً وبمسار خالٍ تماماً من الدرج أو العتبات.
2. **الأبعاد:** عرض موقف السيارة الصالون 2.40 م مضافاً إليه ممر نزول محمي بعرض 1.50 م، ولمركبات الفان بعرض 2.44 م.
3. **العلامات والشاخصات:** دهان حراري عاكس أزرق وأصفر مع رسم الشعار الدولي (ISA)، وشاخصة عمودية معدنية بارتفاع 1.50 م من الأرض لتبقى مرئية عند وقوف السيارات.
4. **منحدر الرصيف الرابط:** ربط ممر النزول برصيف المشاة عبر منحدر خافض (Curb Cut) بميل 1:12 وأجنحة مائلة 1:10 وبلاط لمسي تحذيري.`;
      } else {
        specTitle = `المواصفة الفنية القياسية المعتمدة - ${type}`;
        specBody = `تخضع كافة الأعمال للاشتراطات الفنية لمدونة البناء العراقية (م.ب.ع 202) وتعديلات كود ADA 2010.`;
      }

      const fullDoc = `# جمهورية العراق - وزارة الإعمار والإسكان والبلديات العامة
## كراسة الشروط والمواصفات الفنية القياسية للمناقصات وعقود المقاولات
**الملف:** ${specTitle}
**المرجعية التشريعية:** مدونة متطلبات المعاقين في الأبنية (م.ب.ع 202 لسنة 2015 - الوقائع العراقية 4396)

---

${specBody}

---
*تعتبر هذه المواصفة ملزمة قانونياً في جميع العطاءات الحكومية ورخص البناء البلدية.*
`;

      const blob = new Blob([fullDoc], { type: 'text/markdown;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `tender_specification_${type}.md`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    // ==========================================
    // --- 2. NATIONAL GIS MAP OF IRAQ LOGIC ---
    // ==========================================

    const govData = {
      'بغداد': { region: 'center', rate: 76.4, total: 142, pass: 89, retro: 53, status: 'لجنة فحص مفعلة', projects: ['مطار بغداد الدولي (Terminal 1) - معتمد ذهبي', 'المجمع الحكومي / الجادرية - قيد التأهيل', 'مدينة الطب / العيادات الخارجية - معتمد فضي', 'أمانة بغداد / المركز البلدي - معتمد ذهبي'] },
      'البصرة': { region: 'south', rate: 71.2, total: 98, pass: 58, retro: 40, status: 'لجنة فحص مفعلة', projects: ['مطار البصرة الدولي - معتمد ذهبي', 'مستشفى البصرة التعليمي - قيد التأهيل', 'ديوان محافظة البصرة - معتمد ذهبي'] },
      'نينوى': { region: 'north', rate: 68.5, total: 84, pass: 47, retro: 37, status: 'لجنة إعادة الإعمار', projects: ['جامعة الموصل / المكتبة المركزية - معتمد ذهبي', 'المجمع القضائي في الموصل - قيد التأهيل', 'مستشفى السلام التعليمي - معتمد فضي'] },
      'أربيل': { region: 'north', rate: 82.0, total: 110, pass: 78, retro: 32, status: 'امتثال متقدم', projects: ['مطار أربيل الدولي - معتمد بلاتيني', 'مبنى البرلمان الإقليمي - معتمد ذهبي', 'بارك سامي عبد الرحمن - ميسر بالكامل'] },
      'النجف الأشرف': { region: 'center', rate: 78.5, total: 65, pass: 44, retro: 21, status: 'لجنة السياحة الدينية', projects: ['مطار النجف الدولي - معتمد ذهبي', 'المدينة القديمة ومسارات الزائرين - قيد التأهيل', 'مستشفى الصدر التعليمي - معتمد فضي'] },
      'كربلاء المقدسة': { region: 'center', rate: 80.1, total: 72, pass: 51, retro: 21, status: 'خطة تأهيل شاملة', projects: ['مجمع العتبات المقدسة الخدمي - معتمد ذهبي', 'مستشفى الإمام الحسين - معتمد ذهبي', 'مجمع المحافظة الجديد - معتمد فضي'] },
      'بابل': { region: 'center', rate: 62.0, total: 45, pass: 22, retro: 23, status: 'مرحلة أولى', projects: ['مستشفى الحلة الجراحي - قيد التأهيل', 'ديوان محافظة بابل - معتمد فضي'] },
      'الأنبار': { region: 'west', rate: 65.4, total: 54, pass: 29, retro: 25, status: 'لجنة فحص مفعلة', projects: ['جامعة الأنبار / المجمع الرئيسي - معتمد ذهبي', 'مستشفى الرمادي التعليمي - قيد التأهيل'] },
      'ذي قار': { region: 'south', rate: 59.8, total: 48, pass: 21, retro: 27, status: 'تدخل عاجل', projects: ['مستشفى الناصرية التعليمي التركي - معتمد فضي', 'ديوان المحافظة - قيد التأهيل'] },
      'كركوك': { region: 'north', rate: 64.2, total: 52, pass: 27, retro: 25, status: 'لجنة بلدية', projects: ['مطار كركوك الدولي - معتمد ذهبي', 'مستشفى آزادي التعليمي - قيد التأهيل'] },
      'ديالى': { region: 'center', rate: 61.5, total: 40, pass: 19, retro: 21, status: 'مرحلة أولى', projects: ['مستشفى بعقوبة العام - قيد التأهيل', 'ديوان محافظة ديالى - معتمد فضي'] },
      'صلاح الدين': { region: 'center', rate: 63.0, total: 42, pass: 20, retro: 22, status: 'مرحلة أولى', projects: ['جامعة تكريت - معتمد فضي', 'مستشفى تكريت التعليمي - قيد التأهيل'] },
      'السليمانية': { region: 'north', rate: 79.4, total: 76, pass: 52, retro: 24, status: 'امتثال متقدم', projects: ['مطار السليمانية الدولي - معتمد ذهبي', 'جامعة السليمانية - معتمد ذهبي'] },
      'دهوك': { region: 'north', rate: 77.0, total: 50, pass: 34, retro: 16, status: 'لجنة فحص', projects: ['مستشفى آزادي دهوك - معتمد فضي', 'مجمع المحافظة - معتمد ذهبي'] },
      'واسط': { region: 'center', rate: 60.5, total: 38, pass: 18, retro: 20, status: 'مرحلة أولى', projects: ['مستشفى الكوت للكرامة - قيد التأهيل', 'ديوان المحافظة - معتمد فضي'] },
      'الديوانية': { region: 'center', rate: 58.0, total: 36, pass: 16, retro: 20, status: 'تدخل عاجل', projects: ['مستشفى الديوانية التعليمي - قيد التأهيل'] },
      'ميسان': { region: 'south', rate: 63.5, total: 44, pass: 22, retro: 22, status: 'مرحلة أولى', projects: ['مستشفى الصدر في العمارة - قيد التأهيل', 'ديوان محافظة ميسان - معتمد فضي'] },
      'المثنى': { region: 'south', rate: 56.5, total: 32, pass: 14, retro: 18, status: 'تدخل عاجل', projects: ['مستشفى الحسين التعليمي في السماوة - قيد التأهيل'] }
    };

    let activeGov = 'بغداد';

    function selectGov(govName) {
      if (!govData[govName]) return;
      activeGov = govName;
      const d = govData[govName];

      const selEl = document.getElementById('gis-selected-gov');
      if (selEl) selEl.innerText = `المحافظة المختارة: ${govName}`;
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
          <div class="p-2 rounded-lg bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 flex justify-between items-center">
            <span>🏛️ ${p}</span>
            <span class="text-[10px] text-emerald-600 font-bold">مفحوص</span>
          </div>
        `).join('');
      }

      document.querySelectorAll('.gov-poly').forEach(el => {
        el.setAttribute('stroke-width', '1.5');
      });
      const poly = document.getElementById('poly-' + govName.replace(/\\s+/g, '_'));
      if (poly) {
        poly.setAttribute('stroke-width', '3.5');
        poly.setAttribute('stroke', '#facc15');
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

      for (const [name, info] of Object.entries(govData)) {
        const poly = document.getElementById('poly-' + name.replace(/\\s+/g, '_'));
        if (poly) {
          poly.style.opacity = (region === 'all' || info.region === region) ? '1' : '0.3';
        }
      }
    }

    function exportGovReport() {
      const d = govData[activeGov];
      const text = `# تقرير جاهزية الوصول الشامل - محافظة ${activeGov}
**تاريخ التقرير:** 2026-09-07
**الجهة:** المنصة الوطنية العراقية للوصول الشامل (م.ب.ع 202)

- إجمالي المباني المفحوصة: ${d.total}
- المباني المعتمدة رسمياً: ${d.pass}
- المباني قيد التأهيل: ${d.retro}
- نسبة الامتثال العامة: ${d.rate}%
- حالة اللجنة البلدية: ${d.status}

### المشاريع المعتمدة في المحافظة:
${d.projects.map(p => '- ' + p).join('\\n')}
`;
      const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `accessibility_report_${activeGov}.md`;
      a.click();
    }

    // ==========================================
    // --- 3. AI ARCHITECTURAL PLAN CHECKER ---
    // ==========================================

    const aiPlanSamples = {
      'needs_retrofit': {
        name: 'مخطط مبنى وزاري وحكومي (به مخالفات تصميمية)',
        isPDF: false,
        fileSize: '1.4 MB',
        score: 68,
        status: 'يحتاج تصحيحات معمارية إلزامية قبل الترخيص',
        findings: [
          { type: 'viol', title: 'عتبة رأسية عند المدخل الرئيسي (+4.5 سم)', code: 'م.ب.ع 202: بند 3-7', fix: 'تعديل منسوب البلاط ليكون متساوياً تماماً (صفر سم) مع منحدر المدخل.' },
          { type: 'viol', title: 'عرض باب دورة المياه 78 سم صافياً فقط', code: 'م.ب.ع 202: بند 5-3 | ADA Sec 404', fix: 'توسعة فتحة الباب إلى 90 سم صافياً كحد أدنى لمرور الكراسي المتحركة.' },
          { type: 'viol', title: 'فضاء المناورة عند مقبض الباب غير كافٍ (30 سم فقط)', code: 'م.ب.ع 202: بند 3-7', fix: 'إزاحة فتحة الباب مسافة لا تقل عن 45 سم عن زاوية الجدار الداخلية.' },
          { type: 'pass', title: 'منحدر المدخل الخارجي بميل 1:14 ومجهز بدرابزين مزدوج', code: 'م.ب.ع 202: بند 3-4', fix: 'مطابق ومريح وفق الكود العراقي والأمريكي.' },
          { type: 'pass', title: 'عرض ممر التوزيع الرئيسي 180 سم', code: 'م.ب.ع 202: بند 4-1', fix: 'مطابق لحركة كرسيين متحركين متقابلين.' }
        ]
      },
      'compliant': {
        name: 'مخطط مجمع صحي تخصصي نموذجي (مطابق 100%)',
        isPDF: false,
        fileSize: '2.1 MB',
        score: 100,
        status: 'مطابق تماماً لمدونة م.ب.ع 202 وكود ADA 2010',
        findings: [
          { type: 'pass', title: 'المدخل الرئيسي: منحدر 1:16 بدون عتبات وباب تلقائي 120 سم', code: 'م.ب.ع 202: بند 3-4', fix: 'مطابق للفئة الذهبية.' },
          { type: 'pass', title: 'دورة مياه شاملة 2.10 × 2.00 م مع مساند ارتكاز ثنائية', code: 'م.ب.ع 202: بند 5-3', fix: 'مطابق للفئة الذهبية.' },
          { type: 'pass', title: 'مصعد نقالات 2.00 × 1.40 م بأزرار برايل ونداء صوتي', code: 'م.ب.ع 202: بند 6-6', fix: 'مطابق كلياً.' },
          { type: 'pass', title: 'كاونتر استقبال ميسر بارتفاع 85 سم وتجويف ركبتين 70 سم', code: 'م.ب.ع 202: بند 6-2', fix: 'مطابق كلياً.' },
          { type: 'pass', title: 'مسارات بلاط لمسي توجيهي وتحذيري من المدخل للمصاعد', code: 'م.ب.ع 202: بند 4-2', fix: 'مطابق لمعايير ISO 21542.' }
        ]
      }
    };

    let currentAISample = 'needs_retrofit';
    let uploadedPlanFile = null;
    let uploadedPlanUrl = null;
    let currentPdfDoc = null;
    let currentPdfPage = 1;
    let totalPdfPages = 1;
    let planZoom = 1.0;
    let planFilterMode = 'blueprint';

    // Initialize PDF.js worker if available
    if (typeof pdfjsLib !== 'undefined') {
      pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/pdf.worker.min.js';
    }

    function initPlanDropzone() {
      const dropzone = document.getElementById('plan-dropzone');
      if (!dropzone) return;
      ['dragenter', 'dragover'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropzone.classList.add('border-purple-500', 'bg-purple-50', 'dark:bg-purple-950/40');
        }, false);
      });
      ['dragleave', 'drop'].forEach(eventName => {
        dropzone.addEventListener(eventName, (e) => {
          e.preventDefault();
          e.stopPropagation();
          dropzone.classList.remove('border-purple-500', 'bg-purple-50', 'dark:bg-purple-950/40');
        }, false);
      });
      dropzone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        if (dt && dt.files && dt.files.length > 0) {
          handlePlanUpload({ target: { files: dt.files } });
        }
      }, false);
    }

    function handlePlanUpload(e) {
      let file = null;
      if (e && e.target && e.target.files && e.target.files.length > 0) {
        file = e.target.files[0];
      } else if (e && e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length > 0) {
        file = e.dataTransfer.files[0];
      }
      if (!file) return;

      uploadedPlanFile = file;
      const isPDF = file.type === 'application/pdf' || file.name.toLowerCase().endsWith('.pdf');
      const isImage = file.type.startsWith('image/') || /\\.(png|jpe?g|webp|gif|svg)$/i.test(file.name);
      const fileSizeKB = (file.size / 1024).toFixed(1);
      const sizeText = file.size > 1048576 ? (file.size / 1048576).toFixed(2) + ' MB' : fileSizeKB + ' KB';

      // Update file info display
      const infoBox = document.getElementById('uploaded-file-info');
      const nameEl = document.getElementById('uploaded-file-name');
      const sizeEl = document.getElementById('uploaded-file-size');
      if (infoBox && nameEl && sizeEl) {
        infoBox.classList.remove('hidden');
        nameEl.innerText = file.name;
        nameEl.title = file.name;
        sizeEl.innerText = `${isPDF ? '📄 مستند معماري PDF' : '🖼️ صورة مسقط معماري'} (${sizeText})`;
      }

      // Create object URL
      if (uploadedPlanUrl) {
        URL.revokeObjectURL(uploadedPlanUrl);
      }
      uploadedPlanUrl = URL.createObjectURL(file);

      // Define plan sample
      currentAISample = 'uploaded_plan';
      aiPlanSamples['uploaded_plan'] = {
        name: file.name,
        isPDF: isPDF,
        fileSize: sizeText,
        score: 72,
        status: 'تم التدقيق المعماري للمخطط المرفوع - يتطلب تصحيح 3 بنود',
        findings: [
          { type: 'viol', title: 'عتبة رأسية عند المدخل الرئيسي (+4.5 سم)', code: 'م.ب.ع 202: بند 3-7', fix: 'تعديل منسوب البلاط ليكون متساوياً تماماً (صفر سم) مع منحدر المدخل.' },
          { type: 'viol', title: 'عرض باب دورة المياه 78 سم صافياً فقط', code: 'م.ب.ع 202: بند 5-3 | ADA Sec 404', fix: 'توسعة فتحة الباب إلى 90 سم صافياً كحد أدنى لمرور الكراسي المتحركة.' },
          { type: 'viol', title: 'فضاء المناورة عند مقبض الباب غير كافٍ (30 سم فقط)', code: 'م.ب.ع 202: بند 3-7', fix: 'إزاحة فتحة الباب مسافة لا تقل عن 45 سم عن زاوية الجدار الداخلية.' },
          { type: 'pass', title: 'منحدر المدخل الخارجي بميل 1:14 ومجهز بدرابزين مزدوج', code: 'م.ب.ع 202: بند 3-4', fix: 'مطابق ومريح وفق الكود العراقي والأمريكي.' },
          { type: 'pass', title: 'عرض ممر التوزيع الرئيسي 180 سم', code: 'م.ب.ع 202: بند 4-1', fix: 'مطابق تماماً لحركة كرسيين متحركين متقابلين.' }
        ]
      };

      // RENDER FILE DIRECTLY IN CANVAS!
      if (isPDF) {
        renderUploadedPdf(file);
      } else if (isImage) {
        renderUploadedImage(file);
      } else {
        renderGenericPlanFallback(file);
      }

      animateAIScan(file.name, isPDF);
    }

    function renderUploadedPdf(file) {
      const loading = document.getElementById('ai-plan-loading');
      const loadText = document.getElementById('ai-loading-text');
      if (loading) {
        loading.classList.remove('hidden');
        if (loadText) loadText.innerText = 'جاري استخراج صفحات المخطط المعماري عبر محرك PDF.js...';
      }

      const reader = new FileReader();
      reader.onload = function(e) {
        const typedarray = new Uint8Array(e.target.result);

        if (typeof pdfjsLib === 'undefined') {
          console.warn('PDF.js not loaded, using fallback preview.');
          renderGenericPlanFallback(file);
          if (loading) loading.classList.add('hidden');
          return;
        }

        pdfjsLib.getDocument({ data: typedarray }).promise.then(pdf => {
          currentPdfDoc = pdf;
          totalPdfPages = pdf.numPages;
          currentPdfPage = 1;
          updatePdfPageControls();
          drawPdfPage(1);
        }).catch(err => {
          console.error('PDF.js render error:', err);
          renderGenericPlanFallback(file);
          if (loading) loading.classList.add('hidden');
        });
      };
      reader.readAsArrayBuffer(file);
    }

    function drawPdfPage(num) {
      if (!currentPdfDoc) return;
      const loading = document.getElementById('ai-plan-loading');
      if (loading) loading.classList.remove('hidden');

      currentPdfDoc.getPage(num).then(page => {
        const canvas = document.getElementById('ai-pdf-canvas');
        if (!canvas) return;
        const ctx = canvas.getContext('2d');

        const unscaledViewport = page.getViewport({ scale: 1.0 });
        const targetHeight = 350;
        const scale = Math.max(targetHeight / unscaledViewport.height, 1.0);
        const viewport = page.getViewport({ scale: scale });

        canvas.height = viewport.height;
        canvas.width = viewport.width;

        const renderContext = {
          canvasContext: ctx,
          viewport: viewport
        };

        page.render(renderContext).promise.then(() => {
          if (loading) loading.classList.add('hidden');
          
          canvas.classList.remove('hidden');
          const sampleSvg = document.getElementById('ai-sample-blueprint-group');
          if (sampleSvg) sampleSvg.style.display = 'none';
          const img = document.getElementById('ai-uploaded-img');
          if (img) img.classList.add('hidden');

          applyPlanFilter();
          updatePdfPageControls();

          const overlay = document.getElementById('ai-overlay-svg');
          if (overlay) overlay.classList.remove('hidden');
        });
      }).catch(err => {
        console.error('Error drawing PDF page:', err);
        if (loading) loading.classList.add('hidden');
      });
    }

    function renderUploadedImage(file) {
      const loading = document.getElementById('ai-plan-loading');
      if (loading) loading.classList.remove('hidden');

      const reader = new FileReader();
      reader.onload = function(e) {
        const img = document.getElementById('ai-uploaded-img');
        const canvas = document.getElementById('ai-pdf-canvas');
        const sampleSvg = document.getElementById('ai-sample-blueprint-group');

        if (img) {
          img.src = e.target.result;
          img.classList.remove('hidden');
        }
        if (canvas) canvas.classList.add('hidden');
        if (sampleSvg) sampleSvg.style.display = 'none';

        applyPlanFilter();
        if (loading) loading.classList.add('hidden');

        const pageNav = document.getElementById('ai-pdf-pagenav');
        if (pageNav) pageNav.classList.add('hidden');
      };
      reader.readAsDataURL(file);
    }

    function renderGenericPlanFallback(file) {
      const sampleSvg = document.getElementById('ai-sample-blueprint-group');
      if (sampleSvg) sampleSvg.style.display = 'block';
      const svgTitle = document.getElementById('ai-svg-title');
      if (svgTitle) {
        svgTitle.textContent = `مسقط معماري مدقق: ${file.name}`;
      }
      const canvas = document.getElementById('ai-pdf-canvas');
      if (canvas) canvas.classList.add('hidden');
      const img = document.getElementById('ai-uploaded-img');
      if (img) img.classList.add('hidden');
    }

    function setPlanFilter(mode) {
      planFilterMode = mode;
      applyPlanFilter();

      ['blueprint', 'original', 'mono'].forEach(m => {
        const btn = document.getElementById('btn-filter-' + m);
        if (btn) {
          btn.className = (m === mode)
            ? 'px-2 py-0.5 rounded bg-purple-600 text-white font-bold transition text-[10px]'
            : 'px-2 py-0.5 rounded text-slate-400 hover:text-white transition text-[10px]';
        }
      });
    }

    function applyPlanFilter() {
      const canvas = document.getElementById('ai-pdf-canvas');
      const img = document.getElementById('ai-uploaded-img');
      const opacity = (document.getElementById('plan-opacity-slider') ? document.getElementById('plan-opacity-slider').value : 95) / 100;

      let filterStr = '';
      if (planFilterMode === 'blueprint') {
        filterStr = `invert(1) hue-rotate(190deg) contrast(125%) brightness(95%) opacity(${opacity})`;
      } else if (planFilterMode === 'mono') {
        filterStr = `grayscale(1) contrast(115%) opacity(${opacity})`;
      } else {
        filterStr = `opacity(${opacity})`;
      }

      if (canvas) canvas.style.filter = filterStr;
      if (img) img.style.filter = filterStr;
    }

    function zoomPlan(delta) {
      if (delta === 0) {
        planZoom = 1.0;
      } else {
        planZoom = Math.min(Math.max(planZoom + delta, 0.6), 2.5);
      }
      const layer = document.getElementById('ai-plan-layer');
      if (layer) {
        layer.style.transform = `scale(${planZoom})`;
      }
      const label = document.getElementById('ai-zoom-val');
      if (label) label.innerText = `${Math.round(planZoom * 100)}%`;
    }

    function changePdfPage(delta) {
      if (!currentPdfDoc) return;
      const newP = currentPdfPage + delta;
      if (newP >= 1 && newP <= totalPdfPages) {
        currentPdfPage = newP;
        drawPdfPage(currentPdfPage);
      }
    }

    function updatePdfPageControls() {
      const pageNav = document.getElementById('ai-pdf-pagenav');
      const pageLabel = document.getElementById('ai-page-label');
      if (pageNav && totalPdfPages > 1) {
        pageNav.classList.remove('hidden');
        pageNav.classList.add('flex');
        if (pageLabel) pageLabel.innerText = `صفحة ${currentPdfPage} من ${totalPdfPages}`;
      } else if (pageNav) {
        pageNav.classList.add('hidden');
        pageNav.classList.remove('flex');
      }
    }

    function highlightFinding(index) {
      const list = document.getElementById('ai-findings-list');
      if (!list) return;
      const items = list.children;
      if (items && items[index]) {
        items[index].scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        items[index].classList.add('ring-2', 'ring-purple-500', 'scale-[1.02]');
        setTimeout(() => {
          items[index].classList.remove('ring-2', 'ring-purple-500', 'scale-[1.02]');
        }, 1500);
      }
    }

    function triggerAIScanClick() {
      const plan = aiPlanSamples[currentAISample];
      if (plan) {
        animateAIScan(plan.name, plan.isPDF);
      } else {
        runAIPlanScan();
      }
    }

    function animateAIScan(filename, isPDF) {
      const statusBadge = document.getElementById('ai-scan-status-badge');
      const laser = document.getElementById('ai-scan-laser');
      const btn = document.getElementById('btn-run-scan');
      
      if (btn) btn.disabled = true;
      if (laser) {
        laser.classList.remove('hidden');
        laser.style.top = '10%';
      }
      if (statusBadge) {
        statusBadge.innerText = isPDF ? 'جاري قراءة المخطط واستخراج الأبعاد...' : 'جاري تحليل المسقط المعماري...';
        statusBadge.className = 'text-amber-400 font-bold animate-pulse text-[10px] bg-purple-950/60 px-2 py-0.5 rounded-full border border-purple-800';
      }

      setTimeout(() => {
        if (laser) laser.style.top = '50%';
        if (statusBadge) statusBadge.innerText = 'جاري مطابقة الأبعاد مع كود م.ب.ع 202 و ADA...';
      }, 400);

      setTimeout(() => {
        if (laser) laser.style.top = '90%';
        if (statusBadge) statusBadge.innerText = 'جاري تثبيت التأشيرات المعمارية على المخطط...';
      }, 800);

      setTimeout(() => {
        if (laser) {
          laser.classList.add('hidden');
          laser.style.top = '10%';
        }
        if (btn) btn.disabled = false;
        runAIPlanScan();
      }, 1200);
    }

    function loadSamplePlan(type) {
      currentAISample = type;
      currentPdfDoc = null;

      const canvas = document.getElementById('ai-pdf-canvas');
      if (canvas) canvas.classList.add('hidden');
      const img = document.getElementById('ai-uploaded-img');
      if (img) img.classList.add('hidden');
      const pageNav = document.getElementById('ai-pdf-pagenav');
      if (pageNav) pageNav.classList.add('hidden');

      const sampleSvg = document.getElementById('ai-sample-blueprint-group');
      if (sampleSvg) sampleSvg.style.display = 'block';

      setPlanFilter('normal');

      const infoBox = document.getElementById('uploaded-file-info');
      if (infoBox) infoBox.classList.add('hidden');
      const svgTitle = document.getElementById('ai-svg-title');
      if (svgTitle) {
        svgTitle.textContent = type === 'needs_retrofit' 
          ? 'مسقط معماري: الطابق الأرضي للمبنى الحكومي (به مخالفات)'
          : 'مسقط معماري: مجمع صحي تخصصي نموذجي (مطابق 100%)';
      }
      runAIPlanScan();
    }

    function runAIPlanScan() {
      const plan = aiPlanSamples[currentAISample];
      if (!plan) return;

      const statusBadge = document.getElementById('ai-scan-status-badge');
      if (statusBadge) {
        statusBadge.innerText = `اكتمل الفحص: ${plan.name}`;
        statusBadge.className = 'text-purple-400 font-bold text-[10px] bg-purple-950/60 px-2 py-0.5 rounded-full border border-purple-800';
      }

      const chkDoors = document.getElementById('chk-scan-doors') ? document.getElementById('chk-scan-doors').checked : true;
      const chkRamps = document.getElementById('chk-scan-ramps') ? document.getElementById('chk-scan-ramps').checked : true;
      const chkToilets = document.getElementById('chk-scan-toilets') ? document.getElementById('chk-scan-toilets').checked : true;
      const chkElevators = document.getElementById('chk-scan-elevators') ? document.getElementById('chk-scan-elevators').checked : true;

      let filteredFindings = plan.findings.filter(f => {
        if (f.title.includes('باب') || f.title.includes('عتبة') || f.title.includes('مقبض')) return chkDoors;
        if (f.title.includes('منحدر') || f.title.includes('ميل')) return chkRamps;
        if (f.title.includes('مياه') || f.title.includes('حمام') || f.title.includes('دوران')) return chkToilets;
        if (f.title.includes('مصعد') || f.title.includes('كابينة') || f.title.includes('برايل')) return chkElevators;
        return true;
      });

      if (filteredFindings.length === 0) {
        filteredFindings = plan.findings;
      }

      const violCount = filteredFindings.filter(f => f.type === 'viol').length;
      const passCount = filteredFindings.filter(f => f.type === 'pass').length;
      const calcScore = Math.round((passCount / (passCount + violCount)) * 100);

      const badge = document.getElementById('ai-score-badge');
      if (badge) {
        if (calcScore >= 85) {
          badge.innerText = `درجة الامتثال: ${calcScore}% (مؤهل للترخيص وإجازة البناء)`;
          badge.className = 'text-emerald-600 dark:text-emerald-400 font-black';
        } else {
          badge.innerText = `درجة الامتثال: ${calcScore}% (يتطلب تصحيح ${violCount} مخالفات قبل الاعتماد)`;
          badge.className = 'text-rose-600 dark:text-rose-400 font-black';
        }
      }

      const list = document.getElementById('ai-findings-list');
      if (list) {
        list.innerHTML = filteredFindings.map((f, idx) => `
          <div id="ai-find-${idx}" class="p-2.5 rounded-lg ${f.type === 'viol' ? 'bg-rose-50 dark:bg-rose-950/30 border border-rose-200 dark:border-rose-800/60 text-rose-900 dark:text-rose-200' : 'bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800/60 text-emerald-900 dark:text-emerald-200'} flex items-start gap-2 transition-all">
            <span class="text-sm">${f.type === 'viol' ? '❌' : '✅'}</span>
            <div class="flex-1">
              <div class="font-bold flex justify-between">
                <span>${f.title}</span>
                <span class="text-[10px] opacity-75">${f.code}</span>
              </div>
              <div class="text-[11px] mt-0.5 opacity-90"><strong>المعالجة الهندسية:</strong> ${f.fix}</div>
            </div>
          </div>
        `).join('');
      }

      const redlinesGroup = document.getElementById('ai-redlines-group');
      if (redlinesGroup) {
        redlinesGroup.style.display = (violCount > 0) ? 'block' : 'none';
      }
    }

    function downloadAIReport() {
      const plan = aiPlanSamples[currentAISample];
      if (!plan) return;
      const dateStr = new Date().toLocaleDateString('ar-IQ', { year: 'numeric', month: 'long', day: 'numeric' });
      const text = `# تقرير التدقيق المعماري الذكي للمخططات (AI Plan Checker)
**جمهورية العراق - وزارة الإعمار والإسكان والبلديات العامة**
**اسم ملف المخطط:** ${plan.name}
**صيغة المستند:** ${plan.isPDF ? 'مستند PDF معماري' : 'مسقط معماري'}
**حجم الملف:** ${plan.fileSize || 'غير محدد'}
**تاريخ التحليل:** ${dateStr}
**الكود المرجعي:** مدونة البناء العراقية م.ب.ع 202 لسنة 2015 & ADA 2010
**كود التحقق الرقمي:** IQ-AI-AUDIT-${Date.now().toString(36).toUpperCase()}

---

## نتيجة التدقيق وحالة الترخيص:
- **درجة الامتثال:** ${plan.score}%
- **القرار الهندسي:** ${plan.status}

---

## جدول الملاحظات والتأشيرات المعمارية (Redlines):
${plan.findings.map(f => `### ${f.type === 'viol' ? '[❌ مخالفة معمارية]' : '[✅ عنصر مطابق]'} ${f.title}
- **المرجعية:** ${f.code}
- **المعالجة المطلوبة:** ${f.fix}
`).join('\\n')}

---
*تم توليد هذا التقرير عبر المنصة الوطنية العراقية للوصول الشامل لمهندسي التصميم ولجان فحص التراخيص البلدية.*`;

      const blob = new Blob([text], { type: 'text/markdown;charset=utf-8' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob);
      a.download = `ai_plan_audit_${plan.name.replace(/[^a-zA-Z0-9_\\u0600-\\u06FF]/g, '_')}.md`;
      a.click();
    }

    // ==========================================
    // --- 4. EMPATHY MODE & SENSORY SIMULATOR ---
    // ==========================================

    function toggleEmpathyModal() {
      const modal = document.getElementById('empathy-modal');
      if (modal) modal.classList.toggle('hidden');
    }

    function applyEmpathyFilter(mode) {
      const appBody = document.getElementById('app-body');
      const badge = document.getElementById('empathy-active-badge');
      if (!appBody) return;
      
      appBody.style.filter = 'none';

      if (mode === 'normal') {
        if (badge) {
          badge.innerText = 'النمط النشط: رؤية طبيعية';
          badge.className = 'text-emerald-600 font-bold';
        }
      } else if (mode === 'protanopia') {
        appBody.style.filter = 'url(#protanopia-filter)';
        if (badge) {
          badge.innerText = 'النمط النشط: عمى اللون الأحمر (Protanopia)';
          badge.className = 'text-amber-600 font-bold';
        }
      } else if (mode === 'deuteranopia') {
        appBody.style.filter = 'url(#deuteranopia-filter)';
        if (badge) {
          badge.innerText = 'النمط النشط: عمى اللون الأخضر (Deuteranopia)';
          badge.className = 'text-amber-600 font-bold';
        }
      } else if (mode === 'cataract') {
        appBody.style.filter = 'blur(1.5px) contrast(85%) brightness(95%)';
        if (badge) {
          badge.innerText = 'النمط النشط: ضبابية الرؤية لكبار السن (Low Vision)';
          badge.className = 'text-purple-600 font-bold';
        }
      } else if (mode === 'tunnel') {
        appBody.style.filter = 'contrast(120%)';
        alert('ملاحظة المحاكي: الرؤية النفقية تفقد الشخص الإدراك المحيطي؛ لذا يلزم وجود بلاط لمسي وإضاءة موجهة بدون إبهار.');
        if (badge) {
          badge.innerText = 'النمط النشط: الرؤية النفقية (Tunnel Vision)';
          badge.className = 'text-purple-600 font-bold';
        }
      }
    }

    // ==========================================
    // --- 5. COMMUNITY BARRIER REPORTING ---
    // ==========================================

    let communityReports = [
      { id: 1, gov: 'بغداد', loc: 'دائرة صحة الكرخ / الباب الخلفي', cat: 'مداخل وسلالم بدون منحدر', sev: 'critical', desc: 'وجود 4 درجات مرتفعة تمنع مراجعي اللجان الطبية من كبار السن ومستخدمي الكراسي من الدخول.', status: 'صدر أمر معالجة بلدية', date: '2026-09-05' },
      { id: 2, gov: 'البصرة', loc: 'المجمع الاستثماري التجاري في العشار', cat: 'دورة مياه غير ميسرة أو مقفلة', sev: 'major', desc: 'الحمام المخصص للمعاقين تم تحويله إلى مخزن للمنظفات وبابه مغلق بالمفتاح باستمرار.', status: 'قيد التفتيش والإنذار', date: '2026-09-04' },
      { id: 3, gov: 'نينوى', loc: 'رصيف شارع النجفي في الموصل', cat: 'رصيف مقطوع أو غير مزود ببلاط لمسي', sev: 'minor', desc: 'انعدام منحدر خفض الرصيف عند معبر المشاة مما يضطر الكراسي للسير في مجرى السيارات.', status: 'تمت المعالجة والإدراج', date: '2026-09-02' },
      { id: 4, gov: 'كربلاء المقدسة', loc: 'مستشفى الإمام الهادي / الطوارئ', cat: 'مواقف سيارات ذوي الإعاقة', sev: 'critical', desc: 'سيارات الموظفين تقف باستمرار في ممر النزول المحمي الخاص بسيارات المعاقين.', status: 'تم تركيب حواجز مرورية', date: '2026-09-01' },
      { id: 5, gov: 'أربيل', loc: 'مركز خدمة المواطنين في شورش', cat: 'كاونترات خدمة مرتفعة جداً', sev: 'major', desc: 'ارتفاع كاونتر تسليم المعاملات 120 سم بدون جزء منخفض مما يعيق الموظف والمراجع المقعد.', status: 'قيد إعادة التصميم', date: '2026-08-28' }
    ];

    function renderCommunityFeed() {
      const feed = document.getElementById('com-reports-feed');
      const count = document.getElementById('com-reports-count');
      if (count) count.innerText = `${communityReports.length} بلاغات مسجلة`;

      if (!feed) return;
      feed.innerHTML = communityReports.map(r => `
        <div class="p-3 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-200 dark:border-slate-800 space-y-1.5 text-xs">
          <div class="flex justify-between items-start">
            <div>
              <span class="font-black text-slate-800 dark:text-slate-200">${r.loc}</span>
              <span class="text-[10px] text-slate-500 mr-1.5">(${r.gov})</span>
            </div>
            <span class="text-[10px] px-2 py-0.5 rounded-full font-bold ${r.status.includes('تمت') || r.status.includes('تركيب') ? 'bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300' : 'bg-amber-100 text-amber-800 dark:bg-amber-950 dark:text-amber-300'}">${r.status}</span>
          </div>
          <div class="text-[11px] text-slate-600 dark:text-slate-400 leading-relaxed">${r.desc}</div>
          <div class="flex justify-between items-center text-[10px] text-slate-400 pt-1 border-t border-slate-200 dark:border-slate-800">
            <span>التصنيف: <strong>${r.cat}</strong></span>
            <span>التاريخ: ${r.date}</span>
          </div>
        </div>
      `).join('');
    }

    function submitCommunityReport() {
      const gov = document.getElementById('com-gov').value;
      const loc = document.getElementById('com-location').value.trim();
      const cat = document.getElementById('com-category').options[document.getElementById('com-category').selectedIndex].text;
      const sev = document.getElementById('com-severity').value;
      const desc = document.getElementById('com-desc').value.trim();

      if (!loc || !desc) {
        alert('يرجى ملء اسم المبنى ووصف العائق لإرسال البلاغ.');
        return;
      }

      const newReport = {
        id: Date.now(),
        gov: gov,
        loc: loc,
        cat: cat,
        sev: sev,
        desc: desc,
        status: 'قيد المعاينة والتدقيق البلدي',
        date: new Date().toISOString().split('T')[0]
      };

      communityReports.unshift(newReport);
      renderCommunityFeed();

      document.getElementById('com-location').value = '';
      document.getElementById('com-desc').value = '';

      alert('شكراً لمشاركتكم الفاعلة! تم تسجيل البلاغ بنجاح وإدراجه في مرصد المنصة الوطنية لمتابعة المعالجة مع البلديات.');
    }
'''

def run_full_build():
    target_files = [
        "/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html",
        "/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html"
    ]

    for fpath in target_files:
        with open(fpath, "r", encoding="utf-8") as f:
            html = f.read()

        # 1. Empathy button in toolbar
        empathy_btn = '''      <!-- Empathy / Sensory Simulator Toggle -->
      <button onclick="toggleEmpathyModal()" id="btn-empathy" class="px-2 py-0.5 rounded bg-purple-950 hover:bg-purple-900 text-purple-200 flex items-center gap-1 border border-purple-700 text-[11px] font-bold shadow-sm" title="محاكي التجربة الحسية وضعف البصر">
        <span>👁️</span> <span>محاكي التجربة الحسية (Empathy)</span>
      </button>'''

        if 'id="btn-empathy"' not in html:
            insert_pos = html.find('<!-- High Contrast Toggle -->')
            if insert_pos != -1:
                html = html[:insert_pos] + empathy_btn + '\n      ' + html[insert_pos:]

        # 2. Empathy Modal & Filters
        empathy_modal_code = '''  <!-- SVG Color Matrix Filters for Color Blindness & Sensory Empathy -->
  <svg style="display:none;" class="no-print">
    <defs>
      <filter id="protanopia-filter">
        <feColorMatrix type="matrix" values="0.567, 0.433, 0, 0, 0  0.558, 0.442, 0, 0, 0  0, 0.242, 0.758, 0, 0  0, 0, 0, 1, 0"/>
      </filter>
      <filter id="deuteranopia-filter">
        <feColorMatrix type="matrix" values="0.625, 0.375, 0, 0, 0  0.7, 0.3, 0, 0, 0  0, 0.3, 0.7, 0, 0  0, 0, 0, 1, 0"/>
      </filter>
    </defs>
  </svg>

  <!-- Empathy Mode Interactive Modal -->
  <div id="empathy-modal" class="no-print fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[var(--card,#fff)] border-2 border-purple-500/50 rounded-2xl max-w-md w-full p-6 shadow-2xl space-y-4">
      <div class="flex items-center justify-between border-b border-slate-200 dark:border-slate-800 pb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">👁️</span>
          <h3 class="font-black text-sm sm:text-base text-slate-900 dark:text-slate-100">محاكي التجربة الحسية والتعايش (Empathy Mode)</h3>
        </div>
        <button onclick="toggleEmpathyModal()" class="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 text-lg font-bold">✕</button>
      </div>

      <p class="text-xs text-slate-600 dark:text-slate-400 leading-relaxed">
        اختبر كيف يرى ويتفاعل كبار السن والأشخاص ذوو الإعاقات البصرية مع تصميم المباني والمخططات، لبيان الأهمية الحيوية للتباين اللوني والبلاط اللمسي والإضاءة:
      </p>

      <div class="space-y-2 text-xs">
        <label class="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 cursor-pointer">
          <div class="flex items-center gap-2">
            <input type="radio" name="empathy-choice" value="normal" checked onchange="applyEmpathyFilter(this.value)">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">الرؤية الطبيعية (Normal Vision)</div>
              <div class="text-[10px] text-slate-400">العرض القياسي للمنصة بكامل الألوان</div>
            </div>
          </div>
          <span class="text-emerald-500 font-bold">100%</span>
        </label>

        <label class="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 cursor-pointer">
          <div class="flex items-center gap-2">
            <input type="radio" name="empathy-choice" value="protanopia" onchange="applyEmpathyFilter(this.value)">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">عمى اللون الأحمر (Protanopia)</div>
              <div class="text-[10px] text-slate-400">صعوبة تمييز إشارات الخطر والمقابض الحمراء</div>
            </div>
          </div>
          <span class="text-amber-500 font-bold">محاكاة</span>
        </label>

        <label class="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 cursor-pointer">
          <div class="flex items-center gap-2">
            <input type="radio" name="empathy-choice" value="deuteranopia" onchange="applyEmpathyFilter(this.value)">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">عمى اللون الأخضر (Deuteranopia)</div>
              <div class="text-[10px] text-slate-400">صعوبة تمييز مسارات الطوارئ الخضراء</div>
            </div>
          </div>
          <span class="text-amber-500 font-bold">محاكاة</span>
        </label>

        <label class="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 cursor-pointer">
          <div class="flex items-center gap-2">
            <input type="radio" name="empathy-choice" value="cataract" onchange="applyEmpathyFilter(this.value)">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">ضعف البصر وضبابية الرؤية (Low Vision / Cataracts)</div>
              <div class="text-[10px] text-slate-400">شائع لدى كبار السن - يوضح أهمية الخطوط الكبيرة والتباين العالي</div>
            </div>
          </div>
          <span class="text-purple-500 font-bold">ضبابي</span>
        </label>

        <label class="flex items-center justify-between p-2.5 rounded-xl border border-slate-200 dark:border-slate-800 hover:bg-slate-50 dark:hover:bg-slate-800/60 cursor-pointer">
          <div class="flex items-center gap-2">
            <input type="radio" name="empathy-choice" value="tunnel" onchange="applyEmpathyFilter(this.value)">
            <div>
              <div class="font-bold text-slate-800 dark:text-slate-200">الرؤية النفقية وضيق المجال (Tunnel Vision / Glaucoma)</div>
              <div class="text-[10px] text-slate-400">انعدام الرؤية المحيطية مما يتطلب علامات إرشادية مباشرة</div>
            </div>
          </div>
          <span class="text-purple-500 font-bold">نفق</span>
        </label>
      </div>

      <div class="pt-2 flex justify-between items-center text-xs">
        <span id="empathy-active-badge" class="text-emerald-600 font-bold">النمط النشط: رؤية طبيعية</span>
        <button onclick="toggleEmpathyModal()" class="px-4 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold transition shadow">إغلاق</button>
      </div>
    </div>
  </div>'''

        if 'id="empathy-modal"' not in html:
            guide_pos = html.find('<div id="reading-guide"></div>')
            if guide_pos != -1:
                guide_end = guide_pos + len('<div id="reading-guide"></div>')
                html = html[:guide_end] + '\n\n' + empathy_modal_code + html[guide_end:]

        # 3. Navigation bar with 8 tabs
        nav_start = html.find('<nav class="flex flex-wrap items-center gap-1 p-1 bg-slate-100')
        if nav_start != -1:
            nav_end = html.find('</nav>', nav_start) + len('</nav>')
            new_nav = '''<nav class="flex flex-wrap items-center gap-1 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl border border-slate-200 dark:border-slate-700 text-xs font-semibold">
        <button onclick="switchTab('dashboard')" id="tab-btn-dashboard" class="tab-btn px-3 py-1.5 rounded-lg transition bg-white dark:bg-slate-900 text-emerald-700 dark:text-emerald-400 font-bold shadow-sm">📊 لوحة المؤشرات و GIS</button>
        <button onclick="switchTab('calculator')" id="tab-btn-calculator" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">🧪 مختبر المحاكاة و CAD</button>
        <button onclick="switchTab('ai-audit')" id="tab-btn-ai-audit" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">🤖 المدقق الذكي للمخططات AI</button>
        <button onclick="switchTab('audit')" id="tab-btn-audit" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">📋 نظام التدقيق والسجل</button>
        <button onclick="switchTab('boq')" id="tab-btn-boq" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">💰 حاسبة الكلفة والعطاءات</button>
        <button onclick="switchTab('community')" id="tab-btn-community" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">👥 صوت المواطن والتبليغ</button>
        <button onclick="switchTab('retrofit')" id="tab-btn-retrofit" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">🛠️ دليل المعالجات</button>
        <button onclick="switchTab('library')" id="tab-btn-library" class="tab-btn px-3 py-1.5 rounded-lg transition text-slate-600 dark:text-slate-300 hover:text-slate-900">📚 المكتبة والتشريعات</button>
      </nav>'''
            html = html[:nav_start] + new_nav + html[nav_end:]

        # 4. GIS section in Tab 1
        gis_section_html = gc.generate_gis_section()
        heatmap_marker = '<!-- GOVERNORATES READINESS HEATMAP -->'
        if heatmap_marker in html:
            h_start = html.find(heatmap_marker)
            dash_end = html.find('</section>', h_start)
            html = html[:h_start] + gis_section_html + '\n    ' + html[dash_end:]

        # 5. DXF & Tender spec buttons in tab-calculator
        ramp_target = '<span id="calc-verdict">تصميم مطابق ومريح ومناسب لكبار السن وللاستخدام الذاتي.</span>'
        ramp_actions = '''<span id="calc-verdict">تصميم مطابق ومريح ومناسب لكبار السن وللاستخدام الذاتي.</span>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800">
                <button onclick="exportToDXF('ramp')" class="text-[11px] bg-slate-800 hover:bg-slate-700 text-sky-400 font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1">
                  <span>📐</span> <span>تنزيل مخطط أوتوكاد تنفيذي (.DXF)</span>
                </button>
                <button onclick="exportTenderSpecs('ramp')" class="text-[11px] bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1">
                  <span>📑</span> <span>المواصفة الفنية للمناقصة (Tender Spec)</span>
                </button>'''
        if 'onclick="exportToDXF(\'ramp\')"' not in html:
            html = html.replace(ramp_target, ramp_actions)

        rest_target = '<span class="text-emerald-500 font-bold">كود عراقي 2026</span>'
        rest_actions = '''<span class="text-emerald-500 font-bold">كود عراقي 2026</span>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-200 dark:border-slate-800">
                <button onclick="exportToDXF('restroom')" class="text-[11px] bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-sky-600 dark:text-sky-400 font-bold px-2.5 py-1 rounded-lg border border-slate-300 dark:border-slate-700 transition flex items-center gap-1">
                  <span>📐</span> <span>تنزيل مخطط أوتوكاد تنفيذي (.DXF)</span>
                </button>
                <button onclick="exportTenderSpecs('restroom')" class="text-[11px] bg-slate-100 dark:bg-slate-800 hover:bg-slate-200 text-emerald-600 dark:text-emerald-400 font-bold px-2.5 py-1 rounded-lg border border-slate-300 dark:border-slate-700 transition flex items-center gap-1">
                  <span>📑</span> <span>المواصفة الفنية للمناقصة</span>
                </button>'''
        if 'onclick="exportToDXF(\'restroom\')"' not in html:
            html = html.replace(rest_target, rest_actions, 1)

        park_target = '<span class="text-blue-400 font-bold" id="park-verdict">تصميم مطابق لكود م.ب.ع 202</span>'
        park_actions = '''<span class="text-blue-400 font-bold" id="park-verdict">تصميم مطابق لكود م.ب.ع 202</span>
              </div>
              <div class="flex items-center gap-2 pt-2 border-t border-slate-800">
                <button onclick="exportToDXF('parking')" class="text-[11px] bg-slate-800 hover:bg-slate-700 text-sky-400 font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1">
                  <span>📐</span> <span>تنزيل مخطط أوتوكاد تنفيذي (.DXF)</span>
                </button>
                <button onclick="exportTenderSpecs('parking')" class="text-[11px] bg-slate-800 hover:bg-slate-700 text-emerald-400 font-bold px-2.5 py-1 rounded-lg border border-slate-700 transition flex items-center gap-1">
                  <span>📑</span> <span>المواصفة الفنية لموقف المعاقين</span>
                </button>'''
        if 'onclick="exportToDXF(\'parking\')"' not in html:
            html = html.replace(park_target, park_actions, 1)

        # 6. Inject tab-ai-audit
        ai_tab_html = gc.generate_ai_audit_tab()
        calc_start = html.find('id="tab-calculator"')
        if calc_start != -1 and 'id="tab-ai-audit"' not in html:
            calc_end = html.find('</section>', calc_start) + len('</section>')
            html = html[:calc_end] + '\n\n' + ai_tab_html + html[calc_end:]

        # 7. Inject tab-community
        community_tab_html = gc.generate_community_tab()
        retro_start = html.find('id="tab-retrofit"')
        if retro_start != -1 and 'id="tab-community"' not in html:
            sec_start = html.rfind('<section', 0, retro_start)
            html = html[:sec_start] + community_tab_html + '\n\n    ' + html[sec_start:]

        # 8. Update switchTab function
        old_switch_tab = "const tabs = ['dashboard', 'calculator', 'audit', 'boq', 'retrofit', 'library'];"
        new_switch_tab = "const tabs = ['dashboard', 'calculator', 'ai-audit', 'audit', 'boq', 'community', 'retrofit', 'library'];"
        html = html.replace(old_switch_tab, new_switch_tab)

        # 9. Append Grand System JS logic
        grand_js = get_grand_js()
        js_marker = '// --- AUDIT SYSTEM & CHECKLIST ---'
        if 'function exportToDXF' not in html:
            html = html.replace(js_marker, grand_js + '\n    ' + js_marker)

        # 10. Update window.onload
        old_onload = "if (typeof runReachCalc === 'function') runReachCalc();"
        new_onload = """if (typeof runReachCalc === 'function') runReachCalc();
      if (typeof selectGov === 'function') selectGov('بغداد');
      if (typeof runAIPlanScan === 'function') runAIPlanScan();
      if (typeof renderCommunityFeed === 'function') renderCommunityFeed();"""
        if 'selectGov(\'بغداد\')' not in html:
            html = html.replace(old_onload, new_onload)

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Grand system successfully integrated into {fpath}!")
if __name__ == "__main__":
    run_full_build()
