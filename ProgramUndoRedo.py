from copy import deepcopy


class StackList:
    def __init__(self):
        self.stack_data = list()

    def push(self, new_data):
        self.stack_data.append(new_data)

    def top(self):
        if len(self.stack_data) ==0:
            return None
        else:
            return self.stack_data[-1]

    def pop(self):

        if len(self.stack_data) == 0:
            return None
        else:
            pop_data = self.stack_data.pop()
            return pop_data

    def size(self):
        return len(self.stack_data)


class UndoRedo:
    def __init__(self):
        self.mainStack = StackList() #stack ini sebagai tempat menyimpan data pertama kali
        self.backupStack = StackList() #stack ini sebagai tempat menyimpan data yang di hapus

    def write(self,data):
        self.mainStack.push(data)
        print('Data', data, 'berhasil ditambahkan!\n')

    def undo(self):
        if self.mainStack.size() == 0:
            print('Perintah Undo Tidak Dapat Dilakukan !')
            print('Data Undo: None\n')
        else:
            self.backupStack.push(self.mainStack.pop())
            for data in self.mainStack.stack_data:
                print(data, end=' ')
            print()
        

    def redo(self):
        if self.backupStack.size() == 0:
            print('Perintah Redo Tidak Dapat Dilakukan !')
            print('Data Redo: None\n')
        else:
            self.mainStack.push(self.backupStack.pop())
            for data in self.mainStack.stack_data:
                print(data, end=' ')
            print()

    def printInfo(self):
        for data in self.mainStack.stack_data:
            print(data, end=' ')
        print()

if __name__ == '__main__':
    obj_undoredo = UndoRedo()
    obj_undoredo.undo() #Test case Jika belum ada data yang ditambahkan
    obj_undoredo.redo() #Test case jika belum ada data yang di undo
    obj_undoredo.write('Pada Suatu Hari hiduplah seorang kakek-kakek')
    obj_undoredo.write("Dia tinggal sebatang kara di pegunungan")
    obj_undoredo.write("Dia kemudian turun gunung buat kuliah")
    obj_undoredo.write("SEMESTER 5 BANYAK TUGASSSSSSS !!!")
    obj_undoredo.printInfo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.undo()
    obj_undoredo.redo()
    obj_undoredo.redo()
    obj_undoredo.redo()