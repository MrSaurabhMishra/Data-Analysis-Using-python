import pandas as pd
import random
import seaborn as sns
import matplotlib.pyplot as plt

def unemployment_data():
    states = ['Uttar Pradesh', 'Maharashtra', 'Gujarat', 'Delhi', 'Chhattisgarh', 
              'Rajasthan', 'Bihar', 'Odisha', 'Kerala', 'Tamil Nadu', 'Karnataka']
    years = [2020, 2021, 2022, 2023, 2024]

    data = []
    for state in states:
        for year in years:
            rate = round(random.uniform(2.0, 15.0), 2)  # Generate fresh value each time
            data.append([state, year, rate])

    df = pd.DataFrame(data, columns=['State', 'Year', 'Unemployment_Rate'])

    # Statistics
    print(f"Mean Unemployment Rate: {df['Unemployment_Rate'].mean():.2f}")
    print(f"Median Unemployment Rate: {df['Unemployment_Rate'].median():.2f}")
    print(f"Max Unemployment Rate: {df['Unemployment_Rate'].max():.2f}")
    print(f"Min Unemployment Rate: {df['Unemployment_Rate'].min():.2f}")
    print(f"Mode Unemployment Rate: {df['Unemployment_Rate'].mode()[0]:.2f}")
    print(f"Standard Deviation: {df['Unemployment_Rate'].std():.2f}")
    print(f"Variance: {df['Unemployment_Rate'].var():.2f}")
    print(f"Correlation with Year: {df['Unemployment_Rate'].corr(df['Year']):.2f}")

    df.to_csv('unemployment_data.csv', index=False)
    print("unemployment_data.csv generated successfully.")

    # Bar Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Year', y='Unemployment_Rate', data=df, ci=None)
    plt.title('Average Unemployment Rate by Year')
    plt.savefig('barplot_unemployment.png')
    plt.show()

    # Heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.pivot(index="State", columns="Year", values="Unemployment_Rate"),
                annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title('Unemployment Rates Heatmap')
    plt.savefig('heatmap_unemployment.png')
    plt.show()

    # Scatter Plot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Year', y='Unemployment_Rate', data=df, s=100, alpha=0.7)
    plt.title('Unemployment Rates Scatter Plot')
    plt.savefig('scatter_unemployment.png')
    plt.show()

   

    print("All unemployment plots saved successfully.")

if __name__ == '__main__':
    unemployment_data()
