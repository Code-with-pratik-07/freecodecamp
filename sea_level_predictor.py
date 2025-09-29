import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Import data
df = pd.read_csv('epa-sea-level.csv')

def draw_plot():
    # Copy data
    data = df.copy()
    
    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue')
    
    # First line of best fit (all data)
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(data['Year'].min(), 2051))
    best_fit_all = intercept + slope * years_extended
    ax.plot(years_extended, best_fit_all, 'r', label='Fit: All Data')
    
    # Second line of best fit (year >= 2000)
    data_2000 = data[data['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(data_2000['Year'], data_2000['CSIRO Adjusted Sea Level'])
    years_extended_2000 = pd.Series(range(2000, 2051))
    best_fit_2000 = intercept2 + slope2 * years_extended_2000
    ax.plot(years_extended_2000, best_fit_2000, 'green', label='Fit: Year >= 2000')
    
    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()
    
    # Save figure
    fig.savefig('sea_level_plot.png')
    return fig