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


def bellman_ford(graph, source):
    result = {}

    for k in graph.keys():
        result[k] = [float('Inf'), k, '/']
    result[source][0] = 0.0

    for count in range(len(graph)):
        for k in graph.keys():
            for i in graph[k]:
                if result[i[0]][0] > result[k][0] + i[1]:
                    result[i[0]][0] = result[k][0] + i[1]
                    result[i[0]][2] = k

    for k in graph.keys():
        for i in graph[k]:
            if result[i[0]][0] > result[k][0] + i[1]:
                return True, result

    return False, result


def get_negative_circles(result):
    visited = []

    for starting_points in result.keys():

        if starting_points in visited:
            continue

        path = [starting_points]
        visited.append(starting_points)
        current_points = starting_points

        while result[current_points][2] != '/':
            current_points = result[current_points][2]
            path.append(current_points)
            visited.append(current_points)

            if current_points in path[:-1]:
                first_index = path.index(current_points)
                return path[first_index:]


def find_negative_cicles(name_txt_file):
    graph = read_txt_file(name_txt_file)

    neg_circle, result = bellman_ford(graph, '0')

    if neg_circle:
        path = get_negative_circles(result)

        return path[::-1]
    else:
        return "No negative circle"


if __name__ == '__main__':
    find_negative_cicles('graph_5.txt')