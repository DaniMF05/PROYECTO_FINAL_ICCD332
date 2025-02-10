import requests
import csv
import os
from datetime import datetime
import pandas as pd

# 📌 Configuración
API_KEY = "bcbbf1a86a6259f5146814204883582b"  
LAT = -0.95  # 📍 Latitud de Manta, Manabí, Ecuador
LON = -80.7333  # 📍 Longitud de Manta, Manabí, Ecuador
CITY = "Manta"

# 📌 URL del API
url = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}&units=metric"

# 📌 Nombre del archivo CSV
csv_file = "clima-manta-hoy.csv"

# 📌 Realizar la solicitud al API
response = requests.get(url)
data = response.json()



# 📌 Verificar si la solicitud fue exitosa
if response.status_code != 200:
    print(f"❌ ERROR: No se pudo obtener datos. Código {data.get('cod')}: {data.get('message')}")
    exit(1)

# 📌 Extraer datos clave
weather_data = {
    "dt": data['dt'],
    "coord_lon": data['coord']['lon'],
    "coord_lat": data['coord']['lat'],
    "weather_0_id": data['weather'][0]['id'],
    "weather_0_main": data['weather'][0]['main'],
    "weather_0_description": data['weather'][0]['description'],
    "weather_0_icon": data['weather'][0]['icon'],
    "base": data['base'],
    "main_temp": data['main']['temp'],
    "main_feels_like": data['main']['feels_like'],
    "main_temp_min": data['main']['temp_min'],
    "main_temp_max": data['main']['temp_max'],
    "main_pressure": data['main']['pressure'],
    "main_humidity": data['main']['humidity'],
    "main_sea_level": data['main'].get('sea_level', "N/A"),  # Usar get() para campos opcionales
    "main_grnd_level": data['main'].get('grnd_level', "N/A"),  # Usar get() para campos opcionales
    "visibility": data.get('visibility', "N/A"),  # Usar get() para campos opcionales
    "wind_speed": data['wind']['speed'],
    "wind_deg": data['wind']['deg'],
    "wind_gust": data['wind'].get('gust', "N/A"),  # Usar get() para campos opcionales
    "clouds_all": data['clouds']['all'],
    "sys_type": data['sys'].get('type', 'N/A'),
    "sys_country": data['sys']['country'],
    "sys_sunrise": data['sys']['sunrise'],
    "sys_sunset": data['sys']['sunset'],
    "timezone": data['timezone'],
    "id": data['id'],
    "name": data['name'],
    "cod": data['cod']
}

# 📌 Guardar en archivo CSV
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=weather_data.keys())

    # Si el archivo no existía, escribimos los encabezados
    if not file_exists:
        writer.writeheader()

    # Escribir los datos en una nueva fila
    writer.writerow(weather_data)

print(f"✅ Datos climatologicos de Manta guardados exitosamente en {csv_file}")
