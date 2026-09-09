#!/usr/bin/env python3
"""
Adds the disability community classification note to Module 9 (Accessible Stairs)
in both iraqi_accessibility_platform.html and index.html.
"""

import re
import sys

FILES = [
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/iraqi_accessibility_platform.html',
    '/Users/ahmedlouay/.gemini/antigravity/brain/f65941d5-cc59-4217-a7f8-d000f1a41476/index.html'
]

NOTE_HTML = """        <!-- ملاحظة تصنيف المعالجة لمجتمع ذوي الإعاقة -->
        <div class="mb-5 p-4 rounded-xl bg-amber-50/90 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800/60 flex items-start gap-3 text-xs leading-relaxed text-slate-700 dark:text-slate-300 shadow-sm">
          <div class="text-xl shrink-0 leading-none">💡</div>
          <div>
            <div class="flex items-center gap-2 mb-1 flex-wrap">
              <span class="font-bold text-amber-900 dark:text-amber-200 text-sm">
                تصنيف المعالجة لمجتمع ذوي الإعاقة (Target Beneficiaries Classification):
              </span>
              <span class="text-[10px] bg-amber-200/80 dark:bg-amber-900/50 text-amber-900 dark:text-amber-200 px-2 py-0.5 rounded font-bold">
                إيضاح معماري ورقابي هام
              </span>
            </div>
            <p class="text-slate-700 dark:text-slate-300">
              هذه المعالجة الهندسية <strong>ليست مخصصة لمستخدمي الكراسي المتحركة</strong> (الذين يُحظر عليهم استخدام الأدراج وتُخصص لهم المنحدرات والمصاعد الميسرة بالأداتين 1 و 5)، بل صُممت لتأمين وتحقيق السلامة والراحة لأكثر من <strong>85% من مجتمع ذوي الإعاقة وكبار السن</strong>، وتشمل الفئات التالية:
            </p>
            <div class="mt-2.5 flex flex-wrap gap-1.5 text-[11px]">
              <span class="px-2.5 py-1 rounded-lg bg-white dark:bg-slate-800 border border-amber-300 dark:border-amber-700/80 font-bold text-slate-800 dark:text-slate-200 shadow-xs">
                🦯 ذوو الإعاقة الحركية الجزئية ومستخدمو العكازات والأطراف الصناعية
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white dark:bg-slate-800 border border-amber-300 dark:border-amber-700/80 font-bold text-slate-800 dark:text-slate-200 shadow-xs">
                🧓 كبار السن ومرضى ضعف التوازن والقلب
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white dark:bg-slate-800 border border-amber-300 dark:border-amber-700/80 font-bold text-slate-800 dark:text-slate-200 shadow-xs">
                👁️ المكفوفون وضعاف البصر (عبر البلاط اللمسي والأنف المشطوف والمتباين)
              </span>
              <span class="px-2.5 py-1 rounded-lg bg-white dark:bg-slate-800 border border-amber-300 dark:border-amber-700/80 font-bold text-slate-800 dark:text-slate-200 shadow-xs">
                📏 قصار القامة والأطفال (عبر الدرابزين المزدوج السفلي بارتفاع 65 سم)
              </span>
            </div>
          </div>
        </div>
"""

BENEFICIARY_SPEC_TEXT = """5. **الفئات المستفيدة وتصنيف المعالجة:** صُممت هذه السلالم خصيصاً لحماية وتمكين ذوي الإعاقة الحركية الجزئية (مستخدمي العكازات والمشايات والأطراف الصناعية)، كبار السن، مرضى ضعف التوازن والقلب، والمكفوفين وضعاف البصر وقصار القامة؛ حيث يُمنع استخدام السلالم لمستخدمي الكراسي المتحركة وتُخصص لهم المنحدرات والمصاعد بالأداتين 1 و 5."""

for file_path in FILES:
    print(f"Processing: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert NOTE_HTML right before <div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start"> in calc-sec-stairs
    target_pattern = r'(<div id="calc-sec-stairs"[^>]*>[\s\S]*?<span class="text-\[10px\] bg-teal-50[^>]*>معادلة الراحة 2R\+T</span>\s*</div>)(\s*)(<div class="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">)'
    
    match = re.search(target_pattern, content)
    if not match:
        print(f"Error: Could not find header pattern in {file_path}")
        sys.exit(1)
        
    replacement = match.group(1) + "\n\n" + NOTE_HTML + "\n        " + match.group(3)
    content = content[:match.start()] + replacement + content[match.end():]

    # 2. Add beneficiary note to the Results Card in calc-sec-stairs
    eval_card_pattern = r'(<div id="stairs-res-eval"[^>]*>[\s\S]*?</div>\s*</div>)'
    match_eval = re.search(eval_card_pattern, content)
    if match_eval:
        extra_note = """\n              <div class="border-t border-slate-100 dark:border-slate-700 pt-2 text-[10px] text-slate-500 dark:text-slate-400">
                <span class="font-bold text-amber-700 dark:text-amber-400">الفئات المستهدفة:</span> الإعاقة الحركية الجزئية (عكازات/أطراف)، كبار السن، ضعف التوازن، المكفوفين، وقصار القامة.
              </div>"""
        content = content[:match_eval.end()] + extra_note + content[match_eval.end():]

    # 3. Add point 5 to exportTenderSpecs for stairs
    spec_target = "4. **شريط التحذير اللمسي:** تركيب شريط بلاط تحذيري بنقاط بارزة (Tactile Blister Pavers) بعمق 60 سم وبلون متباين (أصفر عاكس) قبل أول درجة في الأعلى والأسفل لتنبيه المكفوفين وضعاف البصر بوجود درج.`"
    if spec_target in content:
        new_spec = spec_target[:-1] + "\n" + BENEFICIARY_SPEC_TEXT + "`"
        content = content.replace(spec_target, new_spec)
        print("  Updated exportTenderSpecs point 5")
    else:
        print("  Warning: spec_target not found in exportTenderSpecs")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated: {file_path}")

print("Done all updates!")
