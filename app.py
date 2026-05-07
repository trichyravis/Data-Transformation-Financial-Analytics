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

# =============================================================================
# MOUNTAIN PATH ACADEMY DESIGN SYSTEM
# =============================================================================
DARK_BLUE = "#003366"
LIGHT_BLUE = "#ADD8E6"
GOLD = "#FFD700"
DARK_GOLD = "#B8860B"
WHITE = "#FFFFFF"
OFF_WHITE = "#F8FAFC"
LIGHT_GOLD_BG = "#FFFDF0"
ACCENT_GREEN = "#2E8B57"

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

    /* Global */
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
    section[data-testid="stSidebar"] .stMarkdown p,
    section[data-testid="stSidebar"] .stMarkdown li,
    section[data-testid="stSidebar"] .stMarkdown h1,
    section[data-testid="stSidebar"] .stMarkdown h2,
    section[data-testid="stSidebar"] .stMarkdown h3,
    section[data-testid="stSidebar"] label {{
        color: {WHITE} !important;
        font-family: 'Source Sans 3', sans-serif;
    }}
    section[data-testid="stSidebar"] .stRadio label span {{
        color: {LIGHT_BLUE} !important;
        font-size: 1.02rem;
    }}
    section[data-testid="stSidebar"] hr {{
        border-color: rgba(173,216,230,0.3);
    }}

    /* Headers */
    h1 {{
        font-family: 'Playfair Display', serif !important;
        color: {DARK_BLUE} !important;
        font-weight: 700 !important;
    }}
    h2, h3, h4 {{
        font-family: 'Source Sans 3', sans-serif !important;
        color: {DARK_BLUE} !important;
        font-weight: 600 !important;
    }}
    p, li, span {{
        font-family: 'Source Sans 3', sans-serif;
    }}

    /* Custom boxes */
    .mp-brand-header {{
        background: linear-gradient(135deg, {DARK_BLUE} 0%, #004080 100%);
        color: white;
        padding: 1.4rem 2rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 15px rgba(0,51,102,0.3);
    }}
    .mp-brand-header h1 {{
        color: white !important;
        font-family: 'Playfair Display', serif !important;
        font-size: 2rem !important;
        margin: 0 !important;
        letter-spacing: 2px;
    }}
    .mp-brand-header .subtitle {{
        color: {GOLD};
        font-size: 1.1rem;
        font-family: 'Source Sans 3', sans-serif;
        margin-top: 0.3rem;
    }}

    .defn-box {{
        background: linear-gradient(135deg, rgba(173,216,230,0.15) 0%, rgba(173,216,230,0.05) 100%);
        border-left: 4px solid {DARK_BLUE};
        border-radius: 0 8px 8px 0;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,51,102,0.08);
    }}
    .defn-box .box-title {{
        background: {DARK_BLUE};
        color: white;
        display: inline-block;
        padding: 3px 14px;
        border-radius: 4px;
        font-weight: 600;
        font-size: 0.95rem;
        margin-bottom: 0.6rem;
        font-family: 'Source Sans 3', sans-serif;
    }}

    .example-box {{
        background: linear-gradient(135deg, {LIGHT_GOLD_BG} 0%, rgba(255,215,0,0.06) 100%);
        border-left: 4px solid {GOLD};
        border-radius: 0 8px 8px 0;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(184,134,11,0.08);
    }}
    .example-box .box-title {{
        color: {DARK_GOLD};
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
        font-family: 'Source Sans 3', sans-serif;
    }}

    .insight-box {{
        background: linear-gradient(135deg, rgba(46,139,87,0.08) 0%, rgba(46,139,87,0.03) 100%);
        border-left: 4px solid {ACCENT_GREEN};
        border-radius: 0 8px 8px 0;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
    }}
    .insight-box .box-title {{
        color: {ACCENT_GREEN};
        font-weight: 700;
        font-size: 0.95rem;
        margin-bottom: 0.5rem;
    }}

    .formula-box {{
        background: #f0f4f8;
        border: 1px solid #d0d8e0;
        border-radius: 6px;
        padding: 0.8rem 1.2rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.92rem;
        color: {DARK_BLUE};
        margin: 0.5rem 0;
    }}

    .metric-card {{
        background: white;
        border-radius: 10px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 2px 10px rgba(0,51,102,0.08);
        border-top: 3px solid {DARK_BLUE};
    }}
    .metric-card .value {{
        font-size: 2rem;
        font-weight: 700;
        color: {DARK_BLUE};
        font-family: 'Playfair Display', serif;
    }}
    .metric-card .label {{
        color: #666;
        font-size: 0.85rem;
        font-family: 'Source Sans 3', sans-serif;
    }}

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0;
        background: {DARK_BLUE};
        border-radius: 8px 8px 0 0;
        padding: 4px 4px 0 4px;
    }}
    .stTabs [data-baseweb="tab"] {{
        color: {LIGHT_BLUE};
        border-radius: 6px 6px 0 0;
        padding: 8px 18px;
        font-family: 'Source Sans 3', sans-serif;
        font-weight: 500;
    }}
    .stTabs [aria-selected="true"] {{
        background: white !important;
        color: {DARK_BLUE} !important;
        font-weight: 700;
    }}

    /* Dataframe styling */
    .stDataFrame {{
        border-radius: 8px;
        overflow: hidden;
    }}

    /* Footer */
    .mp-footer {{
        text-align: center;
        padding: 1.5rem;
        color: #888;
        font-size: 0.85rem;
        border-top: 1px solid #e0e0e0;
        margin-top: 2rem;
    }}
</style>
""", unsafe_allow_html=True)

# =============================================================================
# PLOTLY THEME
# =============================================================================
MP_COLORS = [DARK_BLUE, GOLD, "#4A90D9", ACCENT_GREEN, "#E67E22", "#8E44AD", LIGHT_BLUE, "#C0392B"]

def mp_layout(fig, title="", height=420):
    fig.update_layout(
        title=dict(text=title, font=dict(family="Playfair Display, serif", size=18, color=DARK_BLUE), x=0.5),
        font=dict(family="Source Sans Pro, sans-serif", color="#333"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=height,
        margin=dict(l=50, r=30, t=60, b=40),
        legend=dict(bgcolor="rgba(255,255,255,0.8)", bordercolor=DARK_BLUE, borderwidth=1),
    )
    fig.update_xaxes(gridcolor="#e8e8e8", zeroline=False)
    fig.update_yaxes(gridcolor="#e8e8e8", zeroline=False)
    return fig


def defn_box(title, content):
    st.markdown(f"""<div class="defn-box"><div class="box-title">{title}</div><br>{content}</div>""", unsafe_allow_html=True)

def example_box(title, content):
    st.markdown(f"""<div class="example-box"><div class="box-title">{title}</div><br>{content}</div>""", unsafe_allow_html=True)

def insight_box(content):
    st.markdown(f"""<div class="insight-box"><div class="box-title">Key Insight</div><br>{content}</div>""", unsafe_allow_html=True)

def formula_block(text):
    st.markdown(f"""<div class="formula-box">{text}</div>""", unsafe_allow_html=True)

def metric_card(label, value):
    return f"""<div class="metric-card"><div class="value">{value}</div><div class="label">{label}</div></div>"""


# =============================================================================
# SIDEBAR
# =============================================================================
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

    page = st.radio(
        "Navigate",
        [
            "Home",
            "1. Cleaning",
            "2. Standardize",
            "3. Aggregate",
            "4. Pivot",
            "5. Normalize",
            "6. Categorize",
            "7. Categorical Encode",
            "8. FreshMart Caselet",
        ],
        index=0,
    )

    st.markdown("---")
    st.markdown("""
    <div style="text-align:center; padding:0.5rem 0; font-size:0.82rem; color:rgba(173,216,230,0.7);">
        Prof. V. Ravichandran<br>
        <span style="color:#FFD700;">themountainpathacademy.com</span>
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
    reasons = [
        ("Messy Data", "Typos, blanks, and inconsistent formats break analysis tools."),
        ("Structure Needed", "Charts, formulas, and ML need one row per observation."),
        ("Common Scale", "Comparisons require percentages, z-scores, or same units."),
        ("Summarization", "Decisions need summaries, not millions of raw rows."),
        ("Pattern Discovery", "Categorizing continuous values reveals hidden trends."),
    ]
    for c, (title, desc) in zip(cols, reasons):
        with c:
            st.markdown(f"""
            <div class="metric-card" style="min-height:160px; border-top-color:{GOLD};">
                <div class="value" style="font-size:1.1rem; color:{DARK_BLUE};">{title}</div>
                <div class="label" style="margin-top:0.5rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### The 7 Transformations")

    transform_data = pd.DataFrame({
        "Step": ["1. Cleaning", "2. Standardize", "3. Aggregate", "4. Pivot", "5. Normalize", "6. Categorize", "7. Categorical Encode"],
        "What it does": [
            "Trim spaces, fix case, handle blanks",
            "Convert units and formats to a common scale",
            "Summarize many rows into per-group totals",
            "Reshape long data into wide comparison table",
            "Rescale numbers to a common 0-1 range",
            "Bucket continuous numbers into labeled groups",
            "Convert text categories to numbers (ordinal vs one-hot)",
        ],
        "Key Excel Functions": [
            "TRIM, PROPER, IF",
            "IF (unit conversion), DATEVALUE",
            "SUMIF, COUNTIF, AVERAGEIF",
            "SUMIFS (row + column criteria)",
            "(x - MIN) / (MAX - MIN)",
            "Nested IF / IFS",
            "MATCH / IF columns",
        ],
    })

    # Pipeline visualization
    fig = go.Figure()
    steps = ["Raw\nData", "Clean", "Standardize", "Aggregate", "Pivot", "Normalize", "Categorize", "Encode", "Analysis\nReady"]
    x_pos = list(range(len(steps)))
    colors = ["#999"] + [DARK_BLUE]*7 + [ACCENT_GREEN]

    for i in range(len(steps)):
        fig.add_trace(go.Scatter(
            x=[x_pos[i]], y=[0], mode="markers+text",
            marker=dict(size=52, color=colors[i], line=dict(width=2, color="white")),
            text=[steps[i]], textposition="middle center",
            textfont=dict(color="white", size=9, family="Source Sans Pro"),
            showlegend=False, hoverinfo="skip",
        ))
    for i in range(len(steps)-1):
        fig.add_annotation(x=x_pos[i]+0.35, y=0, ax=x_pos[i+1]-0.35, ay=0,
                           xref="x", yref="y", axref="x", ayref="y",
                           showarrow=True, arrowhead=2, arrowsize=1.3,
                           arrowwidth=2, arrowcolor=GOLD)

    fig.update_layout(
        height=130, margin=dict(l=10, r=10, t=10, b=10),
        xaxis=dict(visible=False, range=[-0.5, 8.5]),
        yaxis=dict(visible=False, range=[-0.5, 0.5]),
        plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(transform_data, use_container_width=True, hide_index=True)

    insight_box("Each coloured tab in the sidebar covers <strong>one transformation</strong>: raw data on the left, transformed data on the right, with interactive charts and the Excel formulas that produce each result.")


# =============================================================================
# PAGE 1: CLEANING
# =============================================================================
elif page == "1. Cleaning":
    st.markdown("""<div class="mp-brand-header"><h1>1. Data Cleaning</h1>
    <div class="subtitle">Trim Spaces &bull; Fix Case &bull; Handle Blanks</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "The same name written 4 different ways (<code>' &nbsp;apple '</code>, <code>'APPLE'</code>, <code>'Apple'</code>, <code>' banana'</code>) cannot be grouped or counted until they match.")

    raw = pd.DataFrame({
        "Raw Name": ["  apple ", "APPLE", "Apple", " banana", "BANANA ", "(blank)", "cherry"],
        "Sales": [10, 15, 8, 7, 12, 5, 9],
    })
    cleaned = pd.DataFrame({
        "Cleaned Name": ["Apple", "Apple", "Apple", "Banana", "Banana", "(missing)", "Cherry"],
        "Sales": [10, 15, 8, 7, 12, 5, 9],
    })

    tab1, tab2, tab3 = st.tabs(["Before & After", "Interactive Chart", "Excel Formulas"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"#### Raw Data")
            st.dataframe(raw, use_container_width=True, hide_index=True)
        with c2:
            st.markdown(f"#### Cleaned Data")
            st.dataframe(cleaned, use_container_width=True, hide_index=True)

        summary = pd.DataFrame({"Product": ["Apple", "Banana", "Cherry", "(missing)"], "Total Sales": [33, 19, 9, 5]})
        fig = go.Figure()
        fig.add_trace(go.Bar(x=summary["Product"], y=summary["Total Sales"],
                             marker_color=[DARK_BLUE, GOLD, ACCENT_GREEN, "#ccc"],
                             text=summary["Total Sales"], textposition="outside"))
        mp_layout(fig, "Sales After Cleaning & Grouping", 350)
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("#### Try It: What happens without cleaning?")
        # Show raw vs cleaned counts
        raw_counts = pd.DataFrame({
            "Name (as entered)": ["  apple ", "APPLE", "Apple", " banana", "BANANA ", "(blank)", "cherry"],
            "Would Count As": ["Separate item"]*7,
            "Sales": [10, 15, 8, 7, 12, 5, 9],
        })
        fig2 = make_subplots(rows=1, cols=2, subplot_titles=("Without Cleaning (7 items)", "With Cleaning (4 groups)"))
        fig2.add_trace(go.Bar(x=["  apple ", "APPLE", "Apple", " banana", "BANANA ", "(blank)", "cherry"],
                              y=[10, 15, 8, 7, 12, 5, 9], marker_color="#CC4444", name="Uncleaned"), row=1, col=1)
        fig2.add_trace(go.Bar(x=["Apple", "Banana", "Cherry", "(missing)"],
                              y=[33, 19, 9, 5], marker_color=DARK_BLUE, name="Cleaned"), row=1, col=2)
        mp_layout(fig2, "", 380)
        fig2.update_layout(showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

        insight_box("Without cleaning, <strong>Apple appears as 3 separate items</strong> totalling 10+15+8 individually. After TRIM + PROPER, they merge into one group with <strong>33 total sales</strong>.")

    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block("=PROPER(TRIM(A2)) &nbsp;&nbsp;&mdash; removes leading/trailing spaces, then capitalizes first letter")
        formula_block('=IF(A2="", "(missing)", PROPER(TRIM(A2))) &nbsp;&nbsp;&mdash; also flags blank cells')
        formula_block("=SUMIF(D:D, A13, E:E) &nbsp;&nbsp;&mdash; sum sales for each cleaned product name")
        formula_block("=CLEAN(A2) &nbsp;&nbsp;&mdash; removes non-printable characters (line breaks, tabs)")

        example_box("Multi-Space Cleaning",
                     '<code>"apple&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; fruit&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1234&nbsp;&nbsp; abc"</code><br>'
                     'After TRIM + PROPER &rarr; <code>"Apple Fruit 1234 Abc"</code><br>'
                     'TRIM collapses <em>internal</em> multi-spaces to single spaces too.')


# =============================================================================
# PAGE 2: STANDARDIZE
# =============================================================================
elif page == "2. Standardize":
    st.markdown("""<div class="mp-brand-header"><h1>2. Standardize</h1>
    <div class="subtitle">Convert Units &bull; Parse Dates &bull; Common Scale</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "Weights are mixed (lbs vs kg) and dates are stored as text strings (<code>'20240115'</code>). You cannot SUM weights or SORT by date until every value is on the same scale and in the correct format.")

    raw_std = pd.DataFrame({
        "Item": ["Item A", "Item B", "Item C", "Item D", "Item E"],
        "Weight": [10, 5, 22, 3, 50],
        "Unit": ["lb", "kg", "lb", "kg", "lb"],
        "Date (text)": ["20240115", "20240203", "20240220", "20240301", "20240318"],
    })
    std = pd.DataFrame({
        "Item": ["Item A", "Item B", "Item C", "Item D", "Item E"],
        "Weight (kg)": [4.536, 5.000, 9.979, 3.000, 22.680],
        "Real Date": ["2024-01-15", "2024-02-03", "2024-02-20", "2024-03-01", "2024-03-18"],
    })

    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Chart", "Excel Formulas"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Raw Data")
            st.dataframe(raw_std, use_container_width=True, hide_index=True)
        with c2:
            st.markdown("#### Standardized Data")
            st.dataframe(std, use_container_width=True, hide_index=True)

    with tab2:
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Original Value", x=raw_std["Item"], y=raw_std["Weight"],
                             marker_color=GOLD, text=[f"{w} {u}" for w, u in zip(raw_std["Weight"], raw_std["Unit"])], textposition="outside"))
        fig.add_trace(go.Bar(name="Standardized (kg)", x=std["Item"], y=std["Weight (kg)"],
                             marker_color=DARK_BLUE, text=[f"{w:.1f} kg" for w in std["Weight (kg)"]], textposition="outside"))
        mp_layout(fig, "Weight Standardization: Original vs Converted", 400)
        fig.update_layout(barmode="group")
        st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"""
        <div class="metric-card" style="border-top-color:{ACCENT_GREEN};">
            <div class="value">45.20 kg</div>
            <div class="label">Total Weight (now computable after standardization)</div>
        </div>
        """, unsafe_allow_html=True)

    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block('=IF(C2="lb", B2 * 0.4536, B2) &nbsp;&nbsp;&mdash; converts lbs to kg, keeps kg as-is')
        formula_block('=DATE(LEFT(D2,4), MID(D2,5,2), RIGHT(D2,2)) &nbsp;&nbsp;&mdash; parses "20240115" into a real date')
        insight_box("Once everything is in <strong>kg</strong> and a real date format, you can SUM weights and SORT by date. Without standardizing, neither operation works correctly.")


# =============================================================================
# PAGE 3: AGGREGATE
# =============================================================================
elif page == "3. Aggregate":
    st.markdown("""<div class="mp-brand-header"><h1>3. Aggregate</h1>
    <div class="subtitle">SUMIF &bull; COUNTIF &bull; AVERAGEIF</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "10 rows of individual sales tell us very little. <em>Which region performed best?</em> We must aggregate the raw transactions into per-group summaries to find out.")

    raw_agg = pd.DataFrame({
        "Order": [f"Order {i}" for i in range(1, 11)],
        "Region": ["North", "South", "North", "East", "South", "West", "North", "East", "West", "South"],
        "Sales": [120, 90, 75, 200, 60, 150, 95, 110, 80, 130],
    })
    agg = pd.DataFrame({
        "Region": ["North", "South", "East", "West"],
        "Total Sales": [290, 280, 310, 230],
        "Order Count": [3, 3, 2, 2],
        "Avg Order": [96.67, 93.33, 155.00, 115.00],
    })

    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Charts", "Excel Formulas"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Raw Transactions (10 orders)")
            st.dataframe(raw_agg, use_container_width=True, hide_index=True)
        with c2:
            st.markdown("#### Aggregated by Region")
            st.dataframe(agg, use_container_width=True, hide_index=True)

    with tab2:
        chart_type = st.selectbox("Chart type", ["Bar Chart", "Pie Chart", "Treemap"], key="agg_chart")

        if chart_type == "Bar Chart":
            fig = go.Figure()
            fig.add_trace(go.Bar(x=agg["Region"], y=agg["Total Sales"], name="Total Sales",
                                 marker_color=DARK_BLUE, text=agg["Total Sales"], textposition="outside"))
            fig.add_trace(go.Bar(x=agg["Region"], y=agg["Avg Order"], name="Avg Order",
                                 marker_color=GOLD, text=[f"${v:.0f}" for v in agg["Avg Order"]], textposition="outside"))
            mp_layout(fig, "Regional Sales Summary", 400)
            fig.update_layout(barmode="group")
        elif chart_type == "Pie Chart":
            fig = px.pie(agg, values="Total Sales", names="Region",
                         color_discrete_sequence=[DARK_BLUE, GOLD, ACCENT_GREEN, LIGHT_BLUE])
            mp_layout(fig, "Sales Distribution by Region", 400)
        else:
            fig = px.treemap(agg, path=["Region"], values="Total Sales",
                             color="Total Sales", color_continuous_scale=[[0, LIGHT_BLUE], [1, DARK_BLUE]])
            mp_layout(fig, "Sales Treemap by Region", 400)
        st.plotly_chart(fig, use_container_width=True)

        cols = st.columns(4)
        for c, (_, r) in zip(cols, agg.iterrows()):
            with c:
                st.markdown(metric_card(f"{r['Region']} ({r['Order Count']} orders)", f"${r['Total Sales']:,.0f}"), unsafe_allow_html=True)

    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block("=SUMIF(B:B, E3, C:C) &nbsp;&nbsp;&mdash; total sales for a given region")
        formula_block("=COUNTIF(B:B, E3) &nbsp;&nbsp;&mdash; number of orders in that region")
        formula_block("=AVERAGEIF(B:B, E3, C:C) &nbsp;&nbsp;&mdash; average order value per region")
        insight_box("<strong>Grand Total check:</strong> 290 + 280 + 310 + 230 = <strong>1,110</strong>, matching the sum of all 10 raw orders. Aggregation preserves totals while revealing regional patterns.")


# =============================================================================
# PAGE 4: PIVOT
# =============================================================================
elif page == "4. Pivot":
    st.markdown("""<div class="mp-brand-header"><h1>4. Pivot</h1>
    <div class="subtitle">Reshape Long Data &rarr; Wide Comparison Table</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "Data is in <strong>long</strong> form (1 row per region-quarter combination = 12 rows). Reshaping it <strong>wide</strong> so each quarter becomes a column makes comparison far easier.")

    long_data = pd.DataFrame({
        "Region": ["North"]*4 + ["South"]*4 + ["East"]*4,
        "Quarter": ["Q1", "Q2", "Q3", "Q4"]*3,
        "Sales": [100, 120, 130, 150, 80, 95, 110, 125, 60, 70, 90, 105],
    })
    wide_data = pd.DataFrame({
        "Region": ["North", "South", "East"],
        "Q1": [100, 80, 60],
        "Q2": [120, 95, 70],
        "Q3": [130, 110, 90],
        "Q4": [150, 125, 105],
    })
    wide_data["Total"] = wide_data[["Q1", "Q2", "Q3", "Q4"]].sum(axis=1)

    tab1, tab2, tab3 = st.tabs(["Data View", "Interactive Heatmap", "Excel Formulas"])

    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("#### Long Format (12 rows)")
            st.dataframe(long_data, use_container_width=True, hide_index=True)
        with c2:
            st.markdown("#### Wide / Pivoted Format (3 rows)")
            st.dataframe(wide_data, use_container_width=True, hide_index=True)

    with tab2:
        view = st.radio("View", ["Heatmap", "Grouped Bars", "Line Trend"], horizontal=True, key="pivot_view")
        if view == "Heatmap":
            z = [wide_data.loc[i, ["Q1","Q2","Q3","Q4"]].tolist() for i in range(3)]
            fig = go.Figure(go.Heatmap(
                z=z, x=["Q1","Q2","Q3","Q4"], y=["North","South","East"],
                colorscale=[[0, LIGHT_BLUE], [0.5, "#4A90D9"], [1, DARK_BLUE]],
                text=z, texttemplate="%{text}", textfont=dict(size=16, color="white"),
            ))
            mp_layout(fig, "Sales Heatmap: Region x Quarter", 350)
        elif view == "Grouped Bars":
            fig = go.Figure()
            for q in ["Q1","Q2","Q3","Q4"]:
                fig.add_trace(go.Bar(name=q, x=wide_data["Region"], y=wide_data[q],
                                     text=wide_data[q], textposition="outside"))
            fig.update_traces(marker_color=None)
            fig.update_layout(colorway=[DARK_BLUE, GOLD, ACCENT_GREEN, "#E67E22"])
            mp_layout(fig, "Quarterly Sales by Region", 400)
            fig.update_layout(barmode="group")
        else:
            fig = go.Figure()
            colors_line = [DARK_BLUE, GOLD, ACCENT_GREEN]
            for i, region in enumerate(["North","South","East"]):
                vals = wide_data[wide_data["Region"]==region][["Q1","Q2","Q3","Q4"]].values[0]
                fig.add_trace(go.Scatter(x=["Q1","Q2","Q3","Q4"], y=vals, mode="lines+markers",
                                         name=region, line=dict(width=3, color=colors_line[i]),
                                         marker=dict(size=10)))
            mp_layout(fig, "Quarterly Trend by Region", 400)
        st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block('=SUMIFS(C:C, A:A, E4, B:B, F3) &nbsp;&nbsp;&mdash; looks up Sales where Region=row label AND Quarter=column header')
        example_box("How SUMIFS Pivots",
                     "Cell F4 (North, Q1): <code>=SUMIFS($C$4:$C$15, $A$4:$A$15, $E4, $B$4:$B$15, F$3)</code><br>"
                     "The mixed references (<code>$E4</code> locks column, <code>F$3</code> locks row) let you copy the formula across the entire grid.")


# =============================================================================
# PAGE 5: NORMALIZE
# =============================================================================
elif page == "5. Normalize":
    st.markdown("""<div class="mp-brand-header"><h1>5. Normalize</h1>
    <div class="subtitle">Min-Max Scaling &bull; Rescale to 0&ndash;1 &bull; Compare Shape</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "Store sales (~$1000s) and items sold (~10s) live on completely different scales. Charting them together hides the smaller series. Rescale both to 0&ndash;1 to compare their <em>shape</em>.")

    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    sales = [1200, 950, 1500, 800, 2200, 2800, 1700]
    items = [18, 14, 22, 11, 30, 38, 25]
    s_min, s_max = min(sales), max(sales)
    i_min, i_max = min(items), max(items)
    sales_norm = [(v - s_min) / (s_max - s_min) for v in sales]
    items_norm = [(v - i_min) / (i_max - i_min) for v in items]

    tab1, tab2, tab3 = st.tabs(["Raw vs Normalized", "Interactive Explorer", "Excel Formulas"])

    with tab1:
        fig = make_subplots(rows=1, cols=2, subplot_titles=("Raw (different scales)", "Normalized (0-1 scale)"))
        fig.add_trace(go.Bar(x=days, y=sales, name="Sales ($)", marker_color=DARK_BLUE), row=1, col=1)
        fig.add_trace(go.Bar(x=days, y=items, name="Items Sold", marker_color=GOLD), row=1, col=1)
        fig.add_trace(go.Scatter(x=days, y=sales_norm, name="Sales (norm)", line=dict(color=DARK_BLUE, width=3), mode="lines+markers"), row=1, col=2)
        fig.add_trace(go.Scatter(x=days, y=items_norm, name="Items (norm)", line=dict(color=GOLD, width=3), mode="lines+markers"), row=1, col=2)
        mp_layout(fig, "", 400)
        st.plotly_chart(fig, use_container_width=True)

        insight_box("On the raw chart, Items Sold is invisible next to Sales. After normalization, both series are on the same 0&ndash;1 scale and you can see they follow <strong>almost the same pattern</strong> &mdash; peaking on Saturday.")

    with tab2:
        st.markdown("#### Adjust Values and See Normalization Live")
        edit_cols = st.columns(7)
        new_sales = []
        for i, (d, s) in enumerate(zip(days, sales)):
            with edit_cols[i]:
                new_sales.append(st.number_input(d, value=s, step=100, key=f"ns_{i}"))

        ns_min, ns_max = min(new_sales), max(new_sales)
        if ns_max > ns_min:
            new_norm = [(v - ns_min) / (ns_max - ns_min) for v in new_sales]
        else:
            new_norm = [0]*7

        df_live = pd.DataFrame({"Day": days, "Sales ($)": new_sales, "Normalized": [f"{v:.3f}" for v in new_norm]})
        st.dataframe(df_live, use_container_width=True, hide_index=True)

        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=days, y=new_norm, marker_color=[DARK_BLUE if v < 1 else GOLD for v in new_norm],
                              text=[f"{v:.2f}" for v in new_norm], textposition="outside"))
        mp_layout(fig3, "Your Normalized Values", 350)
        fig3.update_yaxes(range=[0, 1.15])
        st.plotly_chart(fig3, use_container_width=True)

    with tab3:
        st.markdown("#### The Min-Max Formula")
        formula_block("Normalized = (x &minus; min) / (max &minus; min)")
        formula_block("=(B2 - MIN($B$2:$B$8)) / (MAX($B$2:$B$8) - MIN($B$2:$B$8))")
        example_box("Worked Example",
                     f"Monday Sales = $1,200<br>Min = ${s_min:,} (Thu) &nbsp; Max = ${s_max:,} (Sat)<br>"
                     f"Normalized = (1200 &minus; {s_min}) / ({s_max} &minus; {s_min}) = {(1200-s_min)/(s_max-s_min):.3f}")


# =============================================================================
# PAGE 6: CATEGORIZE
# =============================================================================
elif page == "6. Categorize":
    st.markdown("""<div class="mp-brand-header"><h1>6. Categorize</h1>
    <div class="subtitle">Bucket Continuous Numbers into Labeled Groups</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "A list of ages or test scores is hard to summarize. Bucket them into labels (<strong>Youth / Adult / Senior</strong>; <strong>Fail / Pass / Distinction</strong>) so you can count and chart distributions.")

    cat_data = pd.DataFrame({
        "Name": ["Anna", "Ben", "Cara", "Dan", "Eli", "Fay", "Gus", "Hal"],
        "Age": [12, 17, 25, 34, 47, 58, 66, 73],
        "Score": [45, 72, 88, 55, 91, 38, 76, 60],
        "Age Group": ["Youth", "Youth", "Adult", "Adult", "Adult", "Adult", "Senior", "Senior"],
        "Grade": ["Fail", "Pass", "Distinction", "Pass", "Distinction", "Fail", "Distinction", "Pass"],
    })

    tab1, tab2, tab3 = st.tabs(["Data & Charts", "Custom Buckets", "Excel Formulas"])

    with tab1:
        st.dataframe(cat_data, use_container_width=True, hide_index=True)

        c1, c2 = st.columns(2)
        with c1:
            age_counts = cat_data["Age Group"].value_counts().reindex(["Youth", "Adult", "Senior"])
            fig = go.Figure(go.Bar(x=age_counts.index, y=age_counts.values,
                                   marker_color=[GOLD, DARK_BLUE, ACCENT_GREEN],
                                   text=age_counts.values, textposition="outside"))
            mp_layout(fig, "Age Group Distribution", 350)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            grade_counts = cat_data["Grade"].value_counts().reindex(["Fail", "Pass", "Distinction"])
            fig2 = go.Figure(go.Bar(x=grade_counts.index, y=grade_counts.values,
                                    marker_color=["#CC4444", GOLD, DARK_BLUE],
                                    text=grade_counts.values, textposition="outside"))
            mp_layout(fig2, "Grade Distribution", 350)
            st.plotly_chart(fig2, use_container_width=True)

    with tab2:
        st.markdown("#### Create Your Own Age Buckets")
        bc1, bc2 = st.columns(2)
        with bc1:
            cut1 = st.slider("Youth / Adult boundary", 10, 60, 18, key="cut1")
        with bc2:
            cut2 = st.slider("Adult / Senior boundary", 30, 80, 60, key="cut2")

        if cut1 >= cut2:
            st.warning("Youth boundary must be less than Senior boundary.")
        else:
            def bucket(age):
                if age < cut1: return "Youth"
                elif age < cut2: return "Adult"
                else: return "Senior"
            custom = cat_data.copy()
            custom["Custom Group"] = custom["Age"].apply(bucket)
            counts = custom["Custom Group"].value_counts().reindex(["Youth", "Adult", "Senior"]).fillna(0)
            fig3 = go.Figure(go.Bar(x=counts.index, y=counts.values,
                                    marker_color=[GOLD, DARK_BLUE, ACCENT_GREEN],
                                    text=counts.values.astype(int), textposition="outside"))
            mp_layout(fig3, f"Custom Buckets: Youth (<{cut1}) | Adult ({cut1}-{cut2}) | Senior ({cut2}+)", 350)
            st.plotly_chart(fig3, use_container_width=True)

    with tab3:
        st.markdown("#### Excel Formulas Used")
        formula_block('=IF(B2<18, "Youth", IF(B2<60, "Adult", "Senior")) &nbsp;&nbsp;&mdash; nested IF for age groups')
        formula_block('=IF(C2>=75, "Distinction", IF(C2>=50, "Pass", "Fail")) &nbsp;&nbsp;&mdash; grade boundaries')
        formula_block('=COUNTIF(D:D, "Youth") &nbsp;&nbsp;&mdash; count how many fall in each bucket')
        insight_box("Nested IF maps a continuous number to a label. COUNTIF then summarizes the labels into a distribution &mdash; perfect for bar charts and pivot tables.")


# =============================================================================
# PAGE 7: CATEGORICAL ENCODE
# =============================================================================
elif page == "7. Categorical Encode":
    st.markdown("""<div class="mp-brand-header"><h1>7. Categorical Encoding</h1>
    <div class="subtitle">Ordinal (Ranked) vs Nominal (One-Hot)</div></div>""", unsafe_allow_html=True)

    defn_box("The Problem", "Charts, formulas, and ML models need <strong>numbers</strong>, not text. How we convert text &rarr; numbers depends on whether the categories have a <strong>natural order</strong>.")

    tab1, tab2, tab3 = st.tabs(["Ordinal Encoding", "One-Hot Encoding", "Excel Formulas"])

    with tab1:
        st.markdown("### Ordinal: Categories with a Natural Rank")
        example_box("When to Use Ordinal",
                     "T-shirt size (S &lt; M &lt; L &lt; XL), Satisfaction (Poor &lt; Fair &lt; Good &lt; Excellent), Education level")

        ord_data = pd.DataFrame({
            "Customer": [f"Cust {i}" for i in range(1, 9)],
            "Satisfaction": ["Good", "Excellent", "Poor", "Fair", "Good", "Excellent", "Fair", "Good"],
            "Score (1-4)": [3, 4, 1, 2, 3, 4, 2, 3],
        })
        c1, c2 = st.columns([2, 1])
        with c1:
            st.dataframe(ord_data, use_container_width=True, hide_index=True)
        with c2:
            st.markdown(metric_card("Average Satisfaction Score", "2.75 / 4"), unsafe_allow_html=True)

        mapping = pd.DataFrame({"Category": ["Poor", "Fair", "Good", "Excellent"], "Score": [1, 2, 3, 4]})
        fig = go.Figure(go.Bar(x=mapping["Category"], y=mapping["Score"],
                               marker_color=[f"rgba(0,51,102,{0.25+i*0.25})" for i in range(4)],
                               text=mapping["Score"], textposition="outside"))
        mp_layout(fig, "Ordinal Mapping: Satisfaction", 320)
        st.plotly_chart(fig, use_container_width=True)

        insight_box("Excellent (4) > Good (3) > Fair (2) > Poor (1). Numbers <strong>preserve the order</strong>, so AVERAGE and trend charts are meaningful.")

    with tab2:
        st.markdown("### Nominal: Categories Without Order")
        example_box("When to Use One-Hot",
                     "Color (Red, Blue, Green), City (NY, LA, Chicago), Payment method (Cash, Card, UPI). "
                     "Using 1, 2, 3 would falsely imply Green > Red!")

        st.markdown("#### Color Encoding Example")
        color_raw = pd.DataFrame({"Item": [1, 2, 3, 4, 5], "Color": ["Red", "Blue", "Green", "Red", "Blue"]})
        color_enc = pd.DataFrame({
            "Item": [1, 2, 3, 4, 5], "Color": ["Red", "Blue", "Green", "Red", "Blue"],
            "is_Red": [1, 0, 0, 1, 0], "is_Blue": [0, 1, 0, 0, 1], "is_Green": [0, 0, 1, 0, 0],
        })
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**Raw**")
            st.dataframe(color_raw, use_container_width=True, hide_index=True)
        with c2:
            st.markdown("**One-Hot Encoded**")
            st.dataframe(color_enc, use_container_width=True, hide_index=True)

        # Visual
        fig2 = go.Figure()
        for i, col in enumerate(["is_Red", "is_Blue", "is_Green"]):
            fig2.add_trace(go.Bar(name=col.replace("is_",""), x=[f"Item {j}" for j in range(1,6)],
                                  y=color_enc[col], marker_color=["#CC4444", DARK_BLUE, ACCENT_GREEN][i]))
        mp_layout(fig2, "One-Hot Encoding Visualization", 350)
        fig2.update_layout(barmode="stack")
        st.plotly_chart(fig2, use_container_width=True)

    with tab3:
        st.markdown("#### Excel Formulas")
        st.markdown("**Ordinal Encoding:**")
        formula_block('=MATCH(B2, {"Poor","Fair","Good","Excellent"}, 0) &nbsp;&nbsp;&mdash; returns rank 1-4')
        st.markdown("**One-Hot Encoding:**")
        formula_block('=IF($B2="Red", 1, 0) &nbsp;&nbsp;&mdash; one formula per category column')
        formula_block('=IF($B2="Blue", 1, 0)')
        formula_block('=IF($B2="Green", 1, 0)')
        insight_box("Each row sums to exactly <strong>1</strong> across the one-hot columns &mdash; every item belongs to exactly one category. This is the standard encoding for nominal data in analytics and machine learning.")


# =============================================================================
# PAGE 8: CASELET
# =============================================================================
elif page == "8. FreshMart Caselet":
    st.markdown("""<div class="mp-brand-header"><h1>FreshMart Caselet</h1>
    <div class="subtitle">Cleaning &amp; Transforming Retail Sales Data &mdash; End-to-End Exercise</div></div>""", unsafe_allow_html=True)

    defn_box("Scenario", "FreshMart, a small retail chain, exported 12 orders from 3 stores. The data is messy: "
             "inconsistent region names, mixed currencies (USD/INR), text dates, and an order with a missing region. "
             "Apply data transformations to answer <strong>5 business questions</strong>.<br><br>"
             "<strong>Conversion rate:</strong> 1 USD = 83 INR")

    raw_caselet = pd.DataFrame({
        "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
        "Region": [" north ","SOUTH","North","east","","South ","EAST","north","South"," East","NORTH","south"],
        "Product": ["Apples","Bread","Milk","Apples","Bread","Milk","Apples","Bread","Apples","Milk","Milk","Apples"],
        "Qty": [10,5,8,12,6,15,9,4,20,7,11,14],
        "Amount": [50,1245,24,4980,18,3735,45,996,180,1743,33,12450],
        "Currency": ["USD","INR","USD","INR","USD","INR","USD","INR","USD","INR","USD","INR"],
        "Date (text)": ["20240105","20240108","20240115","20240118","20240122","20240204","20240210","20240215","20240220","20240301","20240310","20240315"],
    })

    clean_caselet = pd.DataFrame({
        "OrderID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012],
        "Region": ["North","South","North","East","Unknown","South","East","North","South","East","North","South"],
        "Product": ["Apples","Bread","Milk","Apples","Bread","Milk","Apples","Bread","Apples","Milk","Milk","Apples"],
        "Qty": [10,5,8,12,6,15,9,4,20,7,11,14],
        "Amount (USD)": [50.00, 15.00, 24.00, 60.00, 18.00, 45.00, 45.00, 12.00, 180.00, 21.00, 33.00, 150.00],
        "Date": pd.to_datetime(["2024-01-05","2024-01-08","2024-01-15","2024-01-18","2024-01-22","2024-02-04","2024-02-10","2024-02-15","2024-02-20","2024-03-01","2024-03-10","2024-03-15"]),
        "Month": ["Jan","Jan","Jan","Jan","Jan","Feb","Feb","Feb","Feb","Mar","Mar","Mar"],
        "Size Bucket": ["Medium","Small","Small","Medium","Small","Small","Small","Small","Large","Small","Small","Large"],
    })

    tab1, tab2, tab3, tab4 = st.tabs(["Raw vs Clean", "5 Business Questions", "Transformations Applied", "Interactive Explorer"])

    with tab1:
        st.markdown("#### Step 1: Raw Data (as exported)")
        st.dataframe(raw_caselet, use_container_width=True, hide_index=True)

        st.markdown("#### Step 3: Cleaned & Transformed Data")
        st.dataframe(clean_caselet.drop(columns=["Date"]).assign(Date=clean_caselet["Date"].dt.strftime("%Y-%m-%d")),
                     use_container_width=True, hide_index=True)

    with tab2:
        st.markdown("### Answers to the 5 Business Questions")

        # Q1 & Q2
        region_summary = clean_caselet.groupby("Region").agg(
            Total_Sales=("Amount (USD)", "sum"),
            Order_Count=("Amount (USD)", "count"),
            Avg_Order=("Amount (USD)", "mean"),
        ).round(2).reset_index()

        st.markdown("#### Q1: Which region had the highest total sales?")
        fig_q1 = go.Figure(go.Bar(x=region_summary["Region"], y=region_summary["Total_Sales"],
                                   marker_color=[DARK_BLUE if r != "South" else GOLD for r in region_summary["Region"]],
                                   text=[f"${v:,.0f}" for v in region_summary["Total_Sales"]], textposition="outside"))
        mp_layout(fig_q1, "Total Sales by Region (USD)", 350)
        st.plotly_chart(fig_q1, use_container_width=True)
        st.success("**Answer:** South with $390 in total sales (highest)")

        st.markdown("#### Q2: Average order value per region?")
        fig_q2 = go.Figure(go.Bar(x=region_summary["Region"], y=region_summary["Avg_Order"],
                                   marker_color=[DARK_BLUE, ACCENT_GREEN, GOLD, "#ccc"],
                                   text=[f"${v:,.0f}" for v in region_summary["Avg_Order"]], textposition="outside"))
        mp_layout(fig_q2, "Average Order Value by Region (USD)", 350)
        st.plotly_chart(fig_q2, use_container_width=True)

        # Q3
        st.markdown("#### Q3: % of total sales by product?")
        product_summary = clean_caselet.groupby("Product")["Amount (USD)"].sum().reset_index()
        product_summary["% of Total"] = (product_summary["Amount (USD)"] / product_summary["Amount (USD)"].sum() * 100).round(1)
        fig_q3 = px.pie(product_summary, values="Amount (USD)", names="Product",
                        color_discrete_sequence=[DARK_BLUE, GOLD, ACCENT_GREEN])
        mp_layout(fig_q3, "Sales Share by Product", 380)
        st.plotly_chart(fig_q3, use_container_width=True)

        # Q4
        st.markdown("#### Q4: Order size buckets?")
        bucket_counts = clean_caselet["Size Bucket"].value_counts().reindex(["Small", "Medium", "Large"]).fillna(0).astype(int)
        fig_q4 = go.Figure(go.Bar(x=bucket_counts.index, y=bucket_counts.values,
                                   marker_color=[LIGHT_BLUE, GOLD, DARK_BLUE],
                                   text=bucket_counts.values, textposition="outside"))
        mp_layout(fig_q4, "Order Size Distribution", 350)
        st.plotly_chart(fig_q4, use_container_width=True)

        # Q5
        st.markdown("#### Q5: Orders per month?")
        month_counts = clean_caselet["Month"].value_counts().reindex(["Jan", "Feb", "Mar"]).fillna(0).astype(int)
        fig_q5 = go.Figure(go.Bar(x=month_counts.index, y=month_counts.values,
                                   marker_color=[DARK_BLUE, GOLD, ACCENT_GREEN],
                                   text=month_counts.values, textposition="outside"))
        mp_layout(fig_q5, "Orders per Month (Jan-Mar 2024)", 350)
        st.plotly_chart(fig_q5, use_container_width=True)

    with tab3:
        st.markdown("### All 6 Transformations Applied in This Caselet")
        transforms = [
            ("1. Cleaning", "TRIM + PROPER on Region; flag blanks as 'Unknown'", "=IF(B2=\"\", \"Unknown\", PROPER(TRIM(B2)))"),
            ("2. Standardize", "Convert INR amounts to USD (rate=83); parse YYYYMMDD text into real dates", "=IF(F2=\"INR\", E2/83, E2)"),
            ("3. Aggregate", "SUMIF / COUNTIF / AVERAGEIF for region & product summaries", "=SUMIF(B:B, region, E:E)"),
            ("4. Normalize", "Percentage share of total sales by product", "=product_total / grand_total"),
            ("5. Categorize", "IF chain to bucket order amounts into Small/Medium/Large", "=IF(E2>100,\"Large\",IF(E2>=50,\"Medium\",\"Small\"))"),
            ("6. Reshape", "TEXT(date,\"mmm yyyy\") groups daily orders into monthly counts", "=TEXT(F2,\"mmm yyyy\")"),
        ]
        for name, desc, formula in transforms:
            st.markdown(f"""
            <div class="defn-box">
                <div class="box-title">{name}</div><br>
                {desc}
                <div class="formula-box" style="margin-top:0.5rem;">{formula}</div>
            </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### Explore the Data Yourself")
        col_choice = st.selectbox("Group by", ["Region", "Product", "Month", "Size Bucket"])
        metric_choice = st.selectbox("Metric", ["Total Sales (USD)", "Order Count", "Average Qty"])

        if metric_choice == "Total Sales (USD)":
            grouped = clean_caselet.groupby(col_choice)["Amount (USD)"].sum().reset_index()
            grouped.columns = [col_choice, "Value"]
            fmt = "${:,.0f}"
        elif metric_choice == "Order Count":
            grouped = clean_caselet.groupby(col_choice).size().reset_index(name="Value")
            fmt = "{:,.0f}"
        else:
            grouped = clean_caselet.groupby(col_choice)["Qty"].mean().round(1).reset_index()
            grouped.columns = [col_choice, "Value"]
            fmt = "{:,.1f}"

        fig_exp = go.Figure(go.Bar(
            x=grouped[col_choice], y=grouped["Value"],
            marker_color=[MP_COLORS[i % len(MP_COLORS)] for i in range(len(grouped))],
            text=[fmt.format(v) for v in grouped["Value"]], textposition="outside",
        ))
        mp_layout(fig_exp, f"{metric_choice} by {col_choice}", 400)
        st.plotly_chart(fig_exp, use_container_width=True)


# =============================================================================
# FOOTER
# =============================================================================
st.markdown("""
<div class="mp-footer">
    <strong>The Mountain Path &mdash; World of Finance</strong><br>
    Prof. V. Ravichandran &bull; themountainpathacademy.com<br>
    <em>Bridging Theory with Practice &bull; Excellence in Financial Education</em>
</div>
""", unsafe_allow_html=True)
