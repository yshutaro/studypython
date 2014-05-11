#Your code here
#You can import some modules or create additional functions


class Node():
    start = None
    goal = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.hs = (x - self.goal[0])**2 + (y - self.goal[1])**2
        self.fs = 0
        self.parent_node = None

    def toString(self):
        s = "(x,y)=" + str(self.pos) \
                + " hs=" + str(self.hs) \
                + " fs=" + str(self.fs)
        return s

class NodeList(list):
    def find(self, x, y):
        l = [t for t in self if t.pos == (x, y)]
        return l[0] if l != [] else None

    def remove(self, node):
        del self[self.index(node)]

openList = NodeList()
closedList = NodeList()

Node.start = (1, 1)
Node.goal = (10, 10)
start_node = Node(*Node.start)
start_node.fs = start_node.hs
openList.append(start_node)

def checkio(maze_map):
    #replace this for solution
    #This is just example for first maze

    map_width = len(maze_map[0])
    map_height = len(maze_map)

    #print(map_width)
    #print(map_height)

    while openList:
        print("######1")
        ol_str = ""
        for ol in openList:
            ol_str = ol_str + ol.toString()
        print("open:" + ol_str)
        n = min(openList, key=lambda x:x.fs)
        print("min_open:" + n.toString())
        openList.remove(n)
        closedList.append(n)

        if n.pos == Node.goal:
            print("###END###")
            end_node = n
            break

        # g*() = f*() - h*()
        print("######2")
        n_gs = n.fs - n.hs
        print("n_gs:" + str(n_gs))

        for v in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x = n.pos[0] + v[0]
            y = n.pos[1] + v[1]

            print("######3")
            print("(x,y):" + str(x) + " " + str(y))
            if not (0 < x < map_width and 
                    0 < y < map_height and
                    maze_map[y][x] != 1):
                continue

            print("######4")
            m = openList.find(x, y)
            cost = (n.pos[0] - x)**2 + (n.pos[1] - y)**2
            if m:
                if m.fs > n_gs + m.hs + cost:
                    m.fs = n_gs + m.hs + cost
                    m.parent_node = n
            else:
                m = closedList.find(x, y)
                if m:
                    if m.fs > n_gs + m.hs + cost:
                        m.fs = n_gs + m.hs + cost
                        m.parent_node = n
                        openList.append(m)
                        closedList.remove(m)
                else:
                    m = Node(x, y)
                    m.fs = n_gs = m.hs + cost
                    m.parent_node = n
                    openList.append(m)

    n = end_node.parent_node
    result_move = (end_node.pos[0] - n.pos[0], end_node.pos[1] - n.pos[1])
    move = {(1, 0): "E", (-1, 0): "W", (0, -1): "N", (0, 1): "S"}
    result = move[result_move]
    print("result=" + result)

    print(n.toString())
    while n.parent_node:
        c_n_x = n.pos[0]
        c_n_y = n.pos[1]
        n = n.parent_node
        movepoint = (c_n_x - n.x, c_n_y - n.y)
        #print(movepoint)
        result = move[movepoint] + result
        print(n.toString())

    print(result)
    return "SSSSSEENNNEEEEEEESSWWWWSSSEEEESS"

if __name__ == '__main__':
    #This code using only for self-checking and not necessary for auto-testing
    def check_route(func, labyrinth):
        MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
        #copy maze
        route = func([row[:] for row in labyrinth])
        pos = (1, 1)
        goal = (10, 10)
        for i, d in enumerate(route):
            move = MOVE.get(d, None)
            if not move:
                print("Wrong symbol in route")
                return False
            pos = pos[0] + move[0], pos[1] + move[1]
            if pos == goal:
                return True
            if labyrinth[pos[0]][pos[1]] == 1:
                print("Player in the pit")
                return False
        print("Player did not reach exit")
        return False

    # These assert are using only for self-testing as examples.
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "First maze"
    assert check_route(checkio, [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Empty maze"
#    assert check_route(checkio, [
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
#        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Up and down maze"
#    assert check_route(checkio, [
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
#        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Dotted maze"
#    assert check_route(checkio, [
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
#        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
#        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
#        [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
#        [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
#        [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
#        [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#        [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
#        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
#        [1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "Need left maze"
#    assert check_route(checkio, [
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
#        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#        [1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1],
#        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
#        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
#        [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]), "The big dead end."
    print("The local tests are done.")
