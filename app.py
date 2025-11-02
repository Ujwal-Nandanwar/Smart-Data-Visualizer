import streamlit as st
import pandas as pd
from utils.data_cleaner import clean_data
from utils.plot_generator import generate_plot

st.set_page_config(page_title="Smart Data Visualizer", layout="wide")

st.title("📊 Smart Data Visualizer")
st.write(
    "Upload your CSV file, choose the type of graph first, "
    "and valid columns for visualization."
)

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    # Step 2: Read & show data
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Data Preview")
    st.dataframe(df.head())

    # Step 3: Clean data
    df = clean_data(df)
    st.success("✅ Data cleaned successfully!")

    # Step 4: Select Graph Type First
    plot_type = st.selectbox(
        "Choose the type of graph you want to visualize:",
        [
            "Line Plot",
            "Bar Plot",
            "Scatter Plot",
            "Histogram",
            "Boxplot",
            "Countplot",
            "Heatmap",
        ],
    )

    # Detect column types
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    x_col, y_col = None, None

    # Step 5: Restrict valid column options based on graph type
    if plot_type == "Line Plot":
        x_col = st.selectbox("Select X-axis (Numeric or Date)", numeric_cols)
        y_col = st.selectbox("Select Y-axis (Numeric)", numeric_cols)

    elif plot_type == "Bar Plot":
        x_col = st.selectbox("Select X-axis (Categorical)", categorical_cols)
        y_col = st.selectbox("Select Y-axis (Numeric)", numeric_cols)

    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("Select X-axis (Numeric)", numeric_cols)
        y_col = st.selectbox("Select Y-axis (Numeric)", numeric_cols)

    elif plot_type == "Histogram":
        x_col = st.selectbox("Select Column (Numeric)", numeric_cols)

    elif plot_type == "Boxplot":
        x_col = st.selectbox("Select X-axis (Categorical)", categorical_cols)
        y_col = st.selectbox("Select Y-axis (Numeric)", numeric_cols)

    elif plot_type == "Countplot":
        x_col = st.selectbox("Select Column (Categorical)", categorical_cols)

    elif plot_type == "Heatmap":
        st.info("Heatmap will use all numeric columns automatically.")

    # Step 6: Generate Plot
    if st.button("Generate Plot"):
        st.subheader(f"📈 {plot_type}")
        fig = generate_plot(df, plot_type, x_col, y_col)
        if fig:
            st.pyplot(fig)
        else:
            st.error("⚠️ Could not generate plot. Check column selections.")
else:
    st.info("👆 Please upload a CSV file to get started.")
