
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

    tab1, tab2, tab3 = st.tabs(["Before & After", "Interactive Chart", "Excel Formulas"])
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


# =============================================================================
# PAGE 2: STANDARDIZE
# =============================================================================
elif page == "2. Standardize":
    st.markdown("""<div class="mp-brand-header"><h1>2. Standardize</h1>
    <div class="subtitle">Convert Units &bull; Parse Dates &bull; Common Scale</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "Weights are mixed (lbs vs kg) and dates are stored as text. You cannot SUM or SORT until every value is on the same scale.")
    raw_std = pd.DataFrame({"Item": [f"Item {c}" for c in "ABCDE"], "Weight": [10,5,22,3,50], "Unit": ["lb","kg","lb","kg","lb"], "Date (text)": ["20240115","20240203","20240220","20240301","20240318"]})
    std = pd.DataFrame({"Item": [f"Item {c}" for c in "ABCDE"], "Weight (kg)": [4.536,5.000,9.979,3.000,22.680], "Real Date": ["2024-01-15","2024-02-03","2024-02-20","2024-03-01","2024-03-18"]})
    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Chart", "Excel Formulas"])
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


# =============================================================================
# PAGE 3: AGGREGATE
# =============================================================================
elif page == "3. Aggregate":
    st.markdown("""<div class="mp-brand-header"><h1>3. Aggregate</h1>
    <div class="subtitle">SUMIF &bull; COUNTIF &bull; AVERAGEIF</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "10 individual sales rows tell us little. Aggregate into per-group summaries to see which region leads.")
    raw_agg = pd.DataFrame({"Order": [f"Order {i}" for i in range(1,11)], "Region": ["North","South","North","East","South","West","North","East","West","South"], "Sales": [120,90,75,200,60,150,95,110,80,130]})
    agg = pd.DataFrame({"Region": ["North","South","East","West"], "Total Sales": [290,280,310,230], "Order Count": [3,3,2,2], "Avg Order": [96.67,93.33,155.00,115.00]})
    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Charts", "Excel Formulas"])
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
    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Heatmap", "Excel Formulas"])
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

    tab1, tab2, tab3 = st.tabs(["Raw vs Scaled", "Live Explorer", "Formula"])
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

    tab1, tab2 = st.tabs(["Visualization", "Formula & Comparison"])
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

    tab1, tab2 = st.tabs(["Comparison of 3 Scalers", "Formula"])
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

    tab1, tab2, tab3 = st.tabs(["Before & After", "Live Explorer", "Formula & Use Cases"])
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

    tab1, tab2 = st.tabs(["Interactive Lambda Explorer", "Formula & Special Cases"])
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

    tab1, tab2, tab3 = st.tabs(["Data & Charts", "Custom Buckets Explorer", "Excel & Python"])
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


# =============================================================================
# PAGE 11: CATEGORICAL ENCODE
# =============================================================================
elif page == "11. Categorical Encode":
    st.markdown("""<div class="mp-brand-header"><h1>11. Categorical Encoding</h1>
    <div class="subtitle">Ordinal (Ranked) vs Nominal (One-Hot)</div></div>""", unsafe_allow_html=True)
    defn_box("The Problem", "Charts, formulas, and ML models need <strong>numbers</strong>. How we convert text &rarr; numbers depends on whether categories have a <strong>natural order</strong>.")

    tab1, tab2, tab3 = st.tabs(["Ordinal Encoding", "One-Hot Encoding", "Formulas"])
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


# =============================================================================
# PAGE 12: FEATURE ENGINEERING
# =============================================================================
elif page == "12. Feature Engineering":
    st.markdown("""<div class="mp-brand-header"><h1>12. Feature Engineering</h1>
    <div class="subtitle">Create New Predictive Features from Existing Data</div></div>""", unsafe_allow_html=True)
    defn_box("What is Feature Engineering?", "The art of creating <strong>new columns</strong> from existing data that better capture the underlying patterns. "
             "Often the single biggest lever for improving model performance. Goes beyond raw transformation into domain-informed variable creation.")

    tab1, tab2, tab3 = st.tabs(["Common Techniques", "Interactive Example", "Python Patterns"])
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

    tab1, tab2, tab3, tab4 = st.tabs(["Raw vs Clean", "5 Business Questions", "Transformations Applied", "Interactive Explorer"])
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
