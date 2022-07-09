import pandas as pd

def verificarCsv():
    try:
        with pd.read_csv('candidatos.csv', sep=';') as arquivo:
            return arquivo
    except:
        dados = {
            "Nome" : ['Bruno', 'Cristina', 'Camilo', 'Sandro'],
            "e": [5, 10, 8, 2],
            "t": [10, 7, 5, 2],
            "p": [8, 5, 4, 9],
            "s": [8, 8, 9, 7]
        }
        #columas = ['Nome', 'e', 't', 'p', 's']
        arquivo = pd.DataFrame(dados)
        arquivo.to_csv('candidatos.csv', sep=';', index= False)
        return pd.read_csv('candidatos.csv', sep=';')

def salvarAqrquivo(dados):
    dados.to_csv('candidatos.csv', sep=';', index= False)