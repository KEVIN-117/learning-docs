La criptografía es la practica que se encarga de convertir texto legible en una notación criptográfica (difícil de leer) y viceversa

### Ofuscación
la ofuscación es el oscurecimiento de texto, es una técnica que se utiliza para hacer que la información sea mas difícil de leer. El objetivo principal es proteger el contenido contra análisis no autorizado, ingeniería inversa o robo de propiedad intelectual. Aunque no garantiza una seguridad absoluta, es una capa adicional de protección que complica los intentos de análisis o acceso no autorizado.
Algunas técnicas de ofuscación son:
### **Técnicas de Ofuscación Conocidas**

#### **1. Ofuscación de Código**

Estas técnicas se aplican al software para dificultar su análisis por parte de terceros:

- **Renombrado de Identificadores**: Cambiar nombres de variables, funciones y clases a valores irreconocibles, como `a`, `b`, o `xyz123`.
- **Inserción de Código Redundante**: Añadir instrucciones innecesarias para dificultar la lectura sin cambiar la funcionalidad, como bucles o declaraciones que no afectan el flujo del programa.
- **Control de Flujo Ofuscado**: Alterar la lógica del programa para que sea más difícil de seguir, utilizando estructuras condicionales y bucles complejos.
- **Desplazamiento de Código (Code Flattening)**: Reestructurar el flujo del programa para que todas las instrucciones parezcan lineales, ocultando la jerarquía de llamadas.
- **Polimorfismo y Metamorfismo**: Generar múltiples versiones funcionalmente equivalentes de un código para confundir los intentos de análisis.

#### **2. Ofuscación de Datos**

Se centra en proteger información sensible, especialmente en aplicaciones y bases de datos:

- **Cifrado Parcial de Datos**: Encriptar porciones de datos sensibles (como contraseñas o claves API), dejando el resto accesible.
    
- **Tokenización**: Sustituir datos sensibles por identificadores únicos o tokens que no revelan información sobre los datos originales.
    
- **Ofuscación de Logs**: Alterar los registros para proteger datos confidenciales sin afectar su uso para depuración.
    

---

#### **3. Ofuscación de Comunicaciones**

Se aplica para dificultar la interceptación o análisis del tráfico entre sistemas:

- **Ofuscación de Protocolo**: Modificar protocolos de comunicación para que no sigan estándares reconocibles, dificultando su identificación y análisis.
    
- **Cifrado de Tráfico**: Usar cifrado adicional en capas superiores para proteger la información.
    

---

#### **4. Ofuscación en Scripts y Lenguajes Interpretados**

En lenguajes como JavaScript o Python, donde el código fuente es fácilmente accesible:

- **Minificación**: Reducir el tamaño del código al eliminar espacios, comentarios y nombres descriptivos.
    
- **Empaquetado**: Combinar múltiples scripts en un único archivo para dificultar su separación.
    
- **Uso de Generadores y Códigos Dinámicos**: Crear partes del código en tiempo de ejecución.
    

---

#### **5. Ofuscación para Ingeniería Inversa**

Protege el software contra herramientas de depuración y descompilación:

- **Anti-Debugging**: Insertar mecanismos que detecten si el software está siendo depurado y actúen en consecuencia, como detener la ejecución o alterar su comportamiento.
    
- **Anti-Decompiling**: Usar técnicas que dificulten la conversión del código compilado a un formato legible, como empaquetado o cifrado binario.
    
- **Virtualización del Código**: Transformar el código original en instrucciones propias de una máquina virtual personalizada, dificultando su análisis.
    

---

#### **6. Ofuscación de Redes**

Aplicada en redes para ocultar patrones de comunicación:

- **Encapsulación de Paquetes**: Usar túneles VPN, SSH o técnicas similares para encapsular paquetes dentro de otros.
    
- **Padding (Relleno)**: Agregar datos adicionales a los paquetes para ocultar el tamaño real del mensaje.

### Ofuscación vs Esteganografía
la ofuscación ase referencia  mas a lo que viene a ser la criptografía ya que tiene un enfoque matemático la cual es utilizado para que la información sea menos legible, mientras que la esteganografía es la técnica que se utiliza para ocultar información, es decir utiliza archivos como contenedores (imágenes, audio, video, texto, etc.) que dentro de las cuales se encuentra la información que se quiere esconder

### Criptografía clásica
la criptografía clásica engloba a todas las técnicas de encriptación que se usaron hasta principios del siglo XX, estos algoritmos se caracterizaban por:
- Trabajaban con cifrados de `substitution` y `transposición`
- Son manuales 
- Su seguridad dependía de **mantener en secreto el algoritmo** o la clave.

#### **Tipos de Criptografía Clásica**

##### **1. Cifrado por Sustitución**

Consiste en reemplazar cada símbolo del texto original (texto plano) por otro símbolo según un conjunto de reglas o una clave.

- **Cifrado Cesar**:
    
    - Cada letra del alfabeto se reemplaza por otra que está un número fijo de posiciones más adelante.
    - Ejemplo: Desplazamiento de 3 posiciones:  
        **Texto plano**: "HOLA"  
        **Texto cifrado**: "KRMD"
- **Cifrado Monoalfabético**:
    
    - Se utiliza un alfabeto de sustitución fijo para todo el mensaje.
    - Ejemplo: A -> M, B -> N, C -> O...
- **Cifrado Polialfabético**:
    
    - Se usan múltiples alfabetos de sustitución para evitar patrones repetidos.
    - Ejemplo famoso: **Cifrado de Vigenère**.

##### **2. Cifrado por Transposición**

Consiste en cambiar el orden de los caracteres del texto plano según una regla predefinida.

- **Cifrado de Columnas**:
    
    - Se escribe el mensaje en una cuadrícula y luego se lee en un orden específico.
    - Ejemplo:  
        **Texto plano**: "ATAQUEALAMANECER"  
        **Cifrado** (reordenando columnas): "AEAALRQTNUCAEMAK"
- **Escítala Espartana**:
    
    - Se usaba una vara cilíndrica donde el mensaje se escribía en espiral. Al desenrollarlo, el texto no tenía sentido sin una vara del mismo diámetro.

##### **3. Cifrado Basado en Reglas Matemáticas Simples**

Algunos métodos clásicos incluyen operaciones numéricas sencillas.

- **Cifrado de Affine**:
    
    - Combina sustitución con operaciones matemáticas (multiplicación y suma).  
        Fórmula: C=(a⋅P+b)mod  mC = (a \cdot P + b) \mod mC=(a⋅P+b)modm, donde:
        - PPP: Texto plano.
        - CCC: Texto cifrado.
        - a,ba, ba,b: Claves.
- **Cifrado de Hill**:
    
    - Usa álgebra lineal para codificar grupos de letras mediante matrices invertibles.

##### **4. Sistemas Mecánicos**

La criptografía clásica también evolucionó con dispositivos mecánicos.

- **Máquina Enigma**:
    
    - Usada por los alemanes en la Segunda Guerra Mundial.
    - Usaba rotores para crear cifrados polialfabéticos complejos.
- **Disco de Alberti**:
    
    - Inventado en el Renacimiento por Leon Battista Alberti.
    - Permitía cifrados polialfabéticos mediante discos concéntricos.


## Generador de números aleatorios
Son **algoritmos o dispositivos** que producen secuencias de números que parecen aleatorios. Estas podemos clasificarlos en 2 **`Verdaderamente aleatorios (TRNGs)`**, **`Pseudoaleatorios (PRNGs)`**

## Criptoanálisis y seguridad de cifrado

 