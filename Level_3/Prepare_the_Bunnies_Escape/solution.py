def solution(n):
    height = len(n) - 1
    length = len(n[0]) - 1

    list_nodes = []
    wall_nodes = []

    for row, row_val, in enumerate(n):
        row_x = n[row]
        for col, col_val in enumerate(row_x):
            new_node = Node(col, row, col_val)
            list_nodes.append(new_node)
            if col_val == 1:
                wall_nodes.append(new_node)
            if row == 0 and col == 0:
                start_node = new_node
            if row == height and col == length:
                end_node = new_node

    for node in list_nodes:
        valid_nbrs = []
        for nbr in list_nodes:
            if node.x == nbr.x and node.y == nbr.y:
                continue

            for i in range(-1, 2):
                for j in range(-1, 2):
                    x = node.x + i
                    y = node.y + j
                    if x <= length and y <= height and (abs(i) != abs(j)) and x >= 0 and y >= 0:
                        valid_nbrs.append((x, y))

            if (nbr.x, nbr.y) in valid_nbrs:
                node.add_to_nbrs(nbr)

    bfs(start_node, True)
    bfs(end_node, False)

    min_distance = 10000000

    for wall in wall_nodes:
        candidates = []
        for nbr in wall.nbrs:
            if nbr.wall == 0:
                candidates.append(nbr)

        if len(candidates) > 1:
            list_start = []
            list_end = []
            for node in candidates:
                list_start.append(node.dist_to_start)
                list_end.append(node.dist_to_end)
            test_distance = min(list_start) + min(list_end) + 1
            min_distance = min(min_distance, test_distance)

    return min_distance


def bfs(entry, direction):
    queue = Queue()
    queue.add(entry)
    count = 0

    while queue.get_size() > 0:
        count += 1
        current_node = queue.get_next()

        if count == 1 and direction == True:
            current_node.visit_start = 1
            current_node.dist_to_start = 1

        if count == 1 and direction == False:
            current_node.visit_end = 1
            current_node.dist_to_end = 1

        for nbr in current_node.nbrs:
            if nbr.wall != 1:
                if direction == 1 and not nbr.visit_start:
                    nbr.dist_to_start = current_node.dist_to_start + 1
                    nbr.visit_start = True
                    queue.add(nbr)

                elif direction == 0 and not nbr.visit_end:
                    nbr.dist_to_end = current_node.dist_to_end + 1
                    nbr.visit_end = True
                    queue.add(nbr)


class Node:

    def __init__(self, x, y, wall):
        self.x = x
        self.y = y
        self.wall = wall
        self.nbrs = []
        self.dist_to_start = 100000
        self.dist_to_end = 100000
        self.visit_start = False
        self.visit_end = False

    def add_to_nbrs(self, nbr):
        self.nbrs.append(nbr)


class Queue:

    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def get_next(self):
        return self.items.pop(0)

    def get_size(self):
        return len(self.items)


def main():
    assert solution([[0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 1, 1, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 1, 1, 1, 1, 1],
                     [0, 1, 1, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0]]) == 11

    assert solution([[0, 1, 1, 0],
                     [0, 0, 0, 1],
                     [1, 1, 0, 0],
                     [1, 1, 1, 0]]) == 7

    assert solution([[0, 1],
                     [1, 0]]) == 3

    assert solution([[0, 1, 1, 1],
                     [0, 1, 1, 1],
                     [0, 1, 1, 1],
                     [0, 1, 1, 1],
                     [1, 0, 0, 0]]) == 8


if __name__ == '__main__':
    main()
