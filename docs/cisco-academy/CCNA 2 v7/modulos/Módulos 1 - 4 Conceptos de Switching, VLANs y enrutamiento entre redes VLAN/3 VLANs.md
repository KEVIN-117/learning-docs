## Introducción

3.0.1

## ¿Por qué debería tomar este módulo?

¡Bienvenido a las VLAN!

Imagina que estás a cargo de una conferencia muy grande. Hay personas de todas partes que comparten un interés común y algunas que también tienen una experiencia especial. Imagínese si cada experto que quisiera presentar su información a un público más pequeño tuviera que hacerlo en la misma sala grande con todos los demás expertos y sus audiencias más pequeñas. Nadie podría oír nada. Tendrías que encontrar salas separadas para todos los expertos y sus audiencias más pequeñas. La LAN virtual (VLAN) hace algo similar en una red. Las VLAN se crean en la Capa 2 para reducir o eliminar el tráfico de difusión. Las VLAN son la forma en que divide la red en redes más pequeñas, de modo que los dispositivos y las personas dentro de una sola VLAN se comunican entre sí y no tienen que administrar el tráfico de otras redes. El administrador de red puede organizar las VLAN por ubicación, quién las está utilizando, el tipo de dispositivo o cualquier categoría que se necesite. Sabes que quieres aprender a hacer esto, ¡así que no esperes!

3.0.2

## ¿Qué aprenderé en este módulo?

**Título del módulo**: VLANs

**Objetivos del módulo**: Implemente VLAN y enlaces troncales en una red conmutada.

| **Título del tema**                             | **Objetivo del tema**                                                                                   |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Descripción general de las VLAN**             | Explique la finalidad de las VLAN en una red conmutada.                                                 |
| **Redes VLAN en un entorno conmutado múltiple** | Explique cómo un switch reenvía tramas según la configuración de VLAN en un entorno conmutado múltiple. |
| **Configuración de VLAN**                       | Configure un puerto para switch que se asignará a una VLAN según los requisitos.                        |
| **Enlaces troncales de la VLAN**                | Configure un puerto de enlace troncal en un switch LAN.                                                 |
| **Protocolo de enlace troncal dinámico**        | Configure el protocolo de enlace troncal dinámico (DTP).                                                |

---

# Descripción general de las VLAN

3.1.1

## Definiciones de VLAN

Por supuesto, organizar su red en redes más pequeñas no es tan simple como separar tornillos y ponerlos en frascos. Pero hará que su red sea más fácil de administrar. Dentro de una red conmutada, las VLAN proporcionan la segmentación y la flexibilidad organizativa. Un grupo de dispositivos dentro de una VLAN se comunica como si cada dispositivo estuviera conectados al mismo cable. Las VLAN se basan en conexiones lógicas, en lugar de conexiones físicas.

Como se muestra en la figura, las VLAN en una red conmutada permiten a los usuarios de varios departamentos (por ejemplo, TI, recursos humanos y ventas) conectarse a la misma red, independientemente del switch físico que se esté utilizando o de la ubicación en una LAN del campus.

![[Pasted image 20241213001506.png]]

Las VLAN permiten que el administrador divida las redes en segmentos según factores como la función, el equipo del proyecto o la aplicación, sin tener en cuenta la ubicación física del usuario o del dispositivo. Cada VLAN se considera una red lógica diferente. Los dispositivos dentro de una VLAN funcionan como si estuvieran en su propia red independiente, aunque compartan una misma infraestructura con otras VLAN. Cualquier puerto de switch puede pertenecer a una VLAN.

Los paquetes de unidifusión, difusión y multidifusión se reenvían solamente a terminales dentro de la VLAN donde los paquetes son de origen. Los paquetes destinados a dispositivos que no pertenecen a la VLAN se deben reenviar a través de un dispositivo que admita el routing.

Varias subredes IP pueden existir en una red conmutada, sin el uso de varias VLAN. Sin embargo, los dispositivos estarán en el mismo dominio de difusión de capa 2. Esto significa que todas las difusiones de capa 2, tales como una solicitud de ARP, serán recibidas por todos los dispositivos de la red conmutada, incluso por aquellos que no se quiere que reciban la difusión.

Una VLAN crea un dominio de difusión lógico que puede abarcar varios segmentos LAN físicos. Las VLAN mejoran el rendimiento de la red mediante la división de grandes dominios de difusión en otros más pequeños. Si un dispositivo en una VLAN envía una trama de Ethernet de difusión, todos los dispositivos en la VLAN reciben la trama, pero los dispositivos en otras VLAN no la reciben.

Mediante las VLAN, los administradores de red pueden implementar políticas de acceso y seguridad de acuerdo con a grupos específicos de usuarios. Cada puerto de switch se puede asignar a una sola VLAN (a excepción de un puerto conectado a un teléfono IP o a otro switch).

3.1.2

## Ventajas de un diseño de VLAN

Cada VLAN en una red conmutada corresponde a una red IP. Por lo tanto, el diseño de VLAN debe tener en cuenta la implementación de un esquema de direccionamiento de red jerárquico. El direccionamiento jerárquico de la red significa que los números de red IP se aplican a los segmentos de red o a las VLAN de manera ordenada, lo que permite que la red se tome en cuenta como conjunto. Los bloques de direcciones de red contiguas se reservan para los dispositivos en un área específica de la red y se configuran en estos, como se muestra en la ilustración.

![[Pasted image 20241213001644.png]]

En la tabla se enumeran las ventajas de diseñar una red con VLAN.

|**Ventaja**|**Descripción**|
|---|---|
|Dominios de difusión más pequeños|- Dividir una red en VLAN reduce el número de dispositivos en el broadcast domain.<br>- En la figura, hay seis computadoras en la red, pero solo tres dominios de difusión (es decir, Facultad, Estudiante e Invitado).|
|Seguridad mejorada|- Sólo los usuarios de la misma VLAN pueden comunicarse juntos.<br>- En la figura, el tráfico de red de profesores en la VLAN 10 es completamente separados y protegidos de los usuarios en otras VLAN.|
|Mejora la eficiencia del departamento de IT.|- Las VLAN simplifican la administración de la red porque los usuarios con una red similar se pueden configurar en la misma VLAN.<br>- Las VLAN se pueden nombrar para facilitar su identificación.<br>- En la figura, VLAN 10 fue nombrado «Facultad», VLAN 20 «Estudiante», y VLAN 30 «Invitado. »|
|Reducción de costos|Las VLAN reducen la necesidad de realizar costosas actualizaciones de red y utilizan el ancho de banda existente y enlaces ascendentes de manera más eficiente, lo que resulta en costos Ahorro|
|Mejor rendimiento|Los dominios de difusión más pequeños reducen el tráfico innecesario en la red y mejorar el rendimiento.|
|Administración más simple de proyectos y aplicaciones|- Las VLAN agregan usuarios y dispositivos de red para admitir empresas o necesidades geográficas.<br>- Tener funciones separadas hace que administrar un proyecto o trabajar con un aplicación especializada más fácil; un ejemplo de tal aplicación es una plataforma de desarrollo de e-learning para profesores.|

3.1.3

## Tipos de VLAN

Las VLAN se utilizan por diferentes razones en las redes modernas. Algunos tipos de VLAN se definen según las clases de tráfico. Otros tipos de VLAN se definen según la función específica que cumplen.

Haga clic en cada tipo de VLAN para obtener más información.

### VLAN predeterminada
La VLAN predeterminada para los switches Cisco es la VLAN 1. Por lo tanto, todos los puertos del switch están en VLAN 1 a menos que esté configurado explícitamente para estar en otra VLAN. Todo el tráfico de control de capa 2 se asocia a la VLAN 1 de manera predeterminada.

Entre los datos importantes que hay que recordar acerca de la VLAN 1 se incluyen los siguientes:

- Todos los puertos se asignan a la VLAN 1 de manera predeterminada.
- De manera predeterminada, la VLAN nativa es la VLAN 1.
- De manera predeterminada, la VLAN de administración es la VLAN 1.
- No es posible eliminar ni cambiar el nombre de VLAN 1.

