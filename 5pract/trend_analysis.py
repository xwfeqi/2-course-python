import matplotlib.pyplot as plt

def plot_trend(covid_data, country):
    country_data = covid_data[covid_data['location'] == country]
    plt.figure(figsize=(10, 6))
    plt.plot(country_data['date'], country_data['total_cases'], label='Випадки')
    plt.plot(country_data['date'], country_data['total_deaths'], label='Смерті')
    plt.title(f'Динаміка захворюваності COVID-19 в {country}', fontsize=15)
    plt.xlabel('Дата')
    plt.ylabel('Кількість випадків')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def top_countries_growth(covid_data):
    covid_data['new_cases'] = covid_data.groupby('location')['total_cases'].diff().fillna(0)
    top_countries = covid_data.groupby('location')['new_cases'].sum().nlargest(5)
    return top_countries
