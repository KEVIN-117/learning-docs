Los **Conventional Commits** son un estándar para escribir mensajes de confirmación (commits) en un proyecto. Este formato sigue una estructura clara que mejora la legibilidad y automatización en proyectos, especialmente en el desarrollo colaborativo y la integración continua. La convención es utilizada comúnmente con herramientas como Semantic Release y ayuda a generar automáticamente versiones, changelogs y más.

### Estructura de un mensaje de commit convencional

```plaintext
<tipo>(<ámbito>): <descripción breve>

[opcional cuerpo del mensaje]

[opcional notas de pie de página]
```

#### Componentes clave:

1. **Tipo**: Describe la categoría del cambio que introduces. Ejemplos comunes:
    
    - `feat`: Nueva funcionalidad.
    - `fix`: Corrección de errores.
    - `docs`: Cambios en documentación.
    - `style`: Cambios que no afectan el significado del código (formato, espacios, comas, etc.).
    - `refactor`: Reestructuración de código sin cambios funcionales.
    - `test`: Adición o modificación de pruebas.
    - `chore`: Tareas auxiliares (actualización de dependencias, cambios en scripts de configuración).
2. **Ámbito (opcional)**: Área del proyecto afectada. Ejemplo: `auth`, `API`, `ui`.
    
3. **Descripción breve**: Resumen claro y conciso del cambio (máximo 72 caracteres).
    
4. **Cuerpo (opcional)**: Detalles adicionales sobre el cambio. Explica **qué**, **por qué** y **cómo**.
    
5. **Notas de pie de página (opcional)**: Información relevante, como cerrar tickets o referencias. Ejemplo: `Closes #123`.
    

---

### Ejemplos:

**Commit para una nueva funcionalidad:**

```plaintext
feat(auth): agregar autenticación con Google
```

**Commit para corrección de errores:**

```plaintext
fix(ui): corregir error en la validación del formulario
```

**Commit con cuerpo y notas:**

```plaintext
fix(api): solucionar error al procesar datos vacíos

Se agregó una condición para verificar si el objeto `data` está vacío antes de procesarlo, previniendo errores en la ejecución.

Closes #456
```

### Ventajas:

- Facilita la generación de changelogs automáticos.
- Ayuda a rastrear el propósito de los cambios.
- Mejora la colaboración y comunicación en equipos.

### Recomendaciones:

- Utiliza herramientas como [Commitizen](https://commitizen-tools.github.io/commitizen/) o [Conventional Commit Linter](https://github.com/conventional-changelog/commitlint) para mantener consistencia en los commits.


---

varios cambios para agregar campos de entrada de autenticación y funcionalidad asociada al proyecto. Los cambios más importantes incluyen agregar el componente `AuthInputFields`, crear ganchos personalizados para la visibilidad de contraseñas y agregar íconos SVG para los campos de correo electrónico y contraseña

### Nuevo componente y Hooks:

* [`src/components/AuthInputFields/index.jsx`](diffhunk://#diff-27ca04603d6989ef8066ed7caedf0b1cec7402a0d20987c4a014ded7f4e2b836R1-R86): Se agregó el componente `AuthInputFields` para manejar los campos de entrada de correo electrónico y contraseña con interruptor de visibilidad y botón de inicio de sesión. * [`src/components/AuthInputFields/hooks/useHandlerPasswordVisibility.js`](diffhunk://#diff-a3de8a4e02a0bdb6252a8b2d4e503026c6f6385602fd88e08ef12719b512ee83R1-R15): Se creó un hook personalizado `useHandlerPasswordVisibility` para administrar la visibilidad del campo de entrada de contraseña.

### Iconos SVG:

* [`src/components/AuthInputFields/icons/email.jsx`](diffhunk://#diff-fb88e1fc402c20993a7ad465bc28790e6e475c5cfb455b8bae595d3483048b0aR1-R25): Se agregó el componente `SvgEmail` para el ícono del campo de entrada de correo electrónico. * [`src/components/AuthInputFields/icons/password.jsx`](diffhunk://#diff-48603021f036dd9fa623916894941bb3474edee6dd1303c6ad57c6515ea20288R1-R102): Se agregaron los componentes `SvgPassword`, `SvgHide` y `SvgShow` para los íconos del campo de ingreso de contraseña.

### Integración y dependencias:

* [`package.json`](diffhunk://#diff-7ae45ad102eab3b6d7e7896acd08c427a9b25b346470d7bc6507b6481575d519L15-R16): Se agregó la dependencia `react-native-svg` para admitir íconos SVG.


### Exportaciones:

* [`src/components/AuthInputFields/index.js`](diffhunk://#diff-80a6b978a99922debc6afa82868328e52353cda47758a984bae586123b165546R1-R3): Se exportaron `AuthInputFields`, íconos SVG y un enlace personalizado para usar en otras partes de la aplicación. * [`src/components/AuthInputFields/icons/index.js`](diffhunk://#diff-e814cddbfafdf56f7f475996dc18e2de3c0dcca5aacda3768e46087c8485c33cR1-R2): Se exportaron íconos SVG desde el directorio `icons`.