Por ejemplo, en la **show vlan brief** ilustración, todos los puertos están asignados a la VLAN 1 predeterminada. No hay ninguna VLAN nativa asignada explícitamente ni otras VLAN activas; por lo tanto, la VLAN nativa de la red que se diseñó es la VLAN de administración. Esto se considera un riesgo de seguridad.

```js
Switch# show vlan brief 
VLAN Name Status Ports
— — — —
1 default active Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                Gi0/1, Gi0/2
1002 fddi-default act/unsup
1003 token-ring-default act/unsup
1004 fddinet-default act/unsup
1005 trnet-default act/unsup
```

### VLAN de datos

Las VLAN de datos son VLAN configuradas para separar el tráfico generado por el usuario. Las VLAN de datos se usan para dividir la red en grupos de usuarios o dispositivos. Una red moderna tendría muchas VLAN de datos en función de los requisitos organizativos. Tenga en cuenta que no se debe permitir el tráfico de administración de voz y red en las VLAN de datos.

### VLAN nativa
El tráfico de usuario de una VLAN debe etiquetarse con su ID de VLAN cuando se envía a otro switch. Los puertos troncal se utilizan entre conmutadores para admitir la transmisión de tráfico etiquetado. Específicamente, un puerto troncal 802.1Q inserta una etiqueta de 4 bytes en el encabezado de trama Ethernet para identificar la VLAN a la que pertenece la trama.

Es posible que un switch también tenga que enviar tráfico sin etiqueta a través de un enlace troncal. El tráfico sin etiquetas es generado por un switch y también puede provenir de dispositivos heredados. El puerto de enlace troncal 802.1Q coloca el tráfico sin etiquetar en la VLAN nativa. La VLAN nativa en un switch Cisco es VLAN 1 (es decir, VLAN predeterminada).

Se recomienda configurar la VLAN nativa como VLAN sin utilizar, independiente de la VLAN 1 y de otras VLAN. De hecho, es común utilizar una VLAN fija para que funcione como VLAN nativa para todos los puertos de enlace troncal en el dominio conmutado.

### VLAN de administración
Una VLAN de administración es una VLAN de datos configurada específicamente para el tráfico de administración de red, incluyendo SSH, Telnet, HTTPS, HHTP y SNMP. De forma predeterminada, la VLAN 1 se configura como la VLAN de administración en un conmutador de capa 2.

### VLAN de voz
**VLAN de voz**

Se necesita una VLAN separada para admitir la tecnología de voz sobre IP (VoIP). Para el tráfico de VoIP, se necesita lo siguiente:

- Ancho de banda garantizado para asegurar la calidad de la voz
- Prioridad de la transmisión sobre los tipos de tráfico de la red
- Capacidad para ser enrutado en áreas congestionadas de la red
- Una demora inferior a 150 ms a través de la red

Para cumplir estos requerimientos, se debe diseñar la red completa para que admita VoIP.

En la figura, la VLAN 150 se diseña para enviar tráfico de voz. La computadora del estudiante PC5 está conectada al teléfono IP de Cisco y el teléfono está conectado al switch S3. La PC5 está en la VLAN 20 que se utiliza para los datos de los estudiantes.
![[Pasted image 20241213001917.png]]
3.1.4

## Packet Tracer: ¿quién escucha la difusión?

En esta actividad de Packet Tracer, completará los siguientes objetivos:

- Parte 1: Observar el tráfico de broadcast en la implementación de una VLAN
- Parte 2: completar las preguntas de repaso
![[3.1.4-packet-tracer---who-hears-the-broadcast_es-XL.pka]]

3.1.5

## Compruebe su comprensión - Descripción general de las VLAN

Elija la MEJOR repuesta para las siguientes preguntas y compruebe su conocimiento sobre VLANs.

1. ¿Verdadero o falso? Las VLAN mejoran el rendimiento de la red mediante la división de grandes dominios de difusión en otros más pequeños.
    
    Verdadero
    
    Falso
    
2. ¿Verdadero o falso? Las VLAN pueden mejorar la seguridad al aislar los datos confidenciales del resto de la red.
    
    Verdadero
    
    Falso
    
3. ¿Qué tipo de VLAN se asigna a los puertos troncal 802.1Q para transportar tráfico sin etiqueta?
    
    default
    
    Nativa
    
    Datos
    
    Gerencia
    
4. ¿Verdadero o falso? Se recomienda configurar la VLAN nativa como VLAN 1.
    
    Verdadero
    
    Falso
    
5. ¿Cuál es el caso de la VLAN 1? (Elija todas las opciones que correspondan).
    
    Todos los puertos del switch se asignan a la VLAN 1 de manera predeterminada.
    
    De manera predeterminada, la VLAN nativa es la VLAN 1.
    
    De manera predeterminada, la VLAN de administración es la VLAN 1.
    
    No es posible eliminar ni cambiar el nombre de VLAN 1.

---

# Redes VLAN en un entorno conmutado múltiple

3.2.1

## Definición de troncos de VLAN

Las VLAN no serían muy útiles sin los enlaces troncales de VLAN. Los troncos de VLAN permiten que todo el tráfico de VLAN se propague entre conmutadores. Esto permite que los dispositivos conectados a diferentes switches pero en la misma VLAN se comuniquen sin pasar por un router.

Un enlace troncal es un enlace punto a punto entre dos dispositivos de red que lleva más de una VLAN. Un enlace troncal de VLAN amplía las VLAN a través de toda la red. Cisco admite IEEE 802.1Q para coordinar enlaces troncales en las interfaces Fast Ethernet, Gigabit Ethernet y 10-Gigabit Ethernet.

Un enlace troncal no pertenece a una VLAN específica. Es más bien un conducto para las VLAN entre los switches y los routers. También se puede utilizar un enlace troncal entre un dispositivo de red y un servidor u otro dispositivo que cuente con una NIC con capacidad 802.1Q. En los switches Cisco Catalyst, se admiten todas las VLAN en un puerto de enlace troncal de manera predeterminada.

En la ilustración, los enlaces entre los switches S1 y S2, y S1 y S3 se configuraron para transmitir el tráfico proveniente de las VLAN 10, 20, 30 y 99 a través de la red. Esta red no podría funcionar sin los enlaces troncales de VLAN.

![[Pasted image 20241213002156.png]]

3.2.2

## Redes sin VLAN

En condiciones normales de funcionamiento, cuando un switch recibe una trama de difusión en uno de sus puertos, reenvía la trama por todos los demás puertos, excepto el puerto por donde recibió la difusión. En la animación de la figura se configuró toda la red en la misma subred (172.17.40.0/24), y no se configuró ninguna VLAN. Como consecuencia, cuando la computadora del cuerpo docente (PC1) envía una trama de difusión, el switch S2 envía dicha trama de difusión por todos sus puertos. Finalmente, toda la red recibe la difusión porque la red es un dominio de difusión.
![[Pasted image 20241213002224.png]]
3.2.3

## Red con VLAN

Haga clic en Reproducir en la animación para ver que la misma red se ha segmentado utilizando dos VLAN. Los dispositivos del cuerpo docente se asignaron a la VLAN 10, y los dispositivos de los estudiantes se asignaron a la VLAN 20. Cuando se envía una trama de difusión desde la computadora del cuerpo docente, la PC1, al switch S2, el switch reenvía esa trama de difusión solo a los puertos de switch configurados para admitir la VLAN 10.

![[Pasted image 20241213002304.png]]

Los puertos que componen la conexión entre los switches S2 y S1 (puertos F0/1), y entre el S1 y el S3 (puertos F0/3) son enlaces troncales y se configuraron para admitir todas las VLAN en la red.

Cuando el S1 recibe la trama de difusión en el puerto F0/1, reenvía la trama de difusión por el único puerto configurado para admitir la VLAN 10, que es el puerto F0/3. Cuando el S3 recibe la trama de difusión en el puerto F0/3, reenvía la trama de difusión por el único puerto configurado para admitir la VLAN 10, que es el puerto F0/11. La trama de difusión llega a la única otra computadora de la red configurada en la VLAN 10, que es la computadora PC4 del cuerpo docente.

Cuando se implementan las VLAN en un switch, la transmisión del tráfico de unidifusión, multidifusión y difusión desde un host en una VLAN en particular se limita a los dispositivos presentes en esa VLAN.

