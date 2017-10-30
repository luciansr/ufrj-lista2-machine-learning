def getVectorFromFile(fileName):
    file_object = open(fileName, 'r')

    lista = file_object.readlines()
    result = map(float, lista)

    return result


def main():
    file1a = 'file-l2-p-1a.txt'
    file1b = 'file-l2-p-1b.txt'
    file1a = 'file-EM.txt'
    print('teste')
    resultado = getVectorFromFile(file1a)

    print(resultado)


main()
