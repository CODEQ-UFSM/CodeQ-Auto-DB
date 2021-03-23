import os
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

def getHtmlFromDir(dir):
    dir = dir if dir != '' else None
    htmls=[]
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

def getTrilhaIdByName(name,cursor):
    cursor.execute('SELECT id_trilha FROM trilha WHERE nome LIKE "%' + name + '%"')
    return cursor.fetchall()

#def orderDirByOrderArray(order_array, dir):

#def clearIdentificationOfDir: