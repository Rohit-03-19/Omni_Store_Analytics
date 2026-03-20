import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class Visualizer:
    @staticmethod
    def plot_sales_by_category(df: pd.DataFrame):
        """Creates a professional bar chart of sales per category."""
        if df.empty:
            print("⚠️ No data available to visualize.")
            return

        plt.figure(figsize=(10, 6))
        sns.set_style("whitegrid")
        
        # Aggregate data for plotting
        category_data = df.groupby('category')['amount'].sum().reset_index()
        
        plot = sns.barplot(data=category_data, x='category', y='amount', hue = 'category',  palette="viridis", legend = False)
        
        plt.title("Revenue Distribution by Product Category", fontsize=15)
        plt.xlabel("Category", fontsize=12)
        plt.ylabel("Total Revenue ($)", fontsize=12)
        
        # Save output to processed data folder
        output_path = "data/processed/category_sales.png"
        plt.savefig(output_path)
        print(f"📊 Visualization saved to {output_path}")
        plt.close()