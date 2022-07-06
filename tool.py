import os

def limparTela():
    return lambda: os.system('cls' if os.name == 'nt' else 'clear')