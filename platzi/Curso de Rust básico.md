
## Creación de proyecto
```bash
cargo new <nombre de proyecto>
```

## Variables de Rust y cómo mostrarlas en pantalla

en rust como todo lenguaje contamos con variables y sus tipos de datos, pero hay ciertos aspectos que hacen que rust sea único.
### Tipado de variables
Rust es de tipado `estatico` lo que significa que el tipo de dato de cada variable se determina en tiempo de compilación, ahora conoceremos los tipos de datos que tiene este lenguaje:
#### Entero (int)
una de la caracteristicas con los tipos numéricos es que rust tiene dos tipos de datos y estas pueden almacenar tipos numéricos con o sin `signo` `signed`, `unsigned`

- `signed`: Se caracterizan por guardar números con signo, suponiendo que tenemos el tipo `i8` lo cual equivale a `8-bit`, lo que indica es que lo reparte entre 50%, la mitad de esos números son para números negativos y la otra mitad para nueros positivos
- `unsigned`: Estos tipos de datos se caracterizan por guardar doble de números positivos

| Signed | Min                       | Max                      | Length  | Unsigned | Min | Max                                     |
| ------ | ------------------------- | ------------------------ | ------- | -------- | --- | --------------------------------------- |
| i8     | -128                      | 127                      | 8-bit   | u8       | 0   | 255                                     |
| i16    | -32768                    | 32767                    | 16-bit  | u16      | 0   | 65535                                   |
| i32    | 2147483648                | 2147483647               | 32-bit  | u32      | 0   | 4294967295                              |
| i64    | -92233720368547…          | 92233720368547…          | 64-bit  | u64      | 0   | 18446744073909551615                    |
| i128   | -17014118346046923173168… | 17014118346046923173168… | 128-bit | u128     | 0   | 340282366920938463463374607431768211455 |
|        |                           |                          |         |          |     |                                         |
#i16 #u16
### Declaración de variables numéricas en Rust
```rust
fn main() { 
	let a: i16 = 100; 
	let b: u16 = 200; 
	println!("El número es {} y {}", a, b); // El número es 100 y 200 
}
```
Algo muy importante a tomar en cuenta es que las variables en rust por defecto son `inmutables`, entonces para poder trabajar con variables mutables es utilizar la palabra reservada `mut` después del `let`. De lo contrario el código no compilara
```rust
fn main() { 
	let mut a: i16 = 100; 
	let mut b: u16 = 200; 
	println!("El número es {} y {}", a, b); // El número es 100 y 200 
}
```

#str
## Variables de tipo `String`
Para el guardado de variables del tipo cadenas de texto, el tipado se realiza con la palabra reservada `&str`.
```rust
fn main() { 
	let name: &str = "Kevin"; 
	println!("Mi nombre es {}", name); // Mi nombre es Kevin 
}
```

#f32 #f64
## Variables de tipo punto flotante
```rust
fn main() {
    let a: f32 = 3.14; // Punto flotante de 32 bits
    let b: f64 = 2.718; // Punto flotante de 64 bits
    println!("a: {}, b: {}", a, b);
}
```

#bool
## Variables booleanos
```rust
fn main() {
    let is_active: bool = true;
    println!("Is active: {}", is_active);
}
```

#char
## Variables de tipo `characters`
```rust
fn main() {
    let letter: char = 'A';
    println!("Letter: {}", letter);
}
```

---

## Algunos tipos de datos extra de `rust`

### Tuplas
```rust
fn main() {
    let tuple: (i32, f64, char) = (42, 6.28, 'x');
    println!("Tuple: ({}, {}, {})", tuple.0, tuple.1, tuple.2);
}
```

### Arrays
```rust
fn main() {
    let array: [i32; 3] = [1, 2, 3];
    println!("Array: {:?}", array);
}
```

### Vectores
```rust
fn main() {
    let mut vec: Vec<i32> = Vec::new();
    vec.push(10);
    vec.push(20);
    vec.push(30);
    println!("Vector: {:?}", vec);
}
```

### Estructuras
```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let point = Point { x: 5, y: 10 };
    println!("Point: ({}, {})", point.x, point.y);
}
```

### Enumeraciones
```rust
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

fn main() {
    let dir: Direction = Direction::Up;
    match dir {
        Direction::Up => println!("Going up!"),
        Direction::Down => println!("Going down!"),
        Direction::Left => println!("Going left!"),
        Direction::Right => println!("Going right!"),
    }
}
```

### Opciones
```rust
fn main() {
    let some_number: Option<i32> = Some(5);
    let no_number: Option<i32> = None;
    
    match some_number {
        Some(n) => println!("Number: {}", n),
        None => println!("No number"),
    }
}
```

