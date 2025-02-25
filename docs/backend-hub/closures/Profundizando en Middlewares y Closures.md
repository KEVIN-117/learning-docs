Los middlewares son un patrón de diseño extremadamente poderoso que utiliza los closures como mecanismo fundamental. Vamos a explorar este concepto en profundidad.

## ¿Qué es un Middleware?

Un middleware es una función intercalada en el flujo de procesamiento de una solicitud/acción que puede:
1. Acceder a los objetos de solicitud y respuesta
2. Ejecutar código
3. Modificar los objetos de solicitud/respuesta
4. Finalizar el ciclo de solicitud-respuesta
5. Llamar al siguiente middleware en la pila

## Cómo los Closures Habilitan los Middlewares

La mayoría de implementaciones de middleware utilizan closures de esta forma:

```javascript
function middleware(opciones) {
  // Fase de configuración - captura opciones en el closure
  const configuracion = { ...opciones };
  
  // Retorna la función real de middleware
  return function(req, res, next) {
    // Tiene acceso a 'configuracion' a través del closure
    // Procesa la solicitud
    // Llama a next() para pasar al siguiente middleware
  };
}
```

## Ejemplos Detallados en Express.js

### 1. Middleware de Autenticación

```javascript
function autenticar(opciones) {
  // Opciones predeterminadas con valores sensatos
  const config = {
    redirectUrl: '/login',
    tokenField: 'authorization',
    ...opciones
  };
  
  // Retorna el middleware real
  return function(req, res, next) {
    const token = req.headers[config.tokenField] || req.query.token;
    
    if (!token) {
      if (config.redirectUnauthorized) {
        return res.redirect(config.redirectUrl);
      }
      return res.status(401).json({ error: 'No autorizado' });
    }
    
    // Verifica el token (ejemplo simplificado)
    try {
      const usuario = verificarToken(token, config.secretKey);
      // Adjunta el usuario al objeto request para middlewares posteriores
      req.usuario = usuario;
      next();
    } catch (error) {
      res.status(401).json({ error: 'Token inválido' });
    }
  };
}

// Uso
app.use('/api/privado', autenticar({ 
  secretKey: process.env.JWT_SECRET,
  redirectUnauthorized: false
}));
```

### 2. Middleware de Registro (Logging)

```javascript
function logger(opciones) {
  // Configuración con valores predeterminados
  const config = {
    formato: 'básico',
    incluirCuerpo: false,
    salida: console.log,
    ...opciones
  };
  
  // Preparación (puede incluir inicialización de recursos)
  const formatters = {
    básico: (req) => `${req.method} ${req.url}`,
    detallado: (req) => `${new Date().toISOString()} - ${req.method} ${req.url} - ${req.ip}`
  };
  
  const formatter = formatters[config.formato] || formatters.básico;
  
  // El middleware real
  return function(req, res, next) {
    // Captura el tiempo de inicio
    const inicio = Date.now();
    
    // Captura el método original para poder interceptarlo
    const end = res.end;
    
    // Modifica el método end para poder registrar al finalizar
    res.end = function(chunk, encoding) {
      // Restaura el método original
      res.end = end;
      
      // Llama al método original
      res.end(chunk, encoding);
      
      // Registra después de que la respuesta ha sido enviada
      const duracion = Date.now() - inicio;
      const logInfo = {
        peticion: formatter(req),
        estado: res.statusCode,
        duracion: `${duracion}ms`
      };
      
      if (config.incluirCuerpo && req.body) {
        logInfo.cuerpo = typeof req.body === 'object' 
          ? JSON.stringify(req.body) 
          : req.body;
      }
      
      config.salida(logInfo);
    };
    
    next();
  };
}

// Uso
app.use(logger({ 
  formato: 'detallado', 
  incluirCuerpo: true,
  salida: (info) => fs.appendFileSync('logs.txt', JSON.stringify(info) + '\n')
}));
```

### 3. Middleware de Control de Ratio (Rate Limiting)

```javascript
function rateLimiter(opciones) {
  // Configuración predeterminada
  const config = {
    ventanaMs: 60 * 1000, // 1 minuto
    max: 100,             // 100 solicitudes por ventana
    mensaje: 'Demasiadas solicitudes, por favor inténtelo más tarde',
    ...opciones
  };
  
  // Estado compartido entre todas las solicitudes (pero privado)
  const clientes = new Map();
  
  // Limpieza periódica para evitar fugas de memoria
  const limpiarIntervalo = setInterval(() => {
    const ahora = Date.now();
    clientes.forEach((datos, ip) => {
      if (ahora - datos.ultimoAcceso > config.ventanaMs * 2) {
        clientes.delete(ip);
      }
    });
  }, config.ventanaMs);
  
  // Previene fugas de memoria si el servidor se reinicia
  if (process.env.NODE_ENV !== 'test') {
    process.on('SIGINT', () => {
      clearInterval(limpiarIntervalo);
      process.exit(0);
    });
  }
  
  // El middleware real
  return function(req, res, next) {
    const ip = config.keyGenerator 
      ? config.keyGenerator(req)
      : req.ip;
    
    const ahora = Date.now();
    
    if (!clientes.has(ip)) {
      clientes.set(ip, {
        contador: 1,
        ultimoAcceso: ahora,
        reinicioEn: ahora + config.ventanaMs
      });
      return next();
    }
    
    const cliente = clientes.get(ip);
    
    // Reiniciar contador si la ventana ha pasado
    if (ahora > cliente.reinicioEn) {
      cliente.contador = 1;
      cliente.ultimoAcceso = ahora;
      cliente.reinicioEn = ahora + config.ventanaMs;
      return next();
    }
    
    // Incrementar contador
    cliente.contador++;
    cliente.ultimoAcceso = ahora;
    
    // Verificar límite
    if (cliente.contador > config.max) {
      const respuestaError = config.handler
        ? config.handler(req, res, next)
        : res.status(429).send(config.mensaje);
      
      return respuestaError;
    }
    
    next();
  };
}

// Uso
app.use('/api', rateLimiter({
  ventanaMs: 15 * 60 * 1000,  // 15 minutos
  max: 100,                   // 100 solicitudes por IP
  keyGenerator: (req) => req.headers['x-forwarded-for'] || req.ip,
  handler: (req, res) => {
    return res.status(429).json({
      error: 'Límite excedido',
      reintentoEn: Math.ceil((clientes.get(req.ip).reinicioEn - Date.now()) / 1000)
    });
  }
}));
```

## Middlewares en Arquitecturas Avanzadas

### Cadenas de Middleware

```javascript
function encadenar(...middlewares) {
  return function(req, res, finalCallback) {
    let index = 0;
    
    function siguiente(error) {
      // Si hay un error, salta a la función final
      if (error) return finalCallback(error);
      
      const middleware = middlewares[index++];
      
      // Si se acabaron los middlewares, llama al callback final
      if (!middleware) return finalCallback();
      
      try {
        middleware(req, res, siguiente);
      } catch (err) {
        siguiente(err);
      }
    }
    
    siguiente();
  };
}

// Uso
const procesarPeticion = encadenar(
  validarEntrada,
  autenticar({ tipo: 'bearer' }),
  verificarPermisos(['admin']),
  procesadorFinal
);

server.on('request', (req, res) => {
  procesarPeticion(req, res, (error) => {
    if (error) {
      res.statusCode = error.codigo || 500;
      res.end(error.mensaje || 'Error interno');
    }
  });
});
```

### Middleware Componible

```javascript
// Define middlewares como funciones generadoras
function* autenticacionFlow() {
  const token = yield extractToken;
  const usuario = yield validateToken(token);
  return usuario;
}

function* autorizacionFlow() {
  const usuario = yield autenticacionFlow();
  const permisosValidos = yield checkPermissions(usuario);
  if (!permisosValidos) {
    throw new Error('No autorizado');
  }
  return { usuario, permisosValidos };
}

// Ejecutor de middleware componible
function ejecutor(generatorFn) {
  return function(req, res, next) {
    const generador = generatorFn();
    
    function manejar(resultado) {
      if (resultado.done) {
        req.resultado = resultado.value;
        return next();
      }
      
      const middlewareFn = resultado.value;
      
      // El próximo middleware puede ser una función simple o otro componible
      Promise.resolve(middlewareFn(req, res, (error) => {
        if (error) return next(error);
        try {
          manejar(generador.next(req.resultado));
        } catch (err) {
          next(err);
        }
      }))
      .catch(next);
    }
    
    try {
      manejar(generador.next());
    } catch (error) {
      next(error);
    }
  };
}

// Uso
app.put('/recursos/:id', 
  ejecutor(autorizacionFlow),
  (req, res) => {
    // Aquí, req.resultado contiene { usuario, permisosValidos }
    res.json({ success: true });
  }
);
```

## Ventajas del Patrón Middleware con Closures

1. **Configurabilidad**: Los closures permiten "cerrar sobre" opciones de configuración
2. **Reutilización**: El mismo middleware puede usarse con diferentes configuraciones
3. **Encapsulación**: Estado y lógica privados que no contaminan el ámbito global
4. **Composición**: Los middlewares pueden componerse y anidarse
5. **Testabilidad**: Fácil de probar de forma aislada o en cadenas

---

[[Generadores en JavaScript]]
