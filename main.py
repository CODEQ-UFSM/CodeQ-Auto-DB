import mysql.connector
from utils import *
from bs4 import BeautifulSoup
import os

trilhas = ['Pensamento', 'Matemática']

dbname = 'codeqatualizado'
db = mysql.connector.connect(host="localhost", user="root", password="")

cursor = db.cursor()

# Recreate database
cursor.execute("DROP DATABASE " + dbname)
cursor.execute("CREATE DATABASE " + dbname)

db = mysql.connector.connect(host="localhost", user="root", password="", database=dbname)
cursor = db.cursor()

# Import existent database
executeScriptsFromFile('codeqmodelo.sql', cursor)
print('Importado com sucesso!')

# Identificando pasta principal
pasta_trilhas = getSubfolderNameThatContains('', 'Trilhas')

# Identificando pastas das trilhas
pastas = []
for trilha in trilhas:
    pastas.append(pasta_trilhas + '/' + getSubfolderNameThatContains(pasta_trilhas, trilha))

html_trilhas = [trilha+'.html' for trilha in pastas] # Html de cada uma das trilhas declaradas na primeira linha

# Pegar a ordem de cada seção dentro da trilha pelo html
teste_html = html_trilhas[1]
plain_html = open(teste_html, 'r', encoding='utf8').read()
soup = BeautifulSoup(plain_html, 'html.parser')
secoes_em_ordem = [t for t in soup.find_all(text=True) if t.parent.name in ['h4']]

print(secoes_em_ordem)



for pasta in pastas:
    # ENTRAR NO HTML DE CADA AULA -> VER A ORDEM DAS AULAS -> ADICIONAR AS AULAS EM ORDEM
    full_secoes = getFoldersFromDir(pasta)
    #html_secoes = getHtmlFromDir(pasta)
    html_secoes = [secao+'.html' for secao in full_secoes]