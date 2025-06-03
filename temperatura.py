import pandas as pd
import streamlit as st

# Título e descrição
st.title("📈 Temperatura da Semana")

# Leitura do CSV
df = pd.read_csv("temperatura_semana.csv")

# Tabela de dados
st.subheader("📋 Tabela de Temperaturas")
st.dataframe(df)

# Gráfico de linha
st.subheader("🌡️ Variação de Temperatura na Semana")
st.line_chart(df.set_index("Dia"))
