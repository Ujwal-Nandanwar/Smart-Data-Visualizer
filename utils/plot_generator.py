import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def generate_plot(df: pd.DataFrame, x_col: str, y_col: str, plot_type: str):
    """Generate and return a Matplotlib figure for given columns and plot type."""
    try:
        fig, ax = plt.subplots(figsize=(8, 5))

        if plot_type == "Line":
            sns.lineplot(data=df, x=x_col, y=y_col, ax=ax)
        elif plot_type == "Bar":
            sns.barplot(data=df, x=x_col, y=y_col, ax=ax)
        elif plot_type == "Scatter":
            sns.scatterplot(data=df, x=x_col, y=y_col, ax=ax)
        elif plot_type == "Histogram":
            sns.histplot(df[x_col], kde=True, ax=ax)
        elif plot_type == "Boxplot":
            sns.boxplot(data=df, x=x_col, y=y_col, ax=ax)
        else:
            return None

        ax.set_title(f"{plot_type} Plot of {y_col} vs {x_col}")
        plt.tight_layout()
        return fig

    except Exception as e:
        print(f"Plot generation failed: {e}")
        return None
