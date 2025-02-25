## Utils
### Formatter
```python
def formatter(data: str, label: str= 'cidsi') -> str:  
    return f'{label}{{{data}}}'
```
### md5 hasher
```python
import hashlib  
  
from ctf.utils.formatter import formatter  
  
  
def convert_to_md5(data: str) -> str:  
    md5_hash = hashlib.md5(data.encode())  
    formatted_string = formatter(md5_hash.hexdigest())  
    return formatted_string
```

### Bacon Cipher Decoder
```python
# Define the Bacon Cipher dictionary  
bacon_dict = {  
    'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',  
    'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'K',  
    'ABABA': 'L', 'ABABB': 'M', 'ABBAA': 'N', 'ABBAB': 'O', 'ABBBA': 'P',  
    'ABBBB': 'Q', 'BAAAA': 'R', 'BAAAB': 'S', 'BAABA': 'T', 'BAABB': 'U',  
    'BABAA': 'W', 'BABAB': 'X', 'BABBA': 'Y', 'BABBB': 'Z'  
}  
  
def decode_bacon_cipher(encoded_message):  
    # Split the encoded message into chunks of 5 characters  
    chunks = [encoded_message[i:i+5] for i in range(0, len(encoded_message), 5)]  
    # Decode each chunk using the Bacon Cipher dictionary  
    decoded_message = ''.join([bacon_dict.get(chunk, '?') for chunk in chunks])  
    return decoded_message
```
## PASE PERDIDO =’) POR LA TÓXICA XD
Enunciado
```
Pablito faltó a clases y quiere participar en la 4 Competencia de Seguridad Informática CIDSI, uno de sus docentes le dejo una pista, será que Pablito participa de la Competencia??? 494a55574b3354574d565847535a44504c354255535243544a465054454d425347493d3d3d3d3d3d
```

### Solución
```python
import base64  
  
from ctf.utils.convert_to_md5 import convert_to_md5  
  
data_input = '494a55574b3354574d565847535a44504c354255535243544a465054454d425347493d3d3d3d3d3d' # this is hex encoded  
decoded = bytes.fromhex(data_input).decode() # decode the hex, 'IJUWK3TWMVXGSZDPL5BUSRCTJFPTEMBSGI======' -> this is base32 encoded  
print(decoded)  
decoded = base64.b32decode(decoded).decode()  # decode the base32, 'Bienvenido_CIDSI_2022' -> this is flag  
print(decoded)  
print(convert_to_md5(decoded))  
# 28e043ef6109375dafe8d541f2896bed  
# 28e043ef6109375dafe8d541f2896bed
```

## Tocino
Enunciado
```
Puerco Araña nos dejo un mensaje en un idioma muy extraño. ¿Ayudaños a entendrlo por favor? AAABABAAAAABAAAABBBABAABAABBABAABBABAAAAAAAAAAABABABAAAAAAAAAAAABAAAAAAAABAABBABABBAA
```

el anunciado describe una cadena en este formato `AAABABAAAAABAAAABBBABAABAABBABAABBABAAAAAAAAAAABABABAAAAAAAAAAAABAAAAAAAABAABBABABBAA` y a esto se le conoce como código Bacon o (código Bacon), un sistema de cifrado ideado por Francis Bacon en el siglo XVI.

Este tipo de cifrado consiste en generar combinaciones de 5 letras usando una alfabeto binario que se representa solo por las letras `A`, `B`.  Por ejemplo
- **A = AAAAA**
- **B = AAAAB**
- **C = AAABA**
entonces la cadena quedaría como:
```
AAABA BAAAA ABAAA ABBBA BAABA ABBAB AABBA BAAAA AAAAA AABAB ABAAA AAAAA AAAAB AAAAA AAABA ABBAB ABBAA
```
entonces usamos https://cyberchef.org/, con el `Bacon Cipher Decode` obtenemos que  la cadena es igual a `CRIPTOGRAFIABACON`
usando python
```python
from ctf.utils.bacon_decoder import decode_bacon_cipher  
from ctf.utils.formatter import formatter  
  
data = 'AAABABAAAAABAAAABBBABAABAABBABAABBABAAAAAAAAAAABABABAAAAAAAAAAAABAAAAAAAABAABBABABBAA'  
decoded = decode_bacon_cipher(data)  
print(formatter(decoded))
```


# Bases
Este es un ejercicio muy bueno, parta solucionar el ejercicio me llevo a pensar mucho tiempo a pesar de ser muy fácil, la idea final del ejercicio proviene de un blog
[Challenge 13: bases | ctf-writeups](https://ahmedheltaher.github.io/ctf-writeups/sites/picoCTF/General-Skills/bases.html)

## Enunciado

Esto es de cajon si sabes de que hablo lo resolverás rápido siempre hay que aprender las bases del encriptado.
Así que comienza.

## La entrada es

```
9e^6t:./`?>'a@B>#\O@@7FdK<`j0;9l"Qb=]]]_=]e]q@W#_$9h0"X<*4)r@5(GW='&:?<btZ39egTB<`iig9en_!:KL^u9iZ:,:01RP>"D7S;__0B=&rILA5u689l<ET:KC>:@k]WW@VfRi@TGcX
```

## Solución
Entonces se me que es desencriptarlo con todas las base 85,64,62,58,,32

logrado en cyber chef
![[Pasted image 20241216051940.png]]
entonces la bandera es:
```
hay_que_aprender_las_bases
```


# Algo le pasa a mi cabeza

algo le pasa es mi cabeza es un ejercicio muy interesante ya que la cadena que se nos da la parecer son las instrucciones de un lenguaje de programación llamado `Brainfuck`

## **Breve introducción a Brainfuck**

1. **Comandos básicos**:
    
    - `>`: Mueve el puntero de memoria una celda a la derecha.
    - `<`: Mueve el puntero de memoria una celda a la izquierda.
    - `+`: Incrementa el valor en la celda actual.
    - `-`: Decrementa el valor en la celda actual.
    - `[` y `]`: Comienzo y final de un bucle (si el valor actual es 0, salta al final del bucle).
    - `.`: Imprime el carácter ASCII correspondiente al valor en la celda actual.
    - `,`: Lee un carácter de entrada y almacena su valor ASCII en la celda actual.
2. **Propósito**:  
    El lenguaje manipula directamente valores ASCII en celdas de memoria. Cada secuencia como la que muestras probablemente genera texto al decodificarse.
    

---

### **Cómo interpretar la cadena**

Tu cadena realiza una serie de operaciones en memoria para generar caracteres ASCII como salida. Cada grupo de comandos ajusta el valor en las celdas y los imprime.

---
## Interprete Brainfuck
```python
def brainfuck_interpreter(code):
    """Interprets Brainfuck code and returns the output."""
    memory = [0] * 30000  # Memory array
    pointer = 0  # Memory pointer
    output = []
    code_pointer = 0  # Code pointer
    loop_stack = []  # Stack to handle loops

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] = (memory[pointer] + 1) % 256
        elif command == '-':
            memory[pointer] = (memory[pointer] - 1) % 256
        elif command == '.':
            output.append(chr(memory[pointer]))
        elif command == ',':
            # Input is not handled in this example
            pass
        elif command == '[':
            if memory[pointer] == 0:
                # Jump to the command after the matching ']'
                open_brackets = 1
                while open_brackets > 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
            else:
                loop_stack.append(code_pointer)
        elif command == ']':
            if memory[pointer] != 0:
                code_pointer = loop_stack[-1]
            else:
                loop_stack.pop()

        code_pointer += 1

    return ''.join(output)

# Brainfuck program provided
brainfuck_code = ">+++++++++++[<+++++++++++>-]<-----.+.>+++++[<----->-]<+++.>++++[<++++>-]<--.--------.>+++[<+++>-]<.++++++.>++++[<---->-]<+.------.++++++.>++++[<++++>-]<--.+.>++++[<---->-]<---.--.>+++[<+++>-]<++.+++++.>+++[<--->-]<--.+++++.-----.---.>++++++++[<-------->-]<-."
decoded_output = brainfuck_interpreter(brainfuck_code)
print(decoded_output)
```

la bandera es `tu_mente_esta_jodida`

# Ok?
un ejercicio muy interesante hablando de leguajes de programación raras

La cadena que proporcionaste, "Ook. Ook? Ook. ..." es una referencia directa a **"The Secret of the Ook"**, una frase famosa utilizada en la obra de **"Brainfuck"**.

La clave está en que **"Ook"** es un término recurrente en una parodia del lenguaje de programación Brainfuck, utilizada para hacer referencia a una versión simplificada de este lenguaje llamada **"Ook!"**.

## Compilador
[Ook! Programming Language - Esoteric Code Decoder, Online Translator](https://www.dcode.fr/ook-language)

la bandera es `lenguaje_de_monos`