import mysql.connector
from utils import *
from bs4 import BeautifulSoup
import os

trilhas = ['Pensamento', 'Mat']

dbname = 'codeqatualizado'
db = mysql.connector.connect(host="localhost", user="root", password="", buffered = True)

cursor = db.cursor(buffered=True)

# Recreate database
cursor.execute("DROP DATABASE " + dbname)
cursor.execute("CREATE DATABASE " + dbname)

db = mysql.connector.connect(host="localhost", user="root", password="", database=dbname, buffered = True)
cursor = db.cursor(buffered = True)

# Import existent database
executeScriptsFromFile('codeqmodelo.sql', cursor)
print('Importado com sucesso!')

# Identificando pasta principal
pasta_trilhas = getSubfolderNameThatContains('', 'Trilhas')

for trilha in trilhas:
    # ENTRAR NO HTML DE CADA AULA -> VER A ORDEM DAS AULAS -> ADICIONAR AS AULAS EM ORDEM
    pasta = pasta_trilhas + '/' + getSubfolderNameThatContains(pasta_trilhas, trilha)
    full_secoes = getFoldersFromDir(pasta)
    html_secoes = [secao+'.html' for secao in full_secoes]

    # Pegar a ordem de cada seção dentro da trilha pelo html
    trilha_html = pasta + '.html'                                                      # Html de cada da trilha
    plain_html = open(trilha_html, 'r', encoding='utf8').read()                        # Lendo o html
    soup = BeautifulSoup(plain_html, 'html.parser')                                    # HTML Parser
    secoes_em_ordem = [t for t in soup.find_all(text=True) if t.parent.name in ['h4']] # As seções estão em um elemento h4

    for secao in secoes_em_ordem:
        insertSecaoInTrilha(secao, trilha, cursor, db)
        print('kkk')
        full_aulas = getFoldersFromDir(pasta)
        html_aulas = [secao + '.html' for secao in full_secoes]
