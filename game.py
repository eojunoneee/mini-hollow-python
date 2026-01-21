import random

vida_jogador = 5
vida_grimm = 8
luta_ativa = True
ultimo_ataque = None

ataques = [
    ("dash", 4),
    ("mergulho", 3),
    ("morcegos", 2),
    ("chamas", 1)
]

reacoes = {
    "dash": "pular",
    "mergulho": "esquivar",
    "morcegos": "atacar",
    "chamas": "focar"
}

while luta_ativa:
    print("\n🔥 NKG prepara um ataque...")

    # escolhe ataque sem repetir
    ataque = ultimo_ataque
    while ataque == ultimo_ataque:
        ataque = random.choices(
            [a[0] for a in ataques],
            weights=[a[1] for a in ataques]
        )[0]

    ultimo_ataque = ataque

    print(f"NKG usa: {ataque.upper()}")

    acao = input("Sua reação (pular / esquivar / atacar / focar): ").lower()

    if acao == reacoes[ataque]:
        print("🩰 Movimento perfeito!")
        vida_grimm -= 1
    else:
        print("💥 Você errou o tempo!")
        vida_jogador -= 1

    print(f"❤️ Sua vida: {vida_jogador} | 🩸 Grimm: {vida_grimm}")

    if vida_jogador <= 0:
        print("\n☠️ Você caiu na dança do pesadelo...")
        luta_ativa = False

    elif vida_grimm <= 0:
        print("\n🏆 Você dominou a dança do NKG!")
        luta_ativa = False
