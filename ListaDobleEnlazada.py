import tkinter as tk #interfaz
from tkinter import ttk

class DobleNodo:
    def __init__(self, value):
        self.value = value #Guardar
        self.prev = None #Anterior
        self.next = None #Siguiente

class DoublyLinkedList:
    def __init__(self):
        self.inicio = None
        self.final = None
        self.current = None #actu

    def append(self, value):
        new_node = DobleNodo(value)
        if not self.inicio:
            self.inicio = self.final = new_node
            self.current = new_node
        else:
            self.final.next = new_node
            new_node.prev = self.final
            self.final = new_node

    def delete(self, value):
        node = self.inicio
        while node:
            if node.value == value:
                if node.prev:
                    node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                if node == self.inicio:
                    self.inicio = node.next
                if node == self.final:
                    self.final = node.prev
                return True
            node = node.next
        return False

    def adelante(self):
        if self.current and self.current.next:
            self.current = self.current.next

    def atras(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

    def  valoractual(self):
        return self.current.value if self.current else None

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulacion de historial")
        
        self.doubly_linked_list = DoublyLinkedList()
        
        self.text_area = tk.Text(self.root, wrap="word", width=35, height=10)
        self.text_area.pack(padx=10, pady=10)
        
        self.button_save = ttk.Button(self.root, text="Guardar texto", command=self.save_state)
        self.button_save.pack(side="left", padx=10)
        
        self.button_undo = ttk.Button(self.root, text="Atras", command=self.undo)
        self.button_undo.pack(side="left", padx=10)
        
        self.button_redo = ttk.Button(self.root, text="Adelante", command=self.redo)
        self.button_redo.pack(side="left", padx=10)
    
    def save_state(self):
        text = self.text_area.get("1.0", "end-1c")
        self.doubly_linked_list.append(text)
        print("Texto guardado:", text)

    def undo(self):
        if self.doubly_linked_list.current and self.doubly_linked_list.current.prev:
            self.doubly_linked_list.atras()
            self.text_area.delete("1.0", "end-1c")
            self.text_area.insert("1.0", self.doubly_linked_list.current.value)
            print("Texto anterior:", self.doubly_linked_list.current.value)
    
    def redo(self):
        if self.doubly_linked_list.current and self.doubly_linked_list.current.next:
            self.doubly_linked_list.adelante()
            self.text_area.delete("1.0", "end-1c")
            self.text_area.insert("1.0", self.doubly_linked_list.current.value)
            print("Ultimo texto:", self.doubly_linked_list.current.value)

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