### Resultados
```rust
fn divide(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err(String::from("Cannot divide by zero"))
    } else {
        Ok(a / b)
    }
}

fn main() {
    match divide(10.0, 2.0) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("Error: {}", e),
    }
}
```

## Recibiendo datos del usuario

Poder interactuar con nuestras aplicaciones es una caracteristicas fundamental de todos los lenguajes de programación y `Rust` no es la excepción 
### Input en `Rust`
```rust
use std::io::stdin;  
  
fn main() {  
    let mut input = String::new();  
	let mut age = String::new();
	
	println!("Enter your name: ");  
	stdin().read_line(&mut input).unwrap();  
	println!("Enter your age: ");  
	stdin().read_line(&mut age).unwrap();
	
	let name = input.trim();  
	let age: u8 = age.trim().parse().unwrap(); // casting de datos
	println!("Hello, {}", name);  
	println!("You are {} years old", age);
}
```


## Condicionales
#### `if`, `else if`, `else`
En Rust, las estructuras de control `if`, `else if` y `else` funcionan de manera similar a otros lenguajes de programación:

```rust
fn main() {
    let number = 7;

    if number < 5 {
        println!("El número es menor que 5");
    } else if number == 5 {
        println!("El número es igual a 5");
    } else {
        println!("El número es mayor que 5");
    }
}
```

### Operadores Lógicos

- `&&` (AND lógico)
- `||` (OR lógico)
- `!` (NOT lógico)

### Ejemplos de Operadores Lógicos

#### AND Lógico
```rust
fn main() {
    let a = true;
    let b = false;
    
    if a && b {
        println!("Ambos son verdaderos");
    } else {
        println!("Al menos uno es falso");
    }
}
```

#### OR Lógico
```rust
fn main() {
    let a = true;
    let b = false;
    
    if a || b {
        println!("Al menos uno es verdadero");
    } else {
        println!("Ambos son falsos");
    }
}
```

#### NOT Lógico
```rust
fn main() {
    let a = true;
    
    if !a {
        println!("a es falso");
    } else {
        println!("a es verdadero");
    }
}
```

### Uso de `match`
Aunque no es una estructura `if`, el operador `match` es una poderosa herramienta de control de flujo en Rust, especialmente útil para manejar múltiples condiciones:

```rust
fn main() {
    let number = 6;

    match number {
        1 => println!("El número es uno"),
        2 | 3 | 5 | 7 | 11 => println!("El número es un número primo"),
        13..=19 => println!("El número está entre 13 y 19"),
        _ => println!("El número no tiene ninguna característica especial"),
    }
}
```

## Bucles
### 1. Bucle `loop`
Este es un bucle infinito que se ejecuta indefinidamente a menos que se use la declaración `break` para salir del bucle.

```rust
fn main() {
    let mut count = 0;

    loop {
        count += 1;
        println!("Count: {}", count);

        if count == 10 {
            break; // Sale del bucle cuando count es igual a 10
        }
    }
}
```

### 2. Bucle `while`
El bucle `while` ejecuta el bloque de código siempre que la condición sea verdadera.

```rust
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{}!", number);
        number -= 1;
    }

    println!("¡Despegue!");
}
```

### 3. Bucle `for`
El bucle `for` itera sobre una colección de elementos. Es muy común usarlo con rangos.

```rust
fn main() {
    for number in 1..5 {
        println!("Número: {}", number);
    }

    // O usando un array
    let array = [10, 20, 30, 40];
    for element in array.iter() {
        println!("Elemento: {}", element);
    }
}
```

### Uso de `continue` y `break`
En cualquier tipo de bucle, puedes usar `continue` para saltar a la siguiente iteración y `break` para salir del bucle.

```rust
fn main() {
    for number in 1..10 {
        if number % 2 == 0 {
            continue; // Salta los números pares
        }
        if number == 7 {
            break; // Sale del bucle cuando el número es 7
        }
        println!("Número impar: {}", number);
    }
}
```

### Ejemplo Combinado

```rust
fn main() {
    let array = [1, 2, 3, 4, 5];

    // Bucle `for`
    for element in array.iter() {
        println!("Elemento: {}", element);
    }

    // Bucle `while`
    let mut index = 0;
    while index < array.len() {
        println!("Índice: {}, Valor: {}", index, array[index]);
        index += 1;
    }

    // Bucle `loop`
    let mut count = 0;
    loop {
        if count == array.len() {
            break;
        }
        println!("Loop: {}", array[count]);
        count += 1;
    }
}
```
