import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    ax.set_title('Rise in Sea Level', fontsize=15)
    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Sea Level (inches)', fontsize=10)
    plt.show()
    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(x=df['Year'], y= df['CSIRO Adjusted Sea Level'])
    years_ext_1 = np.array([df['Year'].min(), 2050])
    pred_1 = slope * years_ext_1 + intercept
    # Create second line of best fit
    df2=df[df['Year']>=2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(x=df['Year'], y= df['CSIRO Adjusted Sea Level'])
    years_ext_2 = np.array([df2['Year'].min(), 2050])
    pred_2 = slope2 * years_ext_2 + intercept2


    # Add labels and title
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Gráfico 1 (df)
    ax1.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'], label='Datos observados', color='blue', s=50)
    ax1.plot(years_ext_1, pred_1, color='red', linewidth=2, label='Línea de mejor ajuste')
    ax1.set_title('Rise in Sea Level', fontsize=15, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Sea Level (inches)', fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    # Gráfico 2 (df2)
    ax2.scatter(x=df2['Year'], y=df2['CSIRO Adjusted Sea Level'], label='Datos observados', color='blue', s=50)
    ax2.plot(years_ext_2, pred_2, color='red', linewidth=2, label='Línea de mejor ajuste')
    ax2.set_title('Rise in Sea Level', fontsize=15, fontweight='bold')
    ax2.set_xlabel('Year', fontsize=12)
    ax2.set_ylabel('Sea Level (inches)', fontsize=12)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout() 
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()