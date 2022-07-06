import pandas as pd
import arquivo
import tool




def adicionarCandidato(candidato):
    
    listaCandidatos = arquivo.verificarCsv()
    listaCandidatos.loc[listaCandidatos.shape[0]] = candidato
    arquivo.salvarAqrquivo(listaCandidatos)
    print("Candidato Salvo :)")


def coletarCandidato():
    tool.limparTela()
    novoCandidato = []
    novoCandidato.append(input("Nome do candidato ? "))
    novoCandidato.append(int(input("Nota da entrevista ? ")))
    novoCandidato.append(int(input("Nota do teste teórico ? ")))
    novoCandidato.append(int(input("Nota do teste pratico ? ")))
    novoCandidato.append(int(input("Nota da avaliação deo Soft skills ? ")))
    print(novoCandidato)
    adicionarCandidato(novoCandidato)
