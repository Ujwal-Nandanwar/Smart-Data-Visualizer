import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(df, plot_type, x_col=None, y_col=None):
    """
    Generate and return a matplotlib figure based on the selected plot type.
    """
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5))

    try:
        if plot_type == "Line Plot":
            sns.lineplot(data=df, x=x_col, y=y_col, marker="o", ax=ax)

        elif plot_type == "Bar Plot":
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax)

        elif plot_type == "Scatter Plot":
            sns.scatterplot(data=df, x=x_col, y=y_col, s=70, edgecolor="black", ax=ax)

        elif plot_type == "Histogram":
            sns.histplot(df[x_col], kde=True, bins=25, color="skyblue", ax=ax)

        elif plot_type == "Boxplot":
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)

        elif plot_type == "Countplot":
            sns.countplot(data=df, x=x_col, ax=ax)

        elif plot_type == "Heatmap":
            corr = df.select_dtypes(include=[np.number]).corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)

        else:
            return None

        ax.set_title(f"{plot_type}", fontsize=14, weight="bold")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    except Exception as e:
        print(f"Error while generating {plot_type}: {e}")
        return None
