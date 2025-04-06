### Detalles
- En esta ocasion realice un programa orientado a la implementacion de listas doblemente enlazadas, simulando un historial en donde podremos ingresar textos, guardarlos y navegar entre ellos con el enfoque antes mencionado, construyendo una interfaz basica y dinamica.

### Librerias
- tkinter es la librería estándar de interfaces gráficas en Python.
- ttk proporciona botones y otros widgets con mejor apariencia.
```python
import tkinter as tk 
from tkinter import ttk
```

### Clases principales
##### Clase DobleNodo: 
Define un nodo de la lista doblemente enlazada, cada nodo guarda:
- Un valor (el texto guardado)
- Un enlace al nodo anterior
- Un enlace al nodo siguiente.

##### Clase DoublyLinkedList
Es la estructura que almacena todos los estados del texto. 


### Metodos principales
##### Agregar :
- Este método agrega un nuevo nodo con el valor que le pasamos al final de la lista.
```python
def append(self, value):
        new_node = DobleNodo(value)
        if not self.inicio:
            self.inicio = self.final = new_node
            self.current = new_node
        else:
            self.final.next = new_node
            new_node.prev = self.final
            self.final = new_node
```

##### Elimiar:
- Este método busca un nodo con cierto valor y lo elimina.
```python
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
```

##### Avanzar
- Si existe un nodo actual (self.current) y tiene uno siguiente (self.current.next), simplemente movemos el puntero current hacia adelante.

```python
 def adelante(self):
        if self.current and self.current.next:
            self.current = self.current.next

```

##### Retroceder
- Si existe un nodo actual y tiene uno anterior (prev), entonces movemos el puntero current hacia atrás.

```python
 def atras(self):
        if self.current and self.current.prev:
            self.current = self.current.prev

```
### Interfaz Grafica
```python
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

```
### Bloque que ejecuta el programa
```python
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()

```

