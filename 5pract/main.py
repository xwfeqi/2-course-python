from data_processing import load_covid_data, load_geodata, process_data
from map_visualization import static_map, interactive_map
from trend_analysis import plot_trend, top_countries_growth

def main():
    # Завантаження та обробка даних
    covid_data = load_covid_data()
    geodata = load_geodata()
    merged_data = process_data(covid_data, geodata)
    
    # Візуалізація карт
    static_map(merged_data)
    interactive_map(merged_data)
    
    # Аналіз трендів
    plot_trend(covid_data, 'Ukraine')  # приклад для України
    print(top_countries_growth(covid_data))

if __name__ == "__main__":
    main()
