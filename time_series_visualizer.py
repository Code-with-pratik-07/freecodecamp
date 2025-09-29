import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')

# Clean data by removing top 2.5% and bottom 2.5% of page views
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

# Draw Line Plot
def draw_line_plot():
    # Copy data
    data = df.copy()
    
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(data.index, data['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    
    # Save figure
    fig.savefig('line_plot.png')
    return fig

# Draw Bar Plot
def draw_bar_plot():
    # Copy data
    data = df.copy()
    
    # Add year and month columns
    data['year'] = data.index.year
    data['month'] = data.index.month_name()
    
    # Group by year and month and calculate mean page views
    df_bar = data.groupby(['year', 'month'])['value'].mean().unstack()
    
    # Order months correctly
    month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December']
    df_bar = df_bar[month_order]
    
    # Draw bar plot
    fig = df_bar.plot(kind='bar', figsize=(15,8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')
    
    # Save figure
    fig.savefig('bar_plot.png')
    return fig

# Draw Box Plot
def draw_box_plot():
    # Prepare data
    data = df.copy()
    data.reset_index(inplace=True)
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')
    data['month_num'] = data['date'].dt.month
    
    # Sort by month number
    data = data.sort_values('month_num')
    
    # Draw box plots
    fig, axes = plt.subplots(1, 2, figsize=(20,6))
    
    # Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    
    # Save figure
    fig.savefig('box_plot.png')
    return fig