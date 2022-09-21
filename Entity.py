from turtle import pu


class Todolist() :

    def __init__(self, todo:str = "") -> None:
        self.__todo = todo
    
    def setTodo(self, todo:str) -> None :
        self.__todo = todo

    def getTodo(self) -> str :
        return self.__todo