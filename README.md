# 🚀 AI-Driven News Pipeline: Sentiment Analysis & Data Engineering

Este projeto faz parte do meu portfólio de pós-graduação em **IA, Machine Learning e Engenharia de Dados**. O objetivo é construir um pipeline de dados ponta a ponta (End-to-End) que coleta notícias em tempo real sobre o mercado de tecnologia e aplica modelos de NLP (Processamento de Linguagem Natural) para análise de sentimento.

## 🏗️ Arquitetura do Projeto (Medallion Architecture)

O projeto segue os princípios de engenharia de dados moderna, dividindo o processamento em camadas:

1.  **Bronze (Raw):** Ingestão de dados brutos da [NewsAPI](https://newsapi.org/) via Python.
2.  **Silver (Processed):** Limpeza de dados, remoção de stop-words e aplicação de modelos de IA (Transformer - BERT).
3.  **Gold (Analytics):** Agregação de sentimentos por empresa/tema para visualização de tendências.

## 🛠️ Tech Stack

* **Linguagem:** Python 3.10+
* **Engenharia de Dados:** Pandas, Requests, Logging.
* **IA & Machine Learning:** Hugging Face Transformers (Modelos pré-treinados), PyTorch.
* **Infraestrutura:** Git, Docker (em breve), GitHub Actions para automação.

## 📊 O que este projeto demonstra?

* **Engenharia:** Consumo de APIs REST, manipulação de JSON e persistência de dados.
* **IA/ML:** Uso de modelos de Deep Learning para análise de texto (NLP) e métricas de classificação.
* **Organização:** Estrutura de código modularizada e documentada.

* ## 📈 Visualização dos Resultados
Confira abaixo o Dashboard interativo gerado após o processamento da IA:

![Dashboard Preview](<img width="2527" height="912" alt="Captura de tela 2026-03-11 163045" src="https://github.com/user-attachments/assets/d9dfdcae-9541-4af5-bb5a-1fc45be302c6" />)

## 🚀 Como Executar

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/ai-news-pipeline.git](https://github.com/SEU_USUARIO/ai-news-pipeline.git)
