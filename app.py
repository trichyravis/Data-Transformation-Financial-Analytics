
"""
THE MOUNTAIN PATH - World of Finance
Data Transformation for Data Analysis - Interactive Learning App
Prof. V. Ravichandran
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from scipy import stats as sp_stats

# =============================================================================
# MOUNTAIN PATH ACADEMY DESIGN SYSTEM
# =============================================================================
DARK_BLUE = "#003366"
MID_BLUE = "#004080"
LIGHT_BLUE = "#ADD8E6"
GOLD = "#FFD700"
DARK_GOLD = "#B8860B"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFC"
LIGHT_GOLD_BG = "#FFFDF0"
ACCENT_GREEN = "#2E8B57"
CORAL = "#E74C3C"
PURPLE = "#8E44AD"
TEAL = "#17A589"
ORANGE = "#E67E22"

st.set_page_config(
    page_title="Data Transformation | The Mountain Path",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Mountain Path Academy CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Source+Sans+3:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    .stApp {{
        background: linear-gradient(180deg, {OFF_WHITE} 0%, #EDF2F7 100%);
    }}
    .block-container {{
        padding-top: 1rem;
        max-width: 1200px;
    }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {DARK_BLUE} 0%, #001a33 100%);
    }}
    section[data-testid="stSidebar"] * {{
        color: {WHITE} !important;
    }}
    section[data-testid="stSidebar"] .stRadio > label > div[data-testid="stMarkdownContainer"] > p {{
        color: {GOLD} !important;
        font-weight: 600;
        font-size: 1.1rem;
    }}
    section[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label p {{
        color: {WHITE} !important;
        font-size: 1.02rem;
        font-weight: 500;
    }}
    section[data-testid="stSidebar"] hr {{
        border-color: rgba(173,216,230,0.3);
    }}
    section[data-testid="stSidebar"] a {{
        color: {GOLD} !important;
        text-decoration: none !important;
    }}
    section[data-testid="stSidebar"] a:hover {{
        text-decoration: underline !important;
    }}

    /* Headers */
    h1 {{ font-family: 'Playfair Display', serif !important; color: {DARK_BLUE} !important; font-weight: 700 !important; }}
    h2, h3, h4 {{ font-family: 'Source Sans 3', sans-serif !important; color: {DARK_BLUE} !important; font-weight: 600 !important; }}
    p, li, span {{ font-family: 'Source Sans 3', sans-serif; }}

    /* Brand header */
    .mp-brand-header {{
        background: linear-gradient(135deg, {DARK_BLUE} 0%, {MID_BLUE} 50%, #005599 100%);
        color: white; padding: 1.4rem 2rem; border-radius: 12px; text-align: center;
        margin-bottom: 1.5rem; box-shadow: 0 6px 20px rgba(0,51,102,0.35);
        border-bottom: 4px solid {GOLD};
    }}
    .mp-brand-header h1 {{ color: white !important; font-family: 'Playfair Display', serif !important; font-size: 2rem !important; margin: 0 !important; letter-spacing: 2px; }}
    .mp-brand-header .subtitle {{ color: {GOLD}; font-size: 1.1rem; font-family: 'Source Sans 3', sans-serif; margin-top: 0.3rem; }}

    /* Boxes */
    .defn-box {{
        background: linear-gradient(135deg, rgba(173,216,230,0.15) 0%, rgba(173,216,230,0.05) 100%);
        border-left: 4px solid {DARK_BLUE}; border-radius: 0 8px 8px 0; padding: 1.2rem 1.5rem; margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,51,102,0.08);
    }}
    .defn-box .box-title {{ background: {DARK_BLUE}; color: white; display: inline-block; padding: 3px 14px; border-radius: 4px; font-weight: 600; font-size: 0.95rem; margin-bottom: 0.6rem; }}
    .example-box {{
        background: linear-gradient(135deg, {LIGHT_GOLD_BG} 0%, rgba(255,215,0,0.06) 100%);
        border-left: 4px solid {GOLD}; border-radius: 0 8px 8px 0; padding: 1.2rem 1.5rem; margin: 1rem 0;
    }}
    .example-box .box-title {{ color: {DARK_GOLD}; font-weight: 700; font-size: 0.95rem; margin-bottom: 0.5rem; }}
    .insight-box {{
        background: linear-gradient(135deg, rgba(46,139,87,0.08) 0%, rgba(46,139,87,0.03) 100%);
        border-left: 4px solid {ACCENT_GREEN}; border-radius: 0 8px 8px 0; padding: 1.2rem 1.5rem; margin: 1rem 0;
    }}
    .insight-box .box-title {{ color: {ACCENT_GREEN}; font-weight: 700; font-size: 0.95rem; margin-bottom: 0.5rem; }}
    .formula-box {{
        background: #f0f4f8; border: 1px solid #d0d8e0; border-radius: 6px; padding: 0.8rem 1.2rem;
        font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; color: {DARK_BLUE}; margin: 0.5rem 0;
    }}
    .metric-card {{
        background: white; border-radius: 10px; padding: 1.2rem; text-align: center;
        box-shadow: 0 2px 10px rgba(0,51,102,0.08); border-top: 3px solid {DARK_BLUE};
    }}
    .metric-card .value {{ font-size: 2rem; font-weight: 700; color: {DARK_BLUE}; font-family: 'Playfair Display', serif; }}
    .metric-card .label {{ color: #666; font-size: 0.85rem; font-family: 'Source Sans 3', sans-serif; }}

    /* Pipeline */
    .pipeline-container {{
        display: flex; align-items: center; justify-content: center; flex-wrap: wrap;
        gap: 0; padding: 1.2rem 0; margin: 1rem 0;
    }}
    .pipeline-step {{
        display: flex; align-items: center; justify-content: center; flex-direction: column;
        width: 100px; height: 100px; border-radius: 50%; color: white; font-weight: 600;
        font-size: 0.72rem; text-align: center; line-height: 1.2; padding: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15); transition: transform 0.2s;
        font-family: 'Source Sans 3', sans-serif;
    }}
    .pipeline-step:hover {{ transform: scale(1.12); }}
    .pipeline-arrow {{
        font-size: 1.6rem; color: {GOLD}; margin: 0 2px; font-weight: 900;
        text-shadow: 0 2px 4px rgba(0,0,0,0.15);
    }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{ gap: 0; background: {DARK_BLUE}; border-radius: 8px 8px 0 0; padding: 4px 4px 0 4px; }}
    .stTabs [data-baseweb="tab"] {{ color: {LIGHT_BLUE}; border-radius: 6px 6px 0 0; padding: 8px 18px; font-family: 'Source Sans 3', sans-serif; font-weight: 500; }}
    .stTabs [aria-selected="true"] {{ background: white !important; color: {DARK_BLUE} !important; font-weight: 700; }}

    .stDataFrame {{ border-radius: 8px; overflow: hidden; }}

    /* Footer */
    .mp-footer {{
        text-align: center; padding: 1.5rem; color: #666; font-size: 0.85rem;
        border-top: 2px solid {DARK_BLUE}; margin-top: 2rem;
        background: linear-gradient(180deg, rgba(0,51,102,0.03), rgba(0,51,102,0.08));
    }}
    .mp-footer a {{ color: {DARK_BLUE}; text-decoration: none; font-weight: 600; }}
    .mp-footer a:hover {{ color: {GOLD}; text-decoration: underline; }}
    .social-links a {{
        display: inline-block; padding: 6px 16px; margin: 0 6px; border-radius: 20px;
        font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: all 0.2s;
    }}
    .social-links a.linkedin {{ background: #0077B5; color: white !important; }}
    .social-links a.github {{ background: #333; color: white !important; }}
    .social-links a.web {{ background: {DARK_BLUE}; color: white !important; }}
    .social-links a:hover {{ opacity: 0.85; transform: translateY(-1px); }}

    /* Code blocks for case study */
    .code-block {{
        background: #1e1e2e; color: #cdd6f4; border-radius: 8px; padding: 1rem 1.2rem;
        font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; line-height: 1.5;
        overflow-x: auto; margin: 0.5rem 0; border-left: 4px solid {GOLD};
    }}
    .code-block .kw {{ color: #cba6f7; }} /* keywords */
    .code-block .fn {{ color: #89b4fa; }} /* functions */
    .code-block .st {{ color: #a6e3a1; }} /* strings */
    .code-block .cm {{ color: #6c7086; font-style: italic; }} /* comments */
    .code-block .nb {{ color: #f9e2af; }} /* numbers/builtins */
    .step-header {{
        background: linear-gradient(135deg, {DARK_BLUE}, {MID_BLUE});
        color: white; padding: 0.8rem 1.2rem; border-radius: 8px; margin: 1.5rem 0 0.5rem 0;
        font-family: 'Source Sans 3', sans-serif; font-weight: 600; font-size: 1.05rem;
        display: flex; align-items: center; gap: 10px;
        box-shadow: 0 3px 10px rgba(0,51,102,0.2);
    }}
    .step-num {{
        background: {GOLD}; color: {DARK_BLUE}; width: 32px; height: 32px; border-radius: 50%;
        display: inline-flex; align-items: center; justify-content: center;
        font-weight: 900; font-size: 0.9rem; flex-shrink: 0;
    }}

    /* Q&A Educational Tab */
    .qa-card {{
        background: white; border-radius: 10px; padding: 1.2rem 1.4rem; margin: 0.8rem 0;
        box-shadow: 0 2px 10px rgba(0,51,102,0.07); border-left: 4px solid {DARK_BLUE};
    }}
    .qa-card .qa-q {{
        color: {DARK_BLUE}; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem;
        font-family: 'Source Sans 3', sans-serif;
    }}
    .qa-card .qa-a {{
        color: #333; font-size: 0.93rem; line-height: 1.6;
        font-family: 'Source Sans 3', sans-serif;
    }}
    .adv-lim-container {{
        display: flex; gap: 1rem; margin: 1rem 0;
    }}
    .adv-box, .lim-box {{
        flex: 1; border-radius: 10px; padding: 1.2rem; min-height: 120px;
    }}
    .adv-box {{
        background: linear-gradient(135deg, rgba(46,139,87,0.08), rgba(46,139,87,0.03));
        border: 1px solid rgba(46,139,87,0.3);
    }}
    .adv-box .al-title {{ color: {ACCENT_GREEN}; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }}
    .lim-box {{
        background: linear-gradient(135deg, rgba(231,76,60,0.08), rgba(231,76,60,0.03));
        border: 1px solid rgba(231,76,60,0.3);
    }}
    .lim-box .al-title {{ color: #E74C3C; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }}
    .al-item {{ font-size: 0.9rem; line-height: 1.7; color: #333; }}
    .approach-box {{
        background: linear-gradient(135deg, rgba(0,51,102,0.06), rgba(0,51,102,0.02));
        border: 1px solid rgba(0,51,102,0.2); border-radius: 10px; padding: 1.2rem; margin: 0.8rem 0;
    }}
    .approach-box .al-title {{ color: {DARK_BLUE}; font-weight: 700; font-size: 1rem; margin-bottom: 0.5rem; }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# PLOTLY THEME
# =============================================================================
MP_COLORS = [DARK_BLUE, GOLD, "#4A90D9", ACCENT_GREEN, ORANGE, PURPLE, TEAL, CORAL]

def mp_layout(fig, title="", height=420):
    fig.update_layout(
        title=dict(text=title, font=dict(family="Playfair Display, serif", size=18, color=DARK_BLUE), x=0.5),
        font=dict(family="Source Sans Pro, sans-serif", color="#333"),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        height=height, margin=dict(l=50, r=30, t=60, b=40),
        legend=dict(bgcolor="rgba(255,255,255,0.8)", bordercolor=DARK_BLUE, borderwidth=1),
    )
    fig.update_xaxes(gridcolor="#e8e8e8", zeroline=False)
    fig.update_yaxes(gridcolor="#e8e8e8", zeroline=False)
    return fig

def defn_box(title, content):
    st.markdown(f'<div class="defn-box"><div class="box-title">{title}</div><br>{content}</div>', unsafe_allow_html=True)

def example_box(title, content):
    st.markdown(f'<div class="example-box"><div class="box-title">{title}</div><br>{content}</div>', unsafe_allow_html=True)

def insight_box(content):
    st.markdown(f'<div class="insight-box"><div class="box-title">Key Insight</div><br>{content}</div>', unsafe_allow_html=True)

def formula_block(text):
    st.markdown(f'<div class="formula-box">{text}</div>', unsafe_allow_html=True)

def metric_card(label, value):
    return f'<div class="metric-card"><div class="value">{value}</div><div class="label">{label}</div></div>'

def colored_pipeline(steps_colors):
    """Render a colorful HTML pipeline. steps_colors = [(label, bg_color), ...]"""
    html = '<div class="pipeline-container">'
    for i, (label, color) in enumerate(steps_colors):
        html += f'<div class="pipeline-step" style="background:linear-gradient(135deg, {color}, {color}dd);">{label}</div>'
        if i < len(steps_colors) - 1:
            html += '<div class="pipeline-arrow">&#10148;</div>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

def render_qa_tab(qas, formulas, approach, advantages, limitations):
    """Render a complete Q&A / Learn tab.
    qas: list of (question, answer) tuples
    formulas: list of formula strings
    approach: string (when/how to use)
    advantages: list of strings
    limitations: list of strings
    """
    st.markdown("### Conceptual Q&A")
    for i, (q, a) in enumerate(qas):
        st.markdown(f'<div class="qa-card"><div class="qa-q">Q{i+1}. {q}</div><div class="qa-a">{a}</div></div>', unsafe_allow_html=True)

    if formulas:
        st.markdown("### Formula Reference")
        for f in formulas:
            formula_block(f)

    st.markdown("### When & How to Use")
    st.markdown(f'<div class="approach-box"><div class="al-title">Approach & Application</div><div class="al-item">{approach}</div></div>', unsafe_allow_html=True)

    st.markdown("### Advantages & Limitations")
    adv_html = "".join(f"<div class='al-item'>&#10004; {a}</div>" for a in advantages)
    lim_html = "".join(f"<div class='al-item'>&#10060; {l}</div>" for l in limitations)
    st.markdown(f"""<div class="adv-lim-container">
        <div class="adv-box"><div class="al-title">Advantages</div>{adv_html}</div>
        <div class="lim-box"><div class="al-title">Limitations</div>{lim_html}</div>
    </div>""", unsafe_allow_html=True)


# =============================================================================
# SIDEBAR
# =============================================================================
PAGES = [
    "Home",
    "1. Cleaning",
    "2. Standardize",
    "3. Aggregate",
    "4. Pivot",
    "5. Min-Max Scaling",
    "6. Z-Score Scaling",
    "7. Robust Scaling",
    "8. Log Transform",
    "9. Box-Cox Transform",
    "10. Categorize / Binning",
    "11. Categorical Encode",
    "12. Feature Engineering",
    "13. FreshMart Caselet",
    "14. Python Case Study",
]

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:1rem 0 0.5rem 0;">
        <div style="font-family:'Playfair Display',serif; font-size:1.5rem; font-weight:700; color:white; letter-spacing:1px;">
            THE MOUNTAIN PATH
        </div>
        <div style="color:#FFD700; font-size:0.95rem; margin-top:2px;">World of Finance</div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    page = st.radio("Navigate", PAGES, index=0)
    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; padding:0.5rem 0 0.2rem 0;">
        <div style="font-size:0.95rem; font-weight:600; color:white;">Prof. V. Ravichandran</div>
        <div style="margin-top:8px;">
            <a href="https://www.linkedin.com/in/trichyravis" target="_blank"
               style="display:inline-block; background:#0077B5; color:white !important; padding:4px 12px; border-radius:14px; font-size:0.78rem; font-weight:600; margin:3px; text-decoration:none;">
                LinkedIn
            </a>
            <a href="https://github.com/trichyravis" target="_blank"
               style="display:inline-block; background:#333; color:white !important; padding:4px 12px; border-radius:14px; font-size:0.78rem; font-weight:600; margin:3px; text-decoration:none;">
                GitHub
            </a>
        </div>
        <div style="margin-top:6px;">
            <a href="https://themountainpathacademy.com" target="_blank"
               style="color:#FFD700 !important; font-size:0.82rem; text-decoration:none;">
                themountainpathacademy.com
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# PAGE: HOME
# =============================================================================
if page == "Home":
    st.markdown("""
    <div class="mp-brand-header">
        <h1>THE MOUNTAIN PATH</h1>
        <div class="subtitle">World of Finance &mdash; Data Transformation for Data Analysis</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## What is Data Transformation?")
    defn_box("Definition", "Data transformation is the process of converting raw data into a cleaner, more useful shape so it can be analyzed. "
             "Examples include fixing typos, standardizing units, summarizing by group, reshaping rows into columns, scaling numbers, and bucketing values.")

    st.markdown("### Why is it Required?")
    cols = st.columns(5)
    icons = ["🧹", "📐", "📊", "🔄", "🔍"]
    reasons = [
        ("Messy Data", "Typos, blanks, and inconsistent formats break analysis."),
        ("Structure", "Charts, formulas, and ML need one row per observation."),
        ("Common Scale", "Comparisons require z-scores, percentages, or same units."),
        ("Summarization", "Decisions need summaries, not millions of raw rows."),
        ("Pattern Discovery", "Categorizing continuous values reveals hidden trends."),
    ]
    card_colors = [DARK_BLUE, TEAL, GOLD, PURPLE, ACCENT_GREEN]
    for c, icon, (title, desc), clr in zip(cols, icons, reasons, card_colors):
        with c:
            st.markdown(f"""
            <div class="metric-card" style="min-height:170px; border-top:4px solid {clr};">
                <div style="font-size:2rem;">{icon}</div>
                <div class="value" style="font-size:1rem; color:{clr}; margin-top:0.3rem;">{title}</div>
                <div class="label" style="margin-top:0.4rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### The Complete Transformation Pipeline")
    colored_pipeline([
        ("Raw\nData", "#999"),
        ("Clean", CORAL),
        ("Standardize", ORANGE),
        ("Aggregate", GOLD),
        ("Pivot", ACCENT_GREEN),
        ("Scale &\nNormalize", TEAL),
        ("Transform\n(Log/Box-Cox)", "#4A90D9"),
        ("Categorize\n& Encode", PURPLE),
        ("Feature\nEngineer", MID_BLUE),
        ("Analysis\nReady", DARK_BLUE),
    ])

    st.markdown("### All Transformations Covered")
    transform_data = pd.DataFrame({
        "Step": ["1. Cleaning", "2. Standardize", "3. Aggregate", "4. Pivot",
                 "5. Min-Max Scaling", "6. Z-Score Scaling", "7. Robust Scaling",
                 "8. Log Transform", "9. Box-Cox Transform",
                 "10. Binning / Discretization", "11. Categorical Encode", "12. Feature Engineering"],
        "What it does": [
            "Trim spaces, fix case, handle blanks",
            "Convert units and formats to a common scale",
            "Summarize many rows into per-group totals",
            "Reshape long data into wide comparison table",
            "Rescale numbers to 0-1 range",
            "Center to mean=0, std=1 (Gaussian scaling)",
            "Scale using median & IQR (outlier-resistant)",
            "Compress right-skewed distributions",
            "Optimal power transform toward normality",
            "Bucket continuous numbers into labeled groups",
            "Convert text categories to numbers (ordinal/one-hot)",
            "Create new predictive features from existing data",
        ],
        "Key Tool / Formula": [
            "TRIM, PROPER, IF",
            "IF (unit conversion), DATEVALUE",
            "SUMIF, COUNTIF, AVERAGEIF",
            "SUMIFS (row + column criteria)",
            "(x - min) / (max - min)",
            "(x - mean) / std",
            "(x - median) / IQR",
            "log(x) or log(1+x)",
            "scipy.stats.boxcox()",
            "Nested IF / IFS / pd.cut()",
            "MATCH / pd.get_dummies()",
            "Interaction, ratio, polynomial terms",
        ],
    })
    st.dataframe(transform_data, use_container_width=True, hide_index=True)

    insight_box("Each page in the sidebar covers <strong>one transformation</strong> with interactive charts, live sliders, before-and-after data, and the formulas that produce each result. The FreshMart Caselet ties everything together in an end-to-end exercise.")


# =============================================================================
# PAGE 1: CLEANING
# =============================================================================
elif page == "1. Cleaning":
    st.markdown("""<div class="mp-brand-header"><h1>1. Data Cleaning</h1>
    <div class="subtitle">Trim Spaces &bull; Fix Case &bull; Handle Blanks</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "The same name written 4 different ways (<code>' &nbsp;apple '</code>, <code>'APPLE'</code>, <code>'Apple'</code>, <code>' banana'</code>) cannot be grouped or counted until they match.")

    raw = pd.DataFrame({"Raw Name": ["  apple ", "APPLE", "Apple", " banana", "BANANA ", "(blank)", "cherry"], "Sales": [10, 15, 8, 7, 12, 5, 9]})
    cleaned = pd.DataFrame({"Cleaned Name": ["Apple","Apple","Apple","Banana","Banana","(missing)","Cherry"], "Sales": [10, 15, 8, 7, 12, 5, 9]})

    tab1, tab2, tab3, tab4 = st.tabs(["Before & After", "Interactive Chart", "Excel Formulas", "Q&A / Learn"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Raw Data"); st.dataframe(raw, use_container_width=True, hide_index=True)
        with c2:
            st.markdown("#### Cleaned Data"); st.dataframe(cleaned, use_container_width=True, hide_index=True)
        summary = pd.DataFrame({"Product": ["Apple", "Banana", "Cherry", "(missing)"], "Total Sales": [33, 19, 9, 5]})
        fig = go.Figure(go.Bar(x=summary["Product"], y=summary["Total Sales"], marker_color=[DARK_BLUE, GOLD, ACCENT_GREEN, "#ccc"], text=summary["Total Sales"], textposition="outside"))
        mp_layout(fig, "Sales After Cleaning & Grouping", 350); st.plotly_chart(fig, use_container_width=True)
    with tab2:
        fig2 = make_subplots(rows=1, cols=2, subplot_titles=("Without Cleaning (7 items)", "With Cleaning (4 groups)"))
        fig2.add_trace(go.Bar(x=["  apple ","APPLE","Apple"," banana","BANANA ","(blank)","cherry"], y=[10,15,8,7,12,5,9], marker_color=CORAL, name="Uncleaned"), row=1, col=1)
        fig2.add_trace(go.Bar(x=["Apple","Banana","Cherry","(missing)"], y=[33,19,9,5], marker_color=DARK_BLUE, name="Cleaned"), row=1, col=2)
        mp_layout(fig2, "", 380); fig2.update_layout(showlegend=False); st.plotly_chart(fig2, use_container_width=True)
        insight_box("Without cleaning, <strong>Apple appears as 3 separate items</strong>. After TRIM + PROPER, they merge into one group with <strong>33 total sales</strong>.")
    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block("=PROPER(TRIM(A2)) &mdash; removes spaces, capitalizes first letter")
        formula_block('=IF(A2="", "(missing)", PROPER(TRIM(A2))) &mdash; also flags blank cells')
        formula_block("=SUMIF(D:D, A13, E:E) &mdash; sum sales for each cleaned product")
        formula_block("=CLEAN(A2) &mdash; removes non-printable characters")
    with tab4:
        render_qa_tab(
            qas=[
                ("What is data cleaning?", "Data cleaning (or data cleansing) is the process of identifying and correcting errors, inconsistencies, and missing values in a dataset. It ensures data is accurate, consistent, and usable for analysis."),
                ("Why does '  apple ' and 'APPLE' cause problems?", "Excel and Python treat these as <strong>different values</strong> because of leading/trailing spaces and case differences. SUMIF, VLOOKUP, and groupby operations will fail to match them, resulting in fragmented counts and incorrect totals."),
                ("What does TRIM do vs CLEAN?", "<strong>TRIM</strong> removes leading/trailing spaces and collapses multiple internal spaces to one. <strong>CLEAN</strong> removes non-printable characters (ASCII 0-31) like line breaks, tabs, and control characters that are invisible but break matching."),
                ("How should missing values be handled?", "Options include: (1) Flag as '(missing)' or 'Unknown' for transparency, (2) Delete rows if few, (3) Impute with mean/median/mode, (4) Use forward/backward fill for time series. The best choice depends on the analysis goal and how much data is missing."),
                ("What is the difference between PROPER, UPPER, and LOWER?", "<strong>PROPER</strong> capitalizes the first letter of each word (apple &rarr; Apple). <strong>UPPER</strong> converts everything to uppercase. <strong>LOWER</strong> converts everything to lowercase. PROPER is best for names; UPPER/LOWER for case-insensitive matching."),
            ],
            formulas=["=TRIM(A2) &mdash; remove extra spaces", "=PROPER(A2) &mdash; capitalize first letter of each word",
                       "=CLEAN(A2) &mdash; remove non-printable characters", "=SUBSTITUTE(A2, CHAR(160), \" \") &mdash; remove non-breaking spaces"],
            approach="Apply cleaning as the <strong>first step</strong> in any data pipeline. Start with TRIM + PROPER/UPPER for text standardization, then handle blanks with IF, and finally verify with COUNTIF that duplicate variants have merged. In Python, use <code>str.strip()</code>, <code>str.title()</code>, and <code>fillna()</code>.",
            advantages=["Eliminates duplicate categories caused by inconsistent entry", "Enables accurate SUMIF, VLOOKUP, and groupby operations",
                        "Reduces noise and improves data quality for downstream analysis", "Simple to implement with built-in Excel/Python functions"],
            limitations=["Cannot fix semantic errors (e.g., 'Aple' typo for 'Apple')", "PROPER may not handle special names correctly (e.g., 'McDonald' becomes 'Mcdonald')",
                         "Blank handling strategy depends on context and may introduce bias", "Large datasets may need fuzzy matching (Levenshtein distance) beyond simple TRIM/PROPER"],
        )


# =============================================================================
# PAGE 2: STANDARDIZE
# =============================================================================
elif page == "2. Standardize":
    st.markdown("""<div class="mp-brand-header"><h1>2. Standardize</h1>
    <div class="subtitle">Convert Units &bull; Parse Dates &bull; Common Scale</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "Weights are mixed (lbs vs kg) and dates are stored as text. You cannot SUM or SORT until every value is on the same scale.")
    raw_std = pd.DataFrame({"Item": [f"Item {c}" for c in "ABCDE"], "Weight": [10,5,22,3,50], "Unit": ["lb","kg","lb","kg","lb"], "Date (text)": ["20240115","20240203","20240220","20240301","20240318"]})
    std = pd.DataFrame({"Item": [f"Item {c}" for c in "ABCDE"], "Weight (kg)": [4.536,5.000,9.979,3.000,22.680], "Real Date": ["2024-01-15","2024-02-03","2024-02-20","2024-03-01","2024-03-18"]})
    tab1, tab2, tab3, tab4 = st.tabs(["Data View", "Interactive Chart", "Excel Formulas", "Q&A / Learn"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1: st.markdown("#### Raw Data"); st.dataframe(raw_std, use_container_width=True, hide_index=True)
        with c2: st.markdown("#### Standardized"); st.dataframe(std, use_container_width=True, hide_index=True)
    with tab2:
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Original", x=raw_std["Item"], y=raw_std["Weight"], marker_color=ORANGE, text=[f"{w} {u}" for w,u in zip(raw_std["Weight"],raw_std["Unit"])], textposition="outside"))
        fig.add_trace(go.Bar(name="Standardized (kg)", x=std["Item"], y=std["Weight (kg)"], marker_color=DARK_BLUE, text=[f"{w:.1f} kg" for w in std["Weight (kg)"]], textposition="outside"))
        mp_layout(fig, "Weight Standardization", 400); fig.update_layout(barmode="group"); st.plotly_chart(fig, use_container_width=True)
        st.markdown(metric_card("Total Weight (now computable)", "45.20 kg"), unsafe_allow_html=True)
    with tab3:
        formula_block('=IF(C2="lb", B2*0.4536, B2) &mdash; converts lbs to kg')
        formula_block('=DATE(LEFT(D2,4), MID(D2,5,2), RIGHT(D2,2)) &mdash; parses text date')
        insight_box("Once standardized, you can SUM weights and SORT by date. Without it, neither works.")
    with tab4:
        render_qa_tab(
            qas=[
                ("Why is standardizing units essential before analysis?", "If weights are in mixed units (lbs and kg), SUM, AVERAGE, and comparisons produce meaningless results. Converting everything to a single unit ensures mathematical operations are valid."),
                ("How do you convert pounds to kilograms?", "Multiply by 0.4536. In Excel: =IF(C2=\"lb\", B2*0.4536, B2). This conditionally converts only the rows that are in pounds."),
                ("Why do text dates need conversion?", "Text dates like '20240115' cannot be sorted chronologically or used in date arithmetic (e.g., calculating days between orders). Parsing them to real dates enables SORT, DATEDIF, and timeline charts."),
                ("What is the difference between standardization and normalization?", "Standardization typically refers to making units consistent (same scale/unit). Normalization (like min-max) rescales values to a fixed range. Both prepare data for analysis but serve different purposes."),
                ("Can standardization introduce errors?", "Yes — using wrong conversion factors, truncating decimal places, or applying conversions to already-converted values can introduce systematic errors. Always validate with known reference values."),
            ],
            formulas=[
                '=IF(C2="lb", B2*0.4536, B2) — conditional unit conversion',
                "=DATE(LEFT(D2,4), MID(D2,5,2), RIGHT(D2,2)) — text to date parsing",
                "=CONVERT(B2, \"lbm\", \"kg\") — Excel's built-in CONVERT function",
            ],
            approach="Use standardization whenever your dataset mixes units (currencies, weights, distances, temperatures) or formats (date strings, number-as-text). Apply conversion factors first, then validate totals against known benchmarks before proceeding with analysis.",
            advantages=["Enables valid mathematical operations (SUM, AVERAGE, comparisons)", "Makes data sortable and filterable on a consistent basis", "Prevents misleading charts where mixed units distort visual comparisons", "Prerequisite for downstream transformations like scaling and aggregation"],
            limitations=["Conversion factors must be accurate and up to date (e.g., exchange rates change daily)", "Rounding during conversion can introduce small cumulative errors", "Original units are lost unless preserved in a separate column", "Some conversions are context-dependent (e.g., fiscal year vs calendar year)"],
        )


# =============================================================================
# PAGE 3: AGGREGATE
# =============================================================================
elif page == "3. Aggregate":
    st.markdown("""<div class="mp-brand-header"><h1>3. Aggregate</h1>
    <div class="subtitle">SUMIF &bull; COUNTIF &bull; AVERAGEIF</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "10 individual sales rows tell us little. Aggregate into per-group summaries to see which region leads.")
    raw_agg = pd.DataFrame({"Order": [f"Order {i}" for i in range(1,11)], "Region": ["North","South","North","East","South","West","North","East","West","South"], "Sales": [120,90,75,200,60,150,95,110,80,130]})
    agg = pd.DataFrame({"Region": ["North","South","East","West"], "Total Sales": [290,280,310,230], "Order Count": [3,3,2,2], "Avg Order": [96.67,93.33,155.00,115.00]})
    tab1, tab2, tab3, tab4 = st.tabs(["Data View", "Interactive Charts", "Excel Formulas", "Q&A / Learn"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1: st.markdown("#### Raw (10 orders)"); st.dataframe(raw_agg, use_container_width=True, hide_index=True)
        with c2: st.markdown("#### Aggregated"); st.dataframe(agg, use_container_width=True, hide_index=True)
    with tab2:
        chart_type = st.selectbox("Chart type", ["Bar Chart", "Pie Chart", "Treemap"], key="agg_chart")
        if chart_type == "Bar Chart":
            fig = go.Figure()
            fig.add_trace(go.Bar(x=agg["Region"], y=agg["Total Sales"], name="Total Sales", marker_color=DARK_BLUE, text=agg["Total Sales"], textposition="outside"))
            fig.add_trace(go.Bar(x=agg["Region"], y=agg["Avg Order"], name="Avg Order", marker_color=GOLD, text=[f"${v:.0f}" for v in agg["Avg Order"]], textposition="outside"))
            mp_layout(fig, "Regional Sales Summary", 400); fig.update_layout(barmode="group")
        elif chart_type == "Pie Chart":
            fig = px.pie(agg, values="Total Sales", names="Region", color_discrete_sequence=[DARK_BLUE, GOLD, ACCENT_GREEN, TEAL])
            mp_layout(fig, "Sales Distribution by Region", 400)
        else:
            fig = px.treemap(agg, path=["Region"], values="Total Sales", color="Total Sales", color_continuous_scale=[[0, LIGHT_BLUE],[1, DARK_BLUE]])
            mp_layout(fig, "Sales Treemap", 400)
        st.plotly_chart(fig, use_container_width=True)
        cols = st.columns(4)
        for c, (_, r) in zip(cols, agg.iterrows()):
            with c: st.markdown(metric_card(f"{r['Region']} ({r['Order Count']} orders)", f"${r['Total Sales']:,.0f}"), unsafe_allow_html=True)
    with tab3:
        formula_block("=SUMIF(B:B, E3, C:C) &mdash; total sales for a region")
        formula_block("=COUNTIF(B:B, E3) &mdash; order count")
        formula_block("=AVERAGEIF(B:B, E3, C:C) &mdash; average order value")
        insight_box("<strong>Grand Total check:</strong> 290+280+310+230 = <strong>1,110</strong>, matching sum of all 10 orders.")
    with tab4:
        render_qa_tab(
            qas=[
                ("What is aggregation and why is it needed?", "Aggregation collapses many rows into summary rows using functions like SUM, COUNT, and AVERAGE. Raw transactional data (one row per order) is too granular for decision-making — managers need totals by region, product, or time period."),
                ("What is the difference between SUMIF and SUMIFS?", "SUMIF applies a single condition (e.g., sum sales where Region='North'). SUMIFS supports multiple conditions (e.g., sum sales where Region='North' AND Product='Apples'). SUMIFS is more versatile."),
                ("How does GROUP BY work in Python vs Excel?", "In Python: df.groupby('Region')['Sales'].sum(). In Excel: SUMIF/COUNTIF or Pivot Tables. Both produce the same result — collapsing rows by a grouping key and applying an aggregate function."),
                ("When should you use AVERAGEIF instead of a simple AVERAGE?", "Use AVERAGEIF when you need the average for a specific subset (e.g., average order value for the North region only). A simple AVERAGE would include all regions indiscriminately."),
                ("How do you verify aggregation results?", "Cross-check the grand total: sum of all aggregated group totals should equal the sum of all original rows. If they don't match, a row was missed or double-counted."),
            ],
            formulas=[
                "=SUMIF(range, criteria, sum_range) — sum values matching one condition",
                "=COUNTIF(range, criteria) — count rows matching a condition",
                "=AVERAGEIF(range, criteria, avg_range) — average values matching one condition",
                "Python: df.groupby('col').agg(Total=('Sales','sum'), Count=('Sales','count'))",
            ],
            approach="Use aggregation when raw data has too many rows for meaningful comparison. Group by the dimension of interest (region, product, time period), apply the appropriate aggregate function, and always validate with a grand-total cross-check.",
            advantages=["Reduces data volume from thousands of rows to manageable summaries", "Reveals patterns invisible in row-level data (which region leads?)", "Enables KPI calculation (average order value, conversion rate)", "Foundation for dashboards, reports, and executive summaries"],
            limitations=["Loses individual record detail (can't see which specific order was largest)", "Choice of grouping key affects the story (monthly vs quarterly gives different insights)", "Outliers get hidden inside averages — consider using median alongside mean", "Multi-level aggregation can be complex (region > product > month)"],
        )


# =============================================================================
# PAGE 4: PIVOT
# =============================================================================
elif page == "4. Pivot":
    st.markdown("""<div class="mp-brand-header"><h1>4. Pivot</h1>
    <div class="subtitle">Reshape Long Data &rarr; Wide Comparison Table</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "Data in <strong>long</strong> form (1 row per region-quarter = 12 rows). Reshape <strong>wide</strong> so each quarter is a column.")
    long_data = pd.DataFrame({"Region": ["North"]*4+["South"]*4+["East"]*4, "Quarter": ["Q1","Q2","Q3","Q4"]*3, "Sales": [100,120,130,150,80,95,110,125,60,70,90,105]})
    wide_data = pd.DataFrame({"Region": ["North","South","East"], "Q1": [100,80,60], "Q2": [120,95,70], "Q3": [130,110,90], "Q4": [150,125,105]})
    wide_data["Total"] = wide_data[["Q1","Q2","Q3","Q4"]].sum(axis=1)
    tab1, tab2, tab3, tab4 = st.tabs(["Data View", "Interactive Heatmap", "Excel Formulas", "Q&A / Learn"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1: st.markdown("#### Long (12 rows)"); st.dataframe(long_data, use_container_width=True, hide_index=True)
        with c2: st.markdown("#### Wide (3 rows)"); st.dataframe(wide_data, use_container_width=True, hide_index=True)
    with tab2:
        view = st.radio("View", ["Heatmap", "Grouped Bars", "Line Trend"], horizontal=True, key="pv")
        if view == "Heatmap":
            z = [wide_data.loc[i, ["Q1","Q2","Q3","Q4"]].tolist() for i in range(3)]
            fig = go.Figure(go.Heatmap(z=z, x=["Q1","Q2","Q3","Q4"], y=["North","South","East"], colorscale=[[0,LIGHT_BLUE],[0.5,"#4A90D9"],[1,DARK_BLUE]], text=z, texttemplate="%{text}", textfont=dict(size=16, color="white")))
            mp_layout(fig, "Sales Heatmap", 350)
        elif view == "Grouped Bars":
            fig = go.Figure()
            for q, clr in zip(["Q1","Q2","Q3","Q4"],[DARK_BLUE, GOLD, ACCENT_GREEN, ORANGE]):
                fig.add_trace(go.Bar(name=q, x=wide_data["Region"], y=wide_data[q], text=wide_data[q], textposition="outside", marker_color=clr))
            mp_layout(fig, "Quarterly Sales by Region", 400); fig.update_layout(barmode="group")
        else:
            fig = go.Figure()
            for i, (region, clr) in enumerate(zip(["North","South","East"],[DARK_BLUE, GOLD, ACCENT_GREEN])):
                vals = wide_data[wide_data["Region"]==region][["Q1","Q2","Q3","Q4"]].values[0]
                fig.add_trace(go.Scatter(x=["Q1","Q2","Q3","Q4"], y=vals, mode="lines+markers", name=region, line=dict(width=3, color=clr), marker=dict(size=10)))
            mp_layout(fig, "Quarterly Trend", 400)
        st.plotly_chart(fig, use_container_width=True)
    with tab3:
        formula_block('=SUMIFS(C:C, A:A, E4, B:B, F3) &mdash; Region=row AND Quarter=column')
        example_box("How SUMIFS Pivots", "<code>=SUMIFS($C$4:$C$15, $A$4:$A$15, $E4, $B$4:$B$15, F$3)</code><br>Mixed references let you copy across the grid.")
    with tab4:
        render_qa_tab(
            qas=[
                ("What is pivoting and how does it differ from aggregation?", "Pivoting reshapes data from long format (one row per observation) to wide format (categories become columns). It combines aggregation with restructuring — not just summarizing, but reorganizing the layout for easier comparison."),
                ("When should you use a Pivot Table vs SUMIFS?", "Pivot Tables are interactive and auto-update when data changes — ideal for exploration. SUMIFS formulas are better when you need a fixed layout in a report or when building a dashboard that feeds other calculations."),
                ("What are the components of a pivot operation?", "Three components: (1) Index — what becomes the rows (e.g., Region), (2) Columns — what becomes the column headers (e.g., Quarter), (3) Values — what gets aggregated in each cell (e.g., SUM of Sales)."),
                ("How does pd.pivot_table() work in Python?", "pd.pivot_table(df, values='Sales', index='Region', columns='Quarter', aggfunc='sum') produces the same result as an Excel Pivot Table — rows are regions, columns are quarters, cells are summed sales."),
                ("What happens with missing combinations in a pivot?", "If a region had no sales in a quarter, the cell shows NaN (or 0 with fill_value=0). This is important — missing data may indicate a real gap or a data collection issue."),
            ],
            formulas=[
                "=SUMIFS(values, row_criteria_range, row_value, col_criteria_range, col_value)",
                "Python: pd.pivot_table(df, values='Sales', index='Region', columns='Quarter', aggfunc='sum')",
                "Python: df.pivot(index='Region', columns='Quarter', values='Sales') — no aggregation, requires unique combinations",
            ],
            approach="Use pivoting when you need cross-tabulation: comparing one dimension (rows) against another (columns). Start with long-format data, identify the row key, column key, and value to aggregate, then reshape. Always add row/column totals for validation.",
            advantages=["Makes comparison across two dimensions intuitive (region x quarter)", "Compresses many rows into a compact, readable grid", "Enables heatmap visualization for spotting patterns at a glance", "Foundation for executive dashboards and summary reports"],
            limitations=["Wide tables become unwieldy with many categories (50 products x 12 months = 600 cells)", "Assumes a meaningful two-dimensional relationship exists", "Unpivoting (melting) back to long format is needed for certain analyses", "Duplicate index-column combinations require an aggregate function to resolve"],
        )


# =============================================================================
# PAGE 5: MIN-MAX SCALING
# =============================================================================
elif page == "5. Min-Max Scaling":
    st.markdown("""<div class="mp-brand-header"><h1>5. Min-Max Scaling</h1>
    <div class="subtitle">Rescale to [0, 1] &bull; Compare Shape Across Series</div></div>""", unsafe_allow_html=True)
    defn_box("What is Min-Max Scaling?", "Transforms every value to a <strong>0&ndash;1</strong> range using:<br><code>x_scaled = (x &minus; x_min) / (x_max &minus; x_min)</code><br>The minimum becomes 0, the maximum becomes 1, everything else scales linearly in between.")

    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    sales = [1200,950,1500,800,2200,2800,1700]; items = [18,14,22,11,30,38,25]
    s_min, s_max = min(sales), max(sales); i_min, i_max = min(items), max(items)
    sales_norm = [(v-s_min)/(s_max-s_min) for v in sales]; items_norm = [(v-i_min)/(i_max-i_min) for v in items]

    tab1, tab2, tab3, tab4 = st.tabs(["Raw vs Scaled", "Live Explorer", "Formula", "Q&A / Learn"])
    with tab1:
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Raw (different scales)", "Min-Max Scaled (0-1)"))
        fig.add_trace(go.Bar(x=days, y=sales, name="Sales ($)", marker_color=DARK_BLUE), row=1, col=1)
        fig.add_trace(go.Bar(x=days, y=items, name="Items Sold", marker_color=GOLD), row=1, col=1)
        fig.add_trace(go.Scatter(x=days, y=sales_norm, name="Sales (scaled)", line=dict(color=DARK_BLUE, width=3), mode="lines+markers"), row=1, col=2)
        fig.add_trace(go.Scatter(x=days, y=items_norm, name="Items (scaled)", line=dict(color=GOLD, width=3), mode="lines+markers"), row=1, col=2)
        mp_layout(fig, "", 400); st.plotly_chart(fig, use_container_width=True)
        insight_box("On the raw chart, Items Sold is invisible next to Sales. After min-max scaling, both are on 0&ndash;1 and follow <strong>the same pattern</strong>, peaking Saturday.")
    with tab2:
        st.markdown("#### Adjust Sales and Watch Normalization Live")
        edit_cols = st.columns(7); new_sales = []
        for i, (d, s) in enumerate(zip(days, sales)):
            with edit_cols[i]: new_sales.append(st.number_input(d, value=s, step=100, key=f"mm_{i}"))
        ns_min, ns_max = min(new_sales), max(new_sales)
        new_norm = [(v-ns_min)/(ns_max-ns_min) if ns_max > ns_min else 0 for v in new_sales]
        fig3 = go.Figure(go.Bar(x=days, y=new_norm, marker=dict(color=new_norm, colorscale=[[0,TEAL],[0.5,GOLD],[1,CORAL]]), text=[f"{v:.2f}" for v in new_norm], textposition="outside"))
        mp_layout(fig3, "Your Min-Max Scaled Values", 350); fig3.update_yaxes(range=[0,1.15]); st.plotly_chart(fig3, use_container_width=True)
    with tab3:
        formula_block("x_scaled = (x &minus; min) / (max &minus; min)")
        formula_block("Excel: =(B2 - MIN($B$2:$B$8)) / (MAX($B$2:$B$8) - MIN($B$2:$B$8))")
        formula_block("Python: from sklearn.preprocessing import MinMaxScaler")
        example_box("Worked Example", f"Monday = $1,200 &nbsp; Min=${s_min:,} &nbsp; Max=${s_max:,}<br>Scaled = (1200&minus;{s_min})/({s_max}&minus;{s_min}) = <strong>{(1200-s_min)/(s_max-s_min):.3f}</strong>")
    with tab4:
        render_qa_tab(
            qas=[
                ("Why do we need to scale features to [0, 1]?", "Many ML algorithms (neural networks, KNN, SVM) use distance metrics. If one feature ranges 0–100 and another 0–1,000,000, the larger feature dominates. Min-max scaling puts all features on equal footing."),
                ("What happens to outliers under min-max scaling?", "Outliers compress the rest of the data into a narrow band. If max=1,000,000 and most values are under 100, all non-outlier values will cluster near 0. This is why min-max is sensitive to outliers."),
                ("Can you scale to a range other than [0, 1]?", "Yes. The general formula is: x_scaled = (x - min) / (max - min) * (new_max - new_min) + new_min. sklearn's MinMaxScaler accepts a feature_range parameter, e.g., feature_range=(0, 10)."),
                ("How do you apply min-max scaling to new/test data?", "Use the min and max from the training set, not the test set. In sklearn: fit on train, then transform both train and test. This prevents data leakage — the model should not 'see' test data statistics."),
                ("Is min-max scaling reversible?", "Yes. x_original = x_scaled * (max - min) + min. This is called inverse transformation and is useful when you need to interpret predictions back in the original scale."),
            ],
            formulas=[
                "x_scaled = (x − x_min) / (x_max − x_min) — basic 0-to-1 scaling",
                "x_scaled = (x − min) / (max − min) × (b − a) + a — scale to [a, b]",
                "Excel: =(B2 - MIN($B:$B)) / (MAX($B:$B) - MIN($B:$B))",
                "Python: MinMaxScaler(feature_range=(0,1)).fit_transform(X)",
            ],
            approach="Apply min-max scaling when all features need to be on the same [0,1] scale, especially for distance-based algorithms and neural networks. Check for outliers first — if present, consider robust scaling instead. Always fit on training data only.",
            advantages=["Preserves the original distribution shape exactly", "Bounded output [0,1] is interpretable and compatible with neural network activations", "Simple, fast, and easy to explain to stakeholders", "Reversible — can recover original values via inverse transform"],
            limitations=["Highly sensitive to outliers — a single extreme value compresses all others", "New data outside the training range maps to values outside [0,1]", "Does not center the data around zero (unlike z-score)", "Not suitable when the distribution has extreme skew — log transform first"],
        )


# =============================================================================
# PAGE 6: Z-SCORE (STANDARDIZATION)
# =============================================================================
elif page == "6. Z-Score Scaling":
    st.markdown("""<div class="mp-brand-header"><h1>6. Z-Score Standardization</h1>
    <div class="subtitle">Center to Mean = 0 &bull; Std Dev = 1</div></div>""", unsafe_allow_html=True)
    defn_box("What is Z-Score Scaling?", "Transforms data so <strong>mean = 0</strong> and <strong>std = 1</strong>:<br><code>z = (x &minus; &mu;) / &sigma;</code><br>"
             "A z-score of +2 means the value is 2 standard deviations above the mean. Unlike min-max, z-scores have <strong>no fixed range</strong> and are less affected by outliers.")

    np.random.seed(42)
    data = np.array([45, 50, 55, 48, 52, 200, 47, 51, 49, 53])  # 200 is outlier
    labels = [f"Obs {i+1}" for i in range(len(data))]
    mean_v, std_v = data.mean(), data.std()
    z_scores = (data - mean_v) / std_v

    tab1, tab2, tab3 = st.tabs(["Visualization", "Formula & Comparison", "Q&A / Learn"])
    with tab1:
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Original Data (note outlier)", "Z-Scores (standardized)"))
        fig.add_trace(go.Bar(x=labels, y=data, marker_color=[CORAL if v > 100 else DARK_BLUE for v in data], text=data, textposition="outside"), row=1, col=1)
        fig.add_trace(go.Bar(x=labels, y=z_scores, marker_color=[CORAL if abs(z) > 2 else TEAL for z in z_scores], text=[f"{z:.2f}" for z in z_scores], textposition="outside"), row=1, col=2)
        fig.add_hline(y=0, line_dash="dash", line_color=GOLD, row=1, col=2)
        fig.add_hline(y=2, line_dash="dot", line_color=CORAL, row=1, col=2, annotation_text="+2σ")
        fig.add_hline(y=-2, line_dash="dot", line_color=CORAL, row=1, col=2, annotation_text="-2σ")
        mp_layout(fig, "", 420); st.plotly_chart(fig, use_container_width=True)

        cols = st.columns(3)
        with cols[0]: st.markdown(metric_card("Mean (μ)", f"{mean_v:.1f}"), unsafe_allow_html=True)
        with cols[1]: st.markdown(metric_card("Std Dev (σ)", f"{std_v:.1f}"), unsafe_allow_html=True)
        with cols[2]: st.markdown(metric_card("Outlier Z-score", f"{z_scores[5]:.2f}"), unsafe_allow_html=True)
        insight_box(f"Observation 6 (value=200) has a z-score of <strong>{z_scores[5]:.2f}</strong>, flagging it as an extreme outlier (&gt;2σ). All other values cluster near zero.")

    with tab2:
        formula_block("z = (x &minus; mean) / std_dev")
        formula_block("Excel: =(B2 - AVERAGE($B$2:$B$11)) / STDEV($B$2:$B$11)")
        formula_block("Python: from sklearn.preprocessing import StandardScaler")
        st.markdown("#### Min-Max vs Z-Score: When to Use Which?")
        comp = pd.DataFrame({
            "Feature": ["Output range", "Effect of outliers", "Preserves shape", "Best for"],
            "Min-Max": ["[0, 1]", "Compressed by outliers", "Yes", "Neural networks, image pixels"],
            "Z-Score": ["Unbounded", "Less affected", "Yes", "Linear models, outlier detection"],
        })
        st.dataframe(comp, use_container_width=True, hide_index=True)
    with tab3:
        render_qa_tab(
            qas=[
                ("What does a z-score of +2.5 tell you?", "The value is 2.5 standard deviations above the mean. Under a normal distribution, only ~0.6% of values exceed +2.5σ, making it a potential outlier worth investigating."),
                ("Why does z-score standardization center data at zero?", "Subtracting the mean shifts the distribution so its center is at 0. Dividing by standard deviation scales it so one unit = one σ. This makes different features directly comparable regardless of their original scales."),
                ("When should you choose z-score over min-max?", "Choose z-score when: (1) data has outliers (z-score is less distorted), (2) you need unbounded output (regression, PCA), (3) the algorithm assumes normally distributed features (linear regression, LDA)."),
                ("How does z-score help in outlier detection?", "Values with |z| > 2 or |z| > 3 are flagged as outliers. This provides a statistical threshold rather than an arbitrary cutoff. The 68-95-99.7 rule gives clear probabilistic interpretation."),
                ("Is z-score affected by sample size?", "Yes. With small samples, mean and std are less stable, making z-scores less reliable. With very small datasets (<30 observations), consider using robust scaling with median/IQR instead."),
            ],
            formulas=[
                "z = (x − μ) / σ — standard z-score formula",
                "Excel: =(B2 - AVERAGE($B$2:$B$N)) / STDEV($B$2:$B$N)",
                "Python: StandardScaler().fit_transform(X)",
                "68-95-99.7 rule: 68% within ±1σ, 95% within ±2σ, 99.7% within ±3σ",
            ],
            approach="Use z-score standardization when features have different units or scales and you need mean-centered, unit-variance data. Fit the scaler on training data only to avoid data leakage. Check that the result has mean ≈ 0 and std ≈ 1 as validation.",
            advantages=["Less sensitive to outliers than min-max (outliers don't compress all other values)", "Output is unbounded — no artificial clipping of extreme values", "Directly interpretable: z=2 means '2 standard deviations above average'", "Preserves the shape of the original distribution"],
            limitations=["Assumes the mean and std are meaningful — fails for highly skewed data", "No fixed output range — can't guarantee values fall in [0,1]", "Sensitive to the sample used for computing mean and std", "Not suitable for sparse data where most values are zero"],
        )


# =============================================================================
# PAGE 7: ROBUST SCALING
# =============================================================================
elif page == "7. Robust Scaling":
    st.markdown("""<div class="mp-brand-header"><h1>7. Robust Scaling</h1>
    <div class="subtitle">Median &bull; IQR &bull; Outlier-Resistant</div></div>""", unsafe_allow_html=True)
    defn_box("What is Robust Scaling?", "Uses <strong>median</strong> and <strong>IQR</strong> (interquartile range) instead of mean and std:<br>"
             "<code>x_robust = (x &minus; median) / IQR</code><br>Because median and IQR ignore extreme values, this scaler works well when your data has <strong>significant outliers</strong>.")

    data = np.array([45, 50, 55, 48, 52, 200, 47, 51, 49, 53])
    labels = [f"Obs {i+1}" for i in range(len(data))]
    med = np.median(data); q1, q3 = np.percentile(data, 25), np.percentile(data, 75); iqr = q3 - q1
    robust = (data - med) / iqr
    z_scores = (data - data.mean()) / data.std()
    mm = (data - data.min()) / (data.max() - data.min())

    tab1, tab2, tab3 = st.tabs(["Comparison of 3 Scalers", "Formula", "Q&A / Learn"])
    with tab1:
        fig = make_subplots(rows=1, cols=3, subplot_titles=("Min-Max", "Z-Score", "Robust"))
        fig.add_trace(go.Bar(x=labels, y=mm, marker_color=[CORAL if v>0.9 else TEAL for v in mm]), row=1, col=1)
        fig.add_trace(go.Bar(x=labels, y=z_scores, marker_color=[CORAL if abs(v)>2 else GOLD for v in z_scores]), row=1, col=2)
        fig.add_trace(go.Bar(x=labels, y=robust, marker_color=[CORAL if abs(v)>3 else DARK_BLUE for v in robust]), row=1, col=3)
        mp_layout(fig, "Same Data, Three Scalers (Obs 6 = outlier at 200)", 420); st.plotly_chart(fig, use_container_width=True)

        cols = st.columns(4)
        with cols[0]: st.markdown(metric_card("Median", f"{med:.1f}"), unsafe_allow_html=True)
        with cols[1]: st.markdown(metric_card("Q1 (25th)", f"{q1:.1f}"), unsafe_allow_html=True)
        with cols[2]: st.markdown(metric_card("Q3 (75th)", f"{q3:.1f}"), unsafe_allow_html=True)
        with cols[3]: st.markdown(metric_card("IQR", f"{iqr:.1f}"), unsafe_allow_html=True)

        insight_box("With Robust Scaling, the non-outlier observations cluster tightly around 0, and only the outlier (200) stands far out. Min-Max squashes everything to make room for the outlier.")

    with tab2:
        formula_block("x_robust = (x &minus; median) / IQR &nbsp;&nbsp;where IQR = Q3 &minus; Q1")
        formula_block("Excel: =(B2 - MEDIAN($B$2:$B$11)) / (PERCENTILE($B$2:$B$11, 0.75) - PERCENTILE($B$2:$B$11, 0.25))")
        formula_block("Python: from sklearn.preprocessing import RobustScaler")
    with tab3:
        render_qa_tab(
            qas=[
                ("Why use median and IQR instead of mean and std?", "Median and IQR are resistant to outliers. The mean is pulled toward extreme values, and std inflates when outliers are present. Robust scaling ensures the majority of data is well-scaled regardless of a few extreme points."),
                ("What is IQR and how is it calculated?", "IQR (Interquartile Range) = Q3 − Q1, where Q1 is the 25th percentile and Q3 is the 75th percentile. It captures the spread of the middle 50% of data, ignoring the tails where outliers live."),
                ("How does robust scaling compare to z-score on data with outliers?", "With outliers, z-score compresses the central data because the inflated std reduces all z-scores. Robust scaling keeps the central data well-spread around 0, and only the outlier gets a large scaled value."),
                ("When is robust scaling NOT the best choice?", "When data is clean (no outliers), z-score or min-max may be preferable as they use all information. Robust scaling ignores the tails by design, which wastes information in well-behaved datasets."),
                ("Can you use robust scaling with other quantile ranges?", "Yes. sklearn's RobustScaler accepts quantile_range parameter (default 25.0–75.0). Using a wider range like 10–90 includes more data; a narrower range like 30–70 is even more outlier-resistant."),
            ],
            formulas=[
                "x_robust = (x − median) / IQR, where IQR = Q3 − Q1",
                "Excel: =(B2 - MEDIAN($B:$B)) / (PERCENTILE($B:$B, 0.75) - PERCENTILE($B:$B, 0.25))",
                "Python: RobustScaler(quantile_range=(25.0, 75.0)).fit_transform(X)",
            ],
            approach="Choose robust scaling when your data contains significant outliers that would distort mean-based methods. It is the default recommendation for financial data (income, transaction amounts) and sensor data where extreme readings are common but shouldn't dominate the scaling.",
            advantages=["Immune to outliers — median and IQR are not affected by extreme values", "Central data (middle 50%) is well-scaled and interpretable", "Works well for financial data where heavy tails are expected", "Compatible with all sklearn pipeline workflows"],
            limitations=["Does not produce bounded output — no guaranteed [0,1] range", "Ignores information in the tails of the distribution", "Less intuitive than z-score (no direct probabilistic interpretation like ±2σ)", "Not suitable when the data is already clean and normally distributed"],
        )


# =============================================================================
# PAGE 8: LOG TRANSFORM
# =============================================================================
elif page == "8. Log Transform":
    st.markdown("""<div class="mp-brand-header"><h1>8. Log Transformation</h1>
    <div class="subtitle">Handling Skewed Data &bull; Compress Large Values</div></div>""", unsafe_allow_html=True)
    defn_box("What is Log Transformation?", "Applies <code>log(x)</code> or <code>log(1+x)</code> to compress right-skewed distributions. "
             "Large values get pulled in, small values spread out, making the distribution closer to <strong>normal</strong>. Essential when data spans multiple orders of magnitude (income, population, stock prices).")

    np.random.seed(42)
    skewed = np.random.exponential(scale=5000, size=500)
    log_transformed = np.log1p(skewed)

    tab1, tab2, tab3, tab4 = st.tabs(["Before & After", "Live Explorer", "Formula & Use Cases", "Q&A / Learn"])
    with tab1:
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Original (Right-Skewed)", "After log(1+x)"))
        fig.add_trace(go.Histogram(x=skewed, nbinsx=40, marker_color=CORAL, opacity=0.8, name="Original"), row=1, col=1)
        fig.add_trace(go.Histogram(x=log_transformed, nbinsx=40, marker_color=ACCENT_GREEN, opacity=0.8, name="Log-transformed"), row=1, col=2)
        mp_layout(fig, "Log Transform Tames Right Skew", 400); st.plotly_chart(fig, use_container_width=True)

        cols = st.columns(4)
        with cols[0]: st.markdown(metric_card("Original Skew", f"{pd.Series(skewed).skew():.2f}"), unsafe_allow_html=True)
        with cols[1]: st.markdown(metric_card("Log Skew", f"{pd.Series(log_transformed).skew():.2f}"), unsafe_allow_html=True)
        with cols[2]: st.markdown(metric_card("Original Range", f"{skewed.min():.0f} - {skewed.max():.0f}"), unsafe_allow_html=True)
        with cols[3]: st.markdown(metric_card("Log Range", f"{log_transformed.min():.1f} - {log_transformed.max():.1f}"), unsafe_allow_html=True)

    with tab2:
        st.markdown("#### See How Log Compresses Values")
        x_vals = np.linspace(0.1, 1000, 200)
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=x_vals, y=x_vals, name="y = x (linear)", line=dict(color=CORAL, width=2, dash="dash")))
        fig2.add_trace(go.Scatter(x=x_vals, y=np.log(x_vals), name="y = ln(x)", line=dict(color=DARK_BLUE, width=3)))
        fig2.add_trace(go.Scatter(x=x_vals, y=np.log10(x_vals), name="y = log10(x)", line=dict(color=GOLD, width=3)))
        fig2.add_trace(go.Scatter(x=x_vals, y=np.log1p(x_vals), name="y = ln(1+x)", line=dict(color=ACCENT_GREEN, width=3)))
        mp_layout(fig2, "Logarithmic Functions Compress Large Values", 420); st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        formula_block("log(x) &mdash; natural log (x must be > 0)")
        formula_block("log(1+x) &mdash; safe for zeros (log1p)")
        formula_block("log10(x) &mdash; base-10 log (orders of magnitude)")
        formula_block("Excel: =LN(B2)  or  =LN(1+B2)  or  =LOG10(B2)")
        formula_block("Python: np.log1p(x)  or  np.log(x)")
        example_box("Common Use Cases",
                     "&#8226; <strong>Income data:</strong> most earn $50K, a few earn $10M &rarr; log compresses the tail<br>"
                     "&#8226; <strong>Stock returns:</strong> log returns are additive across periods<br>"
                     "&#8226; <strong>Population:</strong> varies from 1K to 1B &rarr; log makes comparisons possible<br>"
                     "&#8226; <strong>Regression:</strong> log-linear models capture diminishing returns")
    with tab4:
        render_qa_tab(
            qas=[
                ("Why does log transformation reduce right skew?", "Log compresses large values more than small values. A value of 1,000 becomes ~6.9 (ln), while 10 becomes ~2.3. This pulls in the long right tail, making the distribution more symmetric and closer to normal."),
                ("What is the difference between log(x) and log1p(x)?", "log(x) is undefined for x=0 and negative for 0<x<1. log1p(x) = log(1+x) handles zeros safely (log1p(0) = 0) and is preferred when data contains zeros, which is common in count data."),
                ("When should you NOT use a log transform?", "Avoid log transforms when: (1) data is already normally distributed, (2) data contains negative values (log is undefined), (3) the relationship is truly linear (log distorts it), (4) interpretability in original units is critical."),
                ("How do you interpret coefficients in a log-linear regression?", "In ln(Y) = a + bX, a 1-unit increase in X leads to approximately b×100% change in Y. For example, b=0.05 means a 1-unit increase in X increases Y by about 5%. This captures diminishing returns naturally."),
                ("What base of logarithm should you use?", "For data transformation, natural log (ln) is standard. For interpretability with orders of magnitude, log10 is better (each unit = 10× increase). log2 is used in information theory. The choice doesn't affect the shape — only the scale."),
            ],
            formulas=[
                "ln(x) — natural log, base e ≈ 2.718",
                "log1p(x) = ln(1 + x) — safe for zeros",
                "log10(x) — base-10 log, each unit = one order of magnitude",
                "Inverse: exp(y) recovers original value from ln(x)",
            ],
            approach="Apply log transformation when data is right-skewed (skewness > 1) or spans multiple orders of magnitude. Check that all values are positive (or use log1p for zeros). After transforming, verify skewness reduction and visual normality with a histogram or Q-Q plot.",
            advantages=["Effectively reduces right skewness toward normality", "Handles data spanning orders of magnitude (income, population)", "Log returns are additive — essential for financial time series", "Stabilizes variance (heteroscedasticity) in regression models"],
            limitations=["Cannot handle negative values (log is undefined for x ≤ 0)", "Not effective for left-skewed or bimodal distributions", "Interpretation requires back-transformation (exponentiation) for stakeholders", "Over-compresses data if the original distribution is only mildly skewed"],
        )


# =============================================================================
# PAGE 9: BOX-COX TRANSFORM
# =============================================================================
elif page == "9. Box-Cox Transform":
    st.markdown("""<div class="mp-brand-header"><h1>9. Box-Cox Transformation</h1>
    <div class="subtitle">Optimal Power Transform Toward Normality</div></div>""", unsafe_allow_html=True)
    defn_box("What is Box-Cox?", "A <strong>family of power transformations</strong> parameterized by &lambda;:<br>"
             "<code>y = (x<sup>&lambda;</sup> &minus; 1) / &lambda;</code> when &lambda; &ne; 0, and <code>y = ln(x)</code> when &lambda; = 0.<br>"
             "The optimal &lambda; is chosen to make the transformed data as close to <strong>normal</strong> as possible. Requires <strong>x &gt; 0</strong>.")

    np.random.seed(42)
    skewed = np.random.exponential(scale=50, size=500) + 1

    tab1, tab2, tab3 = st.tabs(["Interactive Lambda Explorer", "Formula & Special Cases", "Q&A / Learn"])
    with tab1:
        lam = st.slider("Lambda (λ)", -2.0, 3.0, 0.0, 0.1, key="bc_lam")
        if lam == 0:
            transformed = np.log(skewed)
            label = "ln(x)"
        else:
            transformed = (np.power(skewed, lam) - 1) / lam
            label = f"(x^{lam:.1f} - 1) / {lam:.1f}"

        fig = make_subplots(rows=1, cols=2, subplot_titles=("Original Data", f"Box-Cox (λ={lam:.1f}): {label}"))
        fig.add_trace(go.Histogram(x=skewed, nbinsx=40, marker_color=CORAL, opacity=0.8), row=1, col=1)
        fig.add_trace(go.Histogram(x=transformed, nbinsx=40, marker_color=PURPLE, opacity=0.8), row=1, col=2)
        mp_layout(fig, "", 400); st.plotly_chart(fig, use_container_width=True)

        # Find optimal lambda
        _, opt_lam = sp_stats.boxcox(skewed)
        cols = st.columns(3)
        with cols[0]: st.markdown(metric_card("Current λ", f"{lam:.1f}"), unsafe_allow_html=True)
        with cols[1]: st.markdown(metric_card("Optimal λ", f"{opt_lam:.3f}"), unsafe_allow_html=True)
        with cols[2]: st.markdown(metric_card("Current Skew", f"{pd.Series(transformed).skew():.3f}"), unsafe_allow_html=True)

        insight_box(f"The <strong>optimal &lambda; = {opt_lam:.3f}</strong> minimizes skewness. Drag the slider to see how different &lambda; values reshape the distribution. At &lambda;=0, Box-Cox becomes the natural log.")

    with tab2:
        st.markdown("#### Special Cases of Box-Cox")
        special = pd.DataFrame({
            "λ Value": ["-1", "0", "0.5", "1", "2"],
            "Transform": ["1/x (reciprocal)", "ln(x) (log)", "√x (square root)", "x (no change)", "x² (square)"],
            "Effect": ["Strong compression", "Moderate compression", "Mild compression", "Identity", "Expansion"],
        })
        st.dataframe(special, use_container_width=True, hide_index=True)
        formula_block("Python: from scipy.stats import boxcox; transformed, optimal_lambda = boxcox(data)")
        formula_block("Requirement: All values must be strictly positive (x > 0)")
    with tab3:
        render_qa_tab(
            qas=[
                ("How does Box-Cox differ from a simple log transform?", "Log is a special case of Box-Cox (when λ=0). Box-Cox finds the optimal λ automatically via maximum likelihood estimation, testing the entire family of power transforms to find the one that best achieves normality."),
                ("What does the optimal lambda (λ) represent?", "Lambda determines the type of power transform: λ=1 means no change, λ=0.5 means square root, λ=0 means log, λ=-1 means reciprocal. The optimal λ is the value that makes the transformed data closest to a normal distribution."),
                ("Why must all values be strictly positive for Box-Cox?", "The formula x^λ is undefined or complex for negative values when λ is fractional. For data with zeros or negatives, use Yeo-Johnson transformation instead, which extends Box-Cox to handle all real numbers."),
                ("How do you choose between Box-Cox and log transform?", "If you know your data is right-skewed, log is simple and interpretable. If you're unsure about the optimal transform or need a data-driven choice, use Box-Cox — it will select log if that's optimal, or find a better alternative."),
                ("What is the Yeo-Johnson transformation?", "An extension of Box-Cox that works with zero and negative values. It applies different formulas for positive and negative regions. In sklearn: PowerTransformer(method='yeo-johnson'). Use it when Box-Cox's positivity requirement is too restrictive."),
            ],
            formulas=[
                "y = (x^λ − 1) / λ when λ ≠ 0",
                "y = ln(x) when λ = 0",
                "Special cases: λ=-1 → 1/x, λ=0.5 → √x, λ=1 → x (identity), λ=2 → x²",
                "Python: from scipy.stats import boxcox; transformed, lam = boxcox(data)",
            ],
            approach="Use Box-Cox when you need the most normal-like transformation and don't want to guess which power transform to apply. Ensure all values are strictly positive (add a constant if needed). Compare the skewness before and after, and use Q-Q plots to verify normality improvement.",
            advantages=["Automatically finds the optimal transformation via maximum likelihood", "Encompasses log, square root, reciprocal, and identity as special cases", "Statistically principled — objective function (normality) is well-defined", "scipy.stats.boxcox returns both transformed data and optimal lambda"],
            limitations=["Requires all values to be strictly positive (x > 0)", "Lambda is data-dependent — different datasets yield different lambdas", "Difficult to interpret transformed values when λ is unusual (e.g., λ=0.37)", "Inverse transform is needed to communicate results in original units"],
        )


# =============================================================================
# PAGE 10: CATEGORIZE / BINNING
# =============================================================================
elif page == "10. Categorize / Binning":
    st.markdown("""<div class="mp-brand-header"><h1>10. Categorize / Binning</h1>
    <div class="subtitle">Discretization &bull; Equal-Width &bull; Equal-Frequency &bull; Custom Bins</div></div>""", unsafe_allow_html=True)
    defn_box("What is Binning?", "Converts continuous numbers into <strong>discrete categories</strong> (buckets). Three main strategies:<br>"
             "&#8226; <strong>Equal-width:</strong> same range per bin (0-33, 34-66, 67-100)<br>"
             "&#8226; <strong>Equal-frequency:</strong> same count per bin (quantile-based)<br>"
             "&#8226; <strong>Custom:</strong> domain-specific boundaries (Youth &lt;18, Adult 18-60, Senior 60+)")

    cat_data = pd.DataFrame({
        "Name": ["Anna","Ben","Cara","Dan","Eli","Fay","Gus","Hal"],
        "Age": [12,17,25,34,47,58,66,73], "Score": [45,72,88,55,91,38,76,60],
        "Age Group": ["Youth","Youth","Adult","Adult","Adult","Adult","Senior","Senior"],
        "Grade": ["Fail","Pass","Distinction","Pass","Distinction","Fail","Distinction","Pass"],
    })

    tab1, tab2, tab3, tab4 = st.tabs(["Data & Charts", "Custom Buckets Explorer", "Excel & Python", "Q&A / Learn"])
    with tab1:
        st.dataframe(cat_data, use_container_width=True, hide_index=True)
        c1, c2 = st.columns(2)
        with c1:
            age_counts = cat_data["Age Group"].value_counts().reindex(["Youth","Adult","Senior"])
            fig = go.Figure(go.Bar(x=age_counts.index, y=age_counts.values, marker_color=[GOLD, DARK_BLUE, ACCENT_GREEN], text=age_counts.values, textposition="outside"))
            mp_layout(fig, "Age Group Distribution", 350); st.plotly_chart(fig, use_container_width=True)
        with c2:
            grade_counts = cat_data["Grade"].value_counts().reindex(["Fail","Pass","Distinction"])
            fig2 = go.Figure(go.Bar(x=grade_counts.index, y=grade_counts.values, marker_color=[CORAL, GOLD, DARK_BLUE], text=grade_counts.values, textposition="outside"))
            mp_layout(fig2, "Grade Distribution", 350); st.plotly_chart(fig2, use_container_width=True)
    with tab2:
        st.markdown("#### Create Your Own Age Buckets")
        bc1, bc2 = st.columns(2)
        with bc1: cut1 = st.slider("Youth / Adult boundary", 10, 60, 18, key="cut1")
        with bc2: cut2 = st.slider("Adult / Senior boundary", 30, 80, 60, key="cut2")
        if cut1 >= cut2:
            st.warning("Youth boundary must be less than Senior boundary.")
        else:
            custom = cat_data.copy(); custom["Custom Group"] = custom["Age"].apply(lambda a: "Youth" if a < cut1 else ("Adult" if a < cut2 else "Senior"))
            counts = custom["Custom Group"].value_counts().reindex(["Youth","Adult","Senior"]).fillna(0)
            fig3 = go.Figure(go.Bar(x=counts.index, y=counts.values, marker_color=[GOLD, DARK_BLUE, ACCENT_GREEN], text=counts.values.astype(int), textposition="outside"))
            mp_layout(fig3, f"Youth (<{cut1}) | Adult ({cut1}-{cut2}) | Senior ({cut2}+)", 350); st.plotly_chart(fig3, use_container_width=True)
    with tab3:
        formula_block('Excel: =IF(B2<18, "Youth", IF(B2<60, "Adult", "Senior"))')
        formula_block('Excel: =IF(C2>=75, "Distinction", IF(C2>=50, "Pass", "Fail"))')
        formula_block("Python: pd.cut(df['Age'], bins=[0,18,60,100], labels=['Youth','Adult','Senior'])")
        formula_block("Python (quantile): pd.qcut(df['Score'], q=3, labels=['Low','Mid','High'])")
        insight_box("Use <strong>pd.cut()</strong> for equal-width or custom bins and <strong>pd.qcut()</strong> for equal-frequency (quantile) bins.")
    with tab4:
        render_qa_tab(
            qas=[
                ("What is the difference between equal-width and equal-frequency binning?", "Equal-width bins have the same range (e.g., 0–33, 34–66, 67–100) but may have very different counts. Equal-frequency (quantile) bins have the same count in each bin but different widths. Use quantile bins when the distribution is skewed."),
                ("When should you use custom bins vs automatic binning?", "Custom bins when domain knowledge defines meaningful boundaries (e.g., BMI categories, credit score ranges). Automatic bins when you're exploring data without predefined categories or when the domain doesn't prescribe specific thresholds."),
                ("How does binning affect model performance?", "Binning reduces noise and can capture non-linear relationships (e.g., income bracket matters more than exact income). However, it loses granularity — two values near a bin boundary are treated identically despite being close to different bins."),
                ("What is the boundary problem in binning?", "Values near bin edges (e.g., age 17 vs 18) get assigned to different categories despite being practically identical. Solutions include using overlapping bins, fuzzy boundaries, or keeping the continuous variable alongside the binned version."),
                ("How many bins should you create?", "Too few bins over-simplify (everything is High/Low). Too many bins add noise. Common heuristics: Sturges' rule (k = 1 + log2(n)), Square root rule (k = √n), or domain expertise. For ML, 5-10 bins is typical."),
            ],
            formulas=[
                'Excel: =IF(B2<18, "Youth", IF(B2<60, "Adult", "Senior")) — custom bins',
                "Python: pd.cut(df['col'], bins=[0,18,60,100], labels=['Youth','Adult','Senior'])",
                "Python: pd.qcut(df['col'], q=4, labels=['Q1','Q2','Q3','Q4']) — quantile bins",
                "Sturges' rule: k = 1 + log₂(n) — suggested number of bins",
            ],
            approach="Decide on binning strategy based on the use case: custom bins for domain-specific categories, equal-width for uniform exploration, quantile bins for skewed data. Always visualize the distribution first to choose appropriate boundaries. Keep the original continuous variable for validation.",
            advantages=["Simplifies complex continuous data into interpretable categories", "Handles non-linear relationships without explicit polynomial features", "Reduces the impact of outliers (extreme values land in the top/bottom bin)", "Enables categorical analysis (cross-tabulation, chi-square tests) on continuous data"],
            limitations=["Loses information — exact values within a bin are treated identically", "Boundary sensitivity — small changes near bin edges cause category jumps", "Number and width of bins are somewhat arbitrary without domain guidance", "Can introduce artificial patterns if bin boundaries align with data clusters"],
        )


# =============================================================================
# PAGE 11: CATEGORICAL ENCODE
# =============================================================================
elif page == "11. Categorical Encode":
    st.markdown("""<div class="mp-brand-header"><h1>11. Categorical Encoding</h1>
    <div class="subtitle">Ordinal (Ranked) vs Nominal (One-Hot)</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "Charts, formulas, and ML models need <strong>numbers</strong>. How we convert text &rarr; numbers depends on whether categories have a <strong>natural order</strong>.")

    tab1, tab2, tab3, tab4 = st.tabs(["Ordinal Encoding", "One-Hot Encoding", "Formulas", "Q&A / Learn"])
    with tab1:
        st.markdown("### Ordinal: Categories with a Natural Rank")
        example_box("When to Use", "Size (S&lt;M&lt;L&lt;XL), Satisfaction (Poor&lt;Fair&lt;Good&lt;Excellent), Education level")
        ord_data = pd.DataFrame({"Customer": [f"Cust {i}" for i in range(1,9)], "Satisfaction": ["Good","Excellent","Poor","Fair","Good","Excellent","Fair","Good"], "Score (1-4)": [3,4,1,2,3,4,2,3]})
        c1, c2 = st.columns([2,1])
        with c1: st.dataframe(ord_data, use_container_width=True, hide_index=True)
        with c2: st.markdown(metric_card("Avg Score", "2.75 / 4"), unsafe_allow_html=True)
        mapping = pd.DataFrame({"Category": ["Poor","Fair","Good","Excellent"], "Score": [1,2,3,4]})
        fig = go.Figure(go.Bar(x=mapping["Category"], y=mapping["Score"], marker_color=[f"rgba(0,51,102,{0.25+i*0.25})" for i in range(4)], text=mapping["Score"], textposition="outside"))
        mp_layout(fig, "Ordinal Mapping", 320); st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.markdown("### Nominal: No Natural Order")
        example_box("When to Use", "Color, City, Payment method. Using 1,2,3 falsely implies Green > Red!")
        color_enc = pd.DataFrame({"Item": [1,2,3,4,5], "Color": ["Red","Blue","Green","Red","Blue"], "is_Red": [1,0,0,1,0], "is_Blue": [0,1,0,0,1], "is_Green": [0,0,1,0,0]})
        st.dataframe(color_enc, use_container_width=True, hide_index=True)
        fig2 = go.Figure()
        for i, col in enumerate(["is_Red","is_Blue","is_Green"]):
            fig2.add_trace(go.Bar(name=col.replace("is_",""), x=[f"Item {j}" for j in range(1,6)], y=color_enc[col], marker_color=[CORAL, DARK_BLUE, ACCENT_GREEN][i]))
        mp_layout(fig2, "One-Hot Encoding", 350); fig2.update_layout(barmode="stack"); st.plotly_chart(fig2, use_container_width=True)
    with tab3:
        formula_block('Ordinal: =MATCH(B2, {{"Poor","Fair","Good","Excellent"}}, 0)')
        formula_block('One-Hot: =IF($B2="Red", 1, 0) &mdash; one column per category')
        formula_block("Python: pd.get_dummies(df['Color'], prefix='is')")
        formula_block("Python: from sklearn.preprocessing import LabelEncoder, OneHotEncoder")
    with tab4:
        render_qa_tab(
            qas=[
                ("When should you use ordinal encoding vs one-hot encoding?", "Ordinal encoding when categories have a natural rank (Small < Medium < Large). One-hot encoding when categories are nominal with no inherent order (Red, Blue, Green). Using ordinal encoding on nominal data falsely implies a mathematical ordering."),
                ("What is the dummy variable trap and how do you avoid it?", "With k categories, one-hot encoding creates k binary columns. In linear regression, these are perfectly multicollinear (they sum to 1). Drop one column (drop_first=True in pandas) to avoid the trap. The dropped category becomes the baseline."),
                ("How does one-hot encoding handle high-cardinality features?", "A feature with 1,000 unique values creates 1,000 new columns, causing the curse of dimensionality. Solutions: frequency encoding, target encoding, hashing trick, or grouping rare categories into 'Other' before encoding."),
                ("What is target encoding and when is it useful?", "Replace each category with the mean of the target variable for that category. Useful for high-cardinality features. Risk: data leakage if not done with cross-validation. Use category_encoders library for safe implementation."),
                ("Can tree-based models handle categorical variables directly?", "Some implementations (LightGBM, CatBoost) handle categories natively. Others (sklearn's RandomForest) require encoding. Even when native support exists, encoding can sometimes improve performance by providing a better starting representation."),
            ],
            formulas=[
                '=MATCH(B2, {"Poor","Fair","Good","Excellent"}, 0) — ordinal encoding in Excel',
                '=IF($B2="Red", 1, 0) — one-hot encoding, one column per category',
                "Python: pd.get_dummies(df['Color'], drop_first=True) — avoids dummy trap",
                "Python: LabelEncoder().fit_transform(df['Category']) — ordinal encoding",
            ],
            approach="First determine if categories are ordinal (ranked) or nominal (unordered). For ordinal, map to integers preserving order. For nominal, use one-hot encoding. For high-cardinality features (>20 categories), consider target encoding or frequency encoding. Always drop one dummy column in regression to avoid multicollinearity.",
            advantages=["Converts text categories to numbers that algorithms can process", "One-hot encoding avoids false ordinal relationships between categories", "Ordinal encoding preserves meaningful rank information efficiently", "Essential preprocessing step for virtually all ML algorithms"],
            limitations=["One-hot encoding explodes dimensionality for high-cardinality features", "Ordinal encoding on nominal data introduces false mathematical relationships", "Encoding is model-specific — what works for regression may not suit trees", "New/unseen categories at prediction time require a handling strategy (e.g., 'Unknown' category)"],
        )


# =============================================================================
# PAGE 12: FEATURE ENGINEERING
# =============================================================================
elif page == "12. Feature Engineering":
    st.markdown("""<div class="mp-brand-header"><h1>12. Feature Engineering</h1>
    <div class="subtitle">Create New Predictive Features from Existing Data</div></div>""", unsafe_allow_html=True)
    defn_box("What is Feature Engineering?", "The art of creating <strong>new columns</strong> from existing data that better capture the underlying patterns. "
             "Often the single biggest lever for improving model performance. Goes beyond raw transformation into domain-informed variable creation.")

    tab1, tab2, tab3, tab4 = st.tabs(["Common Techniques", "Interactive Example", "Python Patterns", "Q&A / Learn"])
    with tab1:
        techniques = pd.DataFrame({
            "Technique": ["Ratio / Proportion", "Interaction Terms", "Polynomial Features", "Date Decomposition",
                          "Lag Features", "Rolling Statistics", "Domain Formulas", "Text Length / Counts"],
            "Example": ["Revenue per employee", "Price x Quantity = Revenue", "x, x², x³", "Year, Month, DayOfWeek, IsWeekend",
                        "Sales yesterday, 7 days ago", "7-day moving average", "BMI = weight/height²", "Word count, has_emoji"],
            "Use Case": ["Efficiency metrics", "Capture non-additive effects", "Polynomial regression", "Time-based patterns",
                         "Time series forecasting", "Trend smoothing", "Health, finance, physics", "NLP, sentiment analysis"],
        })
        st.dataframe(techniques, use_container_width=True, hide_index=True)

        colored_pipeline([
            ("Raw\nFeatures", "#999"),
            ("Ratios &\nProportions", CORAL),
            ("Interactions", ORANGE),
            ("Polynomial", GOLD),
            ("Date\nParts", ACCENT_GREEN),
            ("Lag &\nRolling", TEAL),
            ("Domain\nFormulas", PURPLE),
            ("Enriched\nDataset", DARK_BLUE),
        ])

    with tab2:
        st.markdown("#### Feature Engineering on Sales Data")
        fe_data = pd.DataFrame({
            "Date": pd.date_range("2024-01-01", periods=10),
            "Revenue": [1200,950,1500,800,2200,2800,1700,1400,1900,2100],
            "Qty": [18,14,22,11,30,38,25,20,27,29],
            "Customers": [45,38,52,30,65,72,55,48,60,63],
        })
        fe_data["Avg_Price"] = (fe_data["Revenue"] / fe_data["Qty"]).round(2)
        fe_data["Rev_per_Customer"] = (fe_data["Revenue"] / fe_data["Customers"]).round(2)
        fe_data["DayOfWeek"] = fe_data["Date"].dt.day_name()
        fe_data["IsWeekend"] = fe_data["Date"].dt.dayofweek.isin([5,6]).astype(int)
        fe_data["Revenue_Lag1"] = fe_data["Revenue"].shift(1)
        fe_data["Revenue_MA3"] = fe_data["Revenue"].rolling(3).mean().round(0)

        st.dataframe(fe_data, use_container_width=True, hide_index=True)

        fig = make_subplots(rows=1, cols=2, subplot_titles=("Revenue vs 3-day Moving Average", "Revenue per Customer"))
        fig.add_trace(go.Scatter(x=fe_data["Date"], y=fe_data["Revenue"], name="Revenue", line=dict(color=DARK_BLUE, width=2), mode="lines+markers"), row=1, col=1)
        fig.add_trace(go.Scatter(x=fe_data["Date"], y=fe_data["Revenue_MA3"], name="3-day MA", line=dict(color=GOLD, width=3, dash="dash"), mode="lines+markers"), row=1, col=1)
        fig.add_trace(go.Bar(x=fe_data["Date"], y=fe_data["Rev_per_Customer"], name="Rev/Customer", marker_color=TEAL), row=1, col=2)
        mp_layout(fig, "", 400); st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("#### Python Feature Engineering Patterns")
        formula_block("# Ratio features\ndf['price_per_unit'] = df['revenue'] / df['quantity']")
        formula_block("# Date decomposition\ndf['month'] = df['date'].dt.month\ndf['is_weekend'] = df['date'].dt.dayofweek >= 5")
        formula_block("# Lag features (time series)\ndf['sales_lag1'] = df['sales'].shift(1)\ndf['sales_lag7'] = df['sales'].shift(7)")
        formula_block("# Rolling statistics\ndf['ma_7'] = df['sales'].rolling(7).mean()\ndf['std_7'] = df['sales'].rolling(7).std()")
        formula_block("# Polynomial features\nfrom sklearn.preprocessing import PolynomialFeatures\npoly = PolynomialFeatures(degree=2)\nX_poly = poly.fit_transform(X)")
        insight_box("Feature engineering is often more impactful than choosing a fancier model. A good feature derived from domain knowledge can outperform complex algorithms working on raw data.")
    with tab4:
        render_qa_tab(
            qas=[
                ("Why is feature engineering considered the most impactful step in ML?", "Raw features rarely capture the true signal. Engineered features encode domain knowledge (e.g., BMI from height and weight) that algorithms cannot discover on their own. Competitions like Kaggle are often won by creative feature engineering, not model selection."),
                ("What are ratio features and when should you create them?", "Ratios normalize one variable by another: revenue per employee, cost per unit, price-to-earnings. They capture efficiency and intensity, removing the effect of scale. Use them whenever comparing entities of different sizes (companies, regions, time periods)."),
                ("How do lag features help in time series forecasting?", "Lag features (e.g., sales yesterday, sales 7 days ago) let the model learn temporal patterns: autocorrelation, weekly cycles, trends. Without lags, the model has no concept of time — each row is independent and the sequential nature is lost."),
                ("What is the risk of creating too many features?", "The curse of dimensionality: with too many features relative to observations, models overfit, training slows, and noise overwhelms signal. Use feature selection (mutual information, L1 regularization, recursive elimination) to prune irrelevant features."),
                ("How do you validate that an engineered feature is useful?", "Check correlation with the target variable, compute mutual information score, or compare model performance with and without the feature. A feature that doesn't improve cross-validated performance is noise and should be dropped."),
            ],
            formulas=[
                "Ratio: df['price_per_unit'] = df['revenue'] / df['quantity']",
                "Lag: df['sales_lag1'] = df['sales'].shift(1)",
                "Rolling: df['ma_7'] = df['sales'].rolling(7).mean()",
                "Polynomial: PolynomialFeatures(degree=2).fit_transform(X)",
            ],
            approach="Start with domain knowledge: what ratios, differences, or interactions would a subject matter expert find meaningful? Then add systematic features: date decomposition, lag/rolling stats for time series, interaction terms. Always validate each feature's predictive power and drop those that don't improve the model.",
            advantages=["Can dramatically improve model accuracy without changing the algorithm", "Encodes domain expertise that algorithms cannot learn from raw data alone", "Ratio and normalized features enable fair comparison across different scales", "Date decomposition and lag features unlock temporal patterns in time series"],
            limitations=["Risk of overfitting if too many features are created from limited data", "Requires deep domain knowledge to create truly meaningful features", "Engineered features may be collinear with existing features, adding redundancy", "Feature engineering is labor-intensive and doesn't transfer easily between domains"],
        )


# =============================================================================
# PAGE 13: FRESHMART CASELET
# =============================================================================
elif page == "13. FreshMart Caselet":
    st.markdown("""<div class="mp-brand-header"><h1>FreshMart Caselet</h1>
    <div class="subtitle">Cleaning &amp; Transforming Retail Sales Data &mdash; End-to-End Exercise</div></div>""", unsafe_allow_html=True)
    defn_box("Scenario", "FreshMart exported 12 orders from 3 stores. The data is messy: inconsistent region names, mixed currencies (USD/INR), text dates, missing region. "
             "Apply transformations to answer <strong>5 business questions</strong>.<br><strong>Rate:</strong> 1 USD = 83 INR")

    raw_caselet = pd.DataFrame({
        "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
        "Region": [" north ","SOUTH","North","east","","South ","EAST","north","South"," East","NORTH","south"],
        "Product": ["Apples","Bread","Milk","Apples","Bread","Milk","Apples","Bread","Apples","Milk","Milk","Apples"],
        "Qty": [10,5,8,12,6,15,9,4,20,7,11,14], "Amount": [50,1245,24,4980,18,3735,45,996,180,1743,33,12450],
        "Currency": ["USD","INR","USD","INR","USD","INR","USD","INR","USD","INR","USD","INR"],
        "Date (text)": ["20240105","20240108","20240115","20240118","20240122","20240204","20240210","20240215","20240220","20240301","20240310","20240315"],
    })
    clean_caselet = pd.DataFrame({
        "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
        "Region": ["North","South","North","East","Unknown","South","East","North","South","East","North","South"],
        "Product": ["Apples","Bread","Milk","Apples","Bread","Milk","Apples","Bread","Apples","Milk","Milk","Apples"],
        "Qty": [10,5,8,12,6,15,9,4,20,7,11,14],
        "Amount (USD)": [50.00,15.00,24.00,60.00,18.00,45.00,45.00,12.00,180.00,21.00,33.00,150.00],
        "Date": pd.to_datetime(["2024-01-05","2024-01-08","2024-01-15","2024-01-18","2024-01-22","2024-02-04","2024-02-10","2024-02-15","2024-02-20","2024-03-01","2024-03-10","2024-03-15"]),
        "Month": ["Jan","Jan","Jan","Jan","Jan","Feb","Feb","Feb","Feb","Mar","Mar","Mar"],
        "Size Bucket": ["Medium","Small","Small","Medium","Small","Small","Small","Small","Large","Small","Small","Large"],
    })

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Raw vs Clean", "5 Business Questions", "Transformations Applied", "Interactive Explorer", "Q&A / Learn"])
    with tab1:
        st.markdown("#### Raw Data"); st.dataframe(raw_caselet, use_container_width=True, hide_index=True)
        st.markdown("#### Cleaned & Transformed"); st.dataframe(clean_caselet.drop(columns=["Date"]).assign(Date=clean_caselet["Date"].dt.strftime("%Y-%m-%d")), use_container_width=True, hide_index=True)
    with tab2:
        region_summary = clean_caselet.groupby("Region").agg(Total_Sales=("Amount (USD)","sum"), Order_Count=("Amount (USD)","count"), Avg_Order=("Amount (USD)","mean")).round(2).reset_index()
        st.markdown("#### Q1: Highest total sales region?")
        fig_q1 = go.Figure(go.Bar(x=region_summary["Region"], y=region_summary["Total_Sales"], marker_color=[DARK_BLUE if r!="South" else GOLD for r in region_summary["Region"]], text=[f"${v:,.0f}" for v in region_summary["Total_Sales"]], textposition="outside"))
        mp_layout(fig_q1, "Total Sales by Region (USD)", 350); st.plotly_chart(fig_q1, use_container_width=True); st.success("**Answer:** South with $390")

        st.markdown("#### Q2: Average order value per region?")
        fig_q2 = go.Figure(go.Bar(x=region_summary["Region"], y=region_summary["Avg_Order"], marker_color=[DARK_BLUE, ACCENT_GREEN, GOLD, "#ccc"], text=[f"${v:,.0f}" for v in region_summary["Avg_Order"]], textposition="outside"))
        mp_layout(fig_q2, "Avg Order by Region", 350); st.plotly_chart(fig_q2, use_container_width=True)

        st.markdown("#### Q3: % of total sales by product?")
        prod = clean_caselet.groupby("Product")["Amount (USD)"].sum().reset_index()
        fig_q3 = px.pie(prod, values="Amount (USD)", names="Product", color_discrete_sequence=[DARK_BLUE, GOLD, ACCENT_GREEN])
        mp_layout(fig_q3, "Sales Share by Product", 380); st.plotly_chart(fig_q3, use_container_width=True)

        st.markdown("#### Q4: Order size buckets?")
        bkt = clean_caselet["Size Bucket"].value_counts().reindex(["Small","Medium","Large"]).fillna(0).astype(int)
        fig_q4 = go.Figure(go.Bar(x=bkt.index, y=bkt.values, marker_color=[TEAL, GOLD, DARK_BLUE], text=bkt.values, textposition="outside"))
        mp_layout(fig_q4, "Order Size Distribution", 350); st.plotly_chart(fig_q4, use_container_width=True)

        st.markdown("#### Q5: Orders per month?")
        mo = clean_caselet["Month"].value_counts().reindex(["Jan","Feb","Mar"]).fillna(0).astype(int)
        fig_q5 = go.Figure(go.Bar(x=mo.index, y=mo.values, marker_color=[DARK_BLUE, GOLD, ACCENT_GREEN], text=mo.values, textposition="outside"))
        mp_layout(fig_q5, "Orders per Month", 350); st.plotly_chart(fig_q5, use_container_width=True)

    with tab3:
        transforms = [
            ("1. Cleaning", "TRIM + PROPER on Region; blanks → 'Unknown'", '=IF(B2="", "Unknown", PROPER(TRIM(B2)))'),
            ("2. Standardize", "INR→USD (÷83); text→real dates", '=IF(F2="INR", E2/83, E2)'),
            ("3. Aggregate", "SUMIF/COUNTIF/AVERAGEIF per region & product", "=SUMIF(B:B, region, E:E)"),
            ("4. Normalize", "% share of total sales by product", "=product_total / grand_total"),
            ("5. Categorize", "Bucket orders: Small/Medium/Large", '=IF(E2>100,"Large",IF(E2>=50,"Medium","Small"))'),
            ("6. Reshape", "Group daily orders into monthly counts", '=TEXT(F2,"mmm yyyy")'),
        ]
        for name, desc, formula in transforms:
            st.markdown(f'<div class="defn-box"><div class="box-title">{name}</div><br>{desc}<div class="formula-box" style="margin-top:0.5rem;">{formula}</div></div>', unsafe_allow_html=True)

    with tab4:
        col_choice = st.selectbox("Group by", ["Region","Product","Month","Size Bucket"])
        metric_choice = st.selectbox("Metric", ["Total Sales (USD)","Order Count","Average Qty"])
        if metric_choice == "Total Sales (USD)":
            grouped = clean_caselet.groupby(col_choice)["Amount (USD)"].sum().reset_index(); grouped.columns = [col_choice, "Value"]; fmt="${:,.0f}"
        elif metric_choice == "Order Count":
            grouped = clean_caselet.groupby(col_choice).size().reset_index(name="Value"); fmt="{:,.0f}"
        else:
            grouped = clean_caselet.groupby(col_choice)["Qty"].mean().round(1).reset_index(); grouped.columns = [col_choice, "Value"]; fmt="{:,.1f}"
        fig_exp = go.Figure(go.Bar(x=grouped[col_choice], y=grouped["Value"], marker_color=[MP_COLORS[i%len(MP_COLORS)] for i in range(len(grouped))], text=[fmt.format(v) for v in grouped["Value"]], textposition="outside"))
        mp_layout(fig_exp, f"{metric_choice} by {col_choice}", 400); st.plotly_chart(fig_exp, use_container_width=True)
    with tab5:
        render_qa_tab(
            qas=[
                ("What is the typical order of data transformations in a real project?", "1) Clean (fix typos, handle missing values), 2) Standardize (units, formats), 3) Aggregate (group summaries), 4) Normalize/Scale (for ML), 5) Encode (categorical to numeric), 6) Engineer features. Cleaning always comes first — garbage in, garbage out."),
                ("How do you handle missing region values in the FreshMart dataset?", "The blank region in row 5 is replaced with 'Unknown' rather than deleted. Deleting rows loses data; imputing with 'Unknown' preserves the transaction for sales totals while clearly flagging the data quality issue for investigation."),
                ("Why convert INR to USD instead of keeping both currencies?", "You cannot SUM or compare amounts in different currencies. Converting to a single base currency (USD at 1 USD = 83 INR) enables valid aggregation, ranking, and percentage calculations across all orders."),
                ("How do you validate that your transformations are correct?", "Cross-check totals: sum of cleaned USD amounts should equal sum of original amounts after conversion. Check row counts: no rows should be lost unless intentionally filtered. Verify categories: all regions should map to expected clean values."),
                ("What real-world complications does this caselet illustrate?", "Inconsistent casing (' north ' vs 'NORTH'), leading/trailing spaces, mixed currencies, text dates, missing values — these are the top 5 data quality issues found in production data. The caselet teaches that transformation is 80% cleaning, 20% analysis."),
            ],
            formulas=[
                '=IF(B2="", "Unknown", PROPER(TRIM(B2))) — clean region names',
                '=IF(F2="INR", E2/83, E2) — currency standardization',
                "=SUMIF(B:B, region, E:E) — aggregate by region",
                '=IF(E2>100, "Large", IF(E2>=50, "Medium", "Small")) — order size bins',
            ],
            approach="Follow the clean-first principle: fix data quality issues before any analysis. Standardize units and formats next. Only then aggregate and visualize. Document every transformation step so results are reproducible and auditable. Always validate with cross-checks.",
            advantages=["End-to-end workflow demonstrates how transformations chain together", "Real-world messiness (mixed case, currencies, missing data) mirrors production scenarios", "Business questions drive the transformations — purpose-driven data prep", "Cross-validation of totals ensures transformation accuracy"],
            limitations=["Fixed exchange rate (1 USD = 83 INR) doesn't reflect real-time fluctuations", "Small dataset (12 rows) doesn't reveal scalability challenges", "'Unknown' for missing regions may skew regional analysis", "Date parsing assumes a single format — real data often has multiple date formats"],
        )


# =============================================================================
# PAGE 14: PYTHON CASE STUDY
# =============================================================================
elif page == "14. Python Case Study":
    st.markdown("""<div class="mp-brand-header"><h1>Python Case Study</h1>
    <div class="subtitle">Data Transformation Techniques &mdash; End-to-End with sklearn &amp; scipy</div></div>""", unsafe_allow_html=True)

    defn_box("Case Study Overview",
             "A retail customer dataset with <strong>500 records</strong> containing Income (skewed), Age (normal), Spending Score, and Gender. "
             "We apply every major transformation technique step by step, with <strong>before-and-after visualizations</strong> and the Python code that produces each result.")

    def step_header(num, title):
        st.markdown(f'<div class="step-header"><div class="step-num">{num}</div>{title}</div>', unsafe_allow_html=True)

    def show_code(code):
        st.code(code, language="python")

    # --- Generate the dataset (same seed as notebook) ---
    from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, LabelEncoder
    from scipy.stats import boxcox, skew as sp_skew

    np.random.seed(42)
    n = 500
    cs_data = pd.DataFrame({
        'Income': np.random.exponential(scale=50000, size=n),
        'Age': np.abs(np.random.normal(40, 10, n)),
        'Spending_Score': np.random.randint(1, 100, n),
        'Gender': np.random.choice(['Male', 'Female'], n),
    })

    # ---- STEP 1 & 2: Libraries & Dataset ----
    step_header("1", "Import Libraries")
    show_code("""import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, LabelEncoder
from scipy.stats import boxcox, skew""")

    step_header("2", "Create Sample Dataset")
    show_code("""np.random.seed(42)
n = 500
data = pd.DataFrame({
    'Income':         np.random.exponential(scale=50000, size=n),
    'Age':            np.random.normal(40, 10, n),
    'Spending_Score': np.random.randint(1, 100, n),
    'Gender':         np.random.choice(['Male','Female'], n)
})
data['Age'] = abs(data['Age'])""")

    st.markdown("#### Original Data (first 10 rows)")
    st.dataframe(cs_data.head(10), use_container_width=True, hide_index=True)

    cols_m = st.columns(4)
    with cols_m[0]: st.markdown(metric_card("Rows", "500"), unsafe_allow_html=True)
    with cols_m[1]: st.markdown(metric_card("Avg Income", f"${cs_data['Income'].mean():,.0f}"), unsafe_allow_html=True)
    with cols_m[2]: st.markdown(metric_card("Avg Age", f"{cs_data['Age'].mean():.1f}"), unsafe_allow_html=True)
    with cols_m[3]: st.markdown(metric_card("Male / Female", f"{(cs_data['Gender']=='Male').sum()} / {(cs_data['Gender']=='Female').sum()}"), unsafe_allow_html=True)

    # ---- STEP 3 & 4: Skewness + Log Transform ----
    step_header("3", "Understanding Skewness")
    orig_skew = round(sp_skew(cs_data['Income']), 2)
    show_code(f"skew(data['Income'])  # Result: {orig_skew}")

    cs_data['Log_Income'] = np.log1p(cs_data['Income'])
    log_skew = round(sp_skew(cs_data['Log_Income']), 2)

    step_header("4", "Log Transformation")
    show_code("""data['Log_Income'] = np.log1p(data['Income'])
# Skewness drops from {orig} to {after}""".format(orig=orig_skew, after=log_skew))

    fig_log = make_subplots(rows=1, cols=2, subplot_titles=(f"BEFORE: Income (skew={orig_skew})", f"AFTER: Log Income (skew={log_skew})"))
    fig_log.add_trace(go.Histogram(x=cs_data['Income'], nbinsx=40, marker_color=CORAL, opacity=0.85, name="Original"), row=1, col=1)
    fig_log.add_trace(go.Histogram(x=cs_data['Log_Income'], nbinsx=40, marker_color=ACCENT_GREEN, opacity=0.85, name="Log"), row=1, col=2)
    mp_layout(fig_log, "Step 4: Log Transformation Effect", 380); st.plotly_chart(fig_log, use_container_width=True)

    # ---- STEP 5: Min-Max ----
    step_header("5", "Min-Max Scaling")
    show_code("""minmax = MinMaxScaler()
data['Income_MinMax'] = minmax.fit_transform(data[['Income']])
# Range: 0.00 to 1.00""")

    cs_data['Income_MinMax'] = MinMaxScaler().fit_transform(cs_data[['Income']])
    fig_mm = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Original Income", "AFTER: MinMax Scaled [0,1]"))
    fig_mm.add_trace(go.Histogram(x=cs_data['Income'], nbinsx=40, marker_color=CORAL, opacity=0.85), row=1, col=1)
    fig_mm.add_trace(go.Histogram(x=cs_data['Income_MinMax'], nbinsx=40, marker_color=TEAL, opacity=0.85), row=1, col=2)
    mp_layout(fig_mm, "Step 5: Min-Max Scaling Effect", 380); st.plotly_chart(fig_mm, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1: st.markdown(metric_card("Min after scaling", f"{cs_data['Income_MinMax'].min():.2f}"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card("Max after scaling", f"{cs_data['Income_MinMax'].max():.2f}"), unsafe_allow_html=True)

    # ---- STEP 6: Standardization ----
    step_header("6", "Standardization (Z-Score)")
    cs_data['Income_Std'] = StandardScaler().fit_transform(cs_data[['Income']])
    show_code("""standard = StandardScaler()
data['Income_Standardized'] = standard.fit_transform(data[['Income']])
# Mean ≈ 0, Std ≈ 1""")

    fig_std = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Original Income", f"AFTER: Standardized (μ={cs_data['Income_Std'].mean():.4f}, σ={cs_data['Income_Std'].std():.4f})"))
    fig_std.add_trace(go.Histogram(x=cs_data['Income'], nbinsx=40, marker_color=CORAL, opacity=0.85), row=1, col=1)
    fig_std.add_trace(go.Histogram(x=cs_data['Income_Std'], nbinsx=40, marker_color=GOLD, opacity=0.85), row=1, col=2)
    mp_layout(fig_std, "Step 6: Standardization Effect", 380); st.plotly_chart(fig_std, use_container_width=True)

    c1, c2 = st.columns(2)
    with c1: st.markdown(metric_card("Mean after", f"{cs_data['Income_Std'].mean():.4f}"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card("Std Dev after", f"{cs_data['Income_Std'].std():.4f}"), unsafe_allow_html=True)

    # ---- STEP 7: Robust Scaling ----
    step_header("7", "Robust Scaling")
    cs_data['Income_Robust'] = RobustScaler().fit_transform(cs_data[['Income']])
    show_code("""robust = RobustScaler()
data['Income_Robust'] = robust.fit_transform(data[['Income']])""")

    fig_rob = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Original (box plot)", "AFTER: Robust Scaled (box plot)"))
    fig_rob.add_trace(go.Box(y=cs_data['Income'], name="Original", marker_color=CORAL, boxmean=True), row=1, col=1)
    fig_rob.add_trace(go.Box(y=cs_data['Income_Robust'], name="Robust", marker_color=DARK_BLUE, boxmean=True), row=1, col=2)
    mp_layout(fig_rob, "Step 7: Robust Scaling Effect (Box Plots)", 400); st.plotly_chart(fig_rob, use_container_width=True)

    insight_box("Box plots show outliers clearly. Robust Scaling uses <strong>median &amp; IQR</strong> so the central mass of data sits near zero while outliers are flagged without distorting the scale.")

    # ---- STEP 8: Box-Cox ----
    step_header("8", "Box-Cox Transformation")
    cs_data['Income_BoxCox'], bc_lam = boxcox(cs_data['Income'] + 1)
    bc_skew = round(sp_skew(cs_data['Income_BoxCox']), 2)
    show_code(f"""data['Income_BoxCox'], lam = boxcox(data['Income'] + 1)
# Lambda = {bc_lam:.4f}
# Skewness AFTER: {bc_skew}""")

    fig_bc = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Original Income", f"AFTER: Box-Cox (λ={bc_lam:.3f}, skew={bc_skew})"))
    fig_bc.add_trace(go.Histogram(x=cs_data['Income'], nbinsx=40, marker_color=CORAL, opacity=0.85), row=1, col=1)
    fig_bc.add_trace(go.Histogram(x=cs_data['Income_BoxCox'], nbinsx=40, marker_color=PURPLE, opacity=0.85), row=1, col=2)
    mp_layout(fig_bc, "Step 8: Box-Cox Transformation Effect", 380); st.plotly_chart(fig_bc, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(metric_card("Lambda (λ)", f"{bc_lam:.4f}"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card("Skew Before", f"{orig_skew}"), unsafe_allow_html=True)
    with c3: st.markdown(metric_card("Skew After", f"{bc_skew}"), unsafe_allow_html=True)

    # ---- STEP 9: Label Encoding ----
    step_header("9", "Encoding Categorical Variables")
    cs_data['Gender_Encoded'] = LabelEncoder().fit_transform(cs_data['Gender'])
    show_code("""encoder = LabelEncoder()
data['Gender_Encoded'] = encoder.fit_transform(data['Gender'])
# Female -> 0, Male -> 1""")

    fig_enc = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Categorical Gender", "AFTER: Encoded Gender"))
    gb = cs_data['Gender'].value_counts()
    ge = cs_data['Gender_Encoded'].value_counts().sort_index()
    fig_enc.add_trace(go.Bar(x=gb.index, y=gb.values, marker_color=[CORAL, DARK_BLUE], name="Categorical"), row=1, col=1)
    fig_enc.add_trace(go.Bar(x=["0 (Female)", "1 (Male)"], y=[ge.get(0,0), ge.get(1,0)], marker_color=[CORAL, DARK_BLUE], name="Encoded"), row=1, col=2)
    mp_layout(fig_enc, "Step 9: Label Encoding Effect", 380); st.plotly_chart(fig_enc, use_container_width=True)

    # ---- STEP 10: Binning ----
    step_header("10", "Binning / Discretization")
    cs_data['Age_Group'] = pd.cut(cs_data['Age'], bins=[0,25,40,60,100], labels=['Young','Adult','Middle Age','Senior'])
    show_code("""data['Age_Group'] = pd.cut(
    data['Age'],
    bins=[0, 25, 40, 60, 100],
    labels=['Young', 'Adult', 'Middle Age', 'Senior']
)""")

    fig_bin = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Continuous Age", "AFTER: Binned Age Groups"))
    fig_bin.add_trace(go.Histogram(x=cs_data['Age'], nbinsx=30, marker_color=CORAL, opacity=0.85), row=1, col=1)
    ag = cs_data['Age_Group'].value_counts().reindex(['Young','Adult','Middle Age','Senior'])
    fig_bin.add_trace(go.Bar(x=ag.index.astype(str), y=ag.values, marker_color=[GOLD, DARK_BLUE, TEAL, ACCENT_GREEN]), row=1, col=2)
    mp_layout(fig_bin, "Step 10: Binning Effect", 380); st.plotly_chart(fig_bin, use_container_width=True)

    # ---- STEP 11: Feature Engineering ----
    step_header("11", "Feature Engineering")
    cs_data['Spend_per_Age'] = cs_data['Spending_Score'] / cs_data['Age']
    show_code("""data['Spend_per_Age'] = data['Spending_Score'] / data['Age']
# Spending intensity relative to age""")

    fig_fe = make_subplots(rows=1, cols=2, subplot_titles=("BEFORE: Spending Score vs Age", "AFTER: Spend per Age vs Age"))
    fig_fe.add_trace(go.Scatter(x=cs_data['Age'], y=cs_data['Spending_Score'], mode='markers', marker=dict(color=CORAL, size=4, opacity=0.5), name="Spending Score"), row=1, col=1)
    fig_fe.add_trace(go.Scatter(x=cs_data['Age'], y=cs_data['Spend_per_Age'], mode='markers', marker=dict(color=DARK_BLUE, size=4, opacity=0.5), name="Spend/Age"), row=1, col=2)
    mp_layout(fig_fe, "Step 11: Feature Engineering Effect", 400); st.plotly_chart(fig_fe, use_container_width=True)

    insight_box("The engineered feature <strong>Spend_per_Age</strong> reveals that younger customers have a disproportionately higher spending intensity, a pattern invisible in the raw Spending Score.")

    # ---- STEP 12: Final Comparison ----
    step_header("12", "Final Comparison of All Transformations")
    show_code("""# Compare all transformations side by side on the Income column""")

    fig_final = make_subplots(rows=2, cols=3, subplot_titles=("Original", "Log Transform", "Min-Max", "Standardized (Z-Score)", "Robust Scaled", "Box-Cox"))
    hist_cols = [('Income', CORAL), ('Log_Income', ACCENT_GREEN), ('Income_MinMax', TEAL),
                 ('Income_Std', GOLD), ('Income_Robust', DARK_BLUE), ('Income_BoxCox', PURPLE)]
    positions = [(1,1),(1,2),(1,3),(2,1),(2,2),(2,3)]
    for (col, color), (r, c) in zip(hist_cols, positions):
        fig_final.add_trace(go.Histogram(x=cs_data[col], nbinsx=35, marker_color=color, opacity=0.85, showlegend=False), row=r, col=c)
    mp_layout(fig_final, "All 6 Transformations Compared on Income", 500); st.plotly_chart(fig_final, use_container_width=True)

    # ---- STEP 13: Final Dataset ----
    step_header("13", "Final Transformed Dataset")
    show_code(f"data.shape  # Result: {cs_data.shape}")

    st.markdown("#### Final Dataset (first 10 rows)")
    display_cols = ['Income','Log_Income','Income_MinMax','Income_Std','Income_Robust','Income_BoxCox','Age','Age_Group','Spending_Score','Spend_per_Age','Gender','Gender_Encoded']
    st.dataframe(cs_data[display_cols].head(10).round(4), use_container_width=True, hide_index=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(metric_card("Total Columns", f"{len(display_cols)}"), unsafe_allow_html=True)
    with c2: st.markdown(metric_card("Original Columns", "4"), unsafe_allow_html=True)
    with c3: st.markdown(metric_card("Engineered Columns", f"{len(display_cols)-4}"), unsafe_allow_html=True)

    example_box("Summary of Techniques Applied",
                "&#8226; <strong>Log Transform:</strong> Skewness {orig} &rarr; {log}<br>"
                "&#8226; <strong>Min-Max:</strong> Range compressed to [0, 1]<br>"
                "&#8226; <strong>Z-Score:</strong> Mean &rarr; 0, Std &rarr; 1<br>"
                "&#8226; <strong>Robust:</strong> Median-centered, IQR-scaled (outlier-safe)<br>"
                "&#8226; <strong>Box-Cox:</strong> Optimal &lambda;={lam:.3f}, near-normal result<br>"
                "&#8226; <strong>Label Encoding:</strong> Male/Female &rarr; 1/0<br>"
                "&#8226; <strong>Binning:</strong> Age &rarr; Young/Adult/Middle Age/Senior<br>"
                "&#8226; <strong>Feature Engineering:</strong> Spend_per_Age reveals spending intensity".format(
                    orig=orig_skew, log=log_skew, lam=bc_lam))


# =============================================================================
# FOOTER
# =============================================================================
st.markdown(f"""
<div class="mp-footer">
    <strong style="font-size:1.05rem;">The Mountain Path &mdash; World of Finance</strong><br>
    <span style="font-size:0.95rem;">Prof. V. Ravichandran</span><br>
    <div class="social-links" style="margin:0.8rem 0;">
        <a class="linkedin" href="https://www.linkedin.com/in/trichyravis" target="_blank">LinkedIn</a>
        <a class="github" href="https://github.com/trichyravis" target="_blank">GitHub</a>
        <a class="web" href="https://themountainpathacademy.com" target="_blank">themountainpathacademy.com</a>
    </div>
    <em>Bridging Theory with Practice &bull; Excellence in Financial Education</em>
</div>
""", unsafe_allow_html=True)
