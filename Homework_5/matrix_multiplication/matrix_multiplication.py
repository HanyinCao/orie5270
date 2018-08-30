from __future__ import with_statement
import os
import numpy as np
os.environ['SPARK_HOME'] = '/usr/local/Cellar/apache-spark/2.1.0/libexec'
exec(open(os.path.join(os.environ["SPARK_HOME"], 'python/pyspark/shell.py')).read())


def pyspark_matrix(A, v):
    '''
    A is the text file contains the matrix (doesn't contain the row index)
    B is the text file contains the vector
    '''

    A = sc.textFile(A).map(
        lambda line: np.array([float(x) for x in line.split(',')])).cache()
    v = sc.textFile(v).map(
        lambda line: np.array([float(x) for x in line.split(',')])).cache()

    A_flat_j = A.zipWithIndex().map(lambda l: (l[1], [(l[0][i], i) for i in range(len(l[0]))])).flatMap(
        lambda l: [(i[1], (l[0], i[0])) for i in l[1]])

    v = v.flatMap(lambda l: [(i, l[i]) for i in range(len(l))])

    A_flat_join = A_flat_j.join(v).map(lambda l: (l[1][0][0], l[1][0][1] * l[1][1])).reduceByKey(
        lambda a, b: a + b).map(lambda l: l[1])

    result = np.array(A_flat_join.collect())

    file = open("matrix_multiply_output.txt", "w")
    for num in result:
        file.write(str(num) + ', ')
        file.write('\n')
    file.close()

    return

if __name__ == '__main__':
    pyspark_matrix('A.txt', 'v.txt')