3.2.4

## Identificación de VLAN con etiqueta

El encabezado de trama Ethernet estándar no contiene información sobre la VLAN a la que pertenece la trama. Por lo tanto, cuando las tramas de Ethernet se ubican en un enlace troncal, se necesita agregar información sobre las VLAN a las que pertenecen. Este proceso, denominado “etiquetado”, se logra mediante el uso del encabezado IEEE 802.1Q, especificado en el estándar IEEE 802.1Q. El encabezado 802.1Q incluye una etiqueta de 4 bytes insertada en el encabezado de la trama de Ethernet original que especifica la VLAN a la que pertenece la trama.

Cuando el switch recibe una trama en un puerto configurado en modo de acceso y asignado a una VLAN, el switch coloca una etiqueta VLAN en el encabezado de la trama, vuelve a calcular la Secuencia de Verificación de Tramas (FCS) y envía la trama etiquetada por un puerto de enlace troncal.

**Detalles del campo VLAN Tag**

Como se muestra en la figura el campo de etiqueta de la VLAN consta de un campo de tipo, un campo de prioridad, un campo de identificador de formato canónico y un campo de ID de la VLAN:

- **Tipo** - Un valor de 2 bytes denominado “ID de Protocolo de Etiqueta” (TPID). Para Ethernet, este valor se establece en 0x8100 hexadecimal.
- **Prioridad de usuario** - Es un valor de 3 bits que admite la implementación de nivel o de servicio.
- **Identificador de Formato Canónico (CFI)** - Es un identificador de 1 bit que habilita las tramas Token Ring que se van a transportar a través de los enlaces Ethernet.
- **VLAN ID (VID)** - Es un número de identificación de VLAN de 12 bits que admite hasta 4096 ID de VLAN.

Una vez que el switch introduce los campos tipo y de información de control de etiquetas, vuelve a calcular los valores de la FCS e inserta la nueva FCS en la trama.

![[Pasted image 20241213002349.png]]
3.2.5

## VLAN nativas y etiquetado de 802.1Q

El estándar IEEE 802.1Q especifica una VLAN nativa para los enlaces troncal, que por defecto es VLAN 1. Cuando un marco sin etiqueta llega a un puerto troncal, se asigna a la VLAN nativa. Las tramas de administración que se envían entre conmutadores es un ejemplo de tráfico que normalmente no se etiqueta. Si el vínculo entre dos switches es un tronco, el switch envía el tráfico sin etiqueta en la VLAN nativa.

**Marcos etiquetados en la VLAN nativa**

Algunos dispositivos que admiten los enlaces troncales agregan una etiqueta VLAN al tráfico de las VLAN nativas. El tráfico de control que se envía por la VLAN nativa no se debe etiquetar. Si un puerto de enlace troncal 802.1Q recibe una trama etiquetada con la misma ID de VLAN que la VLAN nativa, descarta la trama. Por consiguiente, al configurar un puerto de un switch Cisco, configure los dispositivos de modo que no envíen tramas etiquetadas por la VLAN nativa. Los dispositivos de otros proveedores que admiten tramas etiquetadas en la VLAN nativa incluyen: teléfonos IP, servidores, routers y switches que no pertenecen a Cisco.

**Marcos sin etiquetas en la VLAN nativa**

Cuando un puerto de enlace troncal de un switch Cisco recibe tramas sin etiquetar (poco usuales en las redes bien diseñadas), envía esas tramas a la VLAN nativa. Si no hay dispositivos asociados a la VLAN nativa (lo que es usual) y no existen otros puertos de enlace troncal (es usual), se descarta la trama. La VLAN nativa predeterminada es la VLAN 1. Al configurar un puerto de enlace troncal 802.1Q, se asigna el valor de la ID de VLAN nativa a la ID de VLAN de puerto (PVID) predeterminada. Todo el tráfico sin etiquetar entrante o saliente del puerto 802.1Q se reenvía según el valor de la PVID. Por ejemplo, si se configura la VLAN 99 como VLAN nativa, la PVID es 99, y todo el tráfico sin etiquetar se reenvía a la VLAN 99. Si no se volvió a configurar la VLAN nativa, el valor de la PVID se establece en VLAN 1.

En la ilustración, la PC1 está conectada a un enlace troncal 802.1Q mediante un hub.

![[Pasted image 20241213002418.png]]

La PC1 envía el tráfico sin etiquetar, que los switches asocian a la VLAN nativa configurada en los puertos de enlace troncal y que reenvían según corresponda. El tráfico etiquetado del enlace troncal que recibe la PC1 se descarta. Esta situación refleja un diseño de red deficiente por varios motivos: utiliza un hub, tiene un host conectado a un enlace troncal y esto implica que los switches tengan puertos de acceso asignados a la VLAN nativa. También ilustra la motivación de la especificación IEEE 802.1Q para que las VLAN nativas sean un medio de manejo de entornos antiguos.

3.2.6

## Etiquetado de VLAN de voz

Se necesita una red VLAN de voz separada para admitir VoIP. Esto permite aplicar políticas de calidad de servicio (QoS) y seguridad al tráfico de voz.

Un teléfono IP de Cisco se conecta directamente a un puerto del switch. Un host IP puede conectarse al teléfono IP para obtener conectividad de red también. Un puerto de acceso que conecta un teléfono IP de Cisco puede configurarse para utilizar dos VLAN separadas: Una VLAN es para el tráfico de voz y la otra es una VLAN de datos para admitir el tráfico de host. El enlace entre el switch y el teléfono IP funciona como un enlace troncal para transportar tanto el tráfico de la VLAN de voz como el tráfico de la VLAN de datos.

Específicamente, el teléfono IP Cisco contiene un switch 10/100 de tres puertos integrado. Los puertos proporcionan conexiones dedicadas para estos dispositivos:

- El puerto 1 se conecta al switch o a otro dispositivo VoIP.
- El puerto 2 es una interfaz interna 10/100 que envía el tráfico del teléfono IP.
- El puerto 3 (puerto de acceso) se conecta a una PC u otro dispositivo.

El puerto de acceso del switch envía paquetes CDP que indican al teléfono IP conectado que envíe tráfico de voz de una de las tres maneras. El método utilizado varía según el tipo de tráfico:

- El tráfico VLAN de voz debe etiquetarse con un valor de prioridad CoS de Capa 2 adecuado.
- En una VLAN de acceso con una etiqueta de valor de prioridad de CoS de capa 2
- En una VLAN de acceso sin etiqueta (sin valor de prioridad de CoS de capa 2)

En la figura, la computadora del estudiante PC5 está conectada a un teléfono IP de Cisco, y el teléfono está conectado al switch S3. La VLAN 150 está diseñada para transportar tráfico de voz, mientras que la PC5 está en la VLAN 20, que se usa para los datos de los estudiantes.

![[Pasted image 20241213002500.png]]

3.2.7
## Packet Tracer: investigación de la implementación de una VLAN

En esta actividad, observará el modo en que los switches reenvían el tráfico de difusión cuando se configuran las VLAN y cuando no se configuran las VLAN.

![[3.2.8-packet-tracer---investigate-a-vlan-implementation_es-XL.pka]]


3.2.9

## Compruebe su comprensión - VLAN en un entorno de multiswitch

Esta actividad Comprobar comprensión utiliza un escenario diferente para cada pregunta.

Haga clic en cada botón para el escenario de VLAN que corresponda a la pregunta.

Pregunta 1 Topología
![[Pasted image 20241213002611.png]]
1. Consulte la ilustración **Pregunta 1 Topología**. La PC1 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC2
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
2. Consulte la ilustración **Pregunta 2 Topología**. La PC2 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP? (Elija todas las opciones que correspondan).
    
    PC1
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
3. Consulte la ilustración **Pregunta 3 Topología**. La PC3 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC1
    
    PC2
    
    PC4
    
    PC5
    
    PC6


Pregunta 2 Topología
![[Pasted image 20241213002656.png]]
1. Consulte la ilustración **Pregunta 1 Topología**. La PC1 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC2
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
2. Consulte la ilustración **Pregunta 2 Topología**. La PC2 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP? (Elija todas las opciones que correspondan).
    
    PC1
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
3. Consulte la ilustración **Pregunta 3 Topología**. La PC3 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC1
    
    PC2
    
    PC4
    
    PC5
    
    PC6

