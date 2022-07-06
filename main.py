import pandas as pd
import tool
import arquivo
import buscas

criterios = [4,4,8,8]
def main():
    iniciar = True
    tool.limparTela()
    listaDeCandidatos = arquivo.verificarCsv()
    print('#'*20, "RH Facil", '#'*20, "\n")
    print("Menu:")
    print("Candidatos[1]")
    print("Buscar por Criterios[2]")
    print("Buscar por Nome[3]")
    print("Adicionar Candidato[4]")
    print("Modificar Criterio[5]")
    print("[sair]")
    
    while iniciar:

        entrada = input("Como posso ajudar? ")
        # lista de candidatos
        if(entrada == '1'):
            if(listaDeCandidatos.shape[0] == 0):
                print("A sua lista de Candidatos esta Vazia!")
            else:
                print("Os dez primeiros da sua lista")
                print(listaDeCandidatos.head())
        
        elif(entrada == '2'):
            buscas.buscarCriterio(criterios)
        
        elif(entrada == '3'):
            nome = input("Quem devo procurar? :")
            buscas.buscarNome(nome)
        
        elif(entrada == '4'):
            pr
        elif(entrada == '5'):
            print("1")
        elif(entrada.lower() == "sair"):
            print("1")
            iniciar = False
        else:
            print("Digite uma opção valida!")


main()