import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Конфігурація Selenium
options = Options()
options.add_argument("--headless")  # Запуск у фоновому режимі
service = Service('C:/Users/psycho/Downloads/chromedriver-win64/chromedriver.exe')

def collect_marketplace_data(url, csv_filename):
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    try:
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "goods-tile__inner")]')))
        
        with open(csv_filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Назва товару', 'Ціна', 'Категорія'])
        
            last_height = driver.execute_script("return document.body.scrollHeight")
            
            while True:
                products = driver.find_elements(By.XPATH, '//div[contains(@class, "goods-tile__inner")]')
                
                for product in products:
                    try:
                        title = product.find_element(By.CLASS_NAME, 'goods-tile__title').text
                        price = product.find_element(By.CLASS_NAME, 'goods-tile__price-value').text
                        category = "Ноутбуки"

                        writer.writerow([title, price, category])
                    except Exception as e:
                        print(f"Помилка при зборі даних товару: {e}")

                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:  # Якщо висота не змінилася, досягли кінця сторінки
                    break
                last_height = new_height

    except Exception as e:
        print(f"Помилка завантаження сторінки: {e}")
    finally:
        print(f"Дані збережено у файл {csv_filename}")
        driver.quit()

# Виклик функції з категорією товарів
marketplace_url = "https://rozetka.com.ua/ua/notebooks/c80004/"
csv_output = "marketplace_data.csv"
collect_marketplace_data(marketplace_url, csv_output)
