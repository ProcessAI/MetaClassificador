import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

# Carrega variáveis do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Inicializa o cliente OpenAI
client = OpenAI(api_key=api_key)

# Configuração da página
st.set_page_config(page_title="Classificador de Texto", page_icon="🤖")

st.title("🤖 Classificador de Texto com GPT-4.1-nano")

# Entrada de texto multilinha
texto = st.text_area(
    "Digite o texto que deseja classificar:",
    placeholder="Exemplo: O atendimento foi ótimo, mas o preço é alto.",
    height=150
)

# Botão de ação
if st.button("Classificar"):
    if not texto.strip():
        st.warning("Por favor, digite um texto antes de classificar.")
    else:
        with st.spinner("Analisando o texto..."):
            prompt = f"""
            Classifique o sentimento do seguinte texto como Positivo, Negativo ou Neutro:
            Texto: "{texto}"
            Responda apenas com uma das opções.
            """

            resposta = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system", "content": "Você é um classificador de texto."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0
            )

            classificacao = resposta.choices[0].message.content.strip().lower()

        # Define cor e ícone conforme classificação
        if "positivo" in classificacao:
            cor = "#00C853"  # verde
            icone = "😊"
            texto_label = "Positivo"
        elif "negativo" in classificacao:
            cor = "#D50000"  # vermelho
            icone = "😠"
            texto_label = "Negativo"
        else:
            cor = "#FFD600"  # amarelo
            icone = "😐"
            texto_label = "Neutro"

        # Exibe resultado com cor e ícone
        st.markdown(
            f"""
            <div style='background-color:{cor}; padding:15px; border-radius:10px; text-align:center;'>
                <h3 style='color:white;'>{icone} Classificação: {texto_label}</h3>
            </div>
            """,
            unsafe_allow_html=True
        )
