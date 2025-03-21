from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import os
import datetime


# Configuración de Chrome para parecer un usuario real
chrome_options = Options()
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")
chrome_options.add_argument("--headless=new")  # Modo headless moderno
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Oculta Selenium
chrome_options.add_argument("--window-size=1920,1080")  # Simula una pantalla normal
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Instalar automáticamente el ChromeDriver correcto
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Quitar la detección de WebDriver
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

url = "https://www.pccomponentes.com/ordenador-sobremesa-pcm-trend-nexon-1-intel-core-i9-12900kf-32gb-1tb-ssd-rtx-4060"
driver.get(url)

time.sleep(10)

try:
  cookies_button = WebDriverWait(driver, 5).until(
    visibility_of_element_located((By.ID, "cookiesAcceptAll"))
  )
  cookies_button.click()
  print("Cookies aceptadas automáticamente")
except Exception as e:
  print("Error al aceptar cookies")


def anadir_registro(date, name, price):
  try:
    with open("precios.csv", "a") as f:
      f.write(f"{date},{name},{price} \n")
  except Exception as e:
      print("No se creó el registro") 


try:
  soup = BeautifulSoup(driver.page_source, 'html.parser')
  price_element = soup.find(id="pdp-price-current-integer") 
  name_element = soup.find(id="pdp-title")
  now = datetime.datetime.now().strftime("%d/%m/%Y")
  print(name_element.text, price_element.text)

  if os.path.exists("precios.csv"):
   anadir_registro(now, name_element.text, price_element.text)
  else:
    try:
      with open("precios.csv", "x") as f:
        f.write(f"fecha,nombre,precio\n")
      print("Archivo creado correctamente")
      anadir_registro(now, name_element.text, price_element.text)
    except FileExistsError:
      print("El archivo ya existe") 
except Exception as e:
  print("No se pudo obtener el precio", e)
