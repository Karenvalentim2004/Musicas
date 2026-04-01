import time
from colorama import Fore, Style, init

init(autoreset=True)

def atual(texto):
    return Fore.MAGENTA + Style.BRIGHT + texto

def contexto(texto):
    return texto

def limpar_linha():
    print("\033[K", end="")

def escrever_animado(texto, delay=0.06):
    for char in texto:
        print(char, end="", flush=True)
        time.sleep(delay)

letra = [
    (0, "Bom mesmo é ganhar um beijo seu"),
    (5, "Te ouvir"),
    (8, "E sentir seu corpo junto ao meu"),
    (15, "Pintar o mundo só para nós dois"),
    (19, "Ser feliz, sem pensar no que virá depois"),
]

duracao_total = 31

inicio = time.time()
indice = 0
texto_animado = ""
char_index = 0

print("\033[2J")
print("\033[?25l")

while True:

    tempo_atual = time.time() - inicio

    if tempo_atual > duracao_total:
        break

    if indice < len(letra) - 1 and tempo_atual >= letra[indice + 1][0]:
        indice += 1
        texto_animado = ""
        char_index = 0

    linha_atual = letra[indice][1]

    # controla velocidade da digitação
    if char_index < len(linha_atual):
        texto_animado += linha_atual[char_index]
        char_index += 1
        time.sleep(0.06)

    anterior2 = letra[indice-2][1] if indice >= 2 else ""
    anterior1 = letra[indice-1][1] if indice >= 1 else ""
    proxima1 = letra[indice+1][1] if indice+1 < len(letra) else ""
    proxima2 = letra[indice+2][1] if indice+2 < len(letra) else ""

    print("\033[H", end="")

    limpar_linha()
    print("NO CÉU DOS BRAÇOS TEUS")

    limpar_linha()
    print("Di Paullo & Paulino")

    print()

    limpar_linha()
    print(contexto(anterior2))

    limpar_linha()
    print(contexto(anterior1))

    limpar_linha()
    print(atual(texto_animado))  # aqui anima

    limpar_linha()
    print(contexto(proxima1))

    limpar_linha()
    print(contexto(proxima2))

    time.sleep(0.02)

print("\033[?25h")