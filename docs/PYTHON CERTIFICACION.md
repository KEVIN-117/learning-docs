## 1. Python: Shopping Cart

## Task Description

The task is to implement two classes: `ShoppingCart` and `Item` according to the following requirements:

### `Item`
- An item is instantiated using the constructor `Item(name: str, price: int)` where the name denotes the name of the item, and the price denotes the price of the item.
- Its name can be retrieved as a normal attribute, that is, if `item` is an instance of `Item`, then `item.name` returns the name of the item.

### `ShoppingCart`
- A shopping cart is instantiated using a constructor without arguments, i.e. `ShoppingCart()`.
- It has a method `add(item: Item)` that adds the given item to the cart. An item may be added to the cart multiple times. An item will be added each time the `add` method is called.
- It has a method `total() -> int` that returns the sum of the prices of all items currently in the cart.
- Calling `len(cart)` where the cart is an instance of a `ShoppingCart` returns the number of items in the cart.

## Implementation Notes
Implementations of the classes will be tested by a provided code stub and several input files that contain parameters. First, the stub initializes instances of `Item`s and an instance of the `ShoppingCart`. Next, it performs the given operations on the `ShoppingCart` instance. The result of their executions will be printed to the standard output by the provided code.

### Constraints
- There will be at most 5 different items.
- There will be at most 500 operations to perform on the cart.

---

## Input Format (For Custom Testing)

Input from `stdin` will be processed as follows and passed to the function:

1. In the first line, there is an integer `n`, the number of items to be constructed.
2. Each of the following `n` lines contains 2 space-separated parameters to construct a single item: its `name` and its `price`.
3. In the next line, there is an integer `q`, the number of operations to be performed on a `ShoppingCart` instance.
4. Each of the following `q` lines denotes a single operation to be performed on the `ShoppingCart` along with its parameters, if any.

---

## Sample Case 0

### Sample Input 0
```
```
```python
STDIN                       Function
-----                       --------
2                           → n = 2 (number of item types)
bike 1000                   → name = 'bike', price = 1000
helmet 500                  → name = 'helmet', price = 500
3                           → q = 3 (number of operations)
add bike
add helmet
total
```
### Sample Output 0
1500

The shopping cart contains a bike and a helmet. The total is 1000 + 500 = 1500.
## Solution

```python
#!/bin/python3

import math

import os

import random

import re

import sys

  
  

class Item:

    # Implement the Item here

    def __init__(self, name: str, price: int):

        self.name = name

        self.price = price

  
  

class ShoppingCart:

    # Implement the ShoppingCart here

    def __init__(self):

        self.shoppingCart = []

    def add(self, item: Item):

        self.shoppingCart.append(item)

    def total(self)-> int:

        return sum([item.price for item in self.shoppingCart])

    def __len__(self):

        return len(self.shoppingCart)

  

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

  

    n = int(input())

    items = []

    for _ in range(n):

        name, price = input().split()

        item = Item(name, int(price))

        items.append(item)

  

    cart = ShoppingCart()

  

    q = int(input())

    for _ in range(q):

        line = input().split()

        command, params = line[0], line[1:]

        if command == "len":

            fptr.write(str(len(cart)) + "\n")

        elif command == "total":

            fptr.write(str(cart.total()) + "\n")

        elif command == "add":

            name = params[0]

            item = next(item for item in items if item.name == name)

            cart.add(item)

        else:

            raise ValueError("Unknown command %s" % command)

    fptr.close()
```

---

## 2. Python: String Transformation

### Descripción
Dada una oración formada por cadenas de letras mayúsculas y minúsculas separadas por espacios, transforma cada palabra de acuerdo con el siguiente algoritmo y devuelve la nueva oración.

---

### Reglas de Transformación

1. **El primer carácter de cada palabra permanece sin cambios.**
2. **Para cada carácter subsiguiente `x`, compara con el carácter anterior `y`:**
   - Si `y` precede a `x` en el alfabeto inglés, transforma `x` a **mayúscula**.
   - Si `x` precede a `y` en el alfabeto inglés, transforma `x` a **minúscula**.
   - Si `x` y `y` son iguales, el carácter permanece sin cambios.

---

### Ejemplo

#### Entrada
```plaintext
sentence = "coOL dog"
```

#### Proceso
- **Palabra 1:** `"coOL"`
  - El primer carácter `"c"` permanece sin cambios.
  - `"o"` se convierte a **mayúscula** porque `"c"` precede a `"o"`.
  - El segundo `"O"` permanece sin cambios porque el carácter anterior también es `"o"`.
  - `"L"` se convierte a **minúscula** porque `"O"` precede a `"L"`.
- **Palabra 2:** `"dog"`
  - Se transforma siguiendo las mismas reglas.

#### Salida
```plaintext
"cOOl dOg"
```

---

### Función

Completa la función `transformSentence` para realizar la transformación:

#### Parámetros
- `string sentence`: la oración de entrada.

#### Retorno
- Una cadena de texto con la oración transformada.

---

### Restricciones

- \(1 \leq \text{length of sentence} \leq 100\)
- La oración consiste únicamente en letras inglesas mayúsculas y minúsculas, y espacios.
- La oración empieza y termina con letras, sin espacios consecutivos.

---

### Formato de Entrada (para pruebas personalizadas)

- La primera línea contiene una sola cadena, `sentence`.

---

### Ejemplo

#### Entrada
```plaintext
a Blue MOON
```

#### Salida
```plaintext
a BLUe MOOn
```

#### Explicación
- `"Blue"`: 
  - `"l"` se convierte en **mayúscula** porque `"b"` precede a `"l"`.
  - `"u"` se convierte en **mayúscula** porque `"l"` precede a `"u"`.
  - `"e"` permanece en minúscula porque `"u"` precede a `"e"`.
- `"MOON"`:
  - El último carácter `"n"` se convierte en **minúscula** porque `"O"` precede a `"n"`.

---

### Implementación

```python
def transformSentence(sentence: str) -> str:
    # Tu implementación aquí
    pass
``` 

--- 
## Posible solution
```python
#!/bin/python3

  

import math

import os

import random

import re

import sys

# Complete the 'transformSentence' function below.
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.


def transformSentence(sentence):
    # Write your code here

    def transformator(x: str, y: str):

        if x == ' ':

            return x

        if y < x:

            return x.upper()

        elif y > x:

            return x.lower()

        else:

            return x

    result = [sentence[0]]

    for i in range(1, len(sentence)):

        x, y = sentence[i], sentence[i-1]

        final_word = transformator(x, y)

        result.append(final_word)

    print(result)

    return ''.join(result)

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

  

    sentence = input()

  

    result = transformSentence(sentence)

  

    fptr.write(result + '\n')

  

    fptr.close()
	```