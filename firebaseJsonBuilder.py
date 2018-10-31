fileName = input("What do you want to name this json file? ")
parent = input("What do you want to name your base tree? ")
childs = [str(x) for x in input("What child(s) do you want to add for this parent? ").split()]

def run():
    with open(fileName + '.json', 'a') as jsonFile:
        jsonFile.write('{\n  "' + parent + '" : {\n')
        for child in childs:
            keys = [str(x) for x in input('Does the child "{}" have a key(s)? '.format(child)).split()]
            keyJson = '    "{}" :  {},\n'.format(child, keys).replace("'", '"')
            jsonFile.write(keyJson)

        jsonFile.write('  }\n}')
        print("Json file created.")

if __name__ == '__main__':
    run()
