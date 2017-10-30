import sklearn as sk
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math


def getListFromFile(fileName):
    file_object = open(fileName, 'r')

    lista = file_object.readlines()
    result = list(map(float, lista))

    return result


def getVariance(list):
    return np.var(list)


def getMedian(list):
    return np.median(list)


def likelihoodUniform(a, b, n):
    return math.pow(1 / (b - a), n)


def likelihoodNormal(median, variance, list):
    pi = math.pi
    n = len(list)

    sumOfDifferences = 0

    for item in list:
        sumOfDifferences += math.pow(item - median, 2)

    part1 = math.pow(1 / math.pow(2 * pi * variance, 1 / 2), n)
    part2 = math.exp((-1 / (2 * variance) * sumOfDifferences))
    return part1 * part2


def questao2():
    file1a = 'file-l2-p-1a.txt'
    file1b = 'file-l2-p-1b.txt'
    fileEM = 'file-EM.txt'

    file1aList = getListFromFile(file1a)
    file1bList = getListFromFile(file1b)
    fileEMList = getListFromFile(fileEM)

    # questao 2 - 1
    print('normal 2.1.a')
    mediaf1a = getMedian(file1aList)
    varf1a = getVariance(file1aList)
    print('media 1a normal ' + str(mediaf1a))
    print('variance 1a normal ' + str(varf1a))

    print('uniform 2.1.b')
    minf1b = np.amin(file1aList)
    maxf1b = np.amax(file1aList)
    print('min 1b uniform ' + str(minf1b))
    print('max 1b uniform ' + str(maxf1b))

    print('')
    # questao 2 - 2
    print('normal 2.2.a')
    mediaf2a = getMedian(file1bList)
    varf2a = getVariance(file1bList)
    print('media 2a normal ' + str(mediaf2a))
    print('variance 2a normal ' + str(varf2a))

    print('uniform 2.2.b')
    minf2b = np.amin(file1bList)
    maxf2b = np.amax(file1bList)
    print('min 2b uniform ' + str(minf2b))
    print('max 2b uniform ' + str(maxf2b))

    print('')
    print('2.3a')
    likelihood1Normal = likelihoodNormal(mediaf1a, varf1a, file1aList)
    likelihood1Uniform = likelihoodUniform(minf1b, maxf1b, len(file1aList))

    print('normal ' + str(likelihood1Normal) +
          ' uniform ' + str(likelihood1Uniform))
    # print()
    print('2.3b')
    likelihood2Normal = likelihoodNormal(mediaf2a, varf2a, file1bList)
    likelihood1Uniform = likelihoodUniform(minf2b, maxf2b, len(file1bList))
    print('normal ' + str(likelihood2Normal) +
          ' uniform ' + str(likelihood1Uniform))
    # print(mediaf1)
    # print(varf1)

    hist, bins = np.histogram(file1bList, bins=50)

    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.show()


def erroQuadratico(x, y, f):
    n = len(x)

    somaDeErros = 0

    index = 0
    for xitem in x:
        yitem = y[index]

        erro = yitem - f(xitem)
        erro2 = math.pow(erro, 2)

        somaDeErros += erro2

        ++index

    erroQuadraticoResult = somaDeErros / n

    return erroQuadraticoResult


def questao3():
    areaImovel = np.array([
        334,
        438,
        520,
        605,
        672,
        767
    ])

    precoVenda = np.array([
        39300,
        60000,
        68500,
        86000,
        113000,
        133000
    ])

    m1 = np.polyfit(areaImovel, precoVenda, 1)
    m2 = np.polyfit(areaImovel, precoVenda, 4)

    print('\n3.1')
    print(m1)
    print(m2)

    fM1 = np.poly1d(m1)
    fM2 = np.poly1d(m2)

    print('\n3.2')

    eqm1 = erroQuadratico(areaImovel, precoVenda, fM1)
    eqm2 = erroQuadratico(areaImovel, precoVenda, fM2)
    print(eqm1)
    print(eqm2)

    print(eqm1 / eqm2)

    print('\n3.3')
    print(fM1(848))
    print(fM1(912))
    print(fM2(848))
    print(fM2(912))

    print('\n3.4')

    areaImovel2 = np.array([
        848,
        912
    ])

    precoVenda2 = np.array([
        155900,
        156000
    ])

    eqm12 = erroQuadratico(areaImovel2, precoVenda2, fM1)
    eqm22 = erroQuadratico(areaImovel2, precoVenda2, fM2)
    print(eqm12)
    print(eqm22)

    print(eqm12 / eqm22)


questao3()
