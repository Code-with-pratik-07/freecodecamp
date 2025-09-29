import pandas as pd

def calculate_demographic_data():
    # Load data
    df = pd.read_csv('adult.data.csv')  # make sure the file is in the same folder

    # 1. Number of people of each race
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Percentage of people with a Bachelor's degree
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage of people with advanced education (>50K)
    advanced_edu = ['Bachelors', 'Masters', 'Doctorate']
    adv_edu_rich = df[df['education'].isin(advanced_edu)]
    percentage_adv_edu_rich = round((adv_edu_rich[adv_edu_rich['salary'] == '>50K'].shape[0] / adv_edu_rich.shape[0]) * 100, 1)

    # 5. Percentage of people without advanced education (>50K)
    non_adv_edu = df[~df['education'].isin(advanced_edu)]
    percentage_non_adv_edu_rich = round((non_adv_edu[non_adv_edu['salary'] == '>50K'].shape[0] / non_adv_edu.shape[0]) * 100, 1)

    # 6. Minimum number of hours worked per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of people working minimum hours who earn >50K
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_min_workers = min_workers[min_workers['salary'] == '>50K']
    rich_percentage = round((rich_min_workers.shape[0] / min_workers.shape[0]) * 100, 1)

    # 8. Country with highest percentage of people earning >50K
    country_salary = df[df['salary'] == '>50K'].groupby('native-country').size() / df.groupby('native-country').size() * 100
    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = round(country_salary.max(), 1)

    # 9. Most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    # Return all results
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'percentage_adv_edu_rich': percentage_adv_edu_rich,
        'percentage_non_adv_edu_rich': percentage_non_adv_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }