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

    sumOfDifferences = 0

    for item in list:
        sumOfDifferences += math.pow(item - median, 2)

    part1 = math.pow(1 / math.pow(2 * pi * variance, 1 / 2), n)
    part2 = math.exp((-1 / (2 * variance) * sumOfDifferences)

    return part1 * part2


def main():
    file1a='file-l2-p-1a.txt'
    file1b='file-l2-p-1b.txt'
    fileEM='file-EM.txt'

    file1aList=getListFromFile(file1a)
    file1bList=getListFromFile(file1b)
    fileEMList=getListFromFile(fileEM)

    # questao 2 - 1
    print('normal 2.1.a')
    mediaf1a=getMedian(file1aList)
    varf1a=getVariance(file1aList)
    print('media 1a normal ' + str(mediaf1a))
    print('variance 1a normal ' + str(varf1a))

    print('uniform 2.1.b')
    minf1b=np.amin(file1aList)
    maxf1b=np.amax(file1aList)
    print('min 1b uniform ' + str(minf1b))
    print('max 1b uniform ' + str(maxf1b))

    print('')
    # questao 2 - 2
    print('normal 2.2.a')
    mediaf2a=getMedian(file1bList)
    varf2a=getVariance(file1bList)
    print('media 2a normal ' + str(mediaf2a))
    print('variance 2a normal ' + str(varf2a))

    print('uniform 2.2.b')
    minf2b=np.amin(file1bList)
    maxf2b=np.amax(file1bList)
    print('min 2b uniform ' + str(minf2b))
    print('max 2b uniform ' + str(maxf2b))

    # histogram = np.histogram(file1aList, 10)

    # hist, bins = np.histogram(file1aList, bins=50)


    # width = 0.7 * (bins[1] - bins[0])
    # center = (bins[:-1] + bins[1:]) / 2
    # plt.bar(center, hist, align='center', width=width)
    # plt.show()

    print('')
    print('2.3a')
    likelihood1Normal=likelihoodNormal(mediaf1a, varf1a, file1aList)
    likelihood1Uniform=likelihoodNormal(minf1b, maxf1b)

    print('normal ' + str(likelihood1Normal) + \
        ' uniform ' + str(likelihood1Uniform))
    # print()
    print('2.3b')
    likelihood2Normal=likelihoodNormal(mediaf2a, varf2a, file1bList)
    likelihood1Uniform=likelihoodNormal(minf2b, maxf2b)
    print('normal ' + str(likelihood2Normal) + \
        ' uniform ' + str(likelihood1Uniform))
    # print(mediaf1)
    # print(varf1)


main()
