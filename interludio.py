import time
from colorama import Fore, Style, init

init(autoreset=True)

def atual(texto):
    return Fore.MAGENTA + Style.BRIGHT + texto

def contexto(texto):
    return texto

def limpar_linha():
    print("\033[K", end="")

def formatar_tempo(segundos):
    minutos = int(segundos // 60)
    segundos = int(segundos % 60)
    return f"{minutos}:{segundos:02d}"

def barra_spotify(tempo_real, total):

    tamanho = 30
    progresso = int((tempo_real / total) * tamanho)

    esquerda = "─" * progresso
    direita = "─" * (tamanho - progresso)

    return f"{formatar_tempo(tempo_real)} {esquerda}●{direita} {formatar_tempo(total)}"


letra = [
    (0, "Sentindo isso com tanta força que era quase insuportável"),
    (4, "Eu reli suas mensagens, eu esperei uma resposta"),
    (6, "Eu escrevi cem páginas no meu diário"),
    (9, "Eu procurei o afeto de outras pessoas"),
    (10, "Replicando exatamente a mesma sensação que você havia causado em mim"),
    (14, "E na segunda semana, quando essa agonia já havia esfriado no meu peito"),
    (18, "Eu pensei em te enviar essa mensagem"),
    (20, "Dizendo que você me ensinou uma lição muito valiosa"),
    (23, "O amor é uma coisa que a gente sente sozinho"),
    (26, "Às vezes a gente compartilha com o outro"),
    (28, "Mas no final das contas a gente sente sozinho, o tempo todo"),
    (32, "Você nunca vai saber o quanto eu te amei"),
    (34, "Mas eu te amei infinito"),
    (35, "Mesmo que tenha sido por um segundo, algumas horas, por uma noite"),
    (39, "Eu te amei.")
]

duracao_total = 142
offset = 95

inicio = time.time()
indice = 0

print("\033[2J")
print("\033[?25l")

while True:

    tempo_atual = time.time() - inicio
    tempo_real = tempo_atual + offset

    if tempo_real > duracao_total:
        break

    if indice < len(letra) - 1 and tempo_atual >= letra[indice + 1][0]:
        indice += 1

    anterior2 = letra[indice-2][1] if indice >= 2 else ""
    anterior1 = letra[indice-1][1] if indice >= 1 else ""
    atual_linha = letra[indice][1]
    proxima1 = letra[indice+1][1] if indice+1 < len(letra) else ""
    proxima2 = letra[indice+2][1] if indice+2 < len(letra) else ""

    print("\033[H", end="")

    limpar_linha()
    print("TE AMEI INFINITO (INTERLÚDIO)")

    limpar_linha()
    print("NandaTsunami")

    print()

    limpar_linha()
    print(barra_spotify(tempo_real, duracao_total))

    print()

    limpar_linha()
    print(contexto(anterior2))

    limpar_linha()
    print(contexto(anterior1))

    limpar_linha()
    print(atual(atual_linha))

    limpar_linha()
    print(contexto(proxima1))

    limpar_linha()
    print(contexto(proxima2))

    time.sleep(0.05)

print("\033[?25h") 