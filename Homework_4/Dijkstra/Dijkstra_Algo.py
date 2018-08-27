import heapq

def get_path_weight(lines):
    result = []
    path_weight = lines.split(',')

    for i in range(0, len(path_weight), 2):
        result.append((str(path_weight[i][1:]), float(path_weight[i + 1][:-1])))

    return result


def read_txt_file(file_name):
    text_file = open(file_name, "r")
    raw_list = text_file.read().split('\n')

    graph = {}
    for i in range(0, len(raw_list), 2):
        key_value = str(raw_list[i])
        if i + 1 < len(raw_list) and raw_list[i + 1] != '':
            graph[key_value] = get_path_weight(raw_list[i + 1])
        else:
            graph[key_value] = []

    return graph


def dijkstra(graph, source):
    result = {}

    for k in graph.keys():
        result[k] = [float('Inf'), k, '/']
    result[source][0] = 0.0

    visited = []
    min_heap = []

    source_path = graph[source]
    heapq.heappush(min_heap, result[source])

    while len(min_heap) != 0:
        current_point = heapq.heappop(min_heap)
        current_point_path = graph[current_point[1]]

        if current_point[1] not in visited:
            for i in current_point_path:
                if result[i[0]][0] > current_point[0] + i[1]:
                    result[i[0]][0] = current_point[0] + i[1]
                    result[i[0]][2] = current_point[1]
                    heapq.heappush(min_heap, result[i[0]])

            visited.append(current_point[1])

    return result


def get_distance_path(source, destination, result):
    distance = result[destination][0]

    if distance == float('Inf'):
        return float('Inf'), ['/']

    else:
        path = []
        path.append(destination)
        while source not in path:
            path.append(result[path[-1]][2])
        path = path[::-1]

        return (distance, path)


def find_shortest_path(name_txt_file, source, destination):
    graph = read_txt_file(name_txt_file)

    d_result = dijkstra(graph, source)

    return get_distance_path(source, destination, d_result)


if __name__ == '__main__':
    x = find_shortest_path('graph_3.txt', '2', '0')

    print (x)