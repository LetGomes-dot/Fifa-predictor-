import streamlit as st
import json
import random

# Carrega as estatísticas dos jogadores
with open("players_stats.json", "r") as f:
    jogadores_stats = json.load(f)

# Função que prevê gols com base nos atributos do jogador
def prever_gols(stats):
    media = (stats["ataque"] * 0.4 + stats["finalizacao"] * 0.4 + stats["forma"] * 100 * 0.2) / 100
    gols = round(random.gauss(media, 0.6))
    return max(0, min(gols, 5))

# Interface do app
st.title("🔮 Previsão de Gols - Partidas FIFA (SuperBet)")

jogadores = list(jogadores_stats.keys())

col1, col2 = st.columns(2)
with col1:
    jogador1 = st.selectbox("Jogador 1", jogadores)
with col2:
    jogador2 = st.selectbox("Jogador 2", jogadores)

if st.button("Prever Resultado"):
    stats1 = jogadores_stats[jogador1]
    stats2 = jogadores_stats[jogador2]

    gols1 = prever_gols(stats1)
    gols2 = prever_gols(stats2)

    st.markdown(f"## ⚽ {jogador1} {gols1} x {gols2} {jogador2}")

    # Exibe as estatísticas dos jogadores
    st.subheader("📊 Estatísticas dos Jogadores")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown(f"**{jogador1}**")
        for stat, val in stats1.items():
            st.text(f"{stat.capitalize()}: {val}")
    with col4:
        st.markdown(f"**{jogador2}**")
        for stat, val in stats2.items():
            st.text(f"{stat.capitalize()}: {val}")
