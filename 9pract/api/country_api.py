import requests

def fetch_country_info(country_name):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}")
        if response.status_code == 200:
            data = response.json()
            if not data:
                return None
            
            country_data = data[0]
            return {
                "name": country_data.get("name", {}).get("common", "Невідомо"),
                "capital": country_data.get("capital", ["Невідомо"])[0],
                "region": country_data.get("region", "Невідомо"),
                "population": country_data.get("population", "Невідомо"),
                "area": country_data.get("area", "Невідомо"),
                "currency": ', '.join([info.get("name", "Невідомо") for info in country_data.get("currencies", {}).values()])
            }
        else:
            return None
    except requests.exceptions.RequestException:
        return None
