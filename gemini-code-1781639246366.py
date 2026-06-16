import streamlit as st
import random

# CONFIGURAÇÃO DA PÁGINA (Layout centrado para ecrãs mobile)
st.set_page_config(page_title="FS Soluções - Treino", page_icon="🔧", layout="centered")

# Cabeçalho da Empresa
st.title("FS Soluções 🛠️")
st.subheader("Treino Técnico Mobile")
st.markdown("---")

# Botão de reiniciar destacado para polegar/toque no telemóvel
st.write("### 🔄 Simulação")
if st.button("Gerar Novo Cenário de Falha", use_container_width=True):
    st.session_state.temperatura = random.randint(85, 110)
    st.session_state.vibracao = round(random.uniform(5.5, 9.2), 1)
    st.session_state.corrente = random.randint(45, 60)

# Inicialização de variáveis
if 'temperatura' not in st.session_state:
    st.session_state.temperatura = 95
    st.session_state.vibracao = 7.8
    st.session_state.corrente = 48

st.markdown("---")

# PAINEL DE SENSORES EM FORMATO LISTA (Melhor para leitura vertical no telemóvel)
st.write("### 📊 Sensores do Motor M-101")

st.metric(label="🌡️ Temperatura do Mancal", value=f"{st.session_state.temperatura} °C", delta="CRÍTICO (>75°C)", delta_color="inverse")
st.markdown("---")
st.metric(label="📳 Nível de Vibração", value=f"{st.session_state.vibracao} mm/s", delta="CRÍTICO (>4.5)", delta_color="inverse")
st.markdown("---")
st.metric(label="⚡ Corrente Elétrica", value=f"{st.session_state.corrente} A", delta="ALTA (>40A)", delta_color="inverse")

st.markdown("---")

# TOMADA DE DECISÃO (Menus maiores fáceis de clicar)
st.write("### 🧠 Tomada de Decisão")
st.info("Analise os dados acima e escolha a conduta técnica correta.")

opcao = st.radio(
    "Qual a ação corretiva imediata?",
    (
        "Selecionar uma opção...",
        "A) Lubrificar o mancal imediatamente.",
        "B) Paragem imediata + LOTO + Inspecionar rolamento.",
        "C) Reduzir rotação em 20% para monitorizar.",
        "D) Substituir os cabos elétricos."
    )
)

st.markdown("---")

# CORREÇÃO DIDÁTICA
if opcao != "Selecionar uma opção...":
    st.write("#### 📝 Avaliação Técnica:")
    
    if "B)" in opcao:
        st.success("✅ **CORRETA!**")
        st.markdown("""
        **Justificação da FS Soluções:**
        * Alta vibração ($>4.5 \text{ mm/s}$) com alta temperatura indica falha mecânica severa iminente.
        * O procedimento de **LOTO (Bloqueio e Etiquetagem)** é obrigatório antes de qualquer inspeção para garantir a segurança do técnico.
        """)
    elif "A)" in opcao:
        st.error("❌ **INCORRETA!**")
        st.markdown("**Motivo:** Lubrificar um componente já superaquecido e em vibração crítica pode causar incêndio ou quebra imediata.")
    elif "C)" in opcao:
        st.warning("⚠️ **PARCIALMENTE INCORRETA!**")
        st.markdown("**Motivo:** Reduzir a rotação apenas mascara o defeito mecânico estrutural, que continuará a degradar-se.")
    elif "D)" in opcao:
        st.error("❌ **INCORRETA!**")
        st.markdown("**Motivo:** A corrente alta é reflexo do esforço mecânico (eixo preso), e não um problema nos cabos.")