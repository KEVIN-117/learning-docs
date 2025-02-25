## ¿Qué son realmente los closures?

Un closure es una función que "recuerda" el entorno en el que fue creada. Esto significa que puede acceder a las variables definidas en su ámbito léxico externo incluso después de que la función externa haya finalizado su ejecución.

## Elementos clave de un closure

1. **Función interna**: Una función definida dentro de otra función
2. **Entorno léxico**: Las variables disponibles en el momento de definir la función
3. **Persistencia**: La capacidad de acceder a estas variables incluso cuando la función externa ha terminado

## Ejemplo básico

```javascript title="closureCounter.js" linenums="1"
function crearContador() {
  let contador = 0;  // Variable en el ámbito léxico externo
  
  return function() {  // Función interna (closure)
    contador++;  // Accede y modifica la variable externa
    return contador;
  };
}

const incrementar = crearContador();
console.log(incrementar());  // 1
console.log(incrementar());  // 2
console.log(incrementar());  // 3
```

Aquí, `incrementar` es un closure que "recuerda" la variable `contador` de su ámbito léxico original.

## Casos de uso prácticos

### 1. Encapsulación y datos privados

```javascript linenums="1"
function crearBilletera(saldoInicial) {
  let saldo = saldoInicial;
  
  return {
    consultar: function() { return saldo; },
    depositar: function(monto) { saldo += monto; },
    retirar: function(monto) {
      if (monto <= saldo) {
        saldo -= monto;
        return true;
      }
      return false;
    }
  };
}

const miBilletera = crearBilletera(100);
miBilletera.depositar(50);
console.log(miBilletera.consultar());  // 150
// No hay forma de acceder directamente a `saldo`
```

### 2. Fábricas de funciones

```javascript
function multiplicadorPor(factor) {
  return function(numero) {
    return numero * factor;
  };
}

const duplicar = multiplicadorPor(2);
const triplicar = multiplicadorPor(3);

console.log(duplicar(5));  // 10
console.log(triplicar(5));  // 15
```

### 3. Gestión de eventos

```javascript
function configurarBoton(id, mensaje) {
  const boton = document.getElementById(id);
  boton.addEventListener('click', function() {
    // Closure que recuerda el mensaje específico
    alert(mensaje);
  });
}

configurarBoton('boton1', 'Hola desde el botón 1');
configurarBoton('boton2', 'Saludos desde el botón 2');
```

### 4. Memoización (caché de resultados)

```javascript
function crearFuncionMemoizada(fn) {
  const cache = {};
  
  return function(arg) {
    if (cache[arg] === undefined) {
      cache[arg] = fn(arg);
    }
    return cache[arg];
  };
}

// Función costosa (ejemplo: cálculo de Fibonacci)
const fibonacci = crearFuncionMemoizada(function(n) {
  if (n <= 1) return n;
  return fibonacci(n-1) + fibonacci(n-2);
});
```

## Trampas comunes con closures

### 1. Bucles y closures

```javascript
// Problema clásico
for (var i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);  // Imprime 3, 3, 3
  }, 100);
}

// Solución con IIFE (Immediately Invoked Function Expression)
for (var i = 0; i < 3; i++) {
  (function(capturedI) {
    setTimeout(function() {
      console.log(capturedI);  // Imprime 0, 1, 2
    }, 100);
  })(i);
}

// Solución moderna con let (crea un nuevo ámbito por iteración)
for (let i = 0; i < 3; i++) {
  setTimeout(function() {
    console.log(i);  // Imprime 0, 1, 2
  }, 100);
}
```

### 2. Rendimiento y memoria

Los closures mantienen referencias a variables externas, lo que puede prevenir la liberación de memoria:

```javascript
function procesarDatos(datos) {
  const datosProcesados = procesoDatos(datos);  // Gran objeto
  
  return function() {
    console.log("Longitud de datos:", datosProcesados.length);
    // Aunque solo usamos .length, todo el objeto permanece en memoria
  };
}
```

## Closures y patrones de diseño

Los closures son fundamentales en muchos patrones de JavaScript:

1. **Módulo**: Encapsula código y expone solo una API pública
   ```javascript
   const miModulo = (function() {
     let contador = 0;  // Privado
     
     return {
       incrementar: function() { contador++; },
       obtenerValor: function() { return contador; }
     };
   })();
   ```

2. **Currying**: Transformación de funciones multi-argumento en secuencias de funciones de un solo argumento
   ```javascript
   function curry(fn) {
     return function curried(...args) {
       if (args.length >= fn.length) {
         return fn.apply(this, args);
       }
       return function(...moreArgs) {
         return curried.apply(this, args.concat(moreArgs));
       };
     };
   }
   ```

3. **Middleware** (como en Express.js)
   ```javascript
   function logger(opciones) {
     // Closure que recuerda opciones
     return function(req, res, next) {
       console.log(`${opciones.prefijo}: ${req.method} ${req.url}`);
       next();
     };
   }
   
   app.use(logger({ prefijo: 'PETICIÓN' }));
   ```

[[Profundizando en Middlewares y Closures]]
