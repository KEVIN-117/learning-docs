# Plan de Trabajo de Asignatura

## Datos Generales

**Facultad:** Ingeniería 

**Carrera:** Ingeniería de Sistemas  

**Asignatura:** Técnicas de Programación II  

**Sigla:** SIS-XXX  

**Docente:** [Nombre del Docente]  

**Auxiliar de Docencia:** Kevin [Tu Apellido]  

---

## Objetivos de la Asignatura

### Objetivo General
Desarrollar en los estudiantes la capacidad de programar en Java aplicando los principios de la Programación Orientada a Objetos (POO) para resolver problemas computacionales de manera estructurada y eficiente.

### Objetivos Específicos
- Comprender los fundamentos de la POO y su implementación en Java.  
- Aplicar conceptos de encapsulamiento, herencia, polimorfismo y abstracción.  
- Desarrollar aplicaciones modulares y reutilizables con buenas prácticas de codificación.  
- Implementar estructuras de datos utilizando POO.  
- Manejar excepciones y archivos en Java.  

---

## Contenido Mínimo

### Tema 1: Introducción a la Programación Orientada a Objetos en Java
- Conceptos básicos de POO.  
- Clases y objetos en Java.  
- Métodos y atributos.  

### Tema 2: Encapsulamiento y Modificadores de Acceso
- Modificadores `private`, `public`, `protected`.  
- Métodos `getter` y `setter`.  
- Principios de encapsulación.  

### Tema 3: Herencia y Polimorfismo
- Clases base y derivadas.  
- Sobrecarga y sobrescritura de métodos.  
- Uso de `super` y `this`.  

### Tema 4: Abstracción e Interfaces
- Clases abstractas y métodos abstractos.  
- Implementación de interfaces en Java.  
- Aplicaciones prácticas.  

### Tema 5: Manejo de Excepciones y Archivos
- Uso de `try-catch` y `throws`.  
- Jerarquía de excepciones en Java.  
- Lectura y escritura de archivos.  

---

## Propuesta de Prácticas

### Tema 1: Introducción a la POO en Java
- Práctica N° 1 - "Creación de Clases y Objetos"  
- Práctica N° 2 - "Implementación de Métodos y Atributos"  
- Práctica N° 3 - "Ejercicios de Instanciación y Uso de Objetos"  

### Tema 2: Encapsulamiento y Modificadores de Acceso
- Práctica N° 4 - "Implementación de Getters y Setters"  
- Práctica N° 5 - "Control de Acceso con Modificadores"  
- Práctica N° 6 - "Encapsulación en Modelos de Clases"  

### Tema 3: Herencia y Polimorfismo
- Práctica N° 7 - "Creación de una Jerarquía de Clases"  
- Práctica N° 8 - "Ejercicios de Sobrecarga y Sobrescritura"  
- Práctica N° 9 - "Uso de `super` y `this` en Clases"  

### Tema 4: Abstracción e Interfaces
- Práctica N° 10 - "Implementación de Clases Abstractas"  
- Práctica N° 11 - "Uso de Interfaces en Java"  
- Práctica N° 12 - "Aplicaciones Reales de Interfaces"  

### Tema 5: Manejo de Excepciones y Archivos
- Práctica N° 13 - "Manejo de Excepciones con `try-catch`"  
- Práctica N° 14 - "Creación de Logs de Errores en Archivos"  
- Práctica N° 15 - "Lectura y Escritura de Archivos en Java"  

---

## Herramientas Especializadas
- Lenguaje de Programación: Java.  
- Entornos de Desarrollo: IntelliJ IDEA, Eclipse, VS Code.  
- Librerías y Frameworks: Java Standard Library, JUnit para pruebas.  
- Plataformas de Práctica: LeetCode, Codeforces, HackerRank.  

---

## Metodología
Se aplicarán metodologías activas y participativas para el aprendizaje efectivo de la programación en Java.

- **Aprendizaje Basado en Problemas (ABP):** Desarrollo de proyectos y resolución de problemas prácticos.  
- **Aprendizaje Colaborativo:** Trabajo en equipo para mejorar la lógica de programación.  
- **Flipped Classroom:** Material de lectura y videos antes de cada sesión.  
- **Gamificación:** Retos de codificación y competencias internas.  
- **Evaluación Continua:** Tareas, proyectos individuales y exámenes prácticos.  

---

## Bibliografía
- Deitel, P., & Deitel, H. (2019). *Java: How to Program*. Pearson.  
- Horstmann, C. (2019). *Core Java Volume I – Fundamentals*. Pearson.  
- Bloch, J. (2018). *Effective Java*. Addison-Wesley.  
- Sierra, K., & Bates, B. (2017). *Head First Java*. O'Reilly Media.  

---

**Firma del postulante**  
Nombre y Apellido: Kevin [Tu Apellido]  

## Mejoras
---
Para preparar mejor a los estudiantes para la **programación funcional en Java** o su **siguiente paso en Java**, podríamos mejorar el plan de trabajo en los siguientes aspectos:

### **1. Introducir conceptos de programación funcional dentro del curso**

Aunque el enfoque es POO, podemos empezar a familiarizar a los estudiantes con elementos de **Java funcional** para que la transición sea más fluida.

- **Agregar un nuevo tema**:
    
    - **Tema: Introducción a la Programación Funcional en Java**
        - Explicación de lambdas y `Functional Interfaces`.
        - Uso de `Stream API` para manipulación de colecciones.
        - Introducción a `Optional` para manejo de valores nulos.
        - Explicación de `Method References`.
- **Nuevas prácticas**:
    
    - Implementación de funciones lambda en lugar de clases anónimas.
    - Uso de `Stream API` para filtrar y transformar datos.
    - Aplicación de `Optional` para reducir el uso de `null`.

---

### **2. Uso de patrones de diseño orientados a la extensibilidad**

Para que los estudiantes comprendan **cómo evolucionar el código POO hacia FP**, sería bueno introducir patrones como:

- **Factory Method** y **Builder** (para modularidad).
    
- **Strategy** y **Command** (para reducir código repetitivo).
    
- **Nuevas prácticas**:
    
    - Refactorizar código usando **patrones de diseño**.
    - Comparar diferentes enfoques entre **POO vs. FP** en Java.

---

### **3. Transición a paradigmas modernos con frameworks populares**

- **Agregar un tema sobre Spring Boot** (nivel introductorio)
    
    - Inversión de Control y Dependencia (`@Component`, `@Autowired`).
    - Uso de anotaciones (`@RestController`, `@Service`).
    - Trabajo con `Lombok` para evitar boilerplate code.
    - Integración con **Spring Data** y manejo de bases de datos.
- **Nuevas prácticas**:
    
    - Crear una API REST básica con Spring Boot.
    - Uso de `@FunctionalInterface` para definir interfaces funcionales.

---

### **4. Proyecto Final con enfoque en arquitectura moderna**

En lugar de solo evaluar pequeñas prácticas, un **proyecto final** en donde los estudiantes:

- Implementen una aplicación modular con POO y elementos funcionales.
- Usen `Stream API`, `Optional`, y `Lombok` para mejorar el código.
- Aplicar principios de **SOLID y Clean Code**.

---

Si te parece bien esta propuesta, puedo actualizar el plan de trabajo con estos cambios. 🚀