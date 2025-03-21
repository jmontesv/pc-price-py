Este script realiza web scraping en la web de PCComponentes para obtener el precio y el nombre de un ordenador específico. 
Utiliza Selenium para interactuar con la página y BeautifulSoup para extraer la información relevante del código HTML. Luego, almacena los datos en un archivo CSV para llevar un historial de precios.

🔹 Tecnologías Utilizadas
Selenium 🚀

Automación del navegador para cargar la web y aceptar las cookies.
Configuración de Chrome para evitar detección como bot.
Uso de WebDriverWait para esperar elementos en la página.
BeautifulSoup 🥣

Extrae el precio y el nombre del producto de la página cargada en el navegador.
Manejo de Archivos en Python 📂

Usa os.path.exists() para verificar si el archivo precios.csv ya existe.
Usa open() para crear o escribir en el CSV.
Manejo de Fechas con datetime 🕒

Guarda la fecha de cada consulta para registrar cuándo se obtuvo el precio.
webdriver_manager ⚙️

Instala automáticamente la versión correcta de chromedriver.
