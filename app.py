import streamlit as st
import pandas as pd
from utils.data_cleaner import clean_data
from utils.plot_generator import generate_plot

st.set_page_config(page_title="Smart Data Visualizer", layout="wide")

st.title("📊 Smart Data Visualizer")
st.write("Upload a CSV file, clean it automatically, and visualize your data interactively!")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Preview of Uploaded Data")
    st.dataframe(df.head())

    # Step 2: Clean Data
    df = clean_data(df)
    st.success("✅ Data cleaned successfully!")
    st.dataframe(df.head())

    # Step 3: Column & Plot Selection
    columns = df.columns.tolist()
    x_col = st.selectbox("Select X-axis column", columns)
    y_col = st.selectbox("Select Y-axis column", columns)
    plot_type = st.selectbox("Select Plot Type", ["Line", "Bar", "Scatter", "Histogram", "Boxplot"])

    # Step 4: Generate Plot
    if st.button("Generate Plot"):
        if x_col == y_col and plot_type != "Histogram":
            st.error("❌ X and Y columns cannot be the same (except for histogram).")
        else:
            st.subheader(f"📈 {plot_type} Plot")
            fig = generate_plot(df, x_col, y_col, plot_type)
            if fig:
                st.pyplot(fig)
            else:
                st.warning("⚠️ Incompatible columns or plot type. Please select valid options.")
