podrimos definir a los `Embeddings` como la representación vectorial de los datos con los cuales trabajan los LLM

uno de los conceptos que se suelen utilizar mucho es:
## Similitud por coseno:
### 🔹¿Cómo funciona la similitud por coseno?

Dado dos vectores **A** y **B**, la similitud por coseno se define como:

$$
{Similitud}(A, B) = \frac{A \cdot B}{\|A\| \|B\|}
$$
Donde:

- $A⋅B$ es el **producto punto** de los vectores.
- $∥A∥\|B\|$ son las **normas** (o magnitudes) de los vectores.

El resultado es un valor entre **-1 y 1**, donde:

- **1** significa que los vectores son **idénticos** (máxima similitud).
- **0** significa que los vectores son **ortogonales** (no tienen relación).
- **-1** significa que los vectores son **opuestos** (mínima similitud).

#### 🔹 **Ejemplo en embeddings**

En NLP (procesamiento de lenguaje natural), los embeddings convierten palabras en vectores de alta dimensión. La similitud por coseno nos permite medir qué tan parecidas son dos palabras.

Por ejemplo, si usamos un modelo de embeddings como Word2Vec o BERT:

- **Similitud("gato", "perro") ≈ 0.8** → Son similares.
- **Similitud("gato", "computadora") ≈ 0.2** → Son poco similares.
- **Similitud("gato", "agua") ≈ 0.0** → No tienen relación.

#### 🔹 **¿Por qué usar similitud por coseno?**

A diferencia de la distancia euclidiana, la similitud por coseno **ignora la magnitud** de los vectores y solo se enfoca en la **dirección**, lo que es útil cuando los datos están en diferentes escalas.

- 🔹 **Aplicaciones**:
	- **Búsqueda de información** (documentos similares).
	- **Sistemas de recomendación**.
	- **Agrupamiento de datos (clustering)**.
	- **Reconocimiento facial (comparando embeddings de imágenes)**.

# ¿Cómo funcionan los embeddings?
## Introducción a One-Hot Encoding y TF-IDF en IA
Estas son técnicas utilizadas para el procesamiento de datos en inteligencia artificial $(AI)$, especialmente en los modelos de procesamiento de lenguaje natural ($NLP$) 
### One-Hot Encoding
Este método ayuda a clasificar el texto palabra por palabra para mapearlos, la longitud de la fila de la matriz se determina por la cantidad de palabras que hay en el texto, este método se usa en textos muy cortos.
Técnica usada para clasificar variables categóricas (palabras, etiquetas, categorías), esto consiste en convertir cada `palabra` en una vector binario, es decir en un vector que solo tiene `0` `inactivas` o `1` `activos` donde solo una posición esta activa en cada vector.
#### ¿Cómo funciona?

- Supongamos que tienes una lista de categorías: `["gato", "perro", "pájaro"]`.
    
- Aplicando One-Hot Encoding, cada categoría se convierte en un vector de longitud igual al número de categorías únicas:
    
    - `"gato"` → `[1, 0, 0]`
        
    - `"perro"` → `[0, 1, 0]`
        
    - `"pájaro"` → `[0, 0, 1]`
#### Ejemplo en NLP:

Si tienes una oración: `"El gato y el perro"`, y tu vocabulario es `["el", "gato", "y", "perro"]`, el One-Hot Encoding sería:

- `"el"` → `[1, 0, 0, 0]`
    
- `"gato"` → `[0, 1, 0, 0]`
    
- `"y"` → `[0, 0, 1, 0]`
    
- `"perro"` → `[0, 0, 0, 1]`
    

#### Ventajas:

- Simple y fácil de implementar.
    
- Útil cuando las categorías no tienen una relación ordinal (no hay un orden inherente).
    

#### Desventajas:

- Puede generar vectores muy dispersos (con muchos 0s) si el vocabulario es grande.
    
- No captura relaciones semánticas entre palabras (por ejemplo, "gato" y "perro" no están relacionadas en el espacio vectorial).

¡Claro! Vamos a explicar ambos conceptos, **One-Hot Encoding** y **TF-IDF**, que son técnicas comúnmente utilizadas en el procesamiento de datos para inteligencia artificial (IA), especialmente en el campo del procesamiento de lenguaje natural (NLP).

---

### **1. One-Hot Encoding:**

#### ¿Qué es?
El **One-Hot Encoding** es una técnica utilizada para representar variables categóricas (como palabras, etiquetas o categorías) en un formato numérico que los modelos de IA puedan entender. Consiste en convertir cada categoría en un vector binario (compuesto de 0s y 1s), donde solo una posición del vector es 1 (activa) y el resto son 0s (inactivas).

#### ¿Cómo funciona?
- Supongamos que tienes una lista de categorías: `["gato", "perro", "pájaro"]`.
- Aplicando One-Hot Encoding, cada categoría se convierte en un vector de longitud igual al número de categorías únicas:

  - `"gato"` → `[1, 0, 0]`
  - `"perro"` → `[0, 1, 0]`
  - `"pájaro"` → `[0, 0, 1]`

#### Ejemplo en NLP:
Si tienes una oración: `"El gato y el perro"`, y tu vocabulario es `["el", "gato", "y", "perro"]`, el One-Hot Encoding sería:

- `"el"` → `[1, 0, 0, 0]`
- `"gato"` → `[0, 1, 0, 0]`
- `"y"` → `[0, 0, 1, 0]`
- `"perro"` → `[0, 0, 0, 1]`

---

### **2. TF-IDF (Term Frequency-Inverse Document Frequency):**

#### ¿Qué es?
El **TF-IDF** es una técnica utilizada para cuantificar la importancia de una palabra en un documento dentro de un conjunto de documentos (corpus). Es especialmente útil en tareas de recuperación de información y minería de texto.

#### ¿Cómo funciona?
TF-IDF combina dos métricas:
 - **TF (Term Frequency)**: Mide la frecuencia de una palabra en un documento.
   $$
   {TF}(t, d) = \frac{\text{Número de veces que aparece la palabra } t \text{ en el documento } d}{\text{Número total de palabras en el documento } d}
$$
- **IDF (Inverse Document Frequency)**: Mide la importancia de una palabra en el corpus. Las palabras que aparecen en muchos documentos tienen un IDF bajo.
   $$
   {IDF}(t, D) = \log\left(\frac{\text{Número total de documentos en el corpus } D}{\text{Número de documentos que contienen la palabra } t}\right)
   $$
- **TF-IDF**: Es el producto de TF e IDF.
   $$
   \text{TF-IDF}(t, d, D) = \text{TF}(t, d) \cdot \text{IDF}(t, D)
   $$

#### Ejemplo:
Supongamos que tienes un corpus con dos documentos:
- Documento 1: `"El gato come pescado"`
- Documento 2: `"El perro come carne"`

Calculamos el TF-IDF para la palabra `"come"` en el Documento 1:
1. **TF**: La palabra `"come"` aparece 1 vez en el Documento 1, que tiene 4 palabras.
   $$
   \text{TF} = \frac{1}{4} = 0.25
   $$
2. **IDF**: La palabra `"come"` aparece en 2 documentos (Documento 1 y Documento 2) de un total de 2 documentos.
   $$
   \text{IDF} = \log\left(\frac{2}{2}\right) = \log(1) = 0
   $$
3. **TF-IDF**:
   $$
   \text{TF-IDF} = 0.25 \cdot 0 = 0
   $$

---
### **Comparación entre One-Hot Encoding y TF-IDF:**

| Característica        | One-Hot Encoding            | TF-IDF                                 |
| --------------------- | --------------------------- | -------------------------------------- |
| **Representación**    | Vectores binarios (0s y 1s) | Vectores numéricos (valores continuos) |
| **Uso común**         | Variables categóricas       | Importancia de palabras en documentos  |
| **Captura semántica** | No                          | No                                     |
| **Dispersión**        | Muy disperso (muchos 0s)    | Menos disperso                         |
| **Ejemplo de uso**    | Clasificación de categorías | Recuperación de información, NLP       |

### **Resumen:**

- **One-Hot Encoding**: Representa categorías como vectores binarios. Es simple pero no captura relaciones semánticas.
    
- **TF-IDF**: Cuantifica la importancia de una palabra en un documento relativo a un corpus. Es útil para tareas de NLP pero tampoco captura semántica.
## Representación Vectorial de Palabras


## Evaluación de Similitudes Semánticas: Métodos y Aplicaciones

# Creación de embeddings

## Creación y entrenamiento de modelos Word2Vec con Gensim
