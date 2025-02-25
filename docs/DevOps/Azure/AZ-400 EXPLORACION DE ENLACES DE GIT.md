# Introducción a los enlaces de Git

Completado100 XP

- 3 minutos

La entrega continua exige un nivel considerable de automatización. No se puede entregar de forma continua si no se tiene un código base de calidad. Aquí es donde Git resulta tan útil.

Permite automatizar la mayoría de las comprobaciones en el código base. Antes de confirmar el código en el repositorio local, olvídese del remoto.

## Enlaces de Git

Los enlaces de Git son un mecanismo que permite que el código se ejecute antes o después de determinados eventos del ciclo de vida de Git.

Por ejemplo, se podría enlazar al evento commit-msg para validar que la estructura del mensaje de confirmación sigue el formato recomendado.

Los enlaces pueden ser cualquier código ejecutable, incluido shell, PowerShell, Python u otros scripts. O bien pueden ser un ejecutable binario. Todo vale.

Los únicos criterios son que los enlaces deben almacenarse en la carpeta .git/hooks de la raíz del repositorio. Además, deben tener un nombre que coincida con los eventos relacionados (Git 2.x):

- applypatch-msg
- pre-applypatch
- post-applypatch
- pre-commit
- prepare-commit-msg
- commit-msg
- post-commit
- pre-rebase
- post-checkout
- post-merge
- pre-receive
- update
- post-receive
- post-update
- pre-auto-gc
- post-rewrite
- pre-push

## Casos de uso prácticos del empleo de enlaces de Git

Dado que los enlaces de Git ejecutan los scripts en el tipo de evento específico en el que se les llama, puede hacer con ellos prácticamente lo que quiera.

Algunos ejemplos de dónde se pueden usar enlaces para aplicar directivas, garantizar la coherencia y controlar el entorno:

- Aplicación de condiciones previas para la combinación
- Comprobación de la asociación de identificadores de elementos de trabajo en el mensaje de confirmación
- Prevención de que usted mismo y el equipo confirmen código defectuoso
- Envío de notificaciones al salón de chat del equipo (Teams, Slack, HipChat)


---

# Implementación de enlaces de Git

Completado100 XP

- 4 minutos

La priorización de la calidad del código en el proceso de desarrollo debe comenzar con el desarrollo de código local. Es importante identificar las oportunidades de esta práctica incluso antes de iniciar solicitudes de incorporación de cambios para detectar y corregir posibles problemas de calidad del código.

Los enlaces de Git ofrecen una gran oportunidad. Sirven como mecanismo para ejecutar scripts personalizados en respuesta a eventos significativos dentro del ciclo de vida de Git, como confirmaciones, combinaciones e inserciones. Los scripts, ubicados en el directorio .git\hooks del repositorio, proporcionan una flexibilidad prácticamente ilimitada en la automatización de las tareas de desarrollo de software y la aplicación de estándares de desarrollo.  

## Implementación de enlaces de Git

Vamos a empezar por explorar los enlaces de Git del lado cliente. Navegue al directorio .git\hooks del repositorio: encontrará muchos archivos con la extensión `sample`. Esta extensión no solo indica su propósito, sino que también impide que se ejecuten de forma eficaz. Los nombres de archivo designan las acciones de Git que desencadenan su ejecución una vez que se quita la extensión `sample`.  

![Captura de pantalla de los archivos de enlace de Git para la automatización.](https://learn.microsoft.com/es-es/training/wwl-azure/explore-git-hooks/media/git-hook-files-8bce9eb8.png)

Cambie el nombre del archivo `sample` confirmación previa a la confirmación previa. Como indica el nombre del archivo, el script que contiene se ejecutará cada vez que invoque la acción de confirmación de Git. La confirmación solo sigue si el script de confirmación previa se cierra con el valor devuelto 0.

Sin embargo, es importante tener en cuenta que, de forma predeterminada, esto no funcionará según lo previsto en ninguno de los sistemas operativos Windows. El motivo habitual de este comportamiento es la primera línea del script:  

BashCopiar

```
#!/bin/sh
```

En sistemas operativos Linux, #! el prefijo indica al cargador de programas que el resto del archivo contiene un script que se va a interpretar y /bin/sh es la ruta de acceso completa al intérprete que se debe usar.

Aunque Git para Windows admite comandos de Bash y scripts de shell, no sigue la misma convención al designar rutas de acceso del sistema de archivos. En su lugar, debe proporcionar la ruta de acceso completa al archivo sh.exe, empezando por la letra de unidad.

Sin embargo, hay una advertencia adicional, que resulta del hecho de que Git para Windows se instala de forma predeterminada en el directorio C:\Archivos de programa. Dado que este directorio contiene un espacio en su nombre, la ruta de acceso resultante al archivo sh.exe se interpretaría como dos rutas de acceso independientes, lo que provocaría un error. Para evitarlo, es necesario agregar una sola barra diagonal inversa (\) delante del espacio para servir como carácter de escape. De hecho, al usar la versión de 64 bits de Git para Windows, la primera línea del script debe tener el siguiente formato:

BashCopiar

```bash
#!C:/Program\ Files/Git/usr/bin/sh.exe
```

## Cómo hacerlo

¿Cómo puede usar la funcionalidad recién detectada de scripts de confirmación previa de Git? ¿Cómo impedirle filtrar accidentalmente secretos a GitHub?

Vamos a usar el enlace de Git para examinar el código que se confirma en el repositorio local para ver palabras clave específicas. Reemplace el contenido del archivo de shell de confirmación previa por el código siguiente:

BashCopiar

```bash
#!C:/Program\ Files/Git/usr/bin/sh.exe
matches=$(git diff-index --patch HEAD | grep '^+' | grep -Pi 'password|secret')
if [ ! -z "$matches" ]
then
  cat <<\EOT
Error: Words from the blocked list were present in the diff:
EOT
echo $matches
exit 1
fi
```

Este ejemplo está diseñado para ilustrar el concepto en lugar de una solución completa, por lo que la lista de palabras clave es intencionadamente trivial. Mediante el uso de expresiones regulares, puede ampliar significativamente el ámbito y la flexibilidad. También tiene la opción de hacer referencia a un archivo externo, lo que simplificaría considerablemente el mantenimiento continuo.

## Cómo funciona

Una vez invocado, el script de enlace previo a la confirmación usa los comandos diff y grep de Git para identificar palabras clave o patrones dentro de los cambios incrementales en el código que se confirma. Si se detectan coincidencias, el script genera un mensaje de error e impide que se produzca la confirmación.

## Hay más:

Otros casos de uso comunes de scripts de enlace previo a la confirmación incluyen el formato de código, la linting o la ejecución de pruebas personalizadas para asegurarse de que la confirmación cumple los estándares del proyecto. Prepare-commit-msg se ejecuta antes de iniciar el editor de mensajes de confirmación. Permite la generación dinámica de mensajes de confirmación con el fin de aplicar convenciones de nomenclatura, como el uso de prefijos designados (por ejemplo, proeza: para características o corrección: para correcciones de errores).

Por ejemplo, el siguiente script prepare-commit-msg antepone automáticamente el nombre de la rama actual al mensaje de confirmación al crear una nueva confirmación. Modifica el archivo de mensaje de confirmación ($1) agregando el nombre de la rama seguido de dos puntos y espacio al principio del archivo.

BashCopiar

```bash
#!C:/Program\ Files/Git/usr/bin/sh.exe
# Get the current branch name
branch_name=$(git branch --show-current)
# Check if the commit message file exists
if [[ -f "$1" ]]; then
  # Prepend the branch name to the commit message
  sed -i "1s/^/$branch_name: /" "$1"
fi
```

Los scripts posteriores a la confirmación se ejecutan después de que se complete una confirmación. Se puede usar para desencadenar notificaciones o generar documentación.

Por ejemplo, el siguiente script envía una notificación por correo electrónico a un destinatario designado después de cada confirmación. El script se puede personalizar modificando la dirección de correo electrónico del destinatario, el servidor SMTP y el asunto y el cuerpo del correo electrónico. Además, es posible que tenga que configurar el sistema para enviar correos electrónicos mediante el cmdlet de PowerShell Send-MailMessage o usar un método diferente para enviar notificaciones, en función del entorno y los requisitos.

BashCopiar

```bash
#!C:/Program\ Files/Git/usr/bin/sh.exe
# Set the recipient email address
$recipient="your@email.com"
# Set the subject of the email
$subject="Git Commit Notification"
# Set the body of the email
$body="A new commit has been made to the repository."
# Send the email notification
Send-MailMessage -To $recipient -Subject $subject -Body $body -SmtpServer "your.smtp.server"
```

Cabe destacar que la carpeta .git\hooks del repositorio no se confirma en el control de código fuente. Es posible que se pregunte si hay una manera de compartir los scripts que desarrolló con otro miembro del equipo de desarrollo. La buena noticia es que, a partir de la versión 2.9 de Git, puede asignar enlaces de Git a una carpeta que se pueda confirmar en el control de código fuente. Para ello, actualice la configuración global del repositorio de Git:

BashCopiar

```bash
Git config --global core.hooksPath '~/.githooks'
```

Si alguna vez necesita sobrescribir los enlaces de Git que ha configurado en el lado cliente, puede hacerlo mediante el modificador no-verify:

BashCopiar

```bash
Git commit --no-verify
```

### Enlaces del lado servidor

Aunque los enlaces de Git del lado cliente ofrecen funcionalidades sólidas para mejorar el flujo de trabajo de desarrollo, Azure Repos también proporciona enlaces del lado servidor para aumentar aún más el proceso de desarrollo, incluida la compatibilidad con la creación de solicitudes de incorporación de cambios. Para obtener más información, consulte la referencia Azure Repos[Eventos de enlace de servicio](https://learn.microsoft.com/es-es/azure/devops/service-hooks/events).