Pregunta 3 Topología
![[Pasted image 20241213002725.png]]
1. Consulte la ilustración **Pregunta 1 Topología**. La PC1 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC2
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
2. Consulte la ilustración **Pregunta 2 Topología**. La PC2 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP? (Elija todas las opciones que correspondan).
    
    PC1
    
    PC3
    
    PC4
    
    PC5
    
    PC6
    
3. Consulte la ilustración **Pregunta 3 Topología**. La PC3 envía una trama de difusión ARP. ¿Qué PC recibirá el marco de difusión ARP?
    
    PC1
    
    PC2
    
    PC4
    
    PC5
    
    PC6

---


# Configuración de VLAN

3.3.1

## Rangos de VLAN en los switches Catalyst

Crear VLAN, como la mayoría de los demás aspectos de la red, es cuestión de introducir los comandos apropiados. En este tema se detalla cómo configurar y verificar diferentes tipos de VLAN.

Los distintos switches Cisco Catalyst admiten diversas cantidades de VLAN. La cantidad de VLAN que admiten es suficiente para satisfacer las necesidades de la mayoría de las organizaciones. Por ejemplo, los switches de las series Catalyst 2960 y 3560 admiten más de 4000 VLAN. Las VLAN de rango normal en estos switches se numeran del 1 al 1005, y las VLAN de rango extendido se numeran del 1006 al 4094. En la ilustración, se muestran las VLAN disponibles en un switch Catalyst 2960 que ejecuta IOS de Cisco, versión 15.x.

```js
Switch# show vlan brief
VLAN Name              Status   Ports
---- ----------------- -------  --------------------
1    default           active   Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                Gi0/1, Gi0/2
1002 fddi-default                     act/unsup
1003 token-ring-default               act/unsup
1004 fddinet-default                  act/unsup
1005 trnet-default                    act/unsup
```

**Rango Normal VLANs**

Las siguientes son las características de las VLAN de rango normal:

- Se utiliza en redes de pequeños y medianos negocios y empresas.
- Se identifica mediante una ID de VLAN entre 1 y 1005.
- Las ID de 1002 a 1005 se reservan para las VLAN de Token Ring e interfaz de datos distribuidos por fibra óptica (FDDI).
- Las ID 1 y 1002 a 1005 se crean automáticamente y no se pueden eliminar.
- Las configuraciones se almacenan en un archivo de base de datos de VLAN llamado vlan.dat, que se guarda en la memoria flash.
- Cuando se configura, el protocolo de enlace troncal VLAN (VTP) ayuda a sincronizar la base de datos VLAN entre conmutadores.

**Rango Extendido VLANs**

Las siguientes son las características de las VLAN de rango extendido:

Los proveedores de servicios los* utilizan para dar servicio a varios clientes y por las empresas globales lo suficientemente grandes como para necesitar identificadores de VLAN de rango extendido.

- Se identifican mediante una ID de VLAN entre 1006 y 4094.
- Las configuraciones se guardan en el archivo de configuración en ejecución.
- Admiten menos características de VLAN que las VLAN de rango normal.
- Requiere la configuración del modo transparente VTP para admitir VLAN de rango extendido.

**Nota**: Nota: la cantidad máxima de VLAN disponibles en los switches Catalyst es 4096, ya que el campo ID de VLAN tiene 12 bits en el encabezado IEEE 802.1Q.

3.3.2

## Comandos de creación de VLAN

Al configurar redes VLAN de rango normal, los detalles de configuración se almacenan en la memoria flash del switch en un archivo denominado vlan.dat. La memoria flash es persistente y no requiere el **copy running-config startup-config** comando. Sin embargo, debido a que en los switches Cisco se suelen configurar otros detalles al mismo tiempo que se crean las VLAN, es aconsejable guardar los cambios a la configuración en ejecución en la configuración de inicio.

En la figura 1, se muestra la sintaxis del comando de IOS de Cisco que se utiliza para agregar una VLAN a un switch y asignarle un nombre. Se recomienda asignarle un nombre a cada VLAN en la configuración de un switch.

|**Tarea**|**Comando de IOS**|
|---|---|
|Ingresa al modo de configuración global.|Switch# **configure terminal**|
|Cree una VLAN con un número de ID válido.|Switch(config)# **vlan** _vlan-id_|
|Especificar un nombre único para identificar la VLAN.|Switch(config-vlan)# **name** _vlan-name_|
|Vuelva al modo EXEC privilegiado.|Switch(config-vlan)# **end**|

3.3.3

## Ejemplo de creación de VLAN

En el ejemplo de topología, la computadora del estudiante (PC2) todavía no se asoció a ninguna VLAN, pero tiene la dirección IP 172.17.20.22, que pertenece a la VLAN 20.

![[Pasted image 20241213003437.png]]

En la figura, se muestra cómo se configura la VLAN para estudiantes (VLAN 20) en el switch S1.

```js
S1# configure terminal
S1(config)# vlan 20
S1(config-vlan)# name student
S1(config-vlan)# end
```

**Nota**: Además de introducir una única ID de VLAN, se puede introducir una serie de ID de VLAN separadas por comas o un rango de ID de VLAN separado por guiones usando el **vlan** comando _vlan-id_ . Por ejemplo, al introducir el comando de configuración **vlan 100,102,105-107** global se crearían las VLAN 100, 102, 105, 106 y 107.

3.3.4

## Comandos de asignación de puertos VLAN

Después de crear una VLAN, el siguiente paso es asignar puertos a la VLAN.

En la figura se muestra la sintaxis para definir un puerto como puerto de acceso y asignarlo a una VLAN. EL **switchport mode access** comando es optativo, pero se aconseja como práctica recomendada de seguridad. Con este comando, la interfaz cambia al modo de acceso permanente.

|**Tarea**|**Comando de IOS**|
|---|---|
|Ingrese al modo de configuración global.|Switch# **configure terminal**|
|Ingrese el modo de configuración de interfaz.|Switch(config)# **interface** _interface-id_|
|Establezca el puerto en modo de acceso.|Switch(config-if)# **switchport mode access**|
|Asigne el puerto a una VLAN.|Switch(config-if)# **switchport access vlan** _vlan-id_|
|Vuelva al modo EXEC privilegiado.|Switch(config-if)# **end**|

**Nota**: Use el **interface range** comando para configurar simultáneamente varias interfaces

3.3.5

## Ejemplo de asignación de puerto VLAN

En la figura, el puerto F0/6 en el conmutador S1 se configura como un puerto de acceso y se asigna a la VLAN 20. Cualquier dispositivo conectado a ese puerto está asociado con la VLAN 20. Por lo tanto, en nuestro ejemplo, PC2 está en la VLAN 20.

![[Pasted image 20241213003539.png]]

El ejemplo muestra la configuración de S1 para asignar F0/6 a VLAN 20.

```js
S1# configure terminal
S1(config)# interface fa0/6
S1(config-if)# switchport mode access
S1(config-if)# switchport access vlan 20
S1(config-if)# end
```

Las VLAN se configuran en el puerto del switch y no en el terminal. La PC2 se configura con una dirección IPv4 y una máscara de subred asociadas a la VLAN, que se configura en el puerto de switch. En este ejemplo, es la VLAN 20. Cuando se configura la VLAN 20 en otros switches, el administrador de red debe configurar las otras computadoras de alumnos para que estén en la misma subred que la PC2 (172.17.20.0/24).

3.3.6

## VLAN de voz, datos

Un puerto de acceso puede pertenecer a sólo una VLAN a la vez. Sin embargo, un puerto también se puede asociar a una VLAN de voz. Por ejemplo, un puerto conectado a un teléfono IP y un dispositivo final se asociaría con dos VLAN: una para voz y otra para datos.

Consulte la topología en la figura. En este ejemplo, la PC5 está conectada con el teléfono IP de Cisco, que a su vez está conectado a la interfaz FastEthernet 0/18 en S3. Para implementar esta configuración, se crean una VLAN de datos y una VLAN de voz.

![[Pasted image 20241213003623.png]]
3.3.7

## Ejemplo de VLAN de voz y datos

Utilice el comando **switchport voice vlan** _vlan-id_ interface configuration para asignar una VLAN de voz a un puerto.

Las redes LAN que admiten tráfico de voz por lo general también tienen la Calidad de Servicio (QoS) habilitada. El tráfico de voz debe etiquetarse como confiable apenas ingrese en la red. Use el **mls qos trust [cos | device cisco-phone | dscp | ip-precedence]** comando de configuración para establecer el estado confiable de una interfaz, y para indicar qué campos del paquete se usan para clasificar el tráfico.

La configuración en el ejemplo crea las dos VLAN (es decir, VLAN 20 y VLAN 150), y a continuación, asigna la interfaz F0/18 de S3 como un puerto de switch en VLAN 20. También asigna el tráfico de voz en VLAN 150 y permite la clasificación de QoS basada en la Clase de Servicio (CoS) asignado por el teléfono IP.

```js
S3(config)# vlan 20
S3(config-vlan)# name student
S3(config-vlan)# vlan 150
S3(config-vlan)# name VOICE
S3(config-vlan)# exit
S3(config)# interface fa0/18
S3(config-if)# switchport mode access
S3(config-if)# switchport access vlan 20
S3(config-if)# mls qos trust cos
S3(config-if)# switchport voice vlan 150
S3(config-if)# end
S3#
```

**Nota:** La implementación de QoS no está contemplada en este curso.

El **switchport access vlan** comando fuerza la creación de una VLAN si es que aún no existe en el switch. Por ejemplo, la VLAN 30 no está presente en la salida del comando **show vlan brief** del switch. Si se introduce el comando **switchport access vlan 30** en cualquier interfaz sin configuración previa, el switch muestra lo siguiente:

```js
% Access VLAN does not exist. Creating vlan 30 
```

3.3.8

## Verificar la información de la VLAN

Una vez que se configura una VLAN, se puede validar la configuración con los comandos **show** de IOS de Cisco

El **show vlan** comando muestra la lista de todas las VLAN configuradas. El **show vlan** comando también se puede utilizar con opciones. La sintaxis completa es:
```js
show vlan [brief | id vlan-id | name vlan-name | summary]
```

En la tabla se describen las opciones de **show vlan** comando.

|Tarea|Opción de comando|
|---|---|
|Muestra el nombre de VLAN, el estado y sus puertos una VLAN por linea.|**brief**|
|Muestra información sobre el número de ID de VLAN identificado. Para _vlan-id_, the range is 1 to 4094.|**id** _vlan-id_|
|Muestra información sobre el número de ID de VLAN identificado. El _vlan-name_ es una cadena ASCII de 1 a 32 caracteres.|**name** _vlan-name_|
|Mostrar el resumen de información de la VLAN.|**summary**|

El **show vlan summary** comando muestra la lista de todas las VLAN configuradas.

```js
S1# show vlan summary
Number of existing VLANs              : 7
Number of existing VTP VLANs          : 7
Number of existing extended VLANS     : 0
```

Otros comandos útiles son el comando **show interfaces** _interface-id_ **switchport** y el comando **show interfaces vlan** _vlan-id_. Por ejemplo, el **show interfaces fa0/18 switchport** comando se puede utilizar para confirmar que el puerto FastEthernet 0/18 se ha asignado correctamente a las VLAN de datos y voz.

```js
S1# show interfaces fa0/18 switchport
Name: Fa0/18
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 20 (student) 
Trunking Native Mode VLAN: 1 (default)
Voice VLAN: 150
Administrative private-vlan host-association: none
(Output omitted)
```

3.3.9

## Cambio de pertenencia de puertos de una VLAN

Existen varias maneras de cambiar la pertenencia de puertos de una VLAN.

Si el puerto de acceso del switch se ha asignado incorrectamente a una VLAN, simplemente vuelva a ingresar el comando **switchport access vlan** _vlan-id_ interface configuration con el ID de VLAN correcto. Por ejemplo, suponga que Fa0/18 se configuró incorrectamente para estar en la VLAN 1 predeterminada en lugar de la VLAN 20. Para cambiar el puerto a VLAN 20, simplemente ingrese **switchport access vlan 20**.

Para volver a cambiar la pertenencia de un puerto a la VLAN 1 predeterminada, utilice el comando **no switchport access vlan** interface configuration mode como se muestra.

En la salida, por ejemplo, Fa0/18 está configurado para estar en la VLAN 1 predeterminada, tal como lo confirma el **show vlan brief** comando.

```js
S1(config)# interface fa0/18
S1(config-if)# no switchport access vlan
S1(config-if)# end
S1#
S1# show vlan brief
VLAN Name                 Status    Ports
---- ------------------ --------- -------------------------------
1    default            active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
                                  Fa0/5, Fa0/6, Fa0/7, Fa0/8
                                  Fa0/9, Fa0/10, Fa0/11, Fa0/12
                                  Fa0/13, Fa0/14, Fa0/15, Fa0/16
                                  Fa0/17, Fa0/18, Fa0/19, Fa0/20
                                  Fa0/21, Fa0/22, Fa0/23, Fa0/24
                                  Gi0/1, Gi0/2
20   student            active    
1002 fddi-default       act/unsup 
1003 token-ring-default act/unsup 
1004 fddinet-default    act/unsup 
1005 trnet-default      act/unsup
```

Nota que la VLAN 20 sigue activa, aunque no tenga puertos asignados.

La **show interfaces f0/18 switchport** salida también se puede utilizar para verificar que la VLAN de acceso para la interfaz F0/18 se ha restablecido a la VLAN 1 como se muestra en la salida.

```js
S1# show interfaces fa0/18 switchport
Name: Fa0/18
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: negotiate
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
```

3.3.10

## Eliminar las VLAN

El comando de modo de configuración global **no vlan** _vlan-id_ se usa para remover una VLAN desde el archivo del switch vlan.dat.

**Precaución**: Antes de borrar una VLAN, reasigne todos los puertos miembros a una VLAN distinta. Los puertos que no se trasladen a una VLAN activa no se podrán comunicar con otros hosts una vez que se elimine la VLAN y hasta que se asignen a una VLAN activa.

Se puede eliminar el archivo vlan.dat en su totalidad con el comando delete flash:vlan.dat **delete flash:vlan.dat**del modo EXEC con privilegios. Se puede utilizar la versión abreviada del comando (**delete vlan.dat**) delete vlan.dat si no se trasladó el archivo vlan.dat de su ubicación predeterminada. Después de emitir este comando y de volver a cargar el switch, las VLAN configuradas anteriormente ya no están presentes. Esto vuelve al switch a la condición predeterminada de fábrica con respecto a la configuración de VLAN.

**Nota**: Para restaurar un conmutador Catalyst a su condición predeterminada de fábrica, desconecte todos los cables excepto la consola y el cable de alimentación del conmutador. A continuación, introduzca el comando de modo EXEC **erase startup-config** privilegiado seguido del **delete vlan.dat** comando.

3.3.11
## Packet Tracer: Configuración de redes VLAN

En esta actividad de Packet Tracer, completará los siguientes objetivos:

- Verificar la configuración de VLAN predeterminada
- Configurar las redes VLAN
- Asignar VLAN a los puertos

![[3.3.12-packet-tracer---vlan-configuration_es-XL.pka]]

---
# Enlaces troncales de la VLAN

3.4.1

## Comandos de configuración troncal

Ahora que ha configurado y verificado VLAN, ha llegado el momento de configurar y verificar los troncos de VLAN. Un enlace troncal de VLAN es un enlace de capa 2 del modelo OSI entre dos switches que transporta el tráfico para todas las VLAN (a menos que se restrinja la lista de VLAN permitidas de manera manual o dinámica).

Para habilitar los vínculos troncal, configure los puertos de interconexión con el conjunto de comandos de configuración de interfaz que se muestran en la tabla.

|**Tarea**|**Comando de IOS**|
|---|---|
|Ingrese al modo de configuración global.|Switch# **configure terminal**|
|Ingrese el modo de configuración de interfaz.|Switch(config)# **interface** _interface-id_|
|Establezca el puerto en modo de enlace troncal permanente.|Switch(config-if)# **switchport mode trunk**|
|Cambie la configuración de la VLAN nativa a otra opción que no sea VLAN 1.|Switch(config-if)# **switchport trunk native vlan** _vlan-id_|
|Especifique la lista de VLAN que se permitirán en el enlace troncal.|Switch(config-if)# **switchport trunk allowed vlan** _vlan-list_|
|Vuelva al modo EXEC privilegiado.|Switch(config-if)# **end**|

3.4.2

## Ejemplo de configuración de troncal

En la figura 2, las VLAN 10, 20 y 30 admiten las computadoras de Cuerpo docente, Estudiante e Invitado (PC1, PC2 y PC3). El puerto F0/1 del switch S1 se configuró como puerto de enlace troncal y reenvía el tráfico para las VLAN 10, 20 y 30. La VLAN 99 se configuró como VLAN nativa.

![[Pasted image 20241213004127.png]]

El ejemplo muestra la configuración del puerto F0/1 en el conmutador S1 como puerto troncal. La VLAN nativa se cambia a VLAN 99 y la lista de VLAN permitidas se restringe a 10, 20, 30 y 99.

```js
S1(config)# interface fastEthernet 0/1
S1(config-if)# switchport mode trunk
S1(config-if)# switchport trunk native vlan 99
S1(config-if)# switchport trunk allowed vlan 10,20,30,99
S1(config-if)# end
```

**Nota**: Esta configuración supone el uso de los switches Cisco Catalyst 2960 que utilizan de manera automática la encapsulación 802.1Q en los enlaces troncales. Es posible que otros switches requieran la configuración manual de la encapsulación. Siempre configure ambos extremos de un enlace troncal con la misma VLAN nativa. Si la configuración de enlace troncal 802.1Q no es la misma en ambos extremos, el software IOS de Cisco registra errores.

3.4.3

## Verifique la configuración de enlaces troncales.

La salida del switch muestra la configuración del puerto del switch F0/1 en el switch S1. La configuración se verifica con el **show interfaces** comando **switchport** _interface-ID_.

```js
S1# show interfaces fa0/1 switchport
Name: Fa0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 99 (VLAN0099)
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk private VLANs: none 
Operational private-vlan: none
Trunking VLANs Enabled: 10,20,30,99
Pruning VLANs Enabled: 2-1001
(output omitted)
```

En el área superior resaltada, se muestra que el modo administrativo del puerto F0/1 se estableció en **trunk**. El puerto está en modo de enlace troncal. En la siguiente área resaltada, se verifica que la VLAN nativa es la VLAN 99. Más abajo en el resultado, en el área inferior resaltada, se muestra que las VLAN 10,20,30 y 99 están habilitadas en el enlace troncal.

3.4.4

## Restablecimiento del enlace troncal al estado predeterminado

Use el **no switchport trunk allowed vlan** y el **no switchport trunk native vlan** comando para eliminar las VLAN permitidas y restablecer la VLAN nativa del enlace troncal. Cuando se restablece al estado predeterminado, el enlace troncal permite todas las VLAN y utiliza la VLAN 1 como VLAN nativa. El ejemplo muestra los comandos utilizados para restablecer todas las características de enlace troncal de una interfaz troncal a la configuración predeterminada.

```js
S1(config)# interface fa0/1
S1(config-if)# no switchport trunk allowed vlan
S1(config-if)# no switchport trunk native vlan
S1(config-if)# end
```

El comando **show interfaces fa0/1 switchport** revela que la troncal se ha reconfigurado a un estado predeterminado.

```js
S1# show interfaces fa0/1 switchport
Name: Fa0/1
Switchport: Enabled
Administrative Mode: trunk
Operational Mode: trunk
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: dot1q
Negotiation of Trunking: On
Access Mode VLAN: 1 (default) 
Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: enabled
Voice VLAN: none
Administrative private-vlan host-association: none 
Administrative private-vlan mapping: none 
Administrative private-vlan trunk native VLAN: none
Administrative private-vlan trunk Native VLAN tagging: enabled
Administrative private-vlan trunk encapsulation: dot1q
Administrative private-vlan trunk normal VLANs: none
Administrative private-vlan trunk associations: none
Administrative private-vlan trunk mappings: none
Operational private-vlan: none
Trunking VLANs Enabled: ALL
Pruning VLANs Enabled: 2-1001
(output omitted)
```

La figura muestra el resultado de los comandos utilizados para eliminar la característica de enlace troncal del puerto F0/1 del switch S1. El **show interfaces f0/1 switchport** comando revela que la interfaz F0/1 ahora está en modo de acceso estático.

```js
S1(config)# interface fa0/1
S1(config-if)# switchport mode access
S1(config-if)# end
S1# show interfaces fa0/1 switchport
Name: Fa0/1
Switchport: Enabled
Administrative Mode: static access
Operational Mode: static access
Administrative Trunking Encapsulation: dot1q
Operational Trunking Encapsulation: native
Negotiation of Trunking: Off
Access Mode VLAN: 1 (default)
Trunking Native Mode VLAN: 1 (default)
Administrative Native VLAN tagging: enabled
(output omitted)
```

3.4.5

## Packet Tracer: Configuración de enlaces troncales

En esta actividad de Packet Tracer, completará los siguientes objetivos:

- verificar las VLAN
- configurar los enlaces troncales
![[3.4.5-packet-tracer---configure-trunks_es-XL.pka]]


3.4.6

## Práctica de laboratorio: Configuración de redes VLAN y enlaces troncales

##### Oportunidad de Práctica de habilidades

Tendrá la oportunidad de practicar las siguientes habilidades:

- Part 1: Arme la red y configurar los ajustes básicos de los dispositivos
- Part 2: Cree redes VLAN y asignar puertos de switch
- Part 3: Mantener las asignaciones de puertos de VLAN y la base de datos de VLAN
- Part 4: Configurar un enlace troncal 802.1Q entre los switches

Podrá practicar estas habilidades usando Packet Tracer o equipo de laboratorio, de estar disponible.

![[3.4.6-packet-tracer---configure-vlans-and-trunking---physical-mode_es-XL.pka]]

---

# Protocolo de enlace troncal dinámico

3.5.1

## Introducción a DTP

Algunos switches Cisco tienen un protocolo propietario que les permite negociar automáticamente la conexión troncal con un dispositivo vecino. Este protocolo se denomina Protocolo de Enlace Troncal Dinámico (DTP). DTP puede acelerar el proceso de configuración de un administrador de red. Las interfaces troncal Ethernet admiten diferentes modos de enlace troncal. Una interfaz se puede establecer en trunking o no trunking, o para negociar trunking con la interfaz vecina. La negociación de enlaces troncales entre dispositivos de red la maneja el Protocolo de Enlace Troncal Dinámico (DTP), que solo funciona de punto a punto.

DTP es un protocolo exclusivo de Cisco que se habilita de manera automática en los switches de las series Catalyst 2960 y Catalyst 3560. DTP maneja la negociación de enlaces troncales sólo si el puerto del switch vecino está configurado en un modo de enlace troncal que admite DTP. Los switches de otros proveedores no admiten el DTP.

**Precaución**: Algunos dispositivos de interredes pueden reenviar tramas DTP de manera incorrecta, lo que puede causar errores de configuración. Para evitar esto, desactive el DTP en las interfaces de un switch de Cisco conectado a dispositivos que no admiten DTP.

La configuración DTP predeterminada para los switches Catalyst 2960 y 3650 de Cisco es automática dinámica.

Para habilitar los enlaces troncales desde un switch de Cisco hacia un dispositivo que no admite DTP, utilice los comandos **switchport mode trunk** y **switchport nonegotiate** interface configuration mode commands. Esto hace que la interfaz se convierta en un tronco, pero no generará tramas DTP.

```js
S1(config-if)# switchport mode trunk
S1(config-if)# switchport nonegotiate
```

Para volver a habilitar el protocolo de enlace troncal dinámico, utilice el **switchport mode dynamic** **auto** comando.

```js
S1(config-if)# switchport mode dynamic auto
```

Si los puertos que conectan dos conmutadores están configurados para ignorar todos los anuncios DTP con los **switchport mode trunk** comandos **switchport nonegotiate** y, los puertos se quedarán en modo de puerto troncal. Si los puertos de conexión están configurados en automático dinámico, no negociarán un tronco y permanecerán en el estado de modo de acceso, creando un enlace troncal inactivo.

