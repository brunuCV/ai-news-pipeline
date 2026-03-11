import requests
import pandas as pd
from datetime import datetime

class NewsIngestor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"

    def fetch_news(self, query="Artificial Intelligence"):
        params = {
            'q': query,
            'language': 'en',
            'sortBy': 'publishedAt',
            'apiKey': self.api_key
        }
        
        response = requests.get(self.base_url, params=params, verify=False)
        
        if response.status_code == 200:
            articles = response.json().get('articles', [])
            return pd.DataFrame(articles)
        else:
            print(f"Erro na requisição: {response.status_code}")
            return pd.DataFrame()

# Execução básica
if __name__ == "__main__":
    API_KEY = "a2889283dde7433480cb005ec1dfc366" # Obtenha em newsapi.org
    ingestor = NewsIngestor(API_KEY)
    
    print("Iniciando coleta de dados...")
    df_raw = ingestor.fetch_news("NVIDIA AI")


    import os # Certifique-se de ter o import os no topo do arquivo

# ...código de ingestão ...

if __name__ == "__main__":
    API_KEY = "a2889283dde7433480cb005ec1dfc366" 
    ingestor = NewsIngestor(API_KEY)
    
    print("Iniciando coleta de dados...")
    df_raw = ingestor.fetch_news("NVIDIA AI")
    
    # --- ADICIONE ESTAS LINHAS AQUI ---
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Pasta 'data' criada com sucesso!")
    # ----------------------------------

    # Agora o comando de salvar vai funcionar:
    df_raw.to_csv("data/raw_news.csv", index=False)
    print(f"Sucesso! {len(df_raw)} notícias salvas em data/raw_news.csv")
    
    # Salvando o "Bronze Layer" (Dado Bruto)
    df_raw.to_csv("data/raw_news.csv", index=False)
    print(f"Sucesso! {len(df_raw)} notícias salvas em data/raw_news.csv")