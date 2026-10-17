# Sistema de monitoramento de um reservatório de água
# Exibe no terminal a situação de cada nível, com uma cor diferente.

# Importa da biblioteca colorama: Fore (cor do texto) e Style (estilo)
from colorama import Fore, Style

# Lista com as mensagens dos 5 níveis (posição 0 = nível 1, posição 1 = nível 2...)
mensagens = [
    "Nível 1: Muito baixo (crítico)",
    "Nível 2: Baixo",
    "Nível 3: Médio",
    "Nível 4: Alto",
    "Nível 5: Muito alto (alerta)"
]


# Função: recebe o número do nível e DEVOLVE a cor correspondente
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    else:
        return Fore.BLUE


# Simulação: percorre os 5 níveis e mostra cada mensagem com a sua cor
print("=== Monitoramento do Reservatório ===")
for numero_nivel in range(1, 6):
    cor = definir_cor(numero_nivel)
    print(cor + mensagens[numero_nivel - 1])

# Restaura o estilo padrão do terminal
print(Style.RESET_ALL)