Cuando configure un puerto para que esté en modo de enlace troncal, utilice el **switchport mode trunk** comando. No existe ambigüedad sobre el estado en que se encuentra el enlace troncal: este se encuentra siempre activo.

3.5.2

## Modos de interfaz negociados

El **switchport mode** comando tiene opciones adicionales para negociar el modo de interfaz. La siguiente es la sintaxis del comando :

```js
Switch(config)# switchport mode { access | dynamic { auto | desirable } | trunk }
```

Las opciones del comando se describen en la Tabla

|**Opción**|**Descripción**|
|---|---|
|**access**|- Pone la interfaz (puerto de acceso) en modo permanente de no trunking y negocia para convertir el enlace en un enlace no troncal.<br>- La interfaz se convierte en una interfaz no troncal, independientemente de si la interfaz vecina es una interfaz troncal.|
|**dynamic auto**|- Hace que la interfaz pueda convertir el enlace en un enlace troncal.<br>- La interfaz se convierte en una interfaz de enlace troncal, si la interfaz vecina está configurado en modo troncal o deseable.<br>- El modo de puerto de switch predeterminado para todas las interfaces Ethernet es **dynamic auto**.|
|**dynamic desirable**|- Hace que el puerto intente convertir el enlace en un enlace troncal. 64 K.<br>- La interfaz se convierte en una interfaz de enlace troncal, si la interfaz vecina está configurado en modo automático troncal, deseable o dinámico.|
|**trunk**|- El puerto queda configurado en modo troncal de forma permanente y negocia para que el enlace se convierta en una conexión troncal.<br>- La interfaz se convierte en una interfaz de enlace troncal, incluso si la interfaz vecina no es una interfaz troncal.|

Utilice el comando **switchport nonegotiate** interface configuration para detener la negociación DTP. El switch no participa en la negociación DTP en esta interfaz. Este comando sólo se puede utilizar cuando el modo interface switchport es **access** o **trunk**. Debe configurar manualmente el puerto de vecindad como un puerto troncal para establecer un enlace troncal.

3.5.3

## Resultados de una configuración DTP

La tabla ilustra los resultados de las opciones de configuración DTP en extremos opuestos de un enlace troncal conectado a los puertos del switch Catalyst 2960. Una buena practica es configurar los enlaces troncales estáticamente siempre que sea posible.

|**Dinámico automático**|**Dinámico deseado**|**Troncal**|**Acceso**|
|---|---|---|---|---|
|**Dinámico automático**|Acceso|Troncal|Troncal|Acceso|
|**Dinámico deseado**|Troncal|Troncal|Troncal|Acceso|
|**Troncal**|Troncal|Troncal|Troncal|Conectividad limitada|
|**Acceso**|Acceso|Acceso|Conectividad limitada|Acceso|

3.5.4

## Verificación del modo de DTP

El modo DTP predeterminado depende de la versión del software Cisco IOS y de la plataforma. Para determinar el modo DTP actual, ejecute el **show dtp interface** comando como se muestra en la salida.

```js
S1# show dtp interface fa0/1
DTP information for FastEthernet0/1:
TOS/TAS/TNS: ACCESS/AUTO/ACCESS
TOT/TAT/TNT: NATIVE/NEGOTIATE/NATIVE
Neighbor address 1: C80084AEF101
Neighbor address 2: 000000000000
Hello timer expiration (sec/state): 11/RUNNING
Access timer expiration (sec/state): never/STOPPED
Negotiation timer expiration (sec/state): never/STOPPED
Multidrop timer expiration (sec/state): never/STOPPED
FSM state: S2:ACCESS
# times multi & trunk 0
Enabled: yes
In STP: no
```

**Nota**: Una mejor práctica general cuando se requiere un enlace troncal es establecer la interfaz en **trunk** y **nonegotiate** cuando se necesita un enlace troncal. Se debe inhabilitar DTP en los enlaces cuando no se deben usar enlaces troncales.

3.5.5

## Packet Tracer: Configuración de DTP

En esta actividad Packet Tracer, configurará y verificará DTP.

 ![[3.5.5-packet-tracer---configure-dtp_es-XL.pka]]
 

3.5.6

## Compruebe su comprensión - Protocolo de enlace troncal dinámico

Compruebe su conocimiento sobre DTP, Elija la MEJOR repuesta para las siguientes preguntas

1. ¿Verdadero o falso? DTP es un protocolo IEEE estándar abierto que especifica la negociación automática de vínculos troncal del conmutador.
    
    Verdadero
    
    Falso
    
2. ¿Cuál es el modo de switchport predeterminado para los switches Catalyst de Cisco?
    
    Acceso
    
    Troncal
    
    Dinámico automático
    
    Dinámico deseable
    
3. ¿Verdadero o falso? Dos puertos de conmutación en un enlace ambos configurados como automático dinámico negociarán correctamente un tronco.
    
    Verdadero
    
    Falso
    
4. ¿Qué dos modos DTP formarán un tronco con una interfaz que se configura como automático dinámico? (Escoja dos opciones).
    
    Acceso
    
    Troncal
    
    Dinámico automático
    
    Dinámico deseable

---
# Práctica del módulo y cuestionario

3.6.1

## Packet Tracer - Implementar VLAN y Trunking

En esta actividad de Packet Tracer, completará los siguientes objetivos:

- Configurar las redes VLAN
- Asignar puertos a las VLAN
- Configurar troncales estáticos
- Configurar troncales dinamicos.
![[3.6.1-packet-tracer---implement-vlans-and-trunking_es-XL.pka]]


3.6.2

## Laboratorio: Implementación de VLAN y Troncalización

En este laboratorio, realizará lo siguiente:

- Armar la red y configurar los ajustes básicos de los dispositivos
- Crear redes VLAN y asignar puertos de switch
- Configurar un enlace troncal 802.1Q entre los switches

 Implementar las VLAN y los enlaces troncales

3.6.3

## ¿Qué aprenderé en este módulo?

**Descripción general de las VLANs**

Las LANS virtuales (VLANs) es un grupo de dispositivos dentro de una VLAN que puede comunicarse con cada dispositivo como si estuvieran conectados al mismo cable. Las VLAN se basan en conexiones lógicas, en lugar de conexiones físicas. Los administradores utilizan VLAN para segmentar redes en función de factores como la función, el equipo o la aplicación. Cada VLAN se considera una red lógica diferente. Cualquier puerto de switch puede pertenecer a una VLAN. Una VLAN crea un dominio de difusión lógico que puede abarcar varios segmentos LAN físicos. Las VLAN mejoran el rendimiento de la red mediante la división de grandes dominios de difusión en otros más pequeños. Cada VLAN de una red conmutada corresponde a una red IP; por lo tanto, el diseño de VLAN debe utilizar un esquema jerárquico de direccionamiento de red. Los tipos de VLAN incluyen la VLAN predeterminada, las VLAN de datos, la VLAN nativa, las VLAN de administración. y las VLAN de voz.

**VLANs en un ambiente Multi-Switched**

Un enlace troncal no pertenece a una VLAN específica. Es un conducto para las VLAN entre los switches y los routers. Un enlace troncal es un enlace punto a punto entre dos dispositivos de red que lleva más de una VLAN. Un enlace troncal de VLAN amplía las VLAN a través de toda la red. Cuando se implementan las VLAN en un switch, la transmisión del tráfico de unidifusión, multidifusión y difusión desde un host en una VLAN en particular se limita a los dispositivos presentes en esa VLAN. Los campos de etiqueta de VLAN incluyen el tipo, prioridad de usuario, CFI y VID. Algunos dispositivos que admiten los enlaces troncales agregan una etiqueta VLAN al tráfico de las VLAN nativas. Si un puerto de enlace troncal 802.1Q recibe una trama etiquetada con la misma ID de VLAN que la VLAN nativa, descarta la trama. Se necesita una red VLAN de voz separada para admitir VoIP. Las directivas de QoS y seguridad se pueden aplicar al tráfico de voz. El tráfico VLAN de voz debe etiquetarse con un valor de prioridad CoS de Capa 2 adecuado.

**Configuración de VLAN**

Los diferentes switches Catalyst de Cisco soportan varias cantidades de VLAN, incluidas las VLAN de rango normal y las VLAN de rango extendido. Al configurar redes VLAN de rango normal, los detalles de configuración se almacenan en la memoria flash del switch en un archivo denominado vlan.dat. Aunque no es necesario, se recomienda guardar los cambios de configuración en ejecución en la configuración de inicio. Después de crear una VLAN, el siguiente paso es asignar puertos a la VLAN. Hay muchos comandos para definir un puerto como puerto de acceso y asignarlo a una VLAN. Las VLAN se configuran en el puerto del switch y no en el terminal. Un puerto de acceso puede pertenecer a sólo una VLAN por vez. Sin embargo un puerto puede tambien estar asociado a una VLAN de voz. Por ejemplo, un puerto conectado a un teléfono IP y un dispositivo final se asociaría con dos VLAN: una para voz y otra para datos. Una vez que se configura una VLAN, se puede validar la configuración con los comandos **show** show de IOS de Cisco Si el puerto de acceso del switch se ha asignado incorrectamente a una VLAN, simplemente vuelva a ingresar el comando **switchport access** **vlan** _vlan-id_ interface configuration con el ID de VLAN correcto. El comando de modo de configuración gloabl **no vlan** _vlan-id_ se usa para remover una VLAN desde el archivo del switch vl vlan.dat.

**Enlace troncal de VLAN**

Un enlace troncal de VLAN es un enlace de capa 2 entre dos switches que transporta el tráfico para todas las VLAN. Hay varios comandos para configurar los puertos de interconexión. Para verificar la configuración troncal de VLAN , utilice el **switchport** comando **show interfaces** _interface-ID_. Use el **no switchport trunk allowed vlan** y el **no switchport trunk native vlan** comando para eliminar las VLAN permitidas y restablecer la VLAN nativa del enlace troncal.

**Protocolo de Enlace Troncal Dinámico**

Una interfaz se puede establecer en trunking o no trunking, o para negociar trunking con la interfaz vecina. La negociación de enlaces troncales entre dispositivos de red la maneja el Protocolo de Enlace Troncal Dinámico (DTP), que solo funciona de punto a punto. DTP maneja la negociación de enlaces troncales solo si el puerto del switch vecino está configurado en un modo de enlace troncal que admite DTP. Para habilitar los enlaces troncales desde un switch de Cisco hacia un dispositivo que no admite DTP, utilice los comandos de modo de configuración de interfaz **switchport mode trunk** y **switchport nonegotiate** El **switchport mode** comando tiene opciones adicionales para negociar el modo de interfaz, incluyendo acceso, automático dinámico, dinámico deseable y troncal. Para verificar el modo DTP actual, ejecute el **show dtp interface** comando.

3.6.4

## Módulo Quiz - VLAN

1. ¿Qué sucede con un puerto asociado con VLAN 10 cuando el administrador elimina VLAN 10 del switch?
    
    El puerto se asocia automáticamente con la VLAN nativa.
    
    El puerto se vuelve inactivo.
    
    El puerto vuelve a crear la VLAN.
    
    El puerto vuelve a la VLAN predeterminada.
    
2. ¿En qué ubicación de memoria se almacenan las configuraciones de VLAN de las VLAN de rango normal en un switch Catalyst?
    
    Memoria flash
    
    ROM
    
    RAM
    
    NVRAM
    
3. Un administrador está investigando una falla en un enlace troncal entre un switch Cisco y un switch de otro proveedor. Después de algunos **show** comandos, el administrador nota que los switches no están negociando un tronco. ¿Cuál es una causa probable para este problema?
    
    Ambos conmutadores están en modo no egociado.
    
    Ambos conmutadores están en modo troncal.
    
    Los switches de otros proveedores no admiten el DTP.
    
    Las tramas DTP están inundando toda la red.
    
4. ¿Cuál es el propósito del archivo vlan.dat en un switch?
    
    Contiene el sistema operativo.
    
    Contiene la configuración en ejecución.
    
    Contiene la base de datos de la VLAN.
    
    Contiene la configuración guardada.
    
5. ¿Cuál es el propósito de establecer la VLAN nativa separada de las VLAN de datos?
    
    La VLAN nativa es sólo para transportar tráfico de administración de VLAN.
    
    Se puede mejorar la seguridad de las tramas de administración que se llevan en la VLAN nativa.
    
    Se debe usar una VLAN separada para transportar tramas sin etiquetas poco comunes a fin de evitar la contención del ancho de banda en las VLAN de datos.
    
    La VLAN nativa es para que los enrutadores y conmutadores intercambien su información de administración, por lo que debe ser diferente de las VLAN de datos.
    
6. Cuando un switch Cisco recibe tramas sin etiquetas en un puerto troncal 802.1Q, ¿a qué ID de VLAN se conmuta el tráfico de forma predeterminada?
    
    data VLAN ID
    
    native VLAN ID
    
    ID de VLAN no utilizado
    
    management VLAN ID
    
7. Un administrador de red está determinando la mejor ubicación de los vínculos troncal de VLAN. ¿Qué dos tipos de conexiones punto a punto utilizan la conexión troncal VLAN? (Elija dos.)
    
    entre un switch y un servidor que tiene una NIC 802.1Q
    
    entre dos switches que utilizan varias VLAN
    
    entre un conmutador y una impresora de red
    
    En la RAM
    
    entre un switch y un PC cliente
    
8. ¿Cuáles son los tres principales beneficios de usar redes VLAN? (Elija tres opciones).
    
    reducción de costos
    
    mejora de la eficiencia del personal de TI
    
    Satisfacción del usuario final
    
    Seguridad
    
    Reducción en la cantidad de enlaces troncales
    
9. En un switch Cisco, ¿dónde se almacena la información de VLAN de rango extendido?
    
    NVRAM
    
    Memoria flash
    
    Archivo de configuración de inicio
    
    Archivo de configuración en ejecución
    
10. ¿En qué ubicación se almacenan de forma predeterminada las VLAN de rango normal en un switch Cisco?
    
    memoria flash
    
    startup-config
    
    RAM
    
    running-config
    
11. ¿Qué tipo distinto de VLAN utiliza un administrador para acceder a un switch y configurarlo?
    
    VLAN predeterminada
    
    VLAN de administración
    
    VLAN nativa
    
    data VLAN (VLAN de datos)
    
12. ¿Cuál es el propósito de establecer la VLAN nativa separada de las VLAN de datos?
    
    La VLAN nativa es para que los enrutadores y conmutadores intercambien su información de administración, por lo que debe ser diferente de las VLAN de datos.
    
    Se debe usar una VLAN separada para transportar tramas sin etiquetas poco comunes a fin de evitar la contención del ancho de banda en las VLAN de datos.
    
    Se puede mejorar la seguridad de las tramas de administración que se llevan en la VLAN nativa.
    
    La VLAN nativa es sólo para transportar tráfico de administración de VLAN.
    
13. ¿Dónde se almacena el archivo vlan.dat en un switch?
    
    En la RAM
    
    En los medios de almacenamiento conectados de forma externa o el disco duro interno
    
    En la NVRAM
    
    En la memoria flash
    
14. Si una organización está cambiando para incluir los teléfonos IP de Cisco en su red, ¿qué función de diseño debe tenerse en cuenta para garantizar la calidad de la voz?
    
    El tráfico de voz debe etiquetarse con la VLAN nativa.
    
    El tráfico de voz y el de datos requieren enlaces troncales independientes entre los switches.
    
    Se necesitan puertos de switch adicionales dedicados a los teléfonos IP de Cisco.
    
    Se necesita una VLAN separada para el tráfico de voz.
    
15. Actualmente, un switch Cisco permite el tráfico etiquetado con VLAN 10 y 20 a través del puerto troncal Fa0/5. ¿Cuál es el efecto de emitir un **switchport trunk allowed vlan 30** comando en Fa0/5?
    
    Permite VLAN 1 a 30 en Fa0/5.
    
    Solo permite VLAN 30 en Fa0/5.
    
    Permite implementar una VLAN nativa de 30 en Fa0/5.
    
    Permite VLAN 10, 20 y 30 en Fa0/5.
