from typing import Any


class Cell:
    def __init__(self, content: Any, next_cell : None):
        self.content = content 
        self.next = next_cell



class LinkedList :
    def __init__(self, first_cell : Cell | None):
        self.first = first_cell

    def is_empty(self) -> bool:
        return self.first is None
    
    def length(self) -> int:
        if self.is_empty():
            return 0
        count = 1
        current = self.first 
        while current.next is not None:
            current = current.next
            count += 1
        return count

    def add_elem_beginning(self, elt : Any) -> None :
        new_cell = Cell(elt, self.first)
        self.first = new_cell

    def add_elem_end(self, elt: Any) -> None:

        if self.is_empty():
            self.add_elem_beginning(elt)
        else:
            current = self.first 
            while current.next is not None:
                current = current.next
            new_cell = Cell(elt, None)
            current.next = new_cell
        
    def __str__(self) -> str:
        if self.is_empty():
            return "y'a r"
        element = f"{self.first.content}"
        current = self.first
        while current.next is not None:
            current = current.next
            element += str(current.content)
        return element
    
    def __getitem__(self, index : int) -> Any:
        current = self.first
        for _ in range(index):
            current = current.next
            if current is None:
                raise IndexError("Bad try")
        return current.content
    
    def remove_ele_beg(self)-> None:
        assert not self.is_empty(), "Coup dur, la liste est vide"
        self.first = self.first.next

    def remove_ele_end(self) -> None:
        assert not self.is_empty(), "Coup dur, la liste est vide"
        if self.first.next is None:
            self.first = None
        current = self.first
        while current.next.next is not None:
            current = current.next
        current.next = None

class Stack:  #Pile
    """
    Piles
    """
    
    def __init__(self) -> None:
        self.data = LinkedList(None)

    def is_empty(self) -> bool:
        """
        Détermine si la pile est vide.
        """
        return self.data.is_empty()

    def put(self, elt: Any) -> None:
        """
        Ajoute un element au sommet de la pile.
        """
        self.data.add_elem_beginning(elt)

    def get(self) -> Any:
        """
        Retire l'element du sommet de la pile, et le renvoie.
        """
        assert not self.is_empty(), "oh no, the list is vide"
        removed_elem = self.data.first.content
        self.data.remove_ele_beg()
        return removed_elem