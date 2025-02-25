## ¿Qué es $GraphQL$?
`GraphQL` fue creado por Facebook para proporcionar una manera más eficiente y flexible de gestionar la comunicación entre servidores y aplicaciones móviles o web. Es similar a una API REST, pero ofrece ciertas ventajas específicas.

- **Desacoplo del cliente-servidor**: En lugar de especificar las rutas URL (como en un RESTful API), $GraphQL$ permite que el cliente especifique exactamente qué datos quiere.
  
- **Minimización de tráfico de red**: El servidor envía solo los datos necesarios para cada petición, lo cual reduce la cantidad de datos transmitidos y mejorando así la eficiencia.

## Ventajas de GraphQL frente a REST

1. **Menor overhead**: 
   - Con una API GraphQL, el cliente puede especificar exactamente qué información necesita. Esto significa que no hay necesidad de pedir toda la estructura de datos disponibles, como ocurre con un `GET` en REST (donde se devuelve siempre todo el contenido disponible). Por lo tanto, GraphQL reduce considerablemente la cantidad de datos que deben ser transferidos.

2. **Flexibilidad y eficiencia**:
   - Puedes pedir exactamente los datos que necesitas (y solo esos) sin tener que preocuparte por las estructuras o endpoints disponibles en una API REST. Esto hace que sea más fácil adaptarse a la lógica del cliente, ya que se puede consultar directamente lo que se necesita.

3. **Carga de datos controlada**:
   - Con GraphQL, el cliente decide qué información necesita y cómo se presenta ese contenido. Por ejemplo, si solo necesitas un campo o dos en lugar de toda una estructura compleja, puedes especificar exactamente qué quieres obtener.

4. **Evolución sin cambios al código existente**: 
   - Es más fácil agregar nuevas consultas (queries) y mutaciones (mutations), ya que no estás obligado a modificar el esquema del servidor cada vez que necesitas un dato nuevo o diferente.
   
5. **Consistencia en la respuesta**:
   - GraphQL siempre devuelve los datos especificados en el formato solicitado, independientemente de si los datos existen en la base de datos o no.

6. **Un solo punto de contacto**:
   - Aunque REST puede ser compuesta por múltiples endpoints, GraphQL permite que todos esos recursos estén disponibles en un solo servidor y se obtengan en una sola petición. Esto también ayuda a reducir el número de solicitudes que el cliente tiene que hacer.

## ¿Cuándo usar GraphQL?

GraphQL es ideal para aplicaciones que requieren la capacidad de consultas personalizadas y donde las estructuras de datos varían mucho. Por ejemplo, si estás construyendo una aplicación que necesita diferentes combinaciones de datos en cada petición o consulta, GraphQL podría ser más eficiente.

Sin embargo, hay casos en los que REST puede seguir siendo preferible:
- Cuando la funcionalidad del API no es compleja y sigue un patrón sencillo.
- Si ya tienes una infraestructura estable con APIs REST y no necesitas cambiar mucho.
  
> [!IMPORTANT]
	> Todo en $GraphQL$ es una petición de typo $POST$, lo que ayuda a diferencias las peticiones son las consultas ($queries$) y mutaciones ($mutations$)
	> 

1. **Closure (clausura)**: Es cuando una función "recuerda" y tiene acceso a variables de su ámbito léxico externo, incluso después de que la función externa haya terminado de ejecutarse. En tu ejemplo, la función interna tiene acceso al parámetro `config` de la función externa.

2. **Higher-order function (función de orden superior)**: Es una función que hace al menos una de estas dos cosas:
   - Recibe una o más funciones como argumentos
   - Devuelve una función como resultado

En tu ejemplo `createVariants`, tienes ambos conceptos:
- Es una función de orden superior porque devuelve otra función
- La función retornada es un closure porque "recuerda" y tiene acceso al parámetro `config` de la función externa

Este patrón es muy común en JavaScript y especialmente en bibliotecas de React y sistemas de diseño. Permite:
- Crear configuraciones reutilizables
- Mantener estado entre llamadas de función
- Implementar patrones como "currying" (aplicación parcial de argumentos)
- Crear APIs más expresivas y declarativas

El `createVariants` específicamente está utilizando este patrón para crear una "fábrica de estilos" configurada una vez, que luego puede ser llamada múltiples veces con diferentes props y temas.

```js
// Esta función crea un sistema de variantes de estilo
export function createVariants(config) {
  // Devuelve una función que recibe props del componente y el tema
  return (props, theme) => {
    // Desestructura el tema
    const {palette, isLight} = theme || {};
    
    // Función para resolver valores que pueden ser funciones dependientes del tema
    const resolveThemeValue = value => {
      if (typeof value === 'function') {
        return value({palette, isLight});
      }
      return value;
    };
    
    // Comienza con los estilos base
    let styles = {...config?.base};
    
    // Obtiene las props del componente (o usa un objeto vacío)
    const variantProps = props ?? {};
    
    // PASO 1: APLICAR VARIANTES INDIVIDUALES
    if (config.variants) {
      Object.entries(config.variants).forEach(
        ([variantName, variantOptions]) => {
          // Obtiene el valor de la variante desde props o usa el valor predeterminado
          const value =
            variantProps[variantName] || config.defaultVariants?.[variantName];
            
          // Si hay un valor y está definido en las opciones de la variante
          if (value && variantOptions[value]) {
            // Obtiene los estilos para esa variante
            const variantStyle = variantOptions[value];
            
            // Resuelve valores que dependen del tema
            const resolvedStyle = Object.entries(variantStyle).reduce(
              (acc, [key, val]) => ({
                ...acc,
                [key]: resolveThemeValue(val),
              }),
              {},
            );
            
            // Combina con los estilos acumulados
            styles = {
              ...styles,
              ...resolvedStyle,
            };
          }
        },
      );
    }
    
    // PASO 2: APLICAR VARIANTES COMPUESTAS
    if (config.compoundVariants) {
      config.compoundVariants?.forEach(compoundVariant => {
        // Verifica si todas las condiciones de la variante compuesta coinciden
        const matches = Object.entries(compoundVariant.variants).every(
          ([variantName, variantValue]) =>
            variantProps[variantName] === variantValue ||
            config.defaultVariants?.[variantName] === variantValue,
        );
        
        // Si todas coinciden, aplica estos estilos
        if (matches) {
          // Resuelve valores que dependen del tema
          const resolvedStyle = Object.entries(compoundVariant.styles).reduce(
            (acc, [key, value]) => ({
              ...acc,
              [key]: resolveThemeValue(value),
            }),
            {},
          );
          
          // Combina con los estilos acumulados
          styles = {
            ...styles,
            ...resolvedStyle,
          };
        }
      });
    }
    
    // Devuelve el objeto de estilos final
    return styles;
  };
}

export const ButtonVariants = createVariants({
  base: {
    justifyContent: 'center',
    alignItems: 'center',
  },
  variants: {
    variant: {
      primary: {
        backgroundColor: ({palette, isLight}) =>
          isLight ? palette.turquoise[500] : palette.turquoise[500],
      },
      secondary: {
        backgroundColor: ({palette}) => palette.purple[500],
      },
      tertiary: {
        backgroundColor: ({palette}) => palette.orange[500],
      },
      outline: {
        backgroundColor: 'transparent',
        borderWidth: 1,
        borderColor: '#007AFF',
      },
      solid: {
        borderWidth: 0,
      },
      bordered: {
        borderWidth: 1,
      },
      light: {
        backgroundColor: 'transparent',
      },
      flat: {
        borderWidth: 0,
      },
      faded: {
        borderWidth: 1,
      },
      ghost: {
        borderWidth: 1,
        backgroundColor: 'transparent',
      },
    },
    shadow: {
      default: {
        boxShadow: '0px 4px 4px rgba(33, 33, 33, 0.2)',
      },
      inset: {
        boxShadow: 'inset 5 5 5 0.7 rgba(0, 0, 0, 0.25)',
      },
    },
    position: {
      absolute: {
        position: 'absolute',
      },
      relative: {
        position: 'relative',
      },

      fixed: {
        position: 'fixed',
      },
    },
    size: {
      sm: {
        paddingHorizontal: 12,
        paddingVertical: 6,
      },
      md: {
        paddingHorizontal: 16,
        paddingVertical: 8,
      },
      lg: {
        height: 48,
        gap: 8,
      },
      box: {
        width: 76,
        height: 76,
      },
      full: {
        width: '100%',
      },
    },
    color: {
      default: {
        color: '#ffffff',
      },
      primary: '',
      secondary: '',
      success: '',
      warning: '',
      danger: '',
    },
    radius: {
      none: {
        borderRadius: 0,
      },
      sm: {
        borderRadius: 4,
      },
      md: {
        borderRadius: 8,
      },
      lg: {
        borderRadius: 12,
      },
      xl: {
        borderRadius: 16,
      },
      full: {
        borderRadius: 50,
      },
    },
    fullWidth: {
      true: {
        width: '100%',
      },
    },
    isDisabled: {
      true: {
        opacity: 0.5,
        pointerEvents: 'none',
      },
    },
    isIconOnly: {
      true: {
        paddingHorizontal: 0,
        paddingVertical: 0,
        gap: 0,
      },
      false: {
        '>svg': {
          maxWidth: 24,
          maxHeight: 24,
        },
      },
    },
    disableAnimation: {
      true: {
        transition: 'none',
        dataPressed: 'scale-100',
      },
      false: {
        transition: 'transform-colors-opacity',
        motionReduce: 'transition-none',
      },
    },
    compoundVariant: [
      {
        variants: {
          variant: 'primary',
          size: 'large',
        },
        style: {
          backgroundColor: '#0066CC',
        },
      },
    ],
  },
  defaultVariants: {
    position: 'relative',
    color: 'default',
    fullWidth: false,
    isDisabled: false,
    isInGroup: false,
  },
});
```


Aquí tenemos un caso práctico del uso de `createVariants` que analizamos antes. Vamos a explicar exactamente cómo funciona el acceso a `palette` e `isLight`:

## Lo que está pasando paso a paso

1. **Creación de variantes del botón**:
   ```javascript
   export const ButtonVariants = createVariants({
     base: {
       justifyContent: 'center',
       alignItems: 'center',
     },
     variants: {
       variant: {
         primary: {
           backgroundColor: ({palette, isLight}) =>
             isLight ? palette.turquoise[500] : palette.turquoise[500],
         },
       }
     }
   })
   ```

2. **Proceso interno**:
   - `createVariants` recibe este objeto de configuración
   - Devuelve una función que será asignada a `ButtonVariants`

## Cómo se accede a `palette` e `isLight`

Lo interesante ocurre en la propiedad `backgroundColor`. En lugar de asignar un valor directo como `"#00FFFF"`, estás asignando una **función**:

```javascript
backgroundColor: ({palette, isLight}) =>
  isLight ? palette.turquoise[500] : palette.turquoise[500],
```

Esto es lo que pasa:

1. Cuando posteriormente llamas a `ButtonVariants` con props y un tema:
   ```javascript
   // Ejemplo de uso
   const buttonStyles = ButtonVariants({variant: 'primary'}, themeObject);
   ```

2. Dentro de la implementación de `createVariants`, recuerdas que hay una función `resolveThemeValue`:
   ```javascript
   const resolveThemeValue = value => {
     if (typeof value === 'function') {
       return value({palette, isLight});
     }
     return value;
   };
   ```

3. Esta función detecta cuando un valor es una función (como tu `backgroundColor`) y la ejecuta, pasándole `{palette, isLight}` que provienen del `themeObject`.

4. Tu función recibe estos valores, los desestructura en sus parámetros, y entonces puede usar `palette.turquoise[500]` y comprobar `isLight`.

## El flujo completo

Es como una "función retrasada" que se evaluará cuando se necesite:

1. Defines una **función** como valor para `backgroundColor`
2. Más tarde, cuando `ButtonVariants` se llama con un tema, tu función recibe los valores del tema
3. Entonces puede evaluar condicionalmente qué color usar basado en el tema

## ¿Por qué es útil?

Este patrón permite:
1. **Estilos dinámicos**: Los estilos pueden cambiar basados en el tema actual
2. **Acceso al contexto**: Puedes acceder a todo el objeto de tema para tomar decisiones complejas
3. **Reactividad**: Cuando el tema cambia, los estilos se recalculan automáticamente

En tu ejemplo actual, estás usando el mismo color (`palette.turquoise[500]`) tanto para el modo claro como oscuro, pero podrías usar diferentes colores según `isLight`:

```javascript
backgroundColor: ({palette, isLight}) =>
  isLight ? palette.turquoise[500] : palette.turquoise[700],
```

Esto crearía un botón más oscuro en modo oscuro, por ejemplo.