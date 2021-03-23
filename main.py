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
#print('Importado com sucesso!')

# Identificando pasta principal
pasta_trilhas = getSubfolderNameThatContains('', 'Trilhas')

for trilha in trilhas:
    print('Entrando na trilha ' + trilha)
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
        print('Entrando na seção ' + secao)
        insertSecaoInTrilha(secao, trilha, cursor, db)
        element = getElementThatContains(full_secoes, secao)
        pasta_secao = full_secoes[element]
        secao_html = pasta_secao + '.html'
        plain_html = open(secao_html, 'r', encoding='utf8').read()
        soup = BeautifulSoup(plain_html, 'html.parser')

        aulas_em_ordem = [t for t in soup.find_all(text=True) if t.parent.name in ['a', 'td']]

        full_aulas = getFoldersFromDir(pasta_secao)
        i = 1
        for aula in aulas_em_ordem:
            if getElementThatContains(full_aulas, aula) != -1:
                print('Entrando na aula: '+aula)
                element = getElementThatContains(full_aulas, aula)
                pasta_aula = full_aulas[element]
                aula_html = pasta_aula + '.html'
                plain_html = open(aula_html, 'r', encoding='utf8').read()
                soup = BeautifulSoup(plain_html, 'html.parser')

                if str(soup.find_all("span", {"class": "selected-value"})[0]) == '<span class="selected-value select-value-color-green">Feito</span>':
                    descricao = ''
                    data = ''
                    try:
                        imagem = str(soup.find_all("img", {"class": "page-cover-image"})[0])
                    except:
                        imagem=''
                    insertAulaInSecao(aula, i, descricao, data, imagem, secao, cursor, db)
                    html_aulas = [secao + '.html' for secao in full_secoes]

                    plain_html = open(aula_html, 'r', encoding='utf8').read()
                    soup = BeautifulSoup(plain_html, 'html.parser')
                    paginas_em_ordem = [t for t in soup.find_all(text=True) if t.parent.name in ['a', 'figure']]

                    j = 1
                    for pagina in paginas_em_ordem:
                        html_paginas = getHtmlFromDir(pasta_aula)
                        element = getElementThatContains(html_paginas, pagina)
                        html_atual = html_paginas[element]
                        plain_html = open(html_atual, 'r', encoding='utf8').read()
                        soup = BeautifulSoup(plain_html, 'html.parser')
                        HTML_FINAL = (' '.join(map(str, soup.article.contents))).replace('\n', '')
                        insertPaginaInAula(j, HTML_FINAL, aula, secao, cursor, db)
                        j = j + 1

                    i = i + 1

