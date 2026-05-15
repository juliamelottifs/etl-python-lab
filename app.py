import pandas as pd

# =========================
# EXTRAÇÃO
# =========================

usuarios = [
    {
        "nome": "Julia",
        "conta": "12345-6",
        "cartao": "Gold"
    },
    {
        "nome": "Carlos",
        "conta": "98765-1",
        "cartao": "Platinum"
    },
    {
        "nome": "Amanda",
        "conta": "45678-9",
        "cartao": "Black"
    }
]

# Cria tabela
df = pd.DataFrame(usuarios)

# =========================
# TRANSFORMAÇÃO
# =========================

def gerar_mensagem(nome, cartao):
    return f"Olá {nome}, seu cartão {cartao} possui benefícios exclusivos!"

df["mensagem"] = df.apply(
    lambda row: gerar_mensagem(row["nome"], row["cartao"]),
    axis=1
)

# =========================
# CARREGAMENTO
# =========================

df.to_csv("usuarios_com_mensagem.csv", index=False)

print("Arquivo criado com sucesso!")