import os
from openai import OpenAI
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a chave da variável de ambiente
api_key = os.getenv("OPENAI_API_KEY")

# Inicializa o cliente
client = OpenAI(api_key=api_key)

# Texto que queremos classificar
texto = "O atendimento foi péssimo, mas o produto é bom."

# Prompt para classificação
prompt = f"""
Classifique o sentimento do seguinte texto como Positivo, Negativo ou Neutro:
Texto: "{texto}"
Responda apenas com uma das opções.
"""

# Chamada ao modelo GPT-4.1-nano
resposta = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "system", "content": "Você é um classificador de texto."},
        {"role": "user", "content": prompt}
    ],
    temperature=0
)

# Exibe o resultado
print("Classificação:", resposta.choices[0].message.content.strip())
