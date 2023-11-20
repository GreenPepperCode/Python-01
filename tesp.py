import requests
import pandas as pd

# Spécifier l'endpoint de l'API
endpoint = 'https://whiskyhunter.net/api/distilleries_info/'

# Envoyer une requête GET à l'endpoint
response = requests.get(endpoint)
data = response.json()

# Créer un DataFrame avec les données
df = pd.DataFrame(data)

# Exporter les données dans un fichier Excel
df.to_excel("distilleries_info.xlsx", index=False)
