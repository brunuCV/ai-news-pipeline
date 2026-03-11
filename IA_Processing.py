import pandas as pd
from transformers import pipeline
import os
import urllib3

# Silencia avisos de SSL caso seu ambiente corporativo ainda peça
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def process_sentiment():
    print("🤖 Carregando modelo de IA (na primeira vez, o download de ~260MB começará)...")
    
    # Inicializa o pipeline de análise de sentimento
    # O parâmetro model_kwargs={"verify": False} ajuda se o download travar no SSL
    try:
        analyzer = pipeline(
            "sentiment-analysis", 
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
    except Exception as e:
        print(f"Erro ao carregar modelo: {e}")
        return

    # 1. Carregar os dados da camada Bronze
    file_path = "data/raw_news.csv"
    if not os.path.exists(file_path):
        print("❌ Erro: Arquivo raw_news.csv não encontrado! Rode o script de ingestão primeiro.")
        return

    df = pd.read_csv(file_path)
    df = df.dropna(subset=['title']) # Remove notícias sem título

    print(f"🧠 Analisando sentimentos de {len(df)} notícias...")
    
    # 2. Função para aplicar a IA com tratamento de erros
    def get_sentiment(text):
        try:
            # O modelo aceita no máximo 512 tokens
            result = analyzer(text[:512])[0]
            return result['label']
        except:
            return "NEUTRAL"

    # Criando a nova coluna de inteligência
    df['sentiment'] = df['title'].apply(get_sentiment)

    # 3. Salvando a Camada Silver (Dados Enriquecidos)
    df.to_csv("data/processed_news.csv", index=False)
    
    print("\n✅ Sucesso! Camada SILVER gerada em data/processed_news.csv")
    print("\n--- Amostra dos Resultados ---")
    print(df[['title', 'sentiment']].head())

if __name__ == "__main__":
    process_sentiment()