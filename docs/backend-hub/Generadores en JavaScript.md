# El poder de `function*` y `yield`
Los generadores son una característica especial de JavaScript que permite crear funciones iterables cuya ejecución puede pausarse y reanudarse. Veamos en detalle cómo funcionan.

## Conceptos básicos de generadores

Un generador se define usando `function*` (con asterisco) y utiliza la palabra clave `yield` para pausar la ejecución y producir valores.

```javascript
function* contador() {
  yield 1;
  yield 2;
  yield 3;
}

const generador = contador();
console.log(generador.next()); // { value: 1, done: false }
console.log(generador.next()); // { value: 2, done: false }
console.log(generador.next()); // { value: 3, done: false }
console.log(generador.next()); // { value: undefined, done: true }
```

## Características clave de los generadores

### 1. Ejecución pausable

A diferencia de las funciones regulares, los generadores pueden pausar su ejecución con `yield` y mantener su estado interno:

```javascript
function* procesoLargo() {
  console.log("Iniciando proceso");
  yield "Paso 1 completado";
  
  console.log("Continuando proceso");
  yield "Paso 2 completado";
  
  console.log("Finalizando proceso");
  return "Proceso terminado";
}

const proceso = procesoLargo();
console.log(proceso.next().value); // Muestra "Iniciando proceso" y luego "Paso 1 completado"
console.log(proceso.next().value); // Muestra "Continuando proceso" y luego "Paso 2 completado"
console.log(proceso.next().value); // Muestra "Finalizando proceso" y luego "Proceso terminado"
```

### 2. Comunicación bidireccional

Los generadores permiten comunicación en ambas direcciones. El método `.next()` puede recibir un valor que se convierte en el resultado de la expresión `yield`:

```javascript
function* conversacion() {
  const pregunta1 = yield "¿Cómo te llamas?";
  console.log(`Hola ${pregunta1}`);
  
  const pregunta2 = yield "¿Cuántos años tienes?";
  console.log(`¡Wow, ${pregunta2} años!`);
  
  return "Conversación terminada";
}

const dialogo = conversacion();
console.log(dialogo.next().value);      // "¿Cómo te llamas?"
console.log(dialogo.next("María").value); // Muestra "Hola María" y devuelve "¿Cuántos años tienes?"
console.log(dialogo.next(25).value);      // Muestra "¡Wow, 25 años!" y devuelve "Conversación terminada"
```

### 3. Iterables e iteradores

Los generadores implementan la interfaz de iterador, por lo que pueden usarse con bucles `for...of`:

```javascript
function* fibonacci() {
  let a = 0, b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}

const fib = fibonacci();
// Primeros 10 números de Fibonacci
for (let i = 0; i < 10; i++) {
  console.log(fib.next().value);
}

// Usando for...of (necesitamos limitar, ya que es infinito)
function* primerosCincoFib() {
  let f = fibonacci();
  for (let i = 0; i < 5; i++) {
    yield f.next().value;
  }
}

for (const num of primerosCincoFib()) {
  console.log(num);
}
```

## Casos de uso avanzados

### 1. Gestión de flujos asíncronos

Los generadores fueron usados (antes de async/await) para manejar código asíncrono de forma sincrónica:

```javascript
function ejecutor(generatorFn) {
  const generador = generatorFn();
  
  function manejar(resultado) {
    if (resultado.done) return Promise.resolve(resultado.value);
    
    return Promise.resolve(resultado.value)
      .then(res => manejar(generador.next(res)))
      .catch(err => manejar(generador.throw(err)));
  }
  
  return manejar(generador.next());
}

// Simulación de peticiones
function obtenerUsuario(id) {
  return new Promise(resolve => {
    setTimeout(() => resolve({ id, nombre: "Usuario " + id }), 1000);
  });
}

function obtenerPosts(usuario) {
  return new Promise(resolve => {
    setTimeout(() => resolve([
      { id: 1, titulo: "Post 1 de " + usuario.nombre },
      { id: 2, titulo: "Post 2 de " + usuario.nombre }
    ]), 1000);
  });
}

// Uso con generadores
function* cargarDatosUsuario(userId) {
  try {
    const usuario = yield obtenerUsuario(userId);
    console.log("Usuario cargado:", usuario);
    
    const posts = yield obtenerPosts(usuario);
    console.log("Posts cargados:", posts);
    
    return { usuario, posts };
  } catch (error) {
    console.error("Error:", error);
  }
}

// Ejecutar la secuencia
ejecutor(function* () {
  const resultado = yield* cargarDatosUsuario(123);
  console.log("Proceso completo:", resultado);
});
```

### 2. Delegación con `yield*`

Los generadores pueden delegar a otros generadores usando `yield*`:

```javascript
function* generadorA() {
  yield 1;
  yield 2;
}

function* generadorB() {
  yield 3;
  yield* generadorA(); // Delegación - produce 1, 2
  yield 4;
}

const gen = generadorB();
console.log([...gen]); // [3, 1, 2, 4]
```

### 3. Generadores infinitos

Los generadores pueden representar secuencias infinitas de forma eficiente:

```javascript
function* todosLosEnteros() {
  let n = 0;
  while (true) {
    yield n++;
  }
}

function* numerosPrimos() {
  function esPrimo(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
      if (n % i === 0) return false;
    }
    return true;
  }
  
  for (const n of todosLosEnteros()) {
    if (esPrimo(n)) yield n;
  }
}

// Primeros 10 números primos
const primos = numerosPrimos();
for (let i = 0; i < 10; i++) {
  console.log(primos.next().value);
}
```

### 4. Máquinas de estado

Los generadores pueden implementar máquinas de estado de forma concisa:

```javascript
function* maquinaEstado() {
  let estado = "INICIO";
  
  while (true) {
    switch (estado) {
      case "INICIO":
        estado = yield "Estoy en INICIO, ¿a dónde voy?";
        break;
      case "PROCESAR":
        estado = yield "Estoy PROCESANDO, ¿siguiente paso?";
        break;
      case "FINALIZAR":
        estado = yield "Estoy FINALIZANDO, ¿continuar?";
        break;
      case "TERMINAR":
        return "Máquina detenida";
      default:
        estado = "INICIO";
    }
  }
}

const maquina = maquinaEstado();
console.log(maquina.next().value);            // "Estoy en INICIO, ¿a dónde voy?"
console.log(maquina.next("PROCESAR").value);  // "Estoy PROCESANDO, ¿siguiente paso?"
console.log(maquina.next("FINALIZAR").value); // "Estoy FINALIZANDO, ¿continuar?"
console.log(maquina.next("TERMINAR").value);  // "Máquina detenida"
```

## Generadores y middleware

El ejemplo que viste anteriormente con `autenticacionFlow` es un caso interesante:

```javascript
function* autenticacionFlow() {
  const token = yield extractToken;
  const usuario = yield validateToken(token);
  return usuario;
}
```

Este patrón utiliza generadores para:
1. Definir una secuencia de pasos (extracción de token → validación → resultado)
2. Pausar en cada paso, permitiendo que el ejecutor controle el flujo
3. Comunicar resultados entre pasos (el token extraído se usa para validar)

El ejecutor maneja cada paso del generador, lo que permite:
- Manejar excepciones uniformemente
- Proporcionar un flujo lineal para código asíncrono
- Componer flujos complejos de forma declarativa

## Ventajas y desventajas

### Ventajas
- Memoria eficiente para secuencias grandes o infinitas
- Control preciso sobre iteraciones
- Código más limpio para algoritmos con estado
- Base para implementar corrutinas

### Desventajas
- Curva de aprendizaje pronunciada
- Pueden ser difíciles de depurar
- En gran parte reemplazados por async/await para código asíncrono
- No todas las bibliotecas están optimizadas para trabajar con ellos

# Casos de uso actuales de generadores en JavaScript

Aunque async/await ha reemplazado a los generadores para muchos casos de programación asíncrona, los generadores siguen siendo relevantes y poderosos en 2025 para ciertos escenarios específicos:

## 1. Procesamiento de datos en streaming

Los generadores son ideales para procesar grandes volúmenes de datos sin cargarlos completamente en memoria:

```javascript
async function* streamDatos(url) {
  const response = await fetch(url);
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  
  while (true) {
    const {done, value} = await reader.read();
    if (done) break;
    
    const chunk = decoder.decode(value, {stream: true});
    const lines = chunk.split('\n');
    
    for (const line of lines) {
      if (line) yield JSON.parse(line);
    }
  }
}

// Procesar gigabytes de datos línea por línea
async function procesarLogs() {
  for await (const entrada of streamDatos('https://api.ejemplo.com/logs')) {
    if (entrada.nivel === 'ERROR') {
      console.log(`Error encontrado: ${entrada.mensaje}`);
    }
  }
}
```

## 2. Iteradores personalizados complejos

Cuando necesitas un control preciso sobre cómo se itera una estructura de datos:

```javascript
class ArbolBinario {
  constructor(valor, izquierda = null, derecha = null) {
    this.valor = valor;
    this.izquierda = izquierda;
    this.derecha = derecha;
  }
  
  // Recorrido inorden usando generador
  *inorden() {
    if (this.izquierda) yield* this.izquierda.inorden();
    yield this.valor;
    if (this.derecha) yield* this.derecha.inorden();
  }
  
  // Recorrido por niveles usando generador
  *porNiveles() {
    const cola = [this];
    while (cola.length > 0) {
      const nodo = cola.shift();
      yield nodo.valor;
      if (nodo.izquierda) cola.push(nodo.izquierda);
      if (nodo.derecha) cola.push(nodo.derecha);
    }
  }
  
  // Permite usar for...of directamente con la instancia
  [Symbol.iterator]() {
    return this.inorden();
  }
}

// Uso
const arbol = new ArbolBinario(4,
  new ArbolBinario(2, new ArbolBinario(1), new ArbolBinario(3)),
  new ArbolBinario(6, new ArbolBinario(5), new ArbolBinario(7))
);

// Iteración simple
for (const valor of arbol) {
  console.log(valor); // 1, 2, 3, 4, 5, 6, 7
}
```

## 3. Paginación y recuperación de datos por lotes

Simplifica el manejo de APIs paginadas:

```javascript
async function* obtenerTodosLosResultados(endpoint, tamañoPagina = 100) {
  let pagina = 1;
  let hayMasResultados = true;
  
  while (hayMasResultados) {
    const respuesta = await fetch(`${endpoint}?page=${pagina}&limit=${tamañoPagina}`);
    const datos = await respuesta.json();
    
    if (datos.resultados.length === 0) {
      hayMasResultados = false;
    } else {
      pagina++;
      // Yield cada resultado individualmente
      for (const item of datos.resultados) {
        yield item;
      }
    }
  }
}

// Procesar todos los usuarios sin preocuparse por la paginación
async function encontrarUsuariosInactivos() {
  const usuariosInactivos = [];
  
  for await (const usuario of obtenerTodosLosResultados('https://api.ejemplo.com/usuarios')) {
    if (usuario.ultimoAcceso < Date.now() - 90*24*60*60*1000) {
      usuariosInactivos.push(usuario);
    }
  }
  
  return usuariosInactivos;
}
```

## 4. Máquinas de estado finito

Implementaciones limpias y mantenibles de máquinas de estado:

```javascript
function* creadorDeWorkflow() {
  // Estado inicial
  let datos = { estado: 'INICIADO' };
  
  // Paso 1: Validación
  datos = yield {
    estado: 'VALIDACIÓN',
    siguientePaso: (datosEntrada) => {
      if (!datosEntrada.email) throw new Error('Email requerido');
      return { ...datos, ...datosEntrada, estado: 'VALIDADO' };
    }
  };
  
  // Paso 2: Procesamiento
  datos = yield {
    estado: 'PROCESANDO',
    siguientePaso: async (datosEntrada) => {
      const resultado = await procesarPago(datosEntrada);
      return { ...datos, resultado, estado: 'PROCESADO' };
    }
  };
  
  // Paso 3: Finalización
  datos = yield {
    estado: 'FINALIZANDO',
    siguientePaso: (datosEntrada) => {
      return { ...datos, ...datosEntrada, estado: 'COMPLETADO' };
    }
  };
  
  return { ...datos, fechaCompletado: new Date() };
}

// Uso en un sistema de workflow
async function ejecutarProcesoDePago(datosPago) {
  const workflow = creadorDeWorkflow();
  let paso = workflow.next().value;
  
  try {
    // Paso 1
    paso = workflow.next(paso.siguientePaso({
      email: datosPago.email,
      monto: datosPago.monto
    })).value;
    
    // Paso 2
    const resultado = await paso.siguientePaso({
      tarjeta: datosPago.tarjeta
    });
    paso = workflow.next(resultado).value;
    
    // Paso 3
    const resultadoFinal = paso.siguientePaso({
      notificarA: datosPago.email
    });
    return workflow.next(resultadoFinal).value;
    
  } catch (error) {
    return { estado: 'ERROR', error: error.message };
  }
}
```

## 5. Testing con datos complejos

Generación de casos de prueba controlados y replicables:

```javascript
function* generadorCasosPrueba() {
  // Caso básico
  yield {
    descripcion: 'Usuario válido, datos completos',
    entrada: {
      nombre: 'Ana García',
      email: 'ana@ejemplo.com',
      edad: 28
    },
    resultadoEsperado: true
  };
  
  // Casos límite
  for (const edad of [18, 17, 100, 101]) {
    yield {
      descripcion: `Verificación para edad límite: ${edad}`,
      entrada: {
        nombre: 'Usuario Prueba',
        email: 'test@ejemplo.com',
        edad
      },
      resultadoEsperado: edad >= 18 && edad <= 100
    };
  }
  
  // Casos de validación de correo
  for (const email of ['', 'invalido', 'usuario@', '@dominio.com']) {
    yield {
      descripcion: `Validación correo: "${email}"`,
      entrada: {
        nombre: 'Test',
        email,
        edad: 30
      },
      resultadoEsperado: false
    };
  }
}

// Framework de testing
function ejecutarTests(validador) {
  const resultados = {
    pasados: 0,
    fallados: 0,
    detalles: []
  };
  
  for (const caso of generadorCasosPrueba()) {
    const resultado = validador(caso.entrada);
    const exitoso = resultado === caso.resultadoEsperado;
    
    resultados.detalles.push({
      descripcion: caso.descripcion,
      exitoso,
      entrada: caso.entrada,
      esperado: caso.resultadoEsperado,
      obtenido: resultado
    });
    
    if (exitoso) resultados.pasados++;
    else resultados.fallados++;
  }
  
  return resultados;
}
```

## 6. Simulación y modelado

Los generadores son excelentes para simulaciones que evolucionan con el tiempo:

```javascript
function* simulacionPoblacion(inicial, tasaCrecimiento, añosMax) {
  let población = inicial;
  let año = 2025;
  
  while (año < 2025 + añosMax) {
    población = Math.floor(población * (1 + tasaCrecimiento));
    
    yield {
      año,
      población,
      eventos: generarEventosAleatorios(año, población)
    };
    
    año++;
  }
}

function* simulaciónEcosistema() {
  const ecosistema = {
    depredadores: 50,
    presas: 1000,
    plantas: 5000,
    año: 0
  };
  
  while (ecosistema.depredadores > 0 && ecosistema.presas > 0) {
    // Actualizar modelo ecológico
    const tasaReproducciónPresas = 0.2 * (ecosistema.plantas / 5000);
    const mortalidadPresas = 0.1 * (ecosistema.depredadores / 50);
    
    ecosistema.presas = Math.floor(ecosistema.presas * (1 + tasaReproducciónPresas - mortalidadPresas));
    ecosistema.depredadores = Math.floor(ecosistema.depredadores * (1 + 0.1 * (ecosistema.presas / 1000) - 0.1));
    ecosistema.plantas = Math.floor(ecosistema.plantas * (1 + 0.15 - 0.1 * (ecosistema.presas / 1000)));
    ecosistema.año++;
    
    yield { ...ecosistema };
  }
  
  return { ...ecosistema, estado: "Extinción" };
}
```

## 7. Bibliotecas y frameworks modernos

Varias bibliotecas modernas usan generadores internamente:

### Redux Saga

[Redux-Saga - Un gestor intuitivo de efectos secundarios de Redux. | Redux-Saga](https://redux-saga.js.org/) utiliza generadores para manejar efectos secundarios en aplicaciones Redux:

```javascript
import { call, put, takeEvery } from 'redux-saga/effects';

// Saga para cargar usuarios
function* cargarUsuarios(accion) {
  try {
    yield put({ type: 'CARGAR_USUARIOS_INICIO' });
    const usuarios = yield call(api.obtenerUsuarios);
    yield put({ type: 'CARGAR_USUARIOS_ÉXITO', payload: usuarios });
  } catch (error) {
    yield put({ type: 'CARGAR_USUARIOS_ERROR', error });
  }
}

// Saga raíz
function* sagaRaíz() {
  yield takeEvery('SOLICITAR_USUARIOS', cargarUsuarios);
}
```

### Herramientas de generación de datos

Bibliotecas como Faker.js usan generadores para crear conjuntos de datos sintéticos:

```javascript
function* generarUsuarios(cantidad) {
  for (let i = 0; i < cantidad; i++) {
    yield {
      id: faker.string.uuid(),
      nombre: faker.person.fullName(),
      email: faker.internet.email(),
      dirección: faker.location.streetAddress(),
      creado: faker.date.past()
    };
  }
}

// Generar 10,000 usuarios sin consumir 10,000 objetos en memoria
const usuarioGen = generarUsuarios(10000);
const primeros100 = Array.from(usuarioGen).slice(0, 100);
```

## Conclusiones sobre el uso actual

Los generadores siguen siendo relevantes en 2025 porque:

1. **Eficiencia de memoria**: Permiten trabajar con conjuntos de datos potencialmente infinitos sin cargarlos completamente en memoria.

2. **Claridad conceptual**: Proporcionan un modelo mental claro para secuencias, iteraciones y flujos de estado.

3. **Composición**: Permiten componer flujos de datos complejos de manera declarativa (`yield*`).

4. **Control preciso**: Ofrecen control granular sobre la iteración y ejecución que es difícil de lograr con otros mecanismos.

A pesar de que async/await ha reemplazado muchos casos de uso, los generadores siguen siendo la herramienta ideal cuando necesitas control preciso sobre secuencias, iteraciones perezosas (lazy) o simulaciones con estado.