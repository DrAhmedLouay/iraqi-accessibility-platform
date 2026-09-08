import streamlit as st
import streamlit.components.v1 as components
import os

# Set page configuration
st.set_page_config(
    page_title="المنصة العراقية لمعايير الوصول الشامل | د. أحمد لؤي",
    page_icon="♿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for clean RTL presentation & prestigious architectural theme
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800;900&display=swap');

.block-container {
    padding-top: 3.25rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
    max-width: 100% !important;
}
header[data-testid="stHeader"] {
    background: transparent !important;
    height: 3rem !important;
    z-index: 99999 !important;
    pointer-events: none !important;
}
header[data-testid="stHeader"] * {
    pointer-events: auto !important;
}

/* Hide decoration line and status widget */
[data-testid="stDecoration"] {
    display: none !important;
}
[data-testid="stStatusWidget"] {
    display: none !important;
}

/* Move toolbar (Deploy & ⋮ menu) to the left to avoid colliding with sidebar toggle on the right */
[data-testid="stToolbar"] {
    left: 0.75rem !important;
    right: auto !important;
}

/* Move Streamlit sidebar to the RIGHT side (RTL Layout) */
[data-testid="stAppViewContainer"] {
    flex-direction: row-reverse !important;
}

/* Completely remove the ugly dividing line */
[data-testid="stSidebar"] {
    border: none !important;
    border-left: none !important;
    border-right: none !important;
    box-shadow: none !important;
    direction: rtl !important;
    text-align: right !important;
}
[data-testid="stSidebar"][aria-expanded="false"] {
    display: none !important;
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
    border: none !important;
    box-shadow: none !important;
    margin: 0 !important;
}

[data-testid="stSidebar"], [data-testid="stSidebar"] * {
    font-family: 'Cairo', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
    direction: rtl !important;
    text-align: right !important;
    box-sizing: border-box;
}

/* Position sidebar toggle button on the right without flipping container */
[data-testid="stSidebarCollapsedControl"] {
    left: auto !important;
    right: 0.75rem !important;
    top: 0.5rem !important;
    transform: none !important;
    z-index: 100000 !important;
}
[data-testid="stSidebarCollapseButton"] {
    transform: none !important;
}

/* Flip ONLY the arrow SVG icon inside the button, never text or tooltips */
[data-testid="stSidebarCollapsedControl"] button svg,
[data-testid="stSidebarCollapseButton"] button svg {
    transform: scaleX(-1) !important;
}

/* Hide overflowing tooltips on the collapse controls that cause text glitches */
[data-testid="stSidebarCollapsedControl"] [data-baseweb="tooltip"],
[data-testid="stSidebarCollapseButton"] [data-baseweb="tooltip"] {
    display: none !important;
}

@media (max-width: 991px) {
    [data-testid="stSidebar"] {
        right: 0 !important;
        left: auto !important;
    }
}

[data-testid="stSidebar"] [data-testid="stImage"] {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    margin-bottom: 0.4rem !important;
}
[data-testid="stSidebar"] [data-testid="stImage"] img {
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
    border: 1px solid rgba(16, 185, 129, 0.25);
}

.sidebar-header-card {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.12) 0%, rgba(15, 23, 42, 0.04) 100%);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 14px;
    padding: 12px 10px;
    margin: 6px 0 12px 0;
    text-align: center;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}
.country-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(16, 185, 129, 0.15);
    color: #047857;
    border: 1px solid rgba(16, 185, 129, 0.35);
    padding: 3px 12px;
    border-radius: 9999px;
    font-size: 11.5px;
    font-weight: 800;
    margin-bottom: 6px;
}
.platform-title {
    font-size: 14px !important;
    font-weight: 900 !important;
    line-height: 1.45 !important;
    margin-bottom: 6px !important;
    color: inherit !important;
}
.platform-edition {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 10px;
    font-weight: 700;
    color: #64748b;
    background: rgba(100, 116, 139, 0.09);
    padding: 2px 9px;
    border-radius: 6px;
}
.pulse-dot {
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: #10b981;
    display: inline-block;
    box-shadow: 0 0 8px #10b981;
}

.sidebar-section-title {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 14px 0 9px 0;
    padding-bottom: 6px;
    border-bottom: 2px solid rgba(16, 185, 129, 0.25);
}
.section-title-text {
    font-size: 12px;
    font-weight: 800;
    color: inherit;
    display: flex;
    align-items: center;
    gap: 6px;
}
.section-badge-counter {
    font-size: 9.5px;
    font-weight: 700;
    background: #047857;
    color: #ffffff !important;
    padding: 2px 8px;
    border-radius: 9999px;
}

.sidebar-cards-container {
    display: flex;
    flex-direction: column;
    gap: 6.5px;
    margin-bottom: 12px;
}
.sidebar-feature-card {
    display: flex;
    align-items: center;
    gap: 9px;
    background: rgba(125, 125, 125, 0.06);
    border: 1px solid rgba(125, 125, 125, 0.16);
    border-radius: 10px;
    padding: 7px 9px;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    text-align: right;
}
.sidebar-feature-card:hover {
    transform: translateX(-3px);
    border-color: #10b981;
    background: rgba(16, 185, 129, 0.08);
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
}
.feature-icon-wrapper {
    width: 30px;
    height: 30px;
    min-width: 30px;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
}
.icon-emerald { background: rgba(16, 185, 129, 0.15); }
.icon-blue    { background: rgba(59, 130, 246, 0.15); }
.icon-purple  { background: rgba(168, 85, 247, 0.15); }
.icon-sky     { background: rgba(14, 165, 233, 0.15); }
.icon-rose    { background: rgba(244, 63, 94, 0.15); }
.icon-amber   { background: rgba(245, 158, 11, 0.15); }
.icon-teal    { background: rgba(20, 184, 166, 0.15); }

.feature-body {
    flex: 1;
    min-width: 0;
}
.feature-name {
    font-size: 11.5px;
    font-weight: 700;
    line-height: 1.35;
    margin-bottom: 2.5px;
    color: inherit;
}
.feature-meta {
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
}
.badge-tag {
    font-size: 9px;
    font-weight: 800;
    padding: 1px 5.5px;
    border-radius: 4px;
    line-height: 1.3;
}
.tag-emerald { background: rgba(16, 185, 129, 0.2); color: #047857; }
.tag-blue    { background: rgba(59, 130, 246, 0.2); color: #1d4ed8; }
.tag-purple  { background: rgba(168, 85, 247, 0.2); color: #7e22ce; }
.tag-sky     { background: rgba(14, 165, 233, 0.2); color: #0369a1; }
.tag-rose    { background: rgba(244, 63, 94, 0.2); color: #be123c; }
.tag-amber   { background: rgba(245, 158, 11, 0.2); color: #b45309; }
.tag-teal    { background: rgba(20, 184, 166, 0.2); color: #0f766e; }

.feature-desc {
    font-size: 9px;
    opacity: 0.75;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

@media (prefers-color-scheme: dark) {
    .country-badge { color: #34d399; }
    .tag-emerald { color: #34d399; }
    .tag-blue    { color: #60a5fa; }
    .tag-purple  { color: #c084fc; }
    .tag-sky     { color: #38bdf8; }
    .tag-rose    { color: #fb7185; }
    .tag-amber   { color: #fbbf24; }
    .tag-teal    { color: #2dd4bf; }
    .platform-edition { color: #94a3b8; }
}

.stDownloadButton button {
    width: 100%;
    background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    color: #ffffff !important;
    border: 1px solid #065f46 !important;
    border-radius: 10px !important;
    font-weight: 700 !important;
    font-size: 11.5px !important;
    padding: 8px 12px !important;
    box-shadow: 0 2px 6px rgba(5, 150, 105, 0.2) !important;
    transition: all 0.2s ease !important;
    margin-bottom: 2px !important;
}
.stDownloadButton button:hover {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 12px rgba(5, 150, 105, 0.3) !important;
}

.sidebar-partner-card {
    font-size: 11px;
    background: rgba(16, 185, 129, 0.08);
    border-right: 3.5px solid #059669;
    padding: 9px 10px;
    border-radius: 8px;
    color: inherit;
    margin: 10px 0;
    line-height: 1.5;
}
.partner-badge {
    font-weight: 800;
    color: #059669;
    margin-bottom: 3px;
    font-size: 11px;
}
.sidebar-credits-card {
    font-size: 11px;
    opacity: 0.85;
    text-align: center;
    padding: 6px 4px;
    line-height: 1.5;
}
.credits-author {
    font-weight: 800;
    color: inherit;
    font-size: 12px;
    margin-top: 2px;
}
</style>""", unsafe_allow_html=True)

# Sidebar with platform information, credits, and document downloads
current_dir = os.path.dirname(os.path.abspath(__file__))
with st.sidebar:
    logo_path = os.path.join(current_dir, "platform_logo.png")
    if not os.path.exists(logo_path):
        logo_path = os.path.join(current_dir, "platform_logo.jpg")
    if os.path.exists(logo_path):
        st.image(logo_path, width=140)
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Coat_of_arms_of_Iraq_%282008%E2%80%93present%29.svg", width=90)

    sidebar_content = """<div class="sidebar-header-card">
<div class="country-badge"><span>🏛️</span><span>جمهورية العراق</span></div>
<div class="platform-title">منصة كود الوصول الشامل والتصميم الدامج</div>
<div class="platform-edition"><span class="pulse-dot"></span>المرجع الهندسي والرقابي الوطني 2026</div>
</div>
<div class="sidebar-section-title">
<div class="section-title-text"><span>📐</span><span>مبنية استناداً إلى:</span></div>
<span class="section-badge-counter">7 ركائز</span>
</div>
<div class="sidebar-cards-container">
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-emerald">📜</div>
<div class="feature-body">
<div class="feature-name">مدونة متطلبات المعاقين العراقية</div>
<div class="feature-meta"><span class="badge-tag tag-emerald">م.ب.ع 202</span><span class="feature-desc">الكود الإلزامي لتراخيص البناء</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-blue">🇺🇸</div>
<div class="feature-body">
<div class="feature-name">المعايير الأمريكية للتصميم المتاح</div>
<div class="feature-meta"><span class="badge-tag tag-blue">ADA 2010</span><span class="feature-desc">المعايير القياسية العالمية</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-purple">🧪</div>
<div class="feature-body">
<div class="feature-name">مختبر المحاكاة الهندسية</div>
<div class="feature-meta"><span class="badge-tag tag-purple">7 محاكيات معمارية وتصدير CAD</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-sky">🗺️</div>
<div class="feature-body">
<div class="feature-name">خارطة GIS التفاعلية لمحافظات العراق</div>
<div class="feature-meta"><span class="badge-tag tag-sky">18 محافظة</span><span class="feature-desc">مؤشرات امتثال جغرافية حية</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-rose">🤖</div>
<div class="feature-body">
<div class="feature-name">المدقق الذكي للمخططات الهندسية</div>
<div class="feature-meta"><span class="badge-tag tag-rose">AI Plan Checker</span><span class="feature-desc">فحص المساقط وتأشيرات Redlines</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-amber">👁️</div>
<div class="feature-body">
<div class="feature-name">محاكي التجربة الحسية والتعايش</div>
<div class="feature-meta"><span class="badge-tag tag-amber">Empathy Mode</span><span class="feature-desc">عمى الألوان وضعف الرؤية</span></div>
</div>
</div>
<div class="sidebar-feature-card">
<div class="feature-icon-wrapper icon-teal">👥</div>
<div class="feature-body">
<div class="feature-name">منظومة صوت المواطن والتبليغ عن العوائق</div>
<div class="feature-meta"><span class="badge-tag tag-teal">بلاغات مجتمعية حية</span></div>
</div>
</div>
</div>"""
    st.markdown(sidebar_content, unsafe_allow_html=True)

    docs_title = """<div class="sidebar-section-title" style="margin-top: 14px;">
<div class="section-title-text"><span>📂</span><span>تحميل الوثائق الهندسية الرسمية:</span></div>
<span class="section-badge-counter">3 وثائق</span>
</div>"""
    st.markdown(docs_title, unsafe_allow_html=True)

    # Read and provide downloads
    code_path = os.path.join(current_dir, "iraqi_accessible_building_code.md")
    if os.path.exists(code_path):
        with open(code_path, "r", encoding="utf-8") as f:
            st.download_button(
                label="📄 مسودة الكود العراقي المعتمد (Markdown)",
                data=f.read(),
                file_name="iraqi_accessible_building_code.md",
                mime="text/markdown"
            )

    csv_path = os.path.join(current_dir, "accessibility_audit_checklist.csv")
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            st.download_button(
                label="📊 استمارة التدقيق الميداني (Excel / CSV)",
                data=f.read(),
                file_name="accessibility_audit_checklist.csv",
                mime="text/csv"
            )

    memo_path = os.path.join(current_dir, "ministerial_memorandum.md")
    if os.path.exists(memo_path):
        with open(memo_path, "r", encoding="utf-8") as f:
            st.download_button(
                label="📑 المذكرة الفنية والوزارية للإلزام",
                data=f.read(),
                file_name="ministerial_memorandum.md",
                mime="text/markdown"
            )

    st.markdown("""<div style="margin: 12px 0 8px 0; border-top: 1px solid rgba(125, 125, 125, 0.15);"></div>""", unsafe_allow_html=True)
    img_path = os.path.join(current_dir, "dr_riyad_al_ubaidi.jpg")
    if os.path.exists(img_path):
        st.image(img_path, caption="الخبير الدولي د. رياض العبيدي في TEDx بغداد", use_container_width=True)

    credits_content = """<div class="sidebar-partner-card">
<div class="partner-badge">🤝 شراكة علمية واستشارية:</div>
<div>تم تطوير هذه المنصة بالتعاون مع الخبير الدولي في تحوير المباني والمدن لصالح ذوي الاحتياجات الخاصة وكبار السن المهندس المعماري الدكتور رياض طالب باقر العبيدي.</div>
</div>
<div class="sidebar-credits-card">
<div><strong>إشراف وتطوير المنظومة:</strong></div>
<div class="credits-author">المهندس المعماري الدكتور أحمد لؤي أحمد</div>
<div style="font-size: 10px; margin-top: 4px; opacity: 0.8;">هذه المنصة قيد التطوير وبمبادرة شخصية من المهندس المعماري الدكتور أحمد لؤي أحمد.</div>
</div>"""
    st.markdown(credits_content, unsafe_allow_html=True)

# Main Platform Embed
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iraqi_accessibility_platform.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1250, scrolling=True)
else:
    st.error("تعذر العثور على ملف المنصة التفاعلية iraqi_accessibility_platform.html")
