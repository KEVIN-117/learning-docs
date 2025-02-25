## **1. `StyleSheet` de React Native**

### **Ventajas**

1. **Optimización de rendimiento:** `StyleSheet.create` optimiza las definiciones de estilos.
2. **Simplicidad y familiaridad:** Es similar a escribir hojas de estilo CSS.
3. **Compatibilidad:** Se integra perfectamente con el ecosistema de React Native, sin necesidad de bibliotecas adicionales.
4. **Estructura clara y modularidad:** Permite definir estilos en un solo lugar, favoreciendo la reutilización y la organización del código.
5. **Sin dependencia externa:** Al ser parte de React Native, no requiere instalar ni mantener librerías adicionales.

---

### **Desventajas**

1. **Menos flexibilidad:** No permite estilos dinámicos o condicionales directamente. Para lograr esto, es necesario usar expresiones JavaScript dentro de los componentes.
2. **Sin soporte para CSS extendido:** Carece de características avanzadas de CSS como mixins, herencia, anidación de reglas o interpolación.
3. **Legibilidad reducida en estilos complejos:** En casos de componentes con múltiples variaciones estilísticas, el uso de `StyleSheet` puede volverse difícil de manejar.

## **Ejemplo `StyleSheet` de React Native**

```javascript
import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';

const App = () => {
  const isActive = true;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Hola, React Native!</Text>
      
      {/* Estilo condicional aplicado con lógica */}
      <TouchableOpacity 
        style={[styles.button, isActive && styles.activeButton]}
      >
        <Text style={styles.buttonText}>Presiona aquí</Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#f5f5f5',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 20,
  },
  button: {
    padding: 15,
    backgroundColor: '#007BFF',
    borderRadius: 5,
  },
  activeButton: {
    backgroundColor: '#28A745', // Cambia el color cuando el botón está activo
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
});

export default App;
```

---

## **2. `styled-components`**

### **Ventajas**

1. **Estilos dinámicos:** Permite crear estilos condicionales y dinámicos basados en las propiedades de los componentes (`props`), lo que lo hace ideal para interfaces interactivas y altamente personalizables.
2. **Legibilidad mejorada:** Los estilos se escriben directamente en el componente, lo que proporciona una mejor asociación entre el componente y su estilo.
3. **Soporte para CSS extendido:** Soporta características avanzadas como anidación, interpolación y mixins, brindando mayor flexibilidad.
4. **Temas globales:** Facilita la creación de temas globales utilizando un proveedor (`ThemeProvider`), lo que simplifica la aplicación de estilos consistentes.
5. **Eliminación automática de estilos no utilizados:** Los estilos específicos de un componente se eliminan cuando el componente no se utiliza, evitando la acumulación de estilos innecesarios.

---

### **Desventajas**

1. **Impacto en el rendimiento:** Puede agregar una ligera sobrecarga en tiempo de ejecución debido a la generación dinámica de estilos y clases.
2. **Dependencia de una biblioteca externa:** Al ser una biblioteca de terceros, existe el riesgo de posibles problemas de compatibilidad con futuras versiones de React Native.
4. **Estilos acoplados al componente:** Aunque mejora la legibilidad, puede dificultar la reutilización de estilos entre múltiples componentes si no se organiza adecuadamente.
5. **Tamaño del bundle:** Añade peso adicional al bundle de la aplicación debido a la inclusión de la biblioteca.

---

### **Conclusión** sobre cuando usarlos

- **Usa `StyleSheet`** cuando:
    - Quieres optimizar el rendimiento.
    - Estás trabajando en una aplicación sencilla o con un equipo que prefiere la simplicidad.
    - Quieres evitar dependencias externas.

- **Usa `styled-components`** cuando:
    - Necesitas estilos dinámicos, personalización avanzada o trabajar con temas.
    - Buscas mantener los estilos estrechamente vinculados a los componentes.
    - Prefieres una sintaxis similar a CSS con características avanzadas.
## **Ejemplo: `styled-components`**

```javascript
import React from 'react';
import styled from 'styled-components/native';

const App = () => {
  const isActive = true;

  return (
    <Container>
      <Title>Hola, Styled-Components!</Title>
      
      {/* Estilos dinámicos basados en props */}
      <Button active={isActive}>
        <ButtonText>Presiona aquí</ButtonText>
      </Button>
    </Container>
  );
};

// Componentes estilizados usando styled-components
const Container = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
`;

const Title = styled.Text`
  font-size: 24px;
  font-weight: bold;
  color: #333;
  margin-bottom: 20px;
`;

const Button = styled.TouchableOpacity`
  padding: 15px;
  border-radius: 5px;
  background-color: ${(props) => (props.active ? '#28A745' : '#007BFF')};
`;

const ButtonText = styled.Text`
  color: #fff;
  font-size: 16px;
`;

export default App;
```


---

# Plantilla de desarrollo de tickets

---
### **Plantilla de Ticket**

#### **Título del Ticket**

[Breve descripción de la tarea o funcionalidad requerida]

---

#### **Descripción**

[Explique en pocas palabras el propósito del ticket, indicando el objetivo principal del desarrollo. Ejemplo: "Implementar el registro de usuarios para permitir a los turistas crear cuentas y acceder a funcionalidades personalizadas."]

---

#### **Tareas**

- [Lista de pasos o actividades necesarias para completar el ticket. Por ejemplo:]
    1. Crear el modelo y configurar los campos en Strapi.
    2. Configurar validaciones en los datos de entrada.
    3. Implementar el endpoint correspondiente.
    4. Probar y documentar la funcionalidad.

---

#### **Colección para Crear**

- **Título de la Colección:** [Nombre de la colección en Strapi, como `Usuarios`]
- **Descripción:** [Breve explicación de la colección. Ejemplo: "Modelo que almacena información de los usuarios registrados."]
- **Campos y Tipos de Datos:**
    - `email`: String (unique, requerido).
    - `password`: String (hashed, requerido).
    - `firstName`: String (requerido).
    - `lastName`: String (requerido).
    - `phoneNumber`: String (opcional).
    - `isVerified`: Boolean (por defecto `false`, indica si el email fue verificado).

---

#### **Detalles del Endpoint**

**Endpoint:**

```
POST /auth/register  
Content-Type: application/json  
```

**Request:**

```json
{
  "email": "string",
  "password": "string",
  "firstName": "string",
  "lastName": "string",
  "phoneNumber": "string" // Opcional
}
```

**Response (200 OK):**

```json
{
  "userId": "string",
  "token": "string",
  "message": "Usuario registrado exitosamente"
}
```

**Errores Comunes:**

- **409 Conflict:** Email ya registrado.
    
    ```json
    {
      "message": "El email ya está registrado."
    }
    ```
    
- **400 Bad Request:** Datos faltantes o inválidos.
    
    ```json
    {
      "message": "El campo 'password' no cumple con los requisitos mínimos de seguridad."
    }
    ```
    

---

#### **Notas Adicionales**

[Opcional: Añade cualquier detalle relevante, como restricciones, dependencias, o configuraciones de plugins necesarios.]

---
