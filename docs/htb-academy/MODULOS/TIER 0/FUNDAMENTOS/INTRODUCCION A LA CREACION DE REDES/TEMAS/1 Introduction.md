# Descripción general de la red

Una red permite la `comunicación` de 2 computadoras entre si, la manera en que estas están conectadas se conoce como `topologia` 
Existe una amplia variedad de `topologías` (malla, árbol, estrella), `medios` (Ethernet, fibra, cable coaxial, inalámbrico) y `protocolos` (TCP, UDP, IPX) que se pueden utilizar para facilitar la red.

## Preguntas
1. ¿Por qué la red de impresoras se comunica con los servidores a través de HTTP?
2. ¿Por qué la red de impresoras se comunica con Internet?
3.  ¿Por qué un escaneo de puerto se originó en la red de impresoras?
## La hora del cuento: un descuido de un **pentester**

## Información Básica
Veamos el siguiente diagrama de alto nivel de cómo podría funcionar una configuración de trabajo desde casa.

![[Pasted image 20241104141911.png]]
- `URL` Localizador uniforme de recursos (`Uniform Resource Locator`)
- `FQDN` Nombre de dominio completamente calificado (`Fully Qualified Domain Name`)
- La diferencia entre URL y FQDN es que:
	-  un FQDN (www.hackthebox.eu) solo especifica la dirección del "edificio" y
	- una URL (https://www.hackthebox.eu/example?floor=2&office=dev&employee=17) también especifica el "piso", la "oficina", el "buzón" y el "empleado" correspondiente a quien está destinado el paquete.
## Historia divertida
Durante la pandemia de COVID, me asignaron la tarea de realizar una prueba de penetración física en distintos estados, y mi estado estaba bajo una orden de quedarse en casa. La empresa a la que estaba haciendo la prueba tenía un personal mínimo en la oficina. Decidí comprar una impresora costosa y la exploté para ponerle un shell inverso, de modo que cuando se conectara a la red, me enviara un shell (acceso remoto). Luego envié la impresora a la empresa y envié un correo electrónico de phishing agradeciendo al personal por venir y explicando que la impresora debería permitirles imprimir o escanear cosas más rápidamente si quieren llevarse algunas cosas a casa para trabajar desde casa durante unos días. La impresora se conectó casi al instante, ¡y la computadora del administrador de su dominio tuvo la amabilidad de enviarle sus credenciales a la impresora!

Si el cliente hubiera diseñado una red segura, este ataque probablemente no hubiera sido posible por muchas razones:
- La impresora no debería haber podido comunicarse con Internet.
- La estación de trabajo no debería haber podido comunicarse con la impresora a través del puerto 445
- La impresora no debería poder iniciar conexiones con estaciones de trabajo. En algunos casos, las combinaciones de impresora y escáner deberían poder comunicarse con un servidor de correo para enviar por correo electrónico documentos escaneados.
- 