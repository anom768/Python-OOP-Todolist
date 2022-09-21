from Repository import TodolistRepositoryImpl
from Service import TodolistServiceImpl
from View import TodolistView

if __name__ == "__main__" :
    print("APLIKASI TODOLIST")
    repository = TodolistRepositoryImpl()
    service = TodolistServiceImpl(repository)
    app = TodolistView(service)
    app.showTodolist()