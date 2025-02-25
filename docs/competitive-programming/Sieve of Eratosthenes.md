
## Segment Sieve of Eratosthenes

```java
import java.util.ArrayList;
import java.util.List;

public class SegmentSieve {
    // Método para encontrar los números primos en un rango [a, b]
    public static List<Integer> findPrimesInRange(int a, int b) {
        // Paso 1: Encuentra todos los primos <= √b usando la criba clásica
        int limit = (int) Math.sqrt(b);
        boolean[] isPrimeSmall = new boolean[limit + 1];
        List<Integer> primes = new ArrayList<>();
        
        // Inicializa todos los números como primos
        for (int i = 2; i <= limit; i++) {
            isPrimeSmall[i] = true;
        }
        
        // Criba clásica para marcar los números no primos
        for (int i = 2; i * i <= limit; i++) {
            if (isPrimeSmall[i]) {
                for (int j = i * i; j <= limit; j += i) {
                    isPrimeSmall[j] = false;
                }
            }
        }
        
        // Almacena los primos encontrados
        for (int i = 2; i <= limit; i++) {
            if (isPrimeSmall[i]) {
                primes.add(i);
            }
        }

        // Paso 2: Crea un array booleano para el rango [a, b]
        boolean[] isPrimeRange = new boolean[b - a + 1];
        for (int i = 0; i < isPrimeRange.length; i++) {
            isPrimeRange[i] = true;
        }

        // Paso 3: Marca los múltiplos de los primos en el rango [a, b]
        for (int prime : primes) {
            // Encuentra el primer múltiplo de 'prime' dentro del rango [a, b]
            int start = Math.max(prime * prime, (a + prime - 1) / prime * prime);

            for (int j = start; j <= b; j += prime) {
                isPrimeRange[j - a] = false;
            }
        }

        // Si a es 1, márquelo como no primo (1 no es primo)
        if (a == 1) {
            isPrimeRange[0] = false;
        }

        // Paso 4: Genera la lista de números primos en el rango
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < isPrimeRange.length; i++) {
            if (isPrimeRange[i]) {
                result.add(a + i);
            }
        }

        return result;
    }
}
```


```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```


```geojson
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "id": 1,
      "properties": {
        "ID": 0
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
              [-90,35],
              [-90,30],
              [-85,30],
              [-85,35],
              [-90,35]
          ]
        ]
      }
    }
  ]
}
```



**The Cauchy-Schwarz Inequality**
```math

\left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)

```


Para crear una tabla similar en Markdown (`.md`), puedes usar caracteres ASCII para representar el tablero y simular el árbol de decisión. Sin embargo, Markdown por sí solo no tiene herramientas avanzadas para generar diagramas, por lo que te recomendaría usar una combinación de código Markdown y herramientas como:

1. **Tablas Markdown** (para una estructura básica).
2. **Mermaid.js** (para diagramas y árboles de decisión).
3. **ASCII Art** (para representar tableros de ajedrez simples).

---

### **Ejemplo con Mermaid.js**

Si tu plataforma admite Mermaid.js (como GitHub o algunas plataformas de documentación), puedes escribir el árbol de la siguiente manera:


```mermaid
graph TD;
    A["Tablero vacío"] --> B1["Reina en 1,1"]
    A --> B2["Reina en 1,2"]
    A --> B3["Reina en 1,3"]
    A --> B4["Reina en 1,4"]

	B1 --> B11["Reina en 2,1 - ilegal"]
	B1 --> B12["Reina en 2,2 - ilegal"]
	B1 --> B13["Reina en 2,3 - valido"]

    B2 --> C1["Reina en 2,1 - ilegal"]
    B2 --> C2["Reina en 2,2 - ilegal"]
    B2 --> C3["Reina en 2,3 - ilegal"]
    B2 --> C4["Reina en 2,4 - válido"]

    style C1 stroke:#ff0000,color:#ffff;
    style C2 stroke:#ff0000,color:#ffff;
    style C3 stroke:#ff0000,color:#ffff;
    style C4 stroke:#00ff00;
    style B13 stroke:#00ff00;
    style B11 stroke:#ff0000,color:#ffff;
    style B12 stroke:#ff0000,color:#ffff;
````

````

---

### **Ejemplo con ASCII en Markdown**
Si prefieres algo más simple y directo en Markdown sin dependencias externas:

```markdown
Tablero inicial:
````

```
. . . .
. . . .
. . . .
. . . .
```

```markdown
Primera Reina colocada en (1,2):
```

```
. Q . .
. . . .
. . . .
. . . .
```

```markdown
Segundo paso del árbol:
```

```
. Q . .
. . Q .
. . . .
. . . .
```

_(Válido)_

---

Si necesitas un formato más detallado, dime qué herramienta prefieres usar (Markdown puro, Mermaid.js, etc.).
