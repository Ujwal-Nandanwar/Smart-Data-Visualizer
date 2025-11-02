# 📊 Smart Data Visualizer

A Streamlit web application that allows users to upload a CSV dataset, automatically clean it, and visualize the data interactively.

## 🚀 Features
- Upload any CSV file
- Automatic data cleaning (missing values, duplicates)
- Select graph type first → dynamic X/Y axis restriction
- Interactive and beautiful charts (Matplotlib + Seaborn)
- Hosted via Streamlit and version controlled on GitHub

## 🧩 Supported Plots
- Line Plot  
- Bar Plot  
- Scatter Plot  
- Histogram  
- Boxplot  
- Countplot  
- Heatmap  

## ⚙️ Installation

```bash
git clone https://github.com/Ujwal-Nandanwar/Smart-Data-Visualizer.git
cd Smart-Data-Visualizer
python -m venv .venv
source .venv/bin/activate   # On Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
