import os
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

def cleanHtmlFromDir(dir):
    dir = dir if dir != '' else None
    for item in os.listdir(dir):
        if item.endswith(".html"):
            os.remove(os.path.join(dir, item))

def addFatherDir(father,sub):
    return None