#easy
## Builder ejercicios con dificultad fácil
### Ejercicio 1: Constructor de Pizza
**Objetivo:** Crear un *Builder* para construir una pizza con ingredientes personalizados.

**Descripción:**
Desarrolla una clase `PizzaBuilder` que permita construir una pizza seleccionando diferentes ingredientes y características:
- **Tamaño**: pequeño, mediano, grande.
- **Tipo de masa**: delgada, gruesa, rellena de queso.
- **Ingredientes**: queso, pepperoni, champiñones, pimientos, etc.

El *Builder* debe permitir elegir cada una de estas opciones de manera independiente y luego construir la pizza final.

**Ejemplo de uso:**
```java
Pizza pizza = new PizzaBuilder()
    .setSize("Large")
    .setCrust("Cheese-stuffed")
    .addTopping("Cheese")
    .addTopping("Pepperoni")
    .build();
```

### Ejercicio 2: Constructor de Computadora
**Objetivo:** Crear un *Builder* para armar una computadora con componentes personalizados.

**Descripción:**
Desarrolla una clase `ComputerBuilder` para armar computadoras. La clase debe permitirte seleccionar componentes como:
- **CPU**: Intel i5, i7, AMD Ryzen.
- **RAM**: 8GB, 16GB, 32GB.
- **Almacenamiento**: HDD de 1TB, SSD de 512GB, etc.
- **Tarjeta gráfica**: integrada, NVIDIA, AMD.

El *Builder* debe permitir construir la computadora con los componentes seleccionados, y debe manejar la verificación de que al menos CPU, RAM, y almacenamiento están definidos antes de construir.

**Ejemplo de uso:**
```java
Computer computer = new ComputerBuilder()
    .setCPU("Intel i7")
    .setRAM("16GB")
    .setStorage("512GB SSD")
    .setGraphicsCard("NVIDIA GTX 1660")
    .build();
```

---

### Ejercicio 3: Constructor de Vehículos
**Objetivo:** Implementar un *Builder* para construir un vehículo con configuraciones básicas.

**Descripción:**
Crea una clase `VehicleBuilder` que permita construir un vehículo con las siguientes características:
- **Tipo de vehículo**: coche, motocicleta, camioneta.
- **Color**: rojo, azul, negro, blanco.
- **Tipo de transmisión**: manual, automática.
- **Características adicionales**: como aire acondicionado, GPS, radio.

El *Builder* debería poder construir un vehículo con las características seleccionadas y, al final, mostrar un resumen de la configuración.

**Ejemplo de uso:**
```java
Vehicle car = new VehicleBuilder()
    .setType("Car")
    .setColor("Red")
    .setTransmission("Automatic")
    .addFeature("GPS")
    .addFeature("Air conditioning")
    .build();
```

---

### Ejercicio 4: Constructor de Perfil de Usuario
**Objetivo:** Crear un *Builder* para configurar un perfil de usuario en una red social.

**Descripción:**
Desarrolla una clase `UserProfileBuilder` que permita crear un perfil de usuario seleccionando detalles básicos como:
- **Nombre de usuario**: nombre visible del usuario.
- **Foto de perfil**: imagen de perfil.
- **Descripción**: breve biografía del usuario.
- **Intereses**: una lista de intereses o hobbies.

Este *Builder* debe permitir construir el perfil del usuario con la información opcionalmente configurada, lo cual es común en aplicaciones de redes sociales.

**Ejemplo de uso:**
```java
UserProfile profile = new UserProfileBuilder()
    .setUsername("JohnDoe")
    .setProfilePicture("profile.jpg")
    .setBio("Developer and tech enthusiast.")
    .addInterest("Programming")
    .addInterest("Gaming")
    .build();
```

---

### Ejercicio 5: Constructor de Habitación de Hotel
**Objetivo:** Crear un *Builder* para configurar una habitación de hotel con distintos servicios.

**Descripción:**
Crea una clase `HotelRoomBuilder` para construir una habitación de hotel. Los servicios configurables podrían ser:
- **Tipo de habitación**: estándar, suite, doble.
- **Vistas**: vista al mar, vista a la ciudad.
- **Servicios adicionales**: desayuno incluido, acceso al gimnasio, Wi-Fi, servicio de lavandería.

El *Builder* debe permitir al cliente seleccionar cada uno de estos servicios y luego construir la reserva de la habitación.

**Ejemplo de uso:**
```java
HotelRoom room = new HotelRoomBuilder()
    .setRoomType("Suite")
    .setView("Ocean")
    .addService("Breakfast included")
    .addService("Gym access")
    .build();
```

---

### Ejercicio 6: Constructor de Libro
**Objetivo:** Crear un *Builder* para construir objetos de tipo "Libro" en una aplicación de biblioteca.

**Descripción:**
Crea una clase `BookBuilder` que permita configurar un libro con información como:
- **Título**: el título del libro.
- **Autor**: nombre del autor.
- **Número de páginas**: cantidad de páginas del libro.
- **Género**: como ficción, no ficción, misterio, ciencia ficción, etc.
- **ISBN**: número de identificación único del libro.

El *Builder* debe permitir construir el libro con todos los detalles proporcionados.

**Ejemplo de uso:**
```java
Book book = new BookBuilder()
    .setTitle("1984")
    .setAuthor("George Orwell")
    .setPages(328)
    .setGenre("Dystopian Fiction")
    .setISBN("1234567890")
    .build();
```

---


#medium
## Ejercicios con dificultad media
### Ejercicio 1: Constructor de Viaje (Travel Itinerary Builder)
**Objetivo:** Crear un *Builder* para organizar un itinerario de viaje personalizado.

**Descripción:**
Desarrolla una clase `TravelItineraryBuilder` que permita construir un itinerario de viaje con los siguientes elementos configurables:
- **Destino**: ciudad o país de destino.
- **Fechas**: fecha de inicio y fecha de fin del viaje.
- **Alojamiento**: nombre del hotel y dirección.
- **Actividades diarias**: permite agregar actividades para cada día del viaje (pueden ser excursiones, visitas turísticas, etc.).
- **Transporte**: añade detalles sobre el transporte, como avión, tren o alquiler de coche.

El *Builder* debe permitir agregar múltiples actividades para cada día del viaje y tener la opción de validar las fechas para asegurar que la fecha de inicio sea anterior a la fecha de fin.

**Dificultad adicional:**
- Incluye métodos para ajustar el itinerario en base al presupuesto máximo.
- Verifica que todas las actividades se realicen en el rango de fechas especificado.

**Ejemplo de uso:**
```java
TravelItinerary itinerary = new TravelItineraryBuilder()
    .setDestination("Paris")
    .setStartDate("2024-05-10")
    .setEndDate("2024-05-20")
    .setAccommodation("Hotel Paris Central", "123 Rue de Paris")
    .addDailyActivity("2024-05-11", "Eiffel Tower visit")
    .addDailyActivity("2024-05-12", "Louvre Museum")
    .setTransport("Flight", "Paris Charles de Gaulle")
    .build();
```

---

### Ejercicio 2: Generador de Factura Compleja (Invoice Builder)
**Objetivo:** Crear un *Builder* para construir facturas con detalles específicos de productos y clientes.

**Descripción:**
Desarrolla una clase `InvoiceBuilder` para crear facturas que incluyan:
- **Información del cliente**: nombre, dirección, número de teléfono.
- **Productos**: permite agregar múltiples productos, cada uno con nombre, cantidad, precio unitario y un descuento opcional.
- **Impuestos y descuentos**: permite agregar impuestos globales y aplicar descuentos al total.
- **Detalles de pago**: método de pago, términos y fecha de vencimiento.

El *Builder* debe calcular automáticamente el total de la factura considerando los productos, descuentos y el impuesto global.

**Dificultad adicional:**
- Incluye un método para aplicar descuentos condicionales basados en la cantidad total de productos comprados.
- Permite agrupar productos similares y mostrar subtotales por categoría de producto.

**Ejemplo de uso:**
```java
Invoice invoice = new InvoiceBuilder()
    .setCustomer("John Doe", "123 Main St", "555-1234")
    .addProduct("Laptop", 1, 1200.00, 0.10)
    .addProduct("Mouse", 2, 25.00)
    .setTax(0.08)
    .setPaymentDetails("Credit Card", "Net 30", "2024-06-01")
    .build();
```

---

### Ejercicio 3: Constructor de Personajes para un Juego de Rol (RPG Character Builder)
**Objetivo:** Crear un *Builder* para construir personajes en un juego de rol (RPG) con atributos personalizables.

**Descripción:**
Crea una clase `CharacterBuilder` para construir un personaje con:
- **Nombre**: el nombre del personaje.
- **Clase de personaje**: guerrero, mago, arquero, etc.
- **Atributos**: fuerza, inteligencia, destreza, cada uno con un valor inicial.
- **Equipo**: arma, armadura y accesorios.
- **Habilidades**: lista de habilidades o hechizos iniciales.

El *Builder* debe verificar que la suma de los valores de los atributos no exceda un total máximo, para asegurar el balance del personaje.

**Dificultad adicional:**
- Implementa un sistema de puntos, de modo que cada atributo y equipo tiene un costo, y el personaje debe mantenerse dentro de un presupuesto de puntos.
- Permite que el personaje tenga diferentes niveles y habilidades adicionales dependiendo de la clase de personaje seleccionada.

**Ejemplo de uso:**
```java
RPGCharacter character = new CharacterBuilder()
    .setName("Aragon")
    .setClass("Warrior")
    .setAttribute("Strength", 15)
    .setAttribute("Intelligence", 8)
    .setAttribute("Dexterity", 10)
    .setWeapon("Sword")
    .setArmor("Chainmail")
    .addSkill("Swordsmanship")
    .build();
```

---

### Ejercicio 4: Generador de Correo Electrónico Complejo (Email Builder)
**Objetivo:** Crear un *Builder* para construir correos electrónicos personalizados y configurables.

**Descripción:**
Desarrolla una clase `EmailBuilder` que permita construir un correo electrónico con opciones de personalización, tales como:
- **Remitente**: dirección de correo electrónico del remitente.
- **Destinatarios**: uno o más destinatarios, incluyendo copias (CC) y copias ocultas (BCC).
- **Asunto**: asunto del correo.
- **Contenido**: cuerpo del correo electrónico, con soporte para texto y HTML.
- **Adjuntos**: permite agregar uno o más archivos adjuntos.

El *Builder* debe permitir configurar estos detalles y luego generar el correo electrónico en un formato listo para ser enviado.

**Dificultad adicional:**
- Permite establecer el correo como de alta prioridad.
- Añade la capacidad de programar el envío del correo para una fecha y hora específica.

**Ejemplo de uso:**
```java
Email email = new EmailBuilder()
    .setSender("sender@example.com")
    .addRecipient("recipient@example.com")
    .addCC("cc@example.com")
    .setSubject("Project Update")
    .setContent("Here's the latest update on the project.", true) // true for HTML content
    .addAttachment("/path/to/file.pdf")
    .setPriority("High")
    .build();
```

---

### Ejercicio 5: Generador de Formularios Web (Form Builder)
**Objetivo:** Crear un *Builder* para construir formularios web configurables.

**Descripción:**
Crea una clase `FormBuilder` que permita construir un formulario web con los siguientes elementos:
- **Campos de entrada**: nombre, correo electrónico, número de teléfono, etc.
- **Tipos de campo**: campo de texto, selección, casilla de verificación, radio button, etc.
- **Validaciones**: longitud mínima y máxima, campos obligatorios, patrones específicos.
- **Diseño**: opciones de diseño como etiquetas alineadas, orientación de los campos, etc.

El *Builder* debe permitir configurar cada campo con sus validaciones y generar el formulario completo.

**Dificultad adicional:**
- Agrega la capacidad de establecer campos condicionales que solo se muestran en función de la selección de otros campos.
- Incluye métodos para generar el formulario en HTML o en JSON para integración con sistemas externos.

**Ejemplo de uso:**
```java
Form form = new FormBuilder()
    .addField("Name", "text", true) // true for required
    .addField("Email", "email", true)
    .addField("Age", "number", false, 18, 99) // with min and max validation
    .addDropdown("Country", Arrays.asList("USA", "Canada", "Mexico"))
    .setLayout("horizontal")
    .build();
```

---
#hard
## Ejercicios con dificultad difícil

### Ejercicio 1: Generador de consultas SQL complejas
**Objetivo:** Crear un *Builder* para construir consultas SQL complejas de forma dinámica.

**Descripción:**
Crea una clase `SQLQueryBuilder` que permita construir consultas SQL de SELECT complejas. La clase debería tener métodos para agregar diferentes partes de la consulta, como:
- **SELECT**: campos a seleccionar
- **FROM**: tabla
- **JOIN**: para agregar una o múltiples uniones
- **WHERE**: filtros con condiciones y operadores lógicos
- **ORDER BY**: para ordenar los resultados
- **LIMIT**: para limitar el número de resultados

**Dificultad adicional:**
- Soporta anidaciones, por ejemplo, subconsultas en los filtros o en los campos seleccionados.
- Permite agregar filtros condicionales (si un campo no está vacío, agregar el filtro correspondiente).

**Ejemplo de uso**:
```java
SQLQueryBuilder builder = new SQLQueryBuilder();
String query = builder.select("name", "age")
                      .from("users")
                      .join("orders", "users.id = orders.user_id")
                      .where("age > 18")
                      .orderBy("name")
                      .limit(10)
                      .build();
```

### Ejercicio 2: Constructor de perfiles de usuario para un sistema de juegos en línea
**Objetivo:** Implementar un *Builder* para crear perfiles de usuario con configuraciones avanzadas en un sistema de juegos en línea.

**Descripción:**
En un sistema de juegos en línea, un perfil de usuario puede tener una gran variedad de configuraciones, tales como:
- **Atributos básicos**: nombre de usuario, avatar, nivel, experiencia.
- **Habilidades desbloqueadas**: habilidades o poderes que se hayan desbloqueado.
- **Configuración de notificaciones**: frecuencia de notificaciones y tipo de notificaciones deseadas.
- **Estadísticas de juegos**: juegos jugados, tiempo total en el juego, logros desbloqueados.

El *Builder* debe permitir construir el perfil de usuario con configuraciones personalizadas, y debe manejar la validación de datos (por ejemplo, que el nombre de usuario sea único) y la persistencia opcional en una base de datos simulada al finalizar la construcción.

**Dificultad adicional:**
- Soporta la posibilidad de guardar el perfil en diferentes formatos (JSON, XML) y realiza la validación de datos según el formato.
- Incluye métodos para agregar diferentes tipos de configuraciones de notificaciones en una lista (ej. `daily`, `weekly`).
  
**Ejemplo de uso**:
```java
UserProfile profile = new UserProfileBuilder()
    .withUsername("Gamer123")
    .withAvatar("warrior.png")
    .withLevel(10)
    .withExperience(1500)
    .withSkill("Stealth", 5)
    .withNotificationPreference("weekly")
    .withAchievement("First Blood")
    .build();
```

### Ejercicio 3: Generador de reportes financieros
**Objetivo:** Crear un *Builder* para construir reportes financieros de manera flexible.

**Descripción:**
Desarrolla un `FinancialReportBuilder` para generar reportes financieros personalizados. El *Builder* debe permitir configurar el reporte con opciones como:
- **Período de tiempo**: diario, semanal, mensual, etc.
- **Filtros**: rango de fechas, tipos de transacciones (ingresos, egresos), categorías de gastos.
- **Visualizaciones**: gráficos como barras, líneas, pasteles.
- **Formato de salida**: JSON, CSV, PDF.

El reporte debe poder construirse y generar la salida en el formato deseado, permitiendo al usuario agregar secciones específicas como "Resumen de Ingresos", "Detalle de Transacciones", etc.

**Dificultad adicional:**
- Permite agregar secciones opcionales, como un análisis de tendencias o predicciones.
- Incluye la opción de generar reportes combinados que unan datos de distintos períodos o categorías.

**Ejemplo de uso**:
```java
FinancialReport report = new FinancialReportBuilder()
    .setTimePeriod("monthly")
    .filterByTransactionType("income")
    .filterByCategory("sales")
    .addVisualization("line chart")
    .setOutputFormat("PDF")
    .build();
```

### Ejercicio 4: Configurador de sistemas de Inteligencia Artificial
**Objetivo:** Construir un sistema de configuración para modelos de IA complejos.

**Descripción:**
Desarrolla una clase `AIModelBuilder` para configurar y construir modelos de IA personalizados. Este *Builder* debe permitir especificar parámetros como:
- **Arquitectura del modelo**: CNN, RNN, Transformer, etc.
- **Capas y neuronas**: número de capas, neuronas por capa.
- **Hiperparámetros de entrenamiento**: tasa de aprendizaje, tamaño de lote, optimizador.
- **Preprocesamiento de datos**: tipo de normalización, aumentación de datos.

El *Builder* debe ofrecer métodos para configurar cada uno de estos aspectos y permitir la creación flexible del modelo final.

**Dificultad adicional:**
- Implementa validaciones complejas, como verificar que los hiperparámetros y arquitecturas sean compatibles.
- Incluye la opción de serializar el modelo para guardar la configuración y los parámetros para reutilización futura.

**Ejemplo de uso**:
```java
AIModel model = new AIModelBuilder()
    .withArchitecture("CNN")
    .addLayer("Conv2D", 64)
    .addLayer("MaxPooling2D")
    .addLayer("Dense", 128)
    .withLearningRate(0.001)
    .withBatchSize(32)
    .build();
```

### Recomendaciones adicionales:
1. **Lenguaje de elección**: Java y C# son ideales por su estructura orientada a objetos y buen soporte para *Builders*, además de una sintaxis robusta para crear instancias complejas.
2. **Implementación dinámica**: Si prefieres lenguajes de tipado dinámico como Python o JavaScript, puedes agregar características adicionales como validaciones dinámicas y serialización en JSON o XML para estos ejercicios.