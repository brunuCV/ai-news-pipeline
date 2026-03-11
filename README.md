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

## 📊 Resultados e Visualização

Confira abaixo o Dashboard interativo gerado a partir do pipeline de dados e processamento de IA:

[Painel de Notícias](imagens/painel.png)
