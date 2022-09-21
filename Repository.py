from Entity import Todolist
from abc import ABC, abstractmethod

class TodolistRepository(ABC) :

    @abstractmethod
    def save(self) -> None :
        pass

    @abstractmethod
    def remove(self) -> bool :
        pass

    @abstractmethod
    def findAll(self) -> list :
        pass

class TodolistRepositoryImpl(TodolistRepository) :

    def __init__(self) -> None:
        super().__init__()
        self.todolist = []

    def save(self, todo:Todolist) -> None :
        self.todolist.append(todo.getTodo())
    
    def remove(self, number:int) -> bool :
        if number < 0 or number > len(self.todolist) :
            return False
        
        self.todolist.remove(self.todolist[number])
        return True
    
    def findAll(self) -> list:
        return self.todolist