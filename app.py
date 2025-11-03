import streamlit as st
import pandas as pd
from utils.data_cleaner import clean_data
from utils.plot_generator import generate_plot
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(
    page_title="Smart Data Visualizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply Custom CSS (defined at bottom of file)
def apply_custom_css():
    st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Inter:wght@300;400;600;700&display=swap');
    
    /* Main background - Clean minimal */
    .stApp {
        background: #0a0a0a;
        font-family: 'Inter', sans-serif;
    }
    
    /* Pixelated font for headers */
    .pixel-font {
        font-family: 'Press Start 2P', cursive;
        line-height: 1.6;
    }
    
    /* Header styling */
    .main-header {
        font-family: 'Press Start 2P', cursive;
        font-size: 2rem;
        color: #ffffff;
        text-align: center;
        margin: 40px 0 20px 0;
        letter-spacing: 2px;
    }
    
    .sub-header {
        text-align: center;
        font-size: 0.95rem;
        color: #888888;
        margin-bottom: 60px;
        font-weight: 300;
        letter-spacing: 1px;
    }
    
    /* Section headers */
    .section-title {
        font-family: 'Press Start 2P', cursive;
        font-size: 0.85rem;
        color: #ffffff;
        margin: 50px 0 25px 0;
        padding-bottom: 12px;
        border-bottom: 2px solid #1a1a1a;
        letter-spacing: 1px;
    }
    
    /* File uploader */
    .stFileUploader {
        background: #111111;
        border-radius: 8px;
        padding: 30px;
        border: 1px solid #1a1a1a;
        transition: all 0.3s ease;
    }
    
    .stFileUploader:hover {
        border-color: #333333;
        background: #141414;
    }
    
    /* Button styling - Minimal black and white */
    .stButton>button {
        background: #000000;
        color: #ffffff;
        border-radius: 4px;
        padding: 16px 40px;
        font-size: 1rem;
        font-weight: 700;
        border: 2px solid #ffffff;
        transition: all 0.3s ease;
        width: 100%;
        letter-spacing: 2px;
        text-transform: uppercase;
        box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1);
    }
    
    .stButton>button:hover {
        background: #ffffff;
        color: #000000;
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.3);
        border-color: #ffffff;
    }
    
    /* Selectbox styling */
    .stSelectbox > div > div {
        background-color: #111111;
        color: #ffffff;
        border: 1px solid #1a1a1a;
        border-radius: 4px;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #333333;
    }
    
    /* Info boxes - Minimal */
    .stInfo {
        background: #111111;
        border-left: 3px solid #444444;
        border-radius: 4px;
        padding: 16px;
        color: #cccccc;
    }
    
    .stSuccess {
        background: #0a1a0a;
        border-left: 3px solid #00ff00;
        border-radius: 4px;
        padding: 16px;
        color: #00ff00;
    }
    
    .stWarning {
        background: #1a1a0a;
        border-left: 3px solid #ffff00;
        border-radius: 4px;
        padding: 16px;
        color: #ffff00;
    }
    
    .stError {
        background: #1a0a0a;
        border-left: 3px solid #ff0000;
        border-radius: 4px;
        padding: 16px;
        color: #ff0000;
    }
    
    /* Metric cards - Clean and minimal */
    div[data-testid="stMetric"] {
        background: #111111;
        padding: 24px;
        border-radius: 4px;
        border: 1px solid #1a1a1a;
        transition: all 0.2s ease;
    }
    
    div[data-testid="stMetric"]:hover {
        border-color: #333333;
        transform: translateY(-2px);
    }
    
    div[data-testid="stMetricValue"] {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 700;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #666666;
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #111111 !important;
        border-right: 2px solid #333333;
    }
    
    section[data-testid="stSidebar"] > div {
        background: #111111 !important;
    }
    
    section[data-testid="stSidebar"] h2 {
        font-family: 'Press Start 2P', cursive;
        font-size: 0.75rem;
        color: #ffffff;
        letter-spacing: 1px;
    }
    
    section[data-testid="stSidebar"] .stMarkdown {
        color: #ffffff !important;
    }
    
    /* Sidebar toggle button - Make it visible */
    button[kind="header"] {
        color: #ffffff !important;
        background-color: #111111 !important;
        border: 1px solid #ffffff !important;
    }
    
    button[kind="header"]:hover {
        color: #000000 !important;
        background-color: #ffffff !important;
        border: 1px solid #ffffff !important;
    }
    
    /* Sidebar collapse button when closed */
    [data-testid="collapsedControl"] {
        color: #ffffff !important;
        background-color: #111111 !important;
        border: 2px solid #ffffff !important;
        border-radius: 4px !important;
    }
    
    [data-testid="collapsedControl"]:hover {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-color: #ffffff !important;
    }
    
    /* Sidebar toggle SVG icons - Make visible */
    button[kind="header"] svg,
    [data-testid="collapsedControl"] svg {
        fill: #ffffff !important;
        stroke: #ffffff !important;
    }
    
    button[kind="header"]:hover svg,
    [data-testid="collapsedControl"]:hover svg {
        fill: #000000 !important;
        stroke: #000000 !important;
    }
    
    /* Header area to ensure button is visible */
    header[data-testid="stHeader"] {
        background-color: #0a0a0a !important;
    }
    
    /* Text colors */
    .stMarkdown, p, label {
        color: #cccccc !important;
    }
    
    /* Dataframe styling */
    .dataframe {
        background-color: #111111 !important;
        border-radius: 4px;
        border: 1px solid #1a1a1a;
    }
    
    .dataframe th {
        background-color: #0a0a0a !important;
        color: #ffffff !important;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 0.5px;
    }
    
    .dataframe td {
        background-color: #111111 !important;
        color: #cccccc !important;
        border-color: #1a1a1a !important;
    }
    
    /* Show header for sidebar toggle */
    header {
        visibility: visible !important;
        background-color: #0a0a0a !important;
    }
    
    /* Hide only menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Divider */
    .minimal-divider {
        height: 1px;
        background: #1a1a1a;
        border: none;
        margin: 40px 0;
    }
    
    /* Input fields */
    input, textarea, select {
        background-color: #111111 !important;
        color: #ffffff !important;
        border: 1px solid #1a1a1a !important;
        border-radius: 4px !important;
    }
    
    input:focus, textarea:focus, select:focus {
        border-color: #333333 !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #0a0a0a;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #0a0a0a;
        color: #666666;
        padding: 12px 24px;
        border: none;
        font-weight: 600;
        font-size: 0.85rem;
        letter-spacing: 0.5px;
    }
    
    .stTabs [aria-selected="true"] {
        background: #111111;
        color: #ffffff;
        border-bottom: 2px solid #ffffff;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background: #111111;
        color: #ffffff;
        font-weight: 600;
        border-radius: 4px;
        border: 1px solid #1a1a1a;
    }
    
    .streamlit-expanderHeader:hover {
        border-color: #333333;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #ffffff !important;
    }
    
    /* Remove padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Checkbox styling */
    .stCheckbox {
        color: #cccccc;
    }
    
    /* Slider styling */
    .stSlider {
        padding: 20px 0;
    }
    
    /* Clean scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0a0a;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #333333;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #444444;
    }
</style>
""", unsafe_allow_html=True)

# Apply the custom CSS
apply_custom_css()

# Configure matplotlib style for professional charts
plt.style.use('dark_background')
sns.set_palette("husl")

# Update matplotlib params for clean, professional look
plt.rcParams.update({
    'figure.facecolor': '#0a0a0a',
    'axes.facecolor': '#111111',
    'axes.edgecolor': '#333333',
    'axes.labelcolor': '#ffffff',
    'axes.grid': True,
    'grid.color': '#1a1a1a',
    'grid.linestyle': '-',
    'grid.linewidth': 0.5,
    'xtick.color': '#888888',
    'ytick.color': '#888888',
    'text.color': '#ffffff',
    'font.size': 10,
    'axes.titlesize': 12,
    'axes.labelsize': 10,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 14,
    'lines.linewidth': 2,
    'patch.edgecolor': '#333333'
})

# Sidebar Configuration - Minimal
with st.sidebar:
    st.markdown('''
    <div style="text-align: center; margin-bottom: 30px;">
        <span style="font-size: 2rem;">📊</span>
        <h2 class="pixel-font" style="font-size: 0.9rem; margin-top: 10px; color: #ffffff;">SMART DATA<br/>VISUALIZER</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("#### Features")
    st.markdown("""
    • Multiple chart types  
    • Auto data cleaning  
    • Real-time preview  
    • Export ready
    """)
    
    st.markdown("---")
    
    st.markdown("#### Chart Types")
    st.markdown("""
    **Line** — Trends  
    **Bar** — Comparison  
    **Scatter** — Correlation  
    **Histogram** — Distribution  
    **Box** — Statistics  
    **Count** — Frequency  
    **Heat** — Matrix
    """)
    
    st.markdown("---")
    
    with st.expander("Settings"):
        chart_dpi = st.slider("Chart Quality", 80, 200, 120, 20)
        show_grid = st.checkbox("Show Grid", value=True)
        dark_mode = st.checkbox("Dark Charts", value=True)
    
    st.markdown("---")
    st.markdown('<p style="font-size: 0.7rem; color: #444444; text-align: center;">v1.0.0</p>', unsafe_allow_html=True)

# Header Section
st.markdown('''
<div style="text-align: center; margin-bottom: 10px;">
    <span style="font-size: 3.5rem; filter: drop-shadow(0 0 20px rgba(0, 212, 255, 0.8));">📊</span>
</div>
<h1 class="main-header">SMART DATA VISUALIZER</h1>
''', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transform your data into beautiful, insightful visualizations</p>', unsafe_allow_html=True)

# File Upload Section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"],
        help="Drag and drop or click to upload",
        label_visibility="collapsed"
    )

if uploaded_file:
    # Reading data
    df = pd.read_csv(uploaded_file)
    
    st.markdown('<hr class="minimal-divider">', unsafe_allow_html=True)
    
    # Initial Data Preview (before cleaning)
    st.markdown('<div class="section-title">📋 DATA PREVIEW</div>', unsafe_allow_html=True)
    st.dataframe(df.head(), use_container_width=True)
    
    # Clean data
    df = clean_data(df)
    st.success("✅ Data cleaned successfully!")
    
    st.markdown('<hr class="minimal-divider">', unsafe_allow_html=True)
    
    # Metrics Section - Minimal
    st.markdown('<div class="section-title">DATASET METRICS</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("ROWS", f"{len(df):,}")
    with col2:
        st.metric("COLUMNS", len(df.columns))
    with col3:
        st.metric("NUMERIC", len(df.select_dtypes(include=['int64', 'float64']).columns))
    with col4:
        st.metric("CATEGORICAL", len(df.select_dtypes(include=['object', 'category']).columns))
    
    st.markdown('<hr class="minimal-divider">', unsafe_allow_html=True)
    
    # Visualization Configuration
    st.markdown('<div class="section-title">VISUALIZATION</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        plot_type = st.selectbox(
            "Chart Type",
            [
                "Line Plot",
                "Bar Plot",
                "Scatter Plot",
                "Histogram",
                "Boxplot",
                "Countplot",
                "Heatmap",
            ],
            label_visibility="visible"
        )

    # Get columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    x_col, y_col = None, None

    with col2:
        if plot_type == "Line Plot":
            x_col = st.selectbox("X-Axis", numeric_cols)
            y_col = st.selectbox("Y-Axis", numeric_cols)

        elif plot_type == "Bar Plot":
            if categorical_cols:
                x_col = st.selectbox("X-Axis", categorical_cols)
            y_col = st.selectbox("Y-Axis", numeric_cols)

        elif plot_type == "Scatter Plot":
            x_col = st.selectbox("X-Axis", numeric_cols)
            y_col = st.selectbox("Y-Axis", numeric_cols)

        elif plot_type == "Histogram":
            x_col = st.selectbox("Column", numeric_cols)

        elif plot_type == "Boxplot":
            if categorical_cols:
                x_col = st.selectbox("X-Axis", categorical_cols)
            y_col = st.selectbox("Y-Axis", numeric_cols)

        elif plot_type == "Countplot":
            if categorical_cols:
                x_col = st.selectbox("Column", categorical_cols)

        elif plot_type == "Heatmap":
            st.info("Using all numeric columns")

    st.markdown('<hr class="minimal-divider">', unsafe_allow_html=True)
    
    # Generate Button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        generate_button = st.button(" GENERATE VISUALIZATION", use_container_width=True)
    
    if generate_button:
        st.markdown('<div class="section-title">OUTPUT</div>', unsafe_allow_html=True)
        
        with st.spinner('Rendering...'):
            fig = generate_plot(df, plot_type, x_col, y_col)
            
            # Apply custom styling to the generated plot
            if fig:
                fig.patch.set_facecolor('#0a0a0a')
                for ax in fig.get_axes():
                    ax.set_facecolor('#111111')
                    ax.spines['top'].set_color('#333333')
                    ax.spines['right'].set_color('#333333')
                    ax.spines['bottom'].set_color('#333333')
                    ax.spines['left'].set_color('#333333')
                    ax.grid(show_grid, color='#1a1a1a', linewidth=0.5)
                    ax.tick_params(colors='#888888')
                    ax.xaxis.label.set_color('#ffffff')
                    ax.yaxis.label.set_color('#ffffff')
                    ax.title.set_color('#ffffff')
        
        if fig:
            st.pyplot(fig, use_container_width=True)
            st.success("✓ Visualization complete")
        else:
            st.error("✗ Generation failed")
            
else:
    # Welcome screen - Minimal
    st.markdown('<hr class="minimal-divider">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("Upload a CSV file to begin")
        
        with st.expander("Requirements"):
            st.markdown("""
            • Valid CSV format  
            • Column headers included  
            • Clean data preferred  
            • Maximum 200MB
            """)
