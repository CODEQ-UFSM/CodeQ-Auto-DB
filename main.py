import mysql.connector
from utils import *
import os

trilhas = ['Pensamento', 'Matemática']

#dbname = 'codeqatualizado'
#db = mysql.connector.connect(host="localhost", user="root", password="")

#cursor = db.cursor()

# Recreate database
#cursor.execute("DROP DATABASE " + dbname)
#cursor.execute("CREATE DATABASE " + dbname)

#db = mysql.connector.connect(host="localhost", user="root", password="", database=dbname)
#cursor = db.cursor()

# Import existent database
#print('IMPORTANDO MODELO COM :\n -Pensamento Lógico\n -Mat\n -Física\n -Est\n -EQ')
#executeScriptsFromFile('codeqmodelo.sql', cursor)
#print('\nIMPORTADO COM SUCESSO!')

# Identificando as pastas

# Tirando .html's da pasta principal
#cleanHtmlFromDir('')

# Identificando pasta principal
pasta_trilhas = getSubfolderNameThatContains('', 'Trilhas')

# "Limpando pastas (principal+cada trilha)
#cleanHtmlFromDir(pasta_trilhas)
#for pasta in os.listdir(pasta_trilhas):
#    cleanHtmlFromDir(pasta_trilhas + '/' + pasta)

# Identificando pastas das trilhas
pastas = []
for trilha in trilhas:
    pastas.append(pasta_trilhas + '/' + getSubfolderNameThatContains(pasta_trilhas, trilha))


for pasta in pastas:
    # ENTRAR NO HTML DE CADA AULA -> VER A ORDEM DAS AULAS -> ADICIONAR AS AULAS EM ORDEM
    secoes = os.listdir(pasta)
    for i in range(len(secoes)):
        secoes[i] = (pasta + '/' + secoes[i])

    print(secoes)































