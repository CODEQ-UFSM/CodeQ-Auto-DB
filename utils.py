import os, shutil
import unicodedata
import mysql.connector


def executeScriptsFromFile(filename, cursor):
    # Open and read the file as a single buffer
    fd = open(filename, encoding="utf8")
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')

    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except:
            print(command)


def getSubfolderNameThatContains(dir, substring):
    return [string for string in os.listdir(dir if dir != '' else None) if substring in string][0]


def getElementThatContains(arr_dir, substring):
    substring = (substring[:45]) if len(substring) > 45 else substring
    for i in range(len(arr_dir)):
        if (simplify(arr_dir[i])).find(((((simplify(substring)).replace(':','')).replace('?','')).replace('!','')).replace('/',' ')) != -1:
            flag=1
            return i
        else:
            flag=-1
    if flag==-1:
        return -1


def getHtmlFromDir(dir):
    dir = dir if dir != '' else None
    htmls = []
    for item in os.listdir(dir):
        if item.endswith(".html"):
            htmls.append(os.path.join(dir, item))
    return htmls


def getFoldersFromDir(dir):
    dir = dir if dir != '' else None
    return [dir + '/' + d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]


def insertSecaoInTrilha(secao, trilha, cursor, db):
    id = str(getTrilhaIdByName(trilha, cursor)[0][0])
    cursor.execute('INSERT INTO secao (id_trilha, nome) VALUES (' + id + ', "' + secao + '")')
    db.commit()


def insertAulaInSecao(aula, i, descricao, data, imagem, secao, cursor, db):
    id = str(getSecaoIdByName(secao, cursor)[0][0])
    data='null'
    sql = 'INSERT INTO aula(nome,num_ordem,descricao,data,imagem,id_secao) VALUES (%s,%s,%s,%s,%s,%s)'
    val=(str(aula), i,str(descricao),str(data),str(imagem),id)
    cursor.execute(sql, val)
    db.commit()

def insertPaginaInAula(j, HTML_FINAL, titulo, aula, secao, cursor, db):
    id_aula = str(getAulaIdByName(aula, secao, cursor)[0][0])
    sql = 'INSERT INTO pagina(num_ordem, html, titulo, id_aula) VALUES (%s, %s, %s, %s)'
    val = (str(j),HTML_FINAL,titulo,id_aula)
    cursor.execute(sql,val)
    db.commit()

def getAulaIdByName(name, secao, cursor):
    id_secao = str(getSecaoIdByName(secao, cursor)[0][0])
    cursor.execute('SELECT id_aula FROM aula WHERE nome LIKE "%' + name + '%" AND id_secao='+id_secao)
    return cursor.fetchall()

def getTrilhaIdByName(name, cursor):
    cursor.execute('SELECT id_trilha FROM trilha WHERE nome LIKE "%' + name + '%"')
    return cursor.fetchall()


def getSecaoIdByName(name, cursor):
    cursor.execute('SELECT id_secao FROM secao WHERE nome LIKE "%' + name + '%"')
    return cursor.fetchall()


# def orderDirByOrderArray(order_array, dir):

# def clearIdentificationOfDir:

def simplify(text):
    import unicodedata
    try:
        text = unicode(text, 'utf-8')
    except NameError:
        pass
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    return str(text)

def clearFolder(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))