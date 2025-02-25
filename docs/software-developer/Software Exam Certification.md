## Question I

## 1. Programa de Conferencias

Se ha publicado el programa de una próxima conferencia tecnológica. El programa incluye los horarios de inicio y finalización de cada presentación. Una vez que una presentación comienza, nadie puede entrar o salir de la sala. No se necesita tiempo para desplazarse de una presentación a otra. Determina el número máximo de presentaciones a las que puede asistir una persona.

---

### Ejemplo

**Entrada:**

- `n = 3`
- `scheduleStart = [1, 1, 2]`
- `scheduleEnd = [3, 2, 4]`

**Explicación:**  
Usando índices basados en 0, un asistente podría asistir a cualquier presentación de forma individual o a ambas presentaciones **1** y **2**. La presentación **0** termina demasiado tarde para poder asistir a la presentación **2** después. El número máximo de presentaciones que puede atender una persona es **2**.

---

### Descripción de la Función

Completa la función `maxPresentations` en el editor.

#### Parámetros:

- **`scheduleStart[n]`**: los horarios de inicio de la presentación `i`.
- **`scheduleEnd[n]`**: los horarios de finalización de la presentación `i`.

#### Retorna:

- **`int`**: el número máximo de presentaciones a las que puede asistir una persona.

---

### Restricciones

1. \( 1 \leq n \leq 10^5 \)
2. \( 1 \leq scheduleStart[i], scheduleEnd[i] \leq 10^9 \)

#### Descripción del problema

Se ha publicado un horario para una próxima conferencia tecnológica. El horario proporciona las horas de inicio y fin de cada una de las presentaciones. Una vez que ha comenzado una presentación, nadie puede entrar o salir de la sala. No toma tiempo desplazarse de una presentación a otra. El objetivo es determinar la cantidad máxima de presentaciones que una sola persona puede asistir.

---

#### Ejemplo

**Entrada:**

```plaintext
n = 3
scheduleStart = [1, 1, 2]
scheduleEnd = [3, 2, 4]
```

Con indexación basada en 0, un asistente podría asistir a cualquiera de las presentaciones por separado, o a las presentaciones 1 y 2. La presentación 0 termina demasiado tarde para que sea posible asistir a la presentación 2 después. El máximo número de presentaciones que una persona puede asistir es 2.

**Salida esperada:**

```plaintext
2
```

---

#### Descripción de la Función

Completa la función `maxPresentations` en el editor a continuación.

**Firma de la función:**

```python
def maxPresentations(scheduleStart: List[int], scheduleEnd: List[int]) -> int:
```

#### Parámetros:

- `scheduleStart` (Lista de enteros): los horarios de inicio de las presentaciones.
- `scheduleEnd` (Lista de enteros): los horarios de finalización de las presentaciones.

#### Retorno:

- `int`: el número máximo de presentaciones que una sola persona puede asistir.

---

#### Restricciones

- `1 ≤ n ≤ 10^5`
- `1 ≤ scheduleStart[i], scheduleEnd[i] ≤ 10^9`

---

#### Formato de Entrada para Pruebas Personalizadas

La entrada estándar se procesará de la siguiente manera y se pasará a la función:

1. La primera línea contiene un entero `n`, el número de presentaciones.
2. La segunda línea contiene una lista de enteros `scheduleStart`, donde cada entero es el horario de inicio de una presentación.
3. La tercera línea contiene una lista de enteros `scheduleEnd`, donde cada entero es el horario de finalización de una presentación.

**Ejemplo de entrada:**

```plaintext
3
1 1 2
3 2 4
```

---

#### Explicación

Para resolver el problema, podemos hacer lo siguiente:

1. Emparejar cada presentación con su hora de inicio y su hora de fin.
2. Ordenar las presentaciones según su hora de finalización.
3. Recorrer las presentaciones y elegir las que se puedan asistir sin superponerse con la anterior.

#### Pseudocódigo para la solución:

1. Crear una lista de tuplas donde cada tupla contiene el inicio y el fin de una presentación.
2. Ordenar la lista de tuplas por la hora de finalización.
3. Recorrer la lista de presentaciones y contar cuántas se pueden asistir sin solaparse.
---

#### Complejidad

- La complejidad de tiempo de esta solución es O(n log n), debido a la ordenación de las presentaciones. La parte de recorrer las presentaciones tiene una complejidad de O(n).
- La complejidad espacial es O(n), ya que almacenamos una lista de tuplas con la misma longitud que la entrada.

---

#### Casos de prueba

##### Caso 1: Caso base

**Entrada:**

```plaintext
3
1 1 2
3 2 4
```

**Salida esperada:**

```plaintext
2
```

##### Caso 2: Todas las presentaciones se solapan

**Entrada:**

```plaintext
3
1 2 3
2 3 4
3 4 5
```

**Salida esperada:**

```plaintext
1
```

##### Caso 3: Ninguna presentación se solapa

**Entrada:**

```plaintext
3
1 3 5
2 4 6
3 5 7
```

**Salida esperada:**

```plaintext
3
```

---

### Solution

```java
import java.io.*;

import java.math.*;

import java.security.*;

import java.text.*;

import java.util.*;

import java.util.concurrent.*;

import java.util.function.*;

import java.util.regex.*;

import java.util.stream.*;

import static java.util.stream.Collectors.joining;

import static java.util.stream.Collectors.toList;

  
  

class Result {

  

    /*

     * Complete the 'maxPresentations' function below.

     *

     * The function is expected to return an INTEGER.

     * The function accepts following parameters:

     *  1. INTEGER_ARRAY scheduleStart

     *  2. INTEGER_ARRAY scheduleEnd

     */

    static class Presentation{

        private Integer start;

        private Integer end;

        public Presentation(Integer start, Integer end){

            this.start = start;

            this.end = end;

        }

        int getStart(){

            return this.start;

        }

        int getEnd(){

            return this.end;

        }

    }

  

    public static int maxPresentations(List<Integer> scheduleStart, List<Integer> scheduleEnd) {

    // Write your code here

        int n = scheduleStart.size();

        List<Presentation> pairsList = new ArrayList<>();

        for (int i = 0; i < n; i++) {

            Integer start = scheduleStart.get(i);

            Integer end = scheduleEnd.get(i);

            Presentation presentation = new Presentation(start, end);

            pairsList.add(presentation);                              

        }

        pairsList.sort((p1, p2) -> Integer.compare(p1.getEnd(), p2.getEnd()));

        int counter = 0;

        int lastEnd = 0;

        for (Presentation presentation : pairsList) {

            if(presentation.getStart() >= lastEnd){

                counter++;

                lastEnd = presentation.getEnd();

            }

        }  

        return counter;  

    }

  

}

public class Solution {

    public static void main(String[] args) throws IOException {

        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

  

        int scheduleStartCount = Integer.parseInt(bufferedReader.readLine().trim());

  

        List<Integer> scheduleStart = IntStream.range(0, scheduleStartCount).mapToObj(i -> {

            try {

                return bufferedReader.readLine().replaceAll("\\s+$", "");

            } catch (IOException ex) {

                throw new RuntimeException(ex);

            }

        })

            .map(String::trim)

            .map(Integer::parseInt)

            .collect(toList());

  

        int scheduleEndCount = Integer.parseInt(bufferedReader.readLine().trim());

  

        List<Integer> scheduleEnd = IntStream.range(0, scheduleEndCount).mapToObj(i -> {

            try {

                return bufferedReader.readLine().replaceAll("\\s+$", "");

            } catch (IOException ex) {

                throw new RuntimeException(ex);

            }

        })

            .map(String::trim)

            .map(Integer::parseInt)

            .collect(toList());

  

        int result = Result.maxPresentations(scheduleStart, scheduleEnd);

  

        bufferedWriter.write(String.valueOf(result));

        bufferedWriter.newLine();

  

        bufferedReader.close();

        bufferedWriter.close();

    }

}
```

## Question II

### Problema: Pago Relativo

Una empresa mantiene una tabla llamada `EMPLOYEE` que contiene información sobre sus empleados. Escribe una consulta para generar una lista con dos columnas:

1. La primera columna debe incluir el nombre de un empleado que gane menos que otro empleado.
2. La segunda columna debe contener el nombre de un empleado que gane más.

Todas las combinaciones de empleados con salarios menores y mayores deben incluirse. Ordena los resultados de forma ascendente, primero por el `ID` del empleado que gana menos y luego por el salario del empleado que gana más.

---

#### Esquema de la Tabla

| Nombre    | Tipo    | Descripción                                   |
|-----------|---------|-----------------------------------------------|
| `ID`      | Integer | Identificador del empleado (clave primaria). |
| `NAME`    | String  | Nombre del empleado (1-20 caracteres).       |
| `AGE`     | Integer | Edad del empleado en años.                   |
| `ADDRESS` | String  | Dirección del empleado (1-25 caracteres).    |
| `SALARY`  | Integer | Salario del empleado.                        |

---

#### Datos de Ejemplo

##### Tabla: `EMPLOYEE`

| `ID` | `NAME`  | `AGE` | `ADDRESS` | `SALARY` |
|------|---------|-------|-----------|----------|
| 1    | Chris   | 27    | Paris     | 74635    |
| 2    | Sam     | 30    | Sydney    | 72167    |
| 3    | Pat     | 29    | Paris     | 75299    |

---

#### Salida Esperada

```plaintext
Chris Pat
Sam Chris
Sam Pat
```

---

#### Explicación

1. **Chris (ID: 1)** gana un salario de `74635`. Pat gana más, por lo que se incluye en la lista:
    
    - `Chris Pat`
2. **Sam (ID: 2)** gana un salario de `72167`. Tanto Chris como Pat ganan más, por lo que se incluyen las combinaciones:
    
    - `Sam Chris`
    - `Sam Pat`
3. **Pat (ID: 3)** gana el salario más alto (`75299`). No hay ningún empleado que gane más, por lo que no aparece en el resultado.
    

---


### Solution
```sql
/*

Enter your query here.

*/

  

SELECT

    E1.name AS "NAME (less salary)",

    E2.name AS "NAME (higher salary)"

FROM Employee E1

JOIN Employee E2

ON E1.salary < E2.salary

ORDER BY E1.ID, E2.SALARY;
```

## Question III

### Enunciado
### API REST: Rastreador de IP

Una API REST contiene información sobre direcciones IP. Dada una dirección IP, realiza una llamada `fetch` a la API REST para obtener su información y encontrar su país de origen.

Realiza una solicitud HTTP GET a:  
**`https://jsonmock.hackerrank.com/api/ip?ip=<ip>`**  
donde `<ip>` es la dirección IP que deseas consultar.

Por ejemplo, una solicitud GET a:  
**`https://jsonmock.hackerrank.com/api/ip?ip=172.217.20.46`**  
devolverá la información para la dirección IP `172.217.20.46`.

La respuesta es un objeto JSON con los siguientes 5 campos:

- **page**: la página actual de los resultados (1).
- **per_page**: el número máximo de resultados devueltos por página.
- **total**: el número total de resultados (1 o 0).
- **total_pages**: el número total de páginas con resultados (1).
- **data**: un array vacío o un array con un único objeto que contiene la información de la IP en el siguiente formato:
    - **ip**: dirección IP [STRING].
    - **country**: código de país asociado [STRING].

Ejemplo de un registro de IP:

```json
{
  "ip": "172.217.20.46",
  "country": "US"
}
```

### Nota importante:

- Obtendrás los datos desde la página 1, ya que cada dirección IP tiene un único registro (si existe).
- La página 1 es la predeterminada al realizar una llamada a la API.
- No se necesitan más llamadas a páginas adicionales.

### Objetivo:

Dada una dirección IP, el objetivo es obtener el código de país asociado con esa dirección IP.

### Instrucciones

##### Descripción de la Función

Completa la función `ipTracker` en el editor.

##### Parámetro

- **`ip`**: Dirección IP que se desea rastrear [CADENA].

##### Retornos

- Si no se encuentra un registro, retorna la cadena `'No Result Found'`.
- Si se encuentra un registro, retorna el código del país [CADENA].

#### Restricciones

1. Solo habrá una página por consulta.
2. La respuesta contendrá 0 o 1 registro.

---

### Formato de Entrada para Pruebas Personalizadas

En la primera y única línea de entrada, se proporciona una dirección IP.

---

### Ejemplo de Caso 0

#### Entrada

```
172.217.20.46
```

#### Salida

```
US
```

#### Explicación

La dirección IP fue consultada y se devolvió el país asociado.

---

### Ejemplo de Caso 1

#### Entrada

```
172.217.20.50
```

#### Salida

```
No Result Found
```

#### Explicación

Se consultó la dirección IP y no se devolvió ningún registro, es decir, `"total": 0`. Por lo tanto, la función retorna `'No Result Found'`.

### Solution
```js
'use strict';

  

const fs = require('fs');

const https = require('https');

  

process.stdin.resume();

process.stdin.setEncoding('utf-8');

  

let inputString = '';

let currentLine = 0;

  

process.stdin.on('data', function (inputStdin) {

    inputString += inputStdin;

});

  

process.stdin.on('end', function () {

    inputString = inputString.split('\n');

  

    main();

});

  

function readLine() {

    return inputString[currentLine++];

}

/*

 * Complete the 'ipTracker' function below.

 *

 * URL for cut and paste

 * https://jsonmock.hackerrank.com/api/ip?ip=<ip>

 *

 * The function is expected to return a STRING.

 * The function accepts a singe parameter ip.

 *

 * In case of no ip record, return string 'No Result Found'

 */

  
  

async function ipTracker(ip) {

    const res = new Promise((resolve, reject) => {

        https.get(`https://jsonmock.hackerrank.com/api/ip?ip=${ip}`, (res) => {

            let data = '';

            res.on('data', (chunk) => {

                data += chunk;

            })

  

            res.on('end', () => {

                resolve(JSON.parse(data))

            })

        }).on('error', (err)=>{

            reject(err)

        });

    });

    const {data} = await res;

    if(!data[0]){

        return 'No Result Found';

    }

    return data[0].country;

}

  

async function main() {

    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  

    const ip = readLine();

  

    const result = await ipTracker(ip);

  

    ws.write(result);

  

    ws.end();

}
```

