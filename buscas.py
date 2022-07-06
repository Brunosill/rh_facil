from mailbox import NotEmptyError
import pandas as pd
import arquivo

def buscarNome(nome):
    listaCandidatos = arquivo.verificarCsv()
    procurar = listaCandidatos['Nome'] == nome
    pessoa = listaCandidatos[procurar]
    if pessoa.shape[0] == 1:
        
        print(f'{pessoa.Nome.to_string(index=False)} Teve as seguintes notas')
        print(f"e{pessoa['e'].to_string(index=False)}, t{pessoa['t'].to_string(index=False)}, p{pessoa['p'].to_string(index=False)}, s{pessoa['s'].to_string(index=False)}")
    else:
        print('Pessoal não esta na lista!')

def buscarCriterio(criterio):
    listaCandidatos = arquivo.verificarCsv()
    aprovados = (listaCandidatos['e'] >= criterio[0]) & (listaCandidatos['t'] >= criterio[1]) & (listaCandidatos['p'] >= criterio[2]) & (listaCandidatos['s'] >= criterio[3]) 
    if(aprovados.shape[0] > 0):
        listaAprovados = listaCandidatos[aprovados]
        for nome in listaAprovados['Nome']:
            print(nome)
    else:
        print('Ninguem passou pelo criteiro :(')

buscarCriterio([10,1,1,1])