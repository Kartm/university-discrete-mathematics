from tabulate import tabulate
from fractions import Fraction

from similarity_functions import Similarity
from set import SetOperation


def tableToSet(table):
    result = []
    for row in table:
        newRow = []
        for i, item in enumerate(row, start=0):
            if(item == 1):
                newRow.append("t{}".format(i+1))
        result.append(newRow)
    return result


def printTable(table):
    for i, row in enumerate(table):
        print("u{}".format(i+1), end=": ")
        for item in row:
            print(item, end=" ")
        print("")


def calculateSimilarities(table):
    modifiedTable = tableToSet(table)
    printTable(modifiedTable)

    results = []
    sums = [0] * 9

    for i, vertical in enumerate(modifiedTable):
        row = []
        row.append("u{}".format(i+1))

        for j, horizontal in enumerate(modifiedTable):
            # if(i >= j):
            # similarity = Similarity.jaccard(vertical, horizontal)
            # similarity = Similarity.dice(vertical, horizontal)
            similarity = Similarity.symmetricDifference(vertical, horizontal)
            sums[j] += float(similarity)

            if(float(similarity) == 1 or float(similarity) == 0):
                row.append("{}".format(str(similarity)))
            else:
                result = "{}≈{}".format(
                    str(similarity), round(float(similarity), 3))
                row.append(result)

        results.append(row)
        print("")

    newSums = ["SUM"]
    for item in sums:
        newSums.append("{}".format(round(item, 3)))

    results.append(newSums)
    return results


def getHeaders(i):
    headers = []
    headers.append("")
    for i in range(i):
        headers.append("u{}".format(i+1))
    return headers

# - t1 t2 t3 ... t3
# u1
# u2
# ...
# u9


U = [
    [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1]
]

results = calculateSimilarities(U)

print(tabulate(results, headers=getHeaders(9), tablefmt="plain"))
