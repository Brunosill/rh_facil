from mailbox import NotEmptyError
from pydoc import apropos
import pandas as pd
import arquivo
import tool 


def buscarNome(nome):
    continuar = True
    while continuar:
        listaCandidatos = arquivo.verificarCsv()
        procurar = listaCandidatos['Nome'] == nome
        pessoa = listaCandidatos[procurar]
        if pessoa.shape[0] == 1:
            
            print(f'{pessoa.Nome.to_string(index=False)} Teve as seguintes notas')
            print(f"e{pessoa['e'].to_string(index=False)}, t{pessoa['t'].to_string(index=False)}, p{pessoa['p'].to_string(index=False)}, s{pessoa['s'].to_string(index=False)}")
        else:
            print('Pessoal não esta na lista!')
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False
    tool.limparTela()

def buscarCriterio(criterio):
    continuar = True
    while continuar:
        listaCandidatos = arquivo.verificarCsv()
        aprovados = (listaCandidatos['e'] >= criterio[0]) & (listaCandidatos['t'] >= criterio[1]) & (listaCandidatos['p'] >= criterio[2]) & (listaCandidatos['s'] >= criterio[3]) 
        listaAprovados = listaCandidatos[aprovados]
        if(listaAprovados.shape[0] >= 1):
            for x in range(listaAprovados.shape[0]):
                aprovado = listaAprovados.iloc[x]
                print(f"Candidato {aprovado['Nome']}: e{aprovado['e']}_t{aprovado['t']}_p{aprovado['p']}_s{aprovado['s']}")
        
        else:
            print('Ninguem passou pelo criteiro :(')
        volta = input("[s] Voltar ? ")
        if volta == "s":
            continuar = False

    tool.limparTela()