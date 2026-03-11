import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI News Sentinel", layout="wide")

st.title("🤖 AI News Sentinel - Dashboard")
st.markdown("Análise de sentimento em tempo real sobre notícias de Tecnologia.")

# 1. Carregar dados processados pela IA
try:
    df = pd.read_csv("data/processed_news.csv")
    
    # Sidebar com filtros
    st.sidebar.header("Filtros")
    sentiment_filter = st.sidebar.multiselect(
        "Selecione o Sentimento:",
        options=df["sentiment"].unique(),
        default=df["sentiment"].unique()
    )
    
    df_filtered = df[df["sentiment"].isin(sentiment_filter)]

    # 2. Métricas principais
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Notícias", len(df_filtered))
    col2.metric("👍 Positivas", len(df_filtered[df_filtered["sentiment"] == "POSITIVE"]))
    col3.metric("👎 Negativas", len(df_filtered[df_filtered["sentiment"] == "NEGATIVE"]))

    # 3. Gráficos
    st.markdown("---")
    c1, c2 = st.columns(2)

    with c1:
        st.subheader("Distribuição de Sentimento")
        fig = px.pie(df_filtered, names='sentiment', color='sentiment',
                     color_discrete_map={'POSITIVE':'#00CC96', 'NEGATIVE':'#EF553B'})
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Últimas Notícias Analisadas")
        st.dataframe(df_filtered[['title', 'sentiment']].head(10), use_container_width=True)

except FileNotFoundError:
    st.error("Arquivo 'processed_news.csv' não encontrado. Rode o script de IA primeiro!")