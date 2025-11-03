import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def generate_plot(df, plot_type, x_col=None, y_col=None):
    # Set custom style - minimal black and white
    sns.set_theme(style="darkgrid")
    sns.set_palette("husl")
    
    # Create figure with minimal dark styling
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#0a0a0a')
    
    # Minimal black and white color palette
    primary_color = '#ffffff'
    secondary_color = '#cccccc'
    gradient_colors = ['#ffffff', '#e0e0e0', '#cccccc', '#b0b0b0']

    try:
        if plot_type == "Line Plot":
            sns.lineplot(
                data=df, x=x_col, y=y_col, 
                marker="o", markersize=8, linewidth=2.5,
                color=primary_color, ax=ax
            )
            ax.fill_between(df[x_col].values, df[y_col].values, alpha=0.3, color=primary_color)

        elif plot_type == "Bar Plot":
            bars = sns.barplot(
                data=df, x=x_col, y=y_col, 
                palette=gradient_colors, ax=ax,
                edgecolor='white', linewidth=1.5
            )
            # Add value labels on bars
            for container in ax.containers:
                ax.bar_label(container, fmt='%.2f', padding=3)

        elif plot_type == "Scatter Plot":
            scatter = sns.scatterplot(
                data=df, x=x_col, y=y_col, 
                s=100, alpha=0.6, 
                color=primary_color, 
                edgecolor="white", linewidth=1.5,
                ax=ax
            )
            # Add trend line
            z = np.polyfit(df[x_col], df[y_col], 1)
            p = np.poly1d(z)
            ax.plot(df[x_col], p(df[x_col]), 
                   linestyle="--", color=secondary_color, 
                   linewidth=2, alpha=0.8, label='Trend')
            ax.legend()

        elif plot_type == "Histogram":
            sns.histplot(
                df[x_col], kde=True, bins=25, 
                color=primary_color, alpha=0.6,
                edgecolor='white', linewidth=1.5,
                ax=ax
            )
            # Enhance KDE line
            ax.lines[0].set_color(secondary_color)
            ax.lines[0].set_linewidth(2.5)

        elif plot_type == "Boxplot":
            box = sns.boxplot(
                data=df, x=x_col, y=y_col, 
                palette=gradient_colors,
                ax=ax, linewidth=2
            )
            # Add mean markers
            means = df.groupby(x_col)[y_col].mean()
            positions = range(len(means))
            ax.scatter(positions, means, color='#ffffff', s=100, 
                      zorder=3, label='Mean', marker='D', edgecolor='#000000', linewidth=1.5)
            ax.legend(facecolor='#111111', edgecolor='#333333', labelcolor='#cccccc')

        elif plot_type == "Countplot":
            bars = sns.countplot(
                data=df, x=x_col, 
                palette=gradient_colors,
                edgecolor='white', linewidth=1.5,
                ax=ax
            )
            # Add count labels
            for container in ax.containers:
                ax.bar_label(container, padding=3)

        elif plot_type == "Heatmap":
            corr = df.select_dtypes(include=[np.number]).corr()
            sns.heatmap(
                corr, annot=True, 
                cmap='Greys',
                linewidths=2, linecolor='#333333',
                square=True, cbar_kws={"shrink": 0.8},
                fmt='.2f', annot_kws={'size': 9, 'color': '#ffffff'},
                ax=ax
            )

        else:
            return None

        # Minimal title and labels - black and white
        ax.set_title(
            f"{plot_type}", 
            fontsize=18, 
            weight="bold", 
            pad=20,
            color='#ffffff'
        )
        
        # Style axes labels - minimal white
        ax.set_xlabel(ax.get_xlabel(), fontsize=12, weight='bold', color='#cccccc')
        ax.set_ylabel(ax.get_ylabel(), fontsize=12, weight='bold', color='#cccccc')
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45, ha='right', color='#cccccc')
        plt.yticks(color='#cccccc')
        
        # Add grid with minimal style
        ax.grid(True, alpha=0.15, linestyle='--', linewidth=0.5, color='#333333')
        ax.set_axisbelow(True)
        
        # Set dark background color
        ax.set_facecolor('#111111')
        
        # Style spines (borders) with subtle gray
        for spine in ax.spines.values():
            spine.set_color('#333333')
            spine.set_linewidth(1)
        
        # Improve layout
        plt.tight_layout()
        return fig

    except Exception as e:
        print(f"Error while generating {plot_type}: {e}")
        return None
