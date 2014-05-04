class Node:

    def __init__(self, name, h):
        self.name = name
        self.h = h
        self.children = []
        self.childrenCosts = dict()
        self.hasG = False
        self.hasF = False

    def getName(self):
        return self.name

    def setPointer(self, node):
        self.pointer = node

    def addChildren(self, child, cost):
        self.children.append(child)
        self.childrenCosts[child] = cost

    def getChildren(self):
        return self.children

    def getCost(self, child):
        return self.childrenCosts[child]

    def toString(self):
        result = self.name + "(h:" + str(self.h) + ")"
        if self.hasG:
            result = result + "g:" + str(self.g) + ")"
        if self.hasF:
            result = result + "f:" + str(self.f) + ")"
        return result

class Search:

    def __init__(self):
        self.node = []
        self.makeStateSpace()

    def makeStateSpace(self):
        self.node.append(Node("A",0))
        self.start = self.node[0]
        
        self.node.append(Node("B",7))
        self.node.append(Node("C",4))
        self.node.append(Node("D",6))
        self.node.append(Node("E",1))
        self.node.append(Node("F",2))
        self.node.append(Node("G",3))
        self.node.append(Node("H",4))
        self.node.append(Node("I",2))
        self.node.append(Node("J",0))

        self.goal = self.node[9]

        self.node[0].addChildren(self.node[1],1)
        self.node[0].addChildren(self.node[2],3)
        self.node[1].addChildren(self.node[2],1)
        self.node[1].addChildren(self.node[6],6)
        self.node[2].addChildren(self.node[3],6)
        self.node[2].addChildren(self.node[6],6)
        self.node[2].addChildren(self.node[7],3)
        self.node[3].addChildren(self.node[4],5)
        self.node[3].addChildren(self.node[7],2)
        self.node[3].addChildren(self.node[8],4)
        self.node[4].addChildren(self.node[8],2)
        self.node[4].addChildren(self.node[9],1)
        self.node[5].addChildren(self.node[1],1)
        self.node[6].addChildren(self.node[5],7)
        self.node[6].addChildren(self.node[7],2)
        self.node[7].addChildren(self.node[8],3)
        self.node[7].addChildren(self.node[9],7)
        self.node[8].addChildren(self.node[9],6)

    def breadthFirst(self):
        open = []
        open.append(self.start)
        success = False
        closed = []

        step = 0
        while True:
            step = step + 1
            print("STEP:" + str(step))
            openstr = ""
            for op in open:
                openstr = openstr + " " + op.toString()
            print("OPEN:" + openstr)
            closedstr = ""
            for cld in closed:
                closedstr = closedstr + " " + cld.toString()
            print("closed:" + closedstr)

            if len(open) == 0:
                success = False
                break
            else:
                node = open[0]
                open.remove(open[0])

                if node == self.goal:
                    success = True
                    break
                else:
                    children = node.getChildren()
                    closed.append(node)

                    for m in children:
                        if m not in open and m not in closed:
                            m.setPointer(node)
                            if m == self.goal:
                                open.insert(0,m)
                            else:
                                open.append(m)
                            
        return success

class Main:
    if __name__ == '__main__':
        print("Start.")

        search = Search()
        search.breadthFirst()

    
        print("End.")
        
