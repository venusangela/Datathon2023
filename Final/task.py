import requests
import pandas as pd

# Ganti dengan API key Anda
api_key = ""

# Endpoint untuk mengambil data lalu lintas
endpoint = "https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json"

# Koordinat Jakarta (contoh: Monas)
latitude = -6.1754
longitude = 106.8272

parameters = {
    "point": f"{latitude},{longitude}",
    "unit": "KMPH",
    "key": api_key
}

response = requests.get(endpoint, params=parameters)
data = response.json()

# Mengubah data menjadi DataFrame
df = pd.DataFrame(data['flowSegmentData'])

# Menyimpan DataFrame dalam file CSV
csv_filename = "C:/Users/vnang/OneDrive - UGM 365/Datathon23/traffic_data/traffic_data_jakarta.csv"
df.to_csv(csv_filename, index=False)
print(f"Data lalu lintas di Jakarta disimpan dalam {csv_filename}")