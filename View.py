from Service import TodolistServiceImpl

class TodolistView() :

    def __init__(self, service:TodolistServiceImpl) -> None:
        self.__service = service

    def showTodolist(self) :
        while True :
            self.__service.showTodolist()
            print("MENU")
            print("1. Tambah Todo")
            print("2. Hapus Todo")
            print("x. keluar")

            menu = input("Pilih Menu: ").lower()

            if menu == "1" :
                self.viewAddTodolist()
            elif menu == "2" :
                self.viewRemoveTodolist()
            elif menu == "x" :
                break
            else :
                print("MENU TIDAK ADA")
        
        print("PROGRAM SELESAI")
    
    def viewAddTodolist(self) :
        todo = input("Tambah Todo (x untuk batal): ")
        if todo.lower() == "x" :
            print("BATAL MENAMBAH TODO")
        else :
            self.__service.addTodolist(todo)

    def viewRemoveTodolist(self) :
        number = input("Nomor (x untuk batal): ")
        if number.lower() == "x" :
            print("BATAL MENGHAPUS TODO")
        else :
            self.__service.removeTodolist(int(number))