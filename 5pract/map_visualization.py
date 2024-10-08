import matplotlib.pyplot as plt
import plotly.express as px

def static_map(merged_data):
    fig, ax = plt.subplots(1, 1, figsize=(15, 10))
    merged_data.plot(column='Total Cases', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    ax.set_title('Кількість випадків COVID-19 по країнах', fontsize=15)
    plt.show()

def interactive_map(merged_data):
    fig = px.choropleth(
        merged_data,
        locations="Country",
        locationmode="country names",
        color="Total Cases",
        hover_name="Country",
        hover_data=["Total Deaths"],
        title="Кількість випадків COVID-19 по країнах",
        color_continuous_scale="OrRd",
        labels={'Total Cases': 'Випадки', 'Total Deaths': 'Смерті'}
    )
    fig.show()
