import random


# ----------------------------
# Configurações do jogo
# ----------------------------
ATAQUES = [
    ("dash", 4),
    ("mergulho", 3),
    ("morcegos", 2),
    ("chamas", 1)
]

REACOES = {
    "dash": "pular",
    "mergulho": "esquivar",
    "morcegos": "atacar",
    "chamas": "focar"
}


# ----------------------------
# Funções
# ----------------------------
def escolher_ataque(ultimo_ataque):
    ataque = ultimo_ataque
    while ataque == ultimo_ataque:
        ataque = random.choices(
            [a[0] for a in ATAQUES],
            weights=[a[1] for a in ATAQUES]
        )[0]
    return ataque


def processar_reacao(ataque, acao, vida_jogador, vida_grimm):
    if acao == REACOES[ataque]:
        print("Movimento perfeito!")
        vida_grimm -= 1
    else:
        print("Você errou o tempo!")
        vida_jogador -= 1

    return vida_jogador, vida_grimm


def mostrar_status(vida
