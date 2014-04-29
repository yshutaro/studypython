class Node:
    name = ""
    h = 0
    g = 0
    f = 0
    hasG = False
    hasF = False
    children = []
    childrenCosts = {}

    def __init__(self, name, h):
        self.name = name
        self.h = h

    def addChildren(self, child, cost):
        children.append(child)
        childrenCosts[child] = cost

    def getCost(self, child):
        return childrenCosts[child]

    def toString(self):
        result = name + "(h:" + str(h) + ")"
        if hasG:
            result = result + "g:" + str(g) + ")"
        if hasF:
            result = result + "f:" + str(f) + ")"
        return result

