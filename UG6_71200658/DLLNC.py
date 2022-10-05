from NodeMahasiswa import NodeMahasiswa

class DLLNC:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def addElementTail(self,nama,ipk):
        newNode = NodeMahasiswa(nama,ipk)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode._prev = self.tail
            self.tail._next = newNode
            self.tail = newNode
        self.size +=1
        print('Data masuk ke tail!\n')

    def deleteLast(self):
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            hapus = self.tail
            self.tail = self.tail._prev
            hapus = None
            self.tail.next = None
            del hapus
        self.size -= 1

    def printAllDescending(self):
        helper = self.tail
        print('===== PRINT DESCENDING =====')
        while helper != None:
            print('====================')
            print('Nama: ', helper.getNama())
            print('IPK: ', helper.getIpk())
            helper = helper._prev

    def rataIpk(self):
        helper = self.head
        average = 0
        sumOfIpk = 0
        while helper != None:
            sumOfIpk += helper.getIpk()
            helper = helper._next
        average = sumOfIpk // self.size
        print('Rata - rata: ', average)

Program = DLLNC()
Program.addElementTail('Shalom',3.9)
Program.addElementTail('Nabilla',3.8)
Program.addElementTail('Kurniadi',3.7)
Program.addElementTail('Haris',3.6)
Program.printAllDescending()

Program.deleteLast()
Program.printAllDescending()

Program.rataIpk()