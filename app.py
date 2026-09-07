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

# Custom Styling for clean RTL presentation
st.markdown("""
<style>
    /* Hide Streamlit default padding and headers for embedded full-view */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    header[data-testid="stHeader"] {
        background: transparent;
    }
    .stDownloadButton button {
        width: 100%;
        background-color: #047857;
        color: white;
        border-radius: 10px;
        font-weight: bold;
    }
    .stDownloadButton button:hover {
        background-color: #065f46;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with platform information, credits, and document downloads
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f6/Coat_of_arms_of_Iraq_%282008%E2%80%93present%29.svg", width=90)
    st.markdown("### 🏛️ جمهورية العراق")
    st.markdown("#### منصة كود الوصول الشامل والتصميم الدامج")
    st.markdown("**مبنية استناداً إلى:**")
    st.markdown("- 📜 مدونة متطلبات المعاقين العراقية (`م.ب.ع 202`)")
    st.markdown("- 🇺🇸 المعايير الأمريكية للتصميم المتاح (`ADA 2010`)")
    st.divider()

    st.markdown("#### 📂 تحميل الوثائق الهندسية الرسمية:")

    # Read and provide downloads
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
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

    st.divider()
    st.markdown("""
    <div style="font-size: 0.85rem; color: #64748b; text-align: center;">
        <strong>إشراف وتطوير:</strong><br>
        المهندس المعماري الدكتور أحمد لؤي أحمد<br>
        <em style="font-size: 0.75rem;">هذه المنصة قيد التطوير وبمبادرة شخصية من المهندس المعماري الدكتور احمد لؤي احمد.</em>
    </div>
    """, unsafe_allow_html=True)

# Main Platform Embed
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iraqi_accessibility_platform.html")
if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    components.html(html_content, height=1150, scrolling=True)
else:
    st.error("تعذر العثور على ملف المنصة التفاعلية iraqi_accessibility_platform.html")
