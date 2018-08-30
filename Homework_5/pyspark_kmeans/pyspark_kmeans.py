from __future__ import with_statement
import os
import numpy as np
os.environ['SPARK_HOME'] = '/usr/local/Cellar/apache-spark/2.1.0/libexec'
exec(open(os.path.join(os.environ["SPARK_HOME"], 'python/pyspark/shell.py')).read())


def load_data(file_1, file_2):
    data = sc.textFile(file_1).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).cache()

    # Load the initial centroids
    centroids1 = sc.textFile(file_2).map(
        lambda line: np.array([float(x) for x in line.split(' ')])).collect()

    return data, centroids1


def distance(point_1, point_2):
    d_square = 0

    for index in range(len(point_1)):
        d_square = d_square + (point_1[index] - point_2[index]) ** 2

    return d_square ** 0.5


def classify(point, centroids):
    d = float('Inf')
    smallest_index = -1

    for index in range(len(centroids)):
        d_single = distance(point, centroids[index])

        if d_single < d:
            d = d_single
            smallest_index = index

    return smallest_index


def if_equal(centroids_1, centroids_2):
    if len(centroids_1) != len(centroids_2):
        return False

    for c in centroids_1:
        if c not in centroids_2:
            return False

    return True



def pyspark_kmeans(data_file, centroids_file, Max_iter=20):

    points, centroids = load_data(data_file, centroids_file)

    centroids = [l.tolist() for l in centroids]

    for i in range(Max_iter):

        points_classified = points.map(lambda d: (classify(d, centroids), [np.array(d), 1]))

        class_sum = points_classified.reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1]))

        new_centroids = class_sum.map(lambda x: x[1][0] / x[1][1]).collect()

        new_centroids = [l.tolist() for l in new_centroids]

        if if_equal(centroids, new_centroids):
            break
        else:
            centroids = new_centroids

    with open('output.txt', 'w') as f:
        for _list in centroids:
            for _string in _list:
                f.write(str(_string) + ', ')
            f.write('\n')

    return

if __name__ == '__main__':
    pyspark_kmeans('data.txt', 'c1.txt')