class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.child = []

class Tree:
    def __init__(self,root):
        self.root = root

    def addChild(self, node_parent,data):
        #tulis kode Anda di sini
        #1. buat node baru menggunakan Class Node()
        #2. isi parent dari node baru tersebut dengan node_parent
        #3. node_parent menambahkan node baru (anaknya)
        #4. return node baru
        new = Node(data)
        new.parent = node_parent
        node_parent.child.append(new)
        return new

    def sums(self,node):
        #tulis kode Anda di sini
        tampung = []
        for i in node.child:
            tampung.append(i.data)
            for x in i.child:
                tampung.append(x.data)
                for z in x.child:
                    tampung.append(z.data)
        return sum(tampung)
                
    def sibling(self,node):
        #tulis kode Anda di sini
        pass
    

if __name__ =='__main__':
    val200 = Node(200)
    t = Tree(val200) #Level 0

    #Level 1 parent 200
    val23 = t.addChild(val200, 23) 
    val11 = t.addChild(val200, 11)

    #Level 2 parent 23
    val13 = t.addChild(val23, 13) 
    val57 = t.addChild(val23, 57) 

    #Level 2 parent 11
    val32 = t.addChild(val11, 32) 

    #Level 3 parent 13
    val42 = t.addChild(val13, 42) 
    val51 = t.addChild(val13, 51) 
    val71 = t.addChild(val13, 71) 

    #Level 3 parent 57
    val12 = t.addChild(val57, 12) 
    val15 = t.addChild(val57, 15)

    #Level 3 parent 24
    val33 = t.addChild(val32, 33)
    val8 = t.addChild(val32, 8)

    # No 2. #
    print(f'Total value of node {val200.data} and all of its decendands = {t.sums(val200)}')

 
    # No 3. #
    print(f'Total value of all sibling on node {val33.data} = {t.sibling(val33)}')