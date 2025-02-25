## Introducción

1.0.1

### ¿Por qué debería tomar este módulo?

¡Bienvenido a la configuración básica del dispositivo!

¡Bienvenido al primer módulo en CCNA Switching, Enrutamiento y Wireless Essentials!. Sabe que los switches y routers vienen con alguna configuración integrada, así que ¿por qué necesitarás aprender a configurar más switches y routers?

Imagina que compraste un juego de tren modelo. Después de haberla configurado, te diste cuenta de que la pista era sólo una forma ovalada simple y que los vagones de tren sólo funcionaban en el sentido de las agujas del reloj. Es posible que desee que la pista sea una figura de ocho con un paso elevado. Es posible que desee tener dos trenes que operen independientemente el uno del otro y sean capaces de moverse en diferentes direcciones. ¿Cómo pudiste hacer que eso pasara? Tendrías que volver a configurar la pista y los controles. Es lo mismo con los dispositivos de red. Como administrador de red, necesita un control detallado de los dispositivos de su red. Esto significa configurar con precisión switches y routeres para que su red haga lo que desea que haga. Este módulo tiene muchas actividades de Comprobador de sintaxis y trazador de paquetes para ayudarle a desarrollar estas habilidades. Comencemos ya mismo.

1.0.2

### ¿Qué aprenderé en este módulo?

**Título del módulo:** Configuración básica de dispositivos

**Objetivos del módulo**: Configuración de los dispositivos mediante los procedimientos recomendados de seguridad.

Leyenda de la tabla
|**Título del tema**|**Objetivo del tema**|
|---|---|
|**Configuración de Parámetros Iniciales de un Switch**|Configurar los parámetros iniciales en un switch Cisco.|
|**Configuración de Puertos de un Switch.**|Configurar los puertos de un switch para cumplir con los requisitos de red.|
|**Acceso remoto seguro**|Configurar el acceso de administración seguro en un switch.|
|**Configuración básica de un router**|Configurar los ajustes básicos en un router para enrutar entre dos redes conectadas directamente, utilizando CLI.|
|**Verificar redes conectadas directamente**|Verificar la conectividad entre dos redes que están conectadas directamente a un router.|

1.0.3

### Video: descargue e instale Packet Tracer

Este video le mostrará cómo descargar e instalar Packet Tracer. Utilizará Packet Tracer para simular la creación y prueba de redes en su equipo. Packet Tracer es un programa de software flexible y divertido que te dará la oportunidad de usar las representaciones de red y teorías que acabas de aprender a construir modelos de red y explorar LAN y WAN relativamente complejas.

Por lo general, los estudiantes usan Packet Tracer para lo siguiente:

- Preparase para un examen de certificación.
- Practicar lo aprendido en los cursos de redes.
- Refinar sus habilidades para una entrevista laboral.
- Examinar el impacto de agregar nuevas tecnologías a los diseños de red existentes.
- Desarrollar sus habilidades para realizar trabajos en Internet de las cosas.
- Competir en desafíos globales de diseño (consulte 2017 PT 7 Desafío de diseño en Facebook).

Packet Tracer es una herramienta esencial de aprendizaje que se utiliza en muchos cursos de Cisco Networking Academy.

Para obtener e instalar Cisco Packet Tracer siga estos pasos:

**Paso 1**. Iniciar sesión en la página de "I'm Learning" de Cisco Networking Academy.  
**Paso 2**. Seleccione Recursos.  
**Paso 3**. Seleccione Descargar Packet Tracer.  
**Paso 4**. Seleccione la versión de Packet Tracer que necesita.  
**Paso 5**. Guarde el archivo en la computadora.  
**Paso 6**. Inicie el programa de instalación de Packet Tracer.

Haga clic en Reproducir en el video para realizar un recorrido detallado del proceso de descarga e instalación de Packet Tracer.

Play Video

1.0.4

### Vídeo - Introducción a Cisco Packet Tracer

Packet Tracer es una herramienta que permite simular redes reales. Proporciona tres menús principales:

- Puede agregar dispositivos y conectarlos a través de cables o inalámbricos.
- Puede seleccionar, eliminar, inspeccionar, etiquetar y agrupar componentes dentro de la red.
- Puede administrar su red abriendo una red existente o de muestra, guardando la red actual y modificando su perfil de usuario o preferencias.

Si ha utilizado algún programa, como un procesador de textos o una hoja de cálculo, ya está familiarizado con los comandos del menú Archivo ubicados en la barra de menús superior. Los comandos Abrir, Guardar, Guardar como y Salir funcionan como lo harían con cualquier programa, pero hay dos comandos especiales para Packet Tracer.

El comando Open Samples mostrará un directorio de ejemplos preconstruidos de características y configuraciones de varios dispositivos de red e Internet de las cosas incluidos en Packet Tracer.

El comando Salir y cerrar sesión eliminará la información de registro de esta copia de Packet Tracer y requerirá que el siguiente usuario de esta copia de Packet Tracer realice el procedimiento de inicio de sesión de nuevo.

Haga clic en Reproducir en el vídeo para aprender a utilizar los menús y a crear su primera red Packet Tracer.

Play Video

1.0.5

### Packet Tracer - Exploración de Modo Lógico y Físico

El modelo de red de esta actividad Packet Tracer Physical Mode (PTPM) incorpora muchas de las tecnologías que puede dominar en los cursos de Cisco Networking Academy. y representa una versión simplificada de la forma en que podría verse una red de pequeña o mediana empresa.

La mayoría de los dispositivos de la sucursal de Seward y del Centro de Datos de Warrenton ya están implementados y configurados. Usted acaba de ser contratado para revisar los dispositivos y redes implementados. No es importante que comprenda todo lo que vea y haga en esta actividad. Siéntase libre de explorar la red por usted mismo. Si desea hacerlo de manera más sistemática, siga estos pasos. Responda las preguntas lo mejor que pueda.

 Exploración de modo Lógico y Físico

 ![[docs/cisco-academy/CCNA 2 v7/modulos/Módulos 1 - 4 Conceptos de Switching, VLANs y enrutamiento entre redes VLAN/ANEXOS/1.0.5-packet-tracer---logical-and-physical-mode-exploration_es-XL.pka]]

---

## Configuración de parámetros iniciales de un switch

1.1.1

### Secuencia de arranque de un switch

Antes de poder configurar un switch, debe encenderlo y permitirle pasar por la secuencia de arranque de cinco pasos. En este tema se tratan los conceptos básicos de la configuración de un switch e incluye un laboratorio al final.

Después de encender un switch Cisco, pasa por la siguiente secuencia de inicio de cinco pasos:

**Paso 1**: Primero, el switch carga un programa de autodiagnóstico al encender (POST) almacenado en la memoria ROM. El POST verifica el subsistema de la CPU. Este comprueba la CPU, la memoria DRAM y la parte del dispositivo flash que integra el sistema de archivos flash.  
**Paso 2**: A continuación, el switch carga el software del cargador de arranque. El cargador de arranque es un pequeño programa almacenado en la memoria ROM que se ejecuta inmediatamente después de que el POST se completa correctamente.  
**Paso 3**: El cargador de arranque lleva a cabo la inicialización de la CPU de bajo nivel. Inicializa los registros de la CPU, que controlan dónde está asignada la memoria física, la cantidad de memoria y su velocidad.  
**Paso 4**: El cargador de arranque inicia el sistema de archivos flash en la placa del sistema.  
**Paso 5**: Por último, el cargador de arranque localiza y carga una imagen de software del sistema operativo de IOS en la memoria y delega el control del switch a IOS.

1.1.2

### El comando boot system

Después de encender un switch Cisco, pasa por la siguiente secuencia de inicio de cinco pasos: Si no se establece esta variable, el switch intenta cargar y ejecutar el primer archivo ejecutable que puede encontrar. En los switches de la serie Catalyst 2960, el archivo de imagen generalmente se encuentra en un directorio que tiene el mismo nombre que el archivo de imagen (excepto la extensión de archivo .bin).

El sistema operativo IOS luego inicializa las interfaces utilizando los comandos Cisco IOS que se encuentran en el archivo de configuración de inicio. Se llama al archivo startup-config **config.text** y se encuentra en flash.

En el ejemplo, la variable de entorno BOOT se establece mediante el **boot system** comando del modo de configuración global. Observe que el IOS se ubica en una carpeta distinta y que se especifica la ruta de la carpeta. Use el comando **show boot** para ver en qué está configurado el archivo de arranque IOS actual.

```
S1(config)# boot system flash:/c2960-lanbasek9-mz.150-2.SE/c2960-lanbasek9-mz.150-2.SE.bin
```

La tabla define cada parte del comando **boot system**.

|Comando|Definición|
|---|---|
|**boot system**|El comando principal|
|**flash:**|The storage device|
|**c2960-lanbasek9-mz.150-2.SE/**|La ruta al sistema de archivos|
|**c2960-lanbasek9-mz.150-2.SE.bin**|El nombre del archivo IOS|

1.1.3

### Indicadores LED del switch

Los switches Cisco Catalyst tienen varios indicadores luminosos LED de estado. Puede usar los LED del switch para controlar rápidamente la actividad y el rendimiento del switch. Los diferentes modelos y conjuntos de características de los switches tienen diferentes LED, y la ubicación de estos en el panel frontal del switch también puede variar.

En la ilustración, se muestran los LED y el botón Mode de un switch Cisco Catalyst 2960.

La figura muestra los indicadores LED, el botón de modo y los puertos en la parte delantera izquierda de un interruptor. Los indicadores LED numerados 1 - 6 de arriba a abajo son: SYST, RPS, STAT, DUPLX, SPEED y PoE. Debajo de los indicadores LED y etiquetados 7 en la figura está el botón de modo. Por encima de los puertos de conmutación y etiquetados 8 en la figura están los LEDs de puerto.

![](https://contenthub.netacad.com/courses/srwe-dl/af9ea780-34fe-11eb-b1b2-9b1b0c1f7e0d/afb58ae1-34fe-11eb-b1b2-9b1b0c1f7e0d/assets/c9569b61-1c27-11ea-af09-3b2e6521927c.jpg)![](https://contenthub.netacad.com/courses/srwe-dl/af9ea780-34fe-11eb-b1b2-9b1b0c1f7e0d/afb58ae1-34fe-11eb-b1b2-9b1b0c1f7e0d/assets/c956c270-1c27-11ea-af09-3b2e6521927c.jpg)

El botón Modo (7 en la figura) se usa para alternar entre el estado del puerto, el dúplex del puerto, la velocidad del puerto y, si es compatible, el estado de la alimentación a través de Ethernet (PoE) de los LED del puerto (8 en la figura).

Haga clic en cada botón para aprender el propósito de los indicadores LED (1-6 en la figura), y el significado de sus colores:

#### SISTEMA

**LED del sistema**

Muestra si el sistema está recibiendo energía y funciona correctamente. Si el LED está apagado, significa que el sistema no está encendido. Si el LED es de color verde, el sistema funciona normalmente. Si el LED es de color ámbar, el sistema recibe alimentación pero no funciona correctamente.

#### RPS

**LED del sistema de alimentación redundante (RPS)**

Muestra el estado de RPS. Si el LED está apagado, el RPS está apagado o no está conectado correctamente. Si el LED es de color verde, el RPS está conectado y listo para proporcionar alimentación de respaldo. Si el LED parpadea y es de color verde, el RPS está conectado pero no está disponible porque está proporcionando alimentación a otro dispositivo. Si el LED es de color ámbar, el RPS está en modo de reserva o presenta una falla. Si el LED parpadea y es de color ámbar, la fuente de alimentación interna del switch presenta una falla, y el RPS está proporcionando alimentación.

#### ESTADÍSTICAS

**LED de estado del puerto**

Indica que el modo de estado del puerto está seleccionado cuando el LED está verde. Este es el modo predeterminado. Al seleccionarlo, los indicadores LED del puerto muestran colores con diferentes significados. Si el LED está apagado, no hay enlace, o el puerto estaba administrativamente inactivo. Si el LED es de color verde, hay un enlace presente. Si el LED parpadea y es de color verde, hay actividad, y el puerto está enviando o recibiendo datos. Si el LED alterna entre verde y ámbar, hay una falla en el enlace. Si el LED es de color ámbar, el puerto está bloqueado para asegurar que no haya un bucle en el dominio de reenvío y no reenvía datos (normalmente, los puertos permanecen en este estado durante los primeros 30 segundos posteriores a su activación). Si el LED parpadea y es de color ámbar, el puerto está bloqueado para evitar un posible bucle en el dominio de reenvío.

#### DUPLX

**LED de modo dúplex del puerto**

Indica que el modo dúplex del puerto está seleccionado cuando el LED está verde. Al seleccionarlo, los LED del puerto que están apagados están en modo semidúplex. Si el LED del puerto es de color verde, el puerto está en modo dúplex completo.

#### VELOCIDADES

**LED de velocidad del puerto**

Indica que el modo de velocidad del puerto está seleccionado. Al seleccionarlo, los indicadores LED del puerto muestran colores con diferentes significados. Si el LED está apagado, el puerto está funcionando a 10 Mbps. Si el LED es verde, el puerto está funcionando a 100 Mbps. Si el LED parpadea en verde, el puerto está funcionando a 1000 Mbps.

#### PoE

**LED de modo de alimentación por Ethernet**

Si se admite PoE, estará presente un LED de modo PoE. Si el LED está apagado, indica que no se seleccionó el modo de alimentación por Ethernet, que a ninguno de los puertos se le negó el suministro de alimentación y ninguno presenta fallas. Si el LED está parpadeando en ámbar, el modo PoE no está seleccionado, pero al menos uno de los puertos ha sido denegado o tiene una falla PoE. Si el LED es de color verde, indica que se seleccionó el modo de alimentación por Ethernet, y los LED del puerto muestran colores con diferentes significados. Si el LED del puerto está apagado, la alimentación por Ethernet está desactivada. Si el LED del puerto es de color verde, la alimentación por Ethernet está activada. Si el LED del puerto alterna entre verde y ámbar, se niega la alimentación por Ethernet, ya que, si se suministra energía al dispositivo alimentado, se excede la capacidad de alimentación del switch. Si el LED parpadea en ámbar, PoE está apagado debido a una falla. Si el LED es de color ámbar, se inhabilitó la alimentación por Ethernet para el puerto.

1.1.4

### Recuperarse de un bloqueo del sistema

El cargador de arranque proporciona acceso al switch si no se puede usar el sistema operativo debido a la falta de archivos de sistema o al daño de estos. El cargador de arranque tiene una línea de comandos que proporciona acceso a los archivos almacenados en la memoria flash.

Se puede acceder al cargador de arranque mediante una conexión de consola con los siguientes pasos:

**Paso 1**. Conecte una computadora al puerto de consola del switch con un cable de consola. Configure el software de emulación de terminal para conectarse al switch.  
**Paso 2**. Desconecte el cable de alimentación del switch.  
**Paso 3**. Vuelva a conectar el cable de alimentación al interruptor y, en 15 segundos, presione y mantenga presionado el botón **Mode** mientras el LED del sistema todavía parpadea en verde.  
**Paso 4**. Continúe presionando el botón **Mode** hasta que el LED del sistema se vuelva brevemente ámbar y luego verde sólido; luego suelte el botón **Mode**.  
**Paso 5**. The boot loader **switch:** El mensaje aparece en el software de emulación de terminal en la PC.

Escriba **help** o **?** en el símbolo del gestor de arranque para ver una lista de comandos disponibles.

De manera predeterminada, el switch intenta iniciarse automáticamente mediante el uso de información en la variable de entorno BOOT. Para ver la ruta de acceso de la variable de entorno BOOT del switch, escriba el comando **set**. A continuación, inicialice el sistema de archivos flash utilizando el comando **flash_init** para ver los archivos actuales en flash, como se muestra en la salida.

```js
switch: set
BOOT=flash:/c2960-lanbasek9-mz.122-55.SE7/c2960-lanbasek9-mz.122-55.SE7.bin
(output omitted)
switch: flash_init
Initializing Flash...
flashfs[0]: 2 files, 1 directories
flashfs[0]: 0 orphaned files, 0 orphaned directories
flashfs[0]: Total bytes: 32514048
flashfs[0]: Bytes used: 11838464
flashfs[0]: Bytes available: 20675584
flashfs[0]: flashfs fsck took 10 seconds.
...done Initializing Flash.
```

Después de que flash haya terminado de inicializar, puede ingresar el **dir flash:** comando para ver los directorios y archivos en flash, como se muestra en la salida.

```js
switch: dir flash: 
Directory of flash:/
    2  -rwx  11834846                 c2960-lanbasek9-mz.150-2.SE8.bin
    3  -rwx  2072                     multiple-fs
```

Introduzca el **BOOT=flash** comando para cambiar la ruta de la variable de entorno BOOT que utiliza el switch para cargar el nuevo IOS en flash. Para verificar la nueva ruta de la variable de entorno BOOT, vuelva a **set** ejecutar el comando. Finalmente, para cargar el nuevo IOS escriba el **boot** comando sin ningún argumento, como se muestra en la salida.

```js
switch: BOOT=flash:c2960-lanbasek9-mz.150-2.SE8.bin
switch: set
BOOT=flash:c2960-lanbasek9-mz.150-2.SE8.bin
(output omitted)
switch: boot
```

Los comandos del gestor de arranque admiten la inicialización de flash, el formateo de flash, la instalación de un nuevo IOS, el cambio de la variable de entorno BOOT y la recuperación de contraseñas pérdidas u olvidadas.

1.1.5

### Acceso a administración de switches

Para el acceso a la administración remota de un switch, este se debe configurar con una dirección IP y una máscara de subred. Tenga en cuenta que para administrar el switch desde una red remota, el switch debe configurarse con una puerta de enlace predeterminada. Este es un proceso muy similar a la configuración de la información de dirección IP en los dispositivos host. En la ilustración, se debe asignar una dirección IP a la interfaz virtual del switch (SVI) de S1. La SVI es una interfaz virtual, no un puerto físico del switch. Se utiliza un cable de consola para acceder a una PC de modo que el switch puede configurar específicamente.

switch con una conexión de red a un router y una conexión por cable de consola a un equipo host

2001:db8:acad:99::1/64172.17.99.1VLAN 99172.17.99.11/242001:db8:acad:99::11/64S1R1PC1R1

Cable de consola

1.1.6

### Ejemplo de Configuración de Switch SVI

De manera predeterminada, el switch está configurado para controlar su administración a través de la VLAN 1. Todos los puertos se asignan a la VLAN 1 de manera predeterminada. Por motivos de seguridad, se considera una práctica recomendada utilizar una VLAN distinta de la VLAN 1 para la VLAN de administración, como la VLAN 99 en el ejemplo.

Haga clic en cada botón para conocer los pasos para configurar el acceso a la administración del switch.

#### Paso 1

**Configuración de la interfaz de administración**

Desde el modo de configuración de la interfaz VLAN, se aplica una dirección IPv4 y una máscara de subred a la SVI de administración del switch.

**Nota**: El SVI para VLAN 99 no aparecerá como "activo / activo" hasta que se cree VLAN 99 y haya un dispositivo conectado a un puerto de switch asociado con VLAN 99.

**Nota**:Es posible que el switch debata configurar para IPv6. Por ejemplo, antes de que pueda configurar el direccionamiento IPv6 en un Cisco Catalyst 2960 que ejecute IOS versión 15.0, deberá ingresar el comando de configuración global **sdm prefer dual-ipv4-and-ipv6 default** y, a continuación, **reload** el switch.

TaskIOSIntroduzca el modo de configuración global.s1configurar TerminalEnter# configurar TerminalEnter modo de configuración de interfaz para el SVI.S1(config)# interfaz vlan 99 Configure la dirección IPv4 de la interfaz de administración. S1(config-if)#dirección IP 172.17.99.11 255.255.255.0 Configuración de la interfaz de administración IPv6 addressS1(config-if)# ipv6 address 2001:db8:acad:99: :1/64Habilite el interfaz de administración. S1(config-if)# sin apagarVolver al EXEC privilegiado mode.S1(config-if)# endSave the running config to the startup config.S1# copy running-config startup-config

|**Tarea**|**Comandos IOS**|
|---|---|
|Ingrese al modo de configuración global.|S1# **configure terminal**|
|Ingrese al modo de configuración de interfaz para la SVI.|S1(config)# **interface vlan 99**|
|Configure la dirección IPv4 de la interfaz de administración.|S1(config-if)# **ip address 172.17.99.11 255.255.255.0**|
|Configure la dirección IPv6 de la interfaz de administración|S1(config-if)# **ipv6 address 2001:db8:acad:99::1/64**|
|Habilite la interfaz de administración.|S1(config-if)# **no shutdown**|
|Vuelva al modo EXEC privilegiado.|S1(config-if)# **end**|
|Guarde la configuración en ejecución en la configuración de inicio.|S1# **copy running-config startup-config**|


#### Paso 2

**Configuración del gateway predeterminado**

Si el switch se va a administrar de forma remota desde redes que no están conectadas directamente, se debe configurar con un gateway predeterminado.

**Nota**: Dado que recibirá la información de la puerta de enlace predeterminada de un mensaje de anuncio de router (RA), el switch no requiere una puerta de enlace predeterminada IPv6.

| **Tarea**                                                           | **Comandos IOS**                               |
| ------------------------------------------------------------------- | ---------------------------------------------- |
| Ingrese al modo de configuración global.                            | S1# **configure terminal**                     |
| Configure el gateway predeterminado para el switch.                 | S1(config)# **ip default-gateway 172.17.99.1** |
| Vuelva al modo EXEC privilegiado.                                   | S1(config-if)# **end**                         |
| Guarde la configuración en ejecución en la configuración de inicio. | S1# **copy running-config startup-config**     |

#### Paso 3

**Verificar la configuración**

Los **show ip interface brief** comandos **show ipv6 interface brief** y son útiles para determinar el estado de las interfaces físicas y virtuales. La información que se muestra confirma que la interfaz VLAN 99 se ha configurado con una dirección IPv4 e IPv6.

**Nota**: Una dirección IP aplicada al SVI es solo para el acceso de administración remota al switch; esto no permite que el switch enrute paquetes de Capa 3.

```js
S1# show ip interface brief
Interface IP-Address OK? Method Status Protocol
Vlan99 172.17.99.11 SÍ manual hacia abajo
(resultado omitido)
S1# show ipv6 interface brief
Vlan99 [abajo/abajo]
    FE80: :C27B:BCFF:FEC4:A9C1
    2001:DB8:ACAD:99: :1
(resultado omitido)
```

1.1.7

### Práctica de laboratorio: configuración básica de un switch

###### Oportunidad de Práctica de habilidades

Tendrá la oportunidad de practicar las siguientes habilidades:

- Part 1: Tender el cableado de red y verificar la configuración predeterminada del switch
- Part 2: Configurar los parámetros básicos de los dispositivos de red
- Part 3: Verificar y probar la conectividad de red

Podrá practicar estas habilidades usando Packet Tracer o equipo de laboratorio, de estar disponible.

**Packet Tracer - Physical Mode (PTPM)**

 Configuración básica del switch - Modo Físico

![[docs/cisco-academy/CCNA 2 v7/modulos/Módulos 1 - 4 Conceptos de Switching, VLANs y enrutamiento entre redes VLAN/ANEXOS/1.1.7-packet-tracer---basic-switch-configuration---physical-mode_es-XL.pka]]

---
## Configuración de puertos de un switch

1.2.1

### Comunicación dúplex

Los puertos de un switch se pueden configurar de forma independiente para diferentes necesidades. En este tema se describe cómo configurar los puertos del switch, cómo verificar las configuraciones, errores comunes y cómo solucionar problemas de configuración del switch.

La comunicación en dúplex completo aumenta el ancho de banda eficaz al permitir que ambos extremos de una conexión transmitan y reciban datos simultáneamente. Esto también se conoce como comunicación bidireccional y requiere microsegmentación. Las LAN microsegmentadas se crean cuando un puerto de switch tiene solo un dispositivo conectado y funciona en modo dúplex completo. Cuando un puerto de switch opera en modo dúplex completo, no hay dominio de colisión conectado al puerto.

A diferencia de la comunicación en dúplex completo, la comunicación en semidúplex es unidireccional. La comunicación en semidúplex genera problemas de rendimiento debido a que los datos fluyen en una sola dirección por vez, lo que a menudo provoca colisiones. Las conexiones semidúplex suelen verse en los dispositivos de hardware más antiguos, como los hubs. La comunicación en dúplex completo reemplazó a la semidúplex en la mayoría del hardware.

En la ilustración, se muestra la comunicación en dúplex completo y semidúplex.

La figura ilustra la diferencia entre las comunicaciones full-duplex y half-duplex entre dos switches. El diagrama en la parte superior muestra dúplex completo con flechas en ambas direcciones en el enlace entre los dos interruptores con el texto: Enviar Y recibir, simultáneamente. El diagrama inferior muestra semidúplex con sólo una flecha que fluye de un interruptor a otro con el texto: Enviar OR recibir.

PC4

Comunicación dúplex completoComunicación semidúplexEnvió Y recepción simultáneosEnvío O recepción

Gigabit Ethernet y NIC de 10 Gb requieren conexiones full-duplex para funcionar. En el modo dúplex completo, el circuito de detección de colisiones de la NIC se encuentra inhabilitado. Dúplex completo ofrece el 100% de eficacia en ambas direcciones (transmisión y recepción). Esto da como resultado una duplicación del uso potencial del ancho de banda establecido.

1.2.2

### Configuración de puertos de switch en la capa física

Los puertos de switch se pueden configurar manualmente con parámetros específicos de dúplex y de velocidad. Use el comando duplex del modo de configuración de interfaz **duplex** para especificar manualmente el modo dúplex de un puerto de switch. Use el **speed** comando del modo de configuración de la interfaz para especificar manualmente la velocidad. Por ejemplo, ambos switches de la topología deben funcionar siempre en dúplex completo a 100 Mbps.

topología de red que muestra una conexión entre dos switches que funcionan en modo dúplex completo a 100/Mpbs

PC1PC2S1S2F0/18F0/1F0/1

Full-Duplex Mode 100/Mbps.Full-Duplex Mode 100/Mbps.

La tabla muestra los comandos para S1. Los mismos comandos se pueden aplicar a S2.

TaskIOSIntroduzca el modo de configuración global.s1configurar TerminalEnter# configurar TerminalEnter modo de configuración de interfaz. S1(config)# interfaz FastEthernet 0/1Configurar el dúplex de interfaz. S1(config-if)# dúplex completoConfigurar la interfaz velocidad. S1(config-if)# velocidad 100Volver al EXEC privilegiado mode.S1(config-if)# endSave the running config to the startup config.S1# copy running-config startup-config

|**Tarea**|**Comandos IOS**|
|---|---|
|Ingrese al modo de configuración global.|S1# **configure terminal**|
|Ingrese el modo de configuración de interfaz.|S1(config)# **interface FastEthernet 0/1**|
|Configure el modo dúplex de la interfaz.|S1(config-if)# **duplex full**|
|Configure la velocidad de la interfaz.|S1(config-if)# **speed 100**|
|Vuelva al modo EXEC privilegiado.|S1(config-if)# **end**|
|Guarda la configuración en ejecución en la configuración de inicio.|S1# **copy running-config startup-config**|

La configuración predeterminada de dúplex y velocidad para los puertos de switch en los switches Cisco Catalyst 2960 y 3560 es automática. Los puertos 10/100/1000 funcionan en modo semidúplex o semidúplex cuando están configurados en 10 o 100 Mbps y operan solo en modo dúplex completo cuando está configurado en 1000 Mbps (1 Gbps). La negociación automática es útil cuando la configuración de velocidad y dúplex del dispositivo que se conecta al puerto es desconocida o puede cambiar. Cuando se conecta a dispositivos conocidos como servidores, estaciones de trabajo dedicadas o dispositivos de red, la mejor práctica es establecer manualmente la configuración de velocidad y dúplex.

Cuando se solucionan problemas relacionados con el puerto del switch, es importante que se verifique la configuración de dúplex y velocidad.

**Nota**: Si la configuración para el modo dúplex y la velocidad de puertos del switch presenta incompatibilidades, se pueden producir problemas de conectividad. Una falla de autonegociación provoca incompatibilidades en la configuración.

Todos los puertos de fibra óptica, como los puertos 1000BASE-SX, solo funcionan a una velocidad predefinida y siempre son dúplex completo.

1.2.3

### Auto-MDIX (MDIX automático)

Hasta hace poco, se requerían determinados tipos de cable (cruzado o directo) para conectar dispositivos. Las conexiones switch a switch o switch a router requerían el uso de diferentes cables Ethernet. Mediante el uso de la característica automática de conexión cruzada de interfaz dependiente del medio (auto-MDIX) en una interfaz, se elimina este problema. Al habilitar la característica auto-MDIX, la interfaz detecta automáticamente el tipo de conexión de cable requerido (directo o cruzado) y configura la conexión conforme a esa información. Al conectarse a los switches sin la función auto-MDIX, los cables directos deben utilizarse para conectar a dispositivos como servidores, estaciones de trabajo o routers. Los cables cruzados se deben utilizar para conectarse a otros switches o repetidores.

Con la característica auto-MDIX habilitada, se puede usar cualquier tipo de cable para conectarse a otros dispositivos, y la interfaz se ajusta de manera automática para proporcionar comunicaciones satisfactorias. En los switches Cisco más nuevos, el comando **mdix auto** del modo de configuración de interfaz habilita la función. Al usar auto-MDIX en una interfaz, la velocidad de la interfaz y el dúplex deben configurarse para que la función **auto** funcione correctamente.

El comando para habilitar Auto-MDIX se emite en el modo de configuración de interfaz en el switch como se muestra:

```
S1(config-if)# mdix auto
```

**Nota**: La función auto-MDIX está habilitada de manera predeterminada en los switches Catalyst 2960 y Catalyst 3560, pero no está disponible en los switches Catalyst 2950 y Catalyst 3550 anteriores.

Para examinar la configuración de auto-MDIX para una interfaz específica, use el comando **show controllers ethernet-controller** con la palabra clave **phy**. Para limitar la salida a líneas que hagan referencia a auto-MDIX, use el filtro **include Auto-MDIX** Como se muestra el resultado indica On (Habilitada) u Off (Deshabilitada) para la característica.

```
S1# show controllers ethernet-controller fa0/1 phy | include MDIX
 Auto-MDIX           :  On   [AdminState=1   Flags=0x00052248]
```

1.2.4

### Switch Verification Commands

En la tabla se resumen algunos de los comandos de verificación de conmutación más útiles.

Comandos de TaskiOS Mostrar el estado de la interfaz y configuración.s1# mostrar interfaces [interface-id] Mostrar la configuración de inicio actual.s1# mostrar Startup-ConfigDisplay actual en funcionamiento Config.s1# mostrar running-config Muestra información sobre el sistema de archivos flash..S1# show estado del software y hardware del sistema flashDisplay.S1# show versionDisplay historial del comando ingresado.S1# show historyMostrar información IP acerca de un Interface.s1# show ip interface [interface-id] Mostrar la dirección MAC table.S1# show mac-address-tableORS1# show mac address-table

|**Tarea**|**Comandos IOS**|
|---|---|
|Muestra el estado y la configuración de la interfaz.|S1# **show interfaces** [_interface-id_]|
|Muestra la configuración de inicio actual.|S1# **show startup-config**|
|Muestra la configuración actual en ejecución.|S1# **show running-config**|
|Muestra información sobre el sistema de archivos flash.|S1# **show flash**|
|Muestra el estado del hardware y el software del sistema.|S1# **show version**|
|Muestra la configuración actual en ejecución.|S1# **show history**|
|Muestra información de IP de una interfaz.|S1# **show ip interface** [_interface-id_]<br><br>O<br><br>S1# **show ipv6 interface** [_interface-id_]|
|Muestra la tabla de direcciones MAC.|S1# **show mac-address-table**<br><br>O<br><br>S1# **show mac address-table**|

1.2.5

### Verificar la configuración de puertos del switch.

El comando **show running-config** se puede usar para verificar que el switch se haya configurado correctamente. De la salida abreviada de muestra en S1, se muestra alguna información importante en la figura:

- La interfaz Fast Ethernet 0/18 se configura con la VLAN de administración 99
- La VLAN 99 está configurada con una dirección IPv4 de 172.17.99.11 255.255.255.0
- La puerta de enlace predeterminada está establecida en 172.17.99.1

```js
S1# show running-config
Building configuration...
Current configuration : 1466 bytes
!
interface FastEthernet0/18
 switchport access vlan 99
 switchport mode access
!
(output omitted)
!
interface Vlan99
 ip address 172.17.99.11 255.255.255.0
 ipv6 address 2001:DB8:ACAD:99::1/64
!
ip default-gateway 172.17.99.1 
```

El comando **show interfaces** es otro comando de uso común, que muestra información de estado y estadísticas en las interfaces de red del switch. El comando **show interfaces** se usa con frecuencia al configurar y monitorear dispositivos de red.

La primera línea de salida para el comando **show interfaces fastEthernet 0/18** indica que la interfaz FastEthernet 0/18 está activa / activa, lo que significa que está operativa. Más abajo en el resultado, se muestra que el modo dúplex es full (completo) y la velocidad es de 100 Mb/s.

```js
S1# show interfaces fastEthernet 0/18
FastEthernet0/18 is up, line protocol is up (connected)
  Hardware is Fast Ethernet, address is 0025.83e6.9092 (bia 0025.83e6.9092)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100BaseTX
```

1.2.6

### Problemas de la capa de acceso a la red

El resultado del comando **show interfaces** es útil para detectar problemas comunes de medios. Una de las partes más importantes de esta salida es la visualización de la línea y el estado del protocolo de enlace de datos, como se muestra en el ejemplo.

```js
S1# show interfaces fastEthernet 0/18
FastEthernet0/18 is up, line protocol is up (connected)
Hardware is Fast Ethernet, address is 0025.83e6.9092 (bia 0025.83e6.9092)MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec,
```

El primer parámetro (FastEthernet0 / 18 está activo) se refiere a la capa de hardware e indica si la interfaz está recibiendo una señal de detección de portadora. El segundo parámetro (line protocol is up) se refiere a la capa de enlace de datos e indica si se reciben los keepalives del protocolo de capa de enlace de datos.

Según el resultado del comando **show interfaces**, los posibles problemas se pueden solucionar de la siguiente manera:

- Si la interfaz está activa y el protocolo de línea está inactivo, hay un problema. Puede haber una incompatibilidad en el tipo de encapsulación, la interfaz en el otro extremo puede estar inhabilitada por errores o puede haber un problema de hardware.
- Si el protocolo de línea y la interfaz están inactivos, no hay un cable conectado o existe algún otro problema de interfaz. Por ejemplo, en una conexión directa, el otro extremo de la conexión puede estar administrativamente inactivo.
- If the interface is administratively down, it has been manually disabled (the **** shutdown) en la configuración activa.

El resultado del comando **show interfaces** muestra contadores y estadísticas para la interfaz Fastethernet0/18, como se destaca en el ejemplo.

```js
S1# show interfaces fastEthernet 0/18
FastEthernet0/18 is up, line protocol is up (connected)
  Hardware is Fast Ethernet, address is 0025.83e6.9092 (bia 0025.83e6.9092)
  MTU 1500 bytes, BW 100000 Kbit/sec, DLY 100 usec,
     reliability 255/255, txload 1/255, rxload 1/255
  Encapsulation ARPA, loopback not set
  Keepalive set (10 sec)
  Full-duplex, 100Mb/s, media type is 10/100BaseTX
  input flow-control is off, output flow-control is unsupported
  ARP type: ARPA, ARP Timeout 04:00:00
  Last input never, output 00:00:01, output hang never
  Last clearing of "show interface" counters never
  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0
  Queueing strategy: fifo
  Output queue: 0/40 (size/max)
  5 minute input rate 0 bits/sec, 0 packets/sec
  5 minute output rate 0 bits/sec, 0 packets/sec
     2295197 packets input, 305539992 bytes, 0 no buffer
     Received 1925500 broadcasts (74 multicasts)
     0 runts, 0 giants, 0 throttles
     3 input errors, 3 CRC, 0 frame, 0 overrun, 0 ignored
     0 watchdog, 74 multicast, 0 pause input
     0 input packets with dribble condition detected
     3594664 packets output, 436549843 bytes, 0 underruns
     8 output errors, 0 collisions, 10 interface resets
     0 unknown protocol drops
     0 babbles, 235 late collision, 0 deferred
```

Algunos errores de los medios no son lo suficientemente graves como para hacer que el circuito falle, pero causan problemas de rendimiento de la red. La tabla explica algunos de estos errores comunes que se pueden detectar con el comando **show interfaces**.

Tipo de errorDescriptionError de entradaNúmero total de errores. Incluye runas, gigantes, sin búfer, CRC, frame, overrun e ignorado recuentos. se descartan porque son más pequeños que el tamaño mínimo de paquete para Medio Por ejemplo, cualquier paquete de Ethernet que tenga menos de 64 bytes es considera un runt.GiantsPackets que se descartan porque superan el valor tamaño máximo del paquete para el medio. Por ejemplo, cualquier paquete Ethernet que sea mayor que 1,518 bytes se considera un giant.CrcCRC errores se generan cuando la suma de verificación calculada no es la misma que la suma de verificación recibida. Errores Suma de todos los errores que impidieron la transmisión final de datagramas fuera de la interfaz que se está examinando.CollisionsNúmero de mensajes retransmitido debido a una colisión Ethernet. Colisiones tardíasUna colisión eso ocurre después de que se hayan transmitido 512 bits de la trama.

|**Tipo de error**|**Descripción**|
|---|---|
|**Errores de entrada**|Cantidad total de errores. Incluye runts, gigantes, sin buffer, CRC, , desbordamiento y recuentos ignorados.|
|**Fragmentos de colisión**|Paquetes que se descartan porque son más pequeños que el mínimo tamaño del paquete para el medio. Por ejemplo, cualquier paquete Ethernet que sea menos de 64 bytes se considera un runt.|
|**Gigantes**|Paquetes que se descartan porque exceden el tamaño máximo de paquete para el medio. Por ejemplo, cualquier paquete de Ethernet que sea mayor que 1.518 bytes se considera un gigante.|
|**CRC**|Los errores de CRC se generan cuando la suma de comprobación calculada no es la misma que la suma de comprobación recibida.|
|**Errores de salida**|Suma de todos los errores que impidieron la transmisión final de datagramas de la interfaz que se está examinando.|
|**Colisiones**|Cantidad de mensajes retransmitidos debido a una colisión de Ethernet.|
|**Colisiones tardías**|Una colisión que ocurre después de 512 bits de la trama han sido Transmitido|

1.2.7

### Errores de entrada y salida de interfaz

“Input errors” indica la suma de todos los errores en los datagramas que se recibieron en la interfaz que se analiza. Estos incluyen los recuentos de fragmentos de colisión, de fragmentos gigantes, de los que no están almacenados en buffer, de CRC, de tramas, de saturación y de ignorados. Los errores de entrada informados del comando **show interfaces** incluyen lo siguiente:

- **Runt Frames** - las tramas Ethernet que son más cortas que la longitud mínima permitida de 64 bytes se llaman runts. La NIC en mal funcionamiento son la causa habitual de las tramas excesivas de fragmentos de colisión, pero también pueden deberse a colisiones.
- **Giants** -Las tramas de Ethernet que son más grandes que el tamaño máximo permitido se llaman gigantes.
- **CRC errors** -En las interfaces Ethernet y serie, los errores de CRC generalmente indican un error de medios o cable. Las causas más comunes incluyen interferencia eléctrica, conexiones flojas o dañadas o cableado incorrecto. Si aparecen muchos errores de CRC, hay demasiado ruido en el enlace, y se debe examinar el cable. También se deben buscar y eliminar las fuentes de ruido.

“Output errors” es la suma de todos los errores que impiden la transmisión final de los datagramas por la interfaz que se analiza. Los errores de salida informados del comando **show interfaces** incluyen lo siguiente:

- **Colisión** - Las colisiones en operaciones half-duplex son normales. Sin embargo, nunca debe observar colisiones en una interfaz configurada para la comunicación en dúplex completo.
- **Colisiones tardías** -Una colisión tardía se refiere a una colisión que ocurre después de que se han transmitido 512 bits de la trama. La longitud excesiva de los cables es la causa más frecuente de las colisiones tardías. Otra causa frecuente es la configuración incorrecta de dúplex. Por ejemplo, el extremo de una conexión puede estar configurado para dúplex completo y el otro para semidúplex. Las colisiones tardías se verían en la interfaz que está configurada para semidúplex. En ese caso, debe configurar los mismos parámetros de dúplex en ambos extremos. Una red diseñada y configurada correctamente nunca debería tener colisiones tardías.

1.2.8

### Resolución de problemas de la capa de acceso a la red

La mayoría de los problemas que afectan a las redes conmutadas se produce durante la implementación inicial. En teoría, una vez instaladas, las redes continúan funcionando sin problemas. Sin embargo, los cables se dañan, la configuración cambia, y se conectan al switch nuevos dispositivos que requieren cambios de configuración en este. Se requiere el mantenimiento y la resolución de problemas de infraestructura de la red de forma permanente.

Una colisión tardía se refiere a una colisión que ocurre después de que se han transmitido 512 bits de la trama.

![[Pasted image 20241212094103.png]]
Utilice el comando **show interfaces** para verificar el estado de la interfaz.

Si la interfaz está inactiva, realice lo siguiente:

- Verifique que se usen los cables adecuados. Además, revise los cables y los conectores para detectar daños. Si se sospecha que hay un cable defectuoso o incorrecto, reemplácelo.
- Si la interfaz continúa inactiva, el problema puede deberse a una incompatibilidad en la configuración de velocidad. La velocidad de una interfaz generalmente se negocia automáticamente; por lo tanto, incluso si se aplica manualmente a una interfaz, la interfaz de conexión debe negociarse automáticamente en consecuencia. Si se produce una incompatibilidad de velocidad debido a una configuración incorrecta o a un problema de hardware o de software, esto podría provocar que la interfaz quede inactiva. Establezca manualmente la misma velocidad en ambos extremos de la conexión si se sospecha que hay un problema.

Si la interfaz está activa pero aún hay problemas de conectividad, realice lo siguiente:

- Using the **comando show interfaces** , verifique si hay indicios de ruido excesivo. Los indicios pueden incluir un aumento en los contadores de fragmentos de colisión, de fragmentos gigantes y de errores de CRC. Si hay un exceso de ruido, primero busque el origen del ruido y, si es posible, elimínelo. Además, verifique qué tipo de cable se utiliza y que el cable no supere la longitud máxima.
- Si no hay problemas de ruido, verifique si hay un exceso de colisiones. Si hay colisiones o colisiones tardías, verifique la configuración de dúplex en ambos extremos de la conexión. Al igual que la configuración de velocidad, la configuración dúplex generalmente se negocia automáticamente. Si parece haber una diferencia entre dúplex, configure manualmente el dúplex como full (completo) en ambos extremos de la conexión.

---
## Acceso remoto seguro

1.3.1

### Operación Telnet

Es posible que no siempre tenga acceso directo al switch cuando necesite configurarlo. Necesita poder acceder a él de forma remota y es imperativo que su acceso sea seguro. En este tema se explica cómo configurar Secure Shell (SSH) para el acceso remoto. Una actividad Packet Tracer le da la oportunidad de probar esto usted mismo.

Telnet utiliza el puerto TCP 23. Es un protocolo más antiguo que utiliza la transmisión de texto sin formato segura tanto de la autenticación de inicio de sesión (nombre de usuario y contraseña) como de los datos transmitidos entre los dispositivos de comunicación. Un actor de amenazas puede monitorear paquetes usando Wireshark. Por ejemplo, en la figura, el actor de amenazas capturó el nombre de usuario **admin** y la contraseña **ccna** de una sesión Telnet.

captura de pantalla de una captura `WireShark` de una sesión Telnet que muestra el nombre de usuario y la contraseña enviados en texto sin formato

![[Pasted image 20241212094357.png]]

1.3.2

### Funcionamiento de SSH

Secure Shell (SSH) es un protocolo seguro que utiliza el puerto TCP 22. Proporciona una conexión de administración segura (encriptada) a un dispositivo remoto. El SSH debe reemplazar a Telnet para las conexiones de administración. SSH proporciona seguridad para las conexiones remotas mediante el cifrado seguro cuando se autentica un dispositivo (nombre de usuario y contraseña) y también para los datos transmitidos entre los dispositivos que se comunican.

Por ejemplo, la figura muestra una captura Wireshark de una sesión SSH. Proporciona una conexión de administración segura (encriptada) a un dispositivo remoto. Sin embargo, a diferencia de Telnet, con SSH el nombre de usuario y la contraseña están cifrados.

captura de pantalla de una captura WireShark de una sesión SSH que muestra el nombre de usuario y la contraseña están cifrados

![[Pasted image 20241212094434.png]]

1.3.3

### Verifique que el switch admita SSH

Para habilitar SSH en un switch Catalyst 2960, el switch debe usar una versión del software IOS que incluya características y capacidades criptográficas (cifradas). Utilice el comando **show version** del switch para ver qué IOS está ejecutando el switch. Un nombre de archivo de IOS que incluye la combinación «k9» admite características y capacidades criptográficas (cifradas). El ejemplo muestra la salida del comando **show version**.

```
S1# show version
Cisco IOS Software, C2960 Software (C2960-LANBASEK9-M), Version 15.0(2)SE7, RELEASE SOFTWARE (fc1)
```

1.3.4

### Configuración de SSH

Antes de configurar SSH, el switch debe tener configurado, como mínimo, un nombre de host único y los parámetros correctos de conectividad de red.

Haga clic en cada botón para aprender los pasos para configurar SSH.

#### Paso 1
**Verifique support SSH.**

Use el comando **show ip ssh** para verificar que el switch sea compatible con SSH. Si el switch no ejecuta un IOS que admita características criptográficas, este comando no se reconoce.

```
S1#  show ip ssh
```

#### Paso 2
**Configure el IP domain.**

Configure el nombre de dominio IP de la red utilizando el comando **ip domain-name** _domain-name_ modo de configuración global. En la figura, el valor _domain-name_ es **cisco.com**.

```
S1(config)# ip domain-name cisco.com
```

#### Paso 3
**Genere un par de claves RSA.**

No todas las versiones del IOS utilizan la versión 2 de SSH de manera predeterminada, y la versión 1 de SSH tiene fallas de seguridad conocidas. Para configurar SSH versión 2, emita el comando del modo de configuración global **ip ssh version 2**. La creación de un par de claves RSA habilita SSH automáticamente. Use el comando del modo de configuración global **crypto key generate rsa**, para habilitar el servidor SSH en el switch y generar un par de claves RSA. Al crear claves RSA, se solicita al administrador que introduzca una longitud de módulo. La configuración de ejemplo en la figura 1 utiliza un tamaño de módulo de 1024 bits. Una longitud de módulo mayor es más segura, pero se tarda más en generarlo y utilizarlo.

**Nota**:Para eliminar el par de claves RSA, use el comando del modo de configuración global **crypto key zeroize rsa**. Después de eliminarse el par de claves RSA, el servidor SSH se deshabilita automáticamente.

```
S1(config)# crypto key generate rsa
How many bits in the modulus [512]: 1024
```

#### Paso 4
**Configure autenticación de usuarios.**

El servidor SSH puede autenticar a los usuarios localmente o con un servidor de autenticación. Para usar el método de autenticación local, cree un par de nombre de usuario y contraseña con el comando **username** _username_ **secret** _password_ modo de configuración global. En el ejemplo, se asignó la contraseña ccna al usuario admin.

```
S1(config)# username admin secret ccna
```

#### Paso 5
**Configure las lineas vty.**

Habilite el protocolo SSH en las líneas vty utilizando el comando del modo de configuración de línea **transport input ssh**. El switch Catalyst 2960 tiene líneas vty que van de 0 a 15. Esta configuración evita las conexiones que no son SSH (como Telnet) y limita al switch a que acepte solo las conexiones SSH. Use el comando **line vty** del modo de configuración global y luego el comando **login local** del modo de configuración de línea para requerir autenticación local para las conexiones SSH de la base de datos de nombre de usuario local.

```
S1(config)# line vty 0 15
S1(config-line)# transport input ssh
S1(config-line)# login local
S1(config-line)# salida
```

#### Paso 6
**EHabilite SSH versión 2.**

De manera predeterminada, SSH admite las versiones 1 y 2. Al admitir ambas versiones, esto se muestra en la salida **show ip ssh** como compatible con la versión 2. Habilite la versión SSH utilizando el comando de configuración global **ip ssh version 2**.

```
S1(config)# ip ssh version 2
```

1.3.5

### Verifique que SSH esté operativo

En las computadoras se usa un cliente SSH, como PuTTY, para conectarse a un servidor SSH. Por ejemplo, suponga que se configura lo siguiente:

- SSH está habilitado en el interruptor S1
- Interfaz VLAN 99 (SVI) con la dirección IPv4 172.17.99.11 en el switch S1.
- PC1 con la dirección IPv4 172.17.99.21.

La figura muestra la configuración de PuTTy para PC1 para iniciar una conexión SSH a la dirección SVI VLAN IPv4 de S1.

La figura muestra un host conectado a un switch y la configuración PuTTY para iniciar una conexión SSH al SVI del switch. El PC1 del host, con dirección 172.17.99.21, tiene una conexión de red a un switch S1, con dirección 172.17.99.11. Una captura de pantalla de la configuración PuTTY en PC1 muestra la dirección 172.17.99.11 introducida en el cuadro bajo Nombre de host (o dirección IP) y 22 introducida en el cuadro bajo Puerto. SSH se ha seleccionado como el tipo de conexión.

172.17.99.11172.17.99.21PC1S1

![[Pasted image 20241212094711.png]]

Cuando está conectado, se solicita al usuario un nombre de usuario y una contraseña como se muestra en el ejemplo. Usando la configuración del ejemplo anterior, se ingresan el nombre de usuario: **admin** y la contraseña: **ccna** Después de ingresar la combinación correcta, el usuario se conecta a través de SSH a la interfaz de línea de comando (CLI) en el switch Catalyst 2960.

```
Login as: admin
Using keyboard-interactive
Authentication.
Password:
S1> enable
Password: 
S1#
```

Para mostrar los datos de la versión y de configuración de SSH en el dispositivo que configuró como servidor SSH, use el comando **show ip ssh**. En el ejemplo, se habilitó la versión 2 de SSH.

```
S1# show ip ssh
SSH Enabled - version 2.0
Authentication timeout: 120 secs; Authentication retries: 3
To check the SSH connections to the device, use the show ssh command as shown.
S1# show ssh
%No SSHv1 server connections running.
Connection Version Mode Encryption  Hmac                State          Username
0          2.0     IN   aes256-cbc  hmac-sha1    Session started       admin
0          2.0     OUT  aes256-cbc  hmac-sha1    Session started       admin
S1#
```

1.3.6

### Packet Tracer - Configurar SSH

SSH debe reemplazar a Telnet para las conexiones de administración. Telnet usa comunicaciones inseguras de texto no cifrado. SSH proporciona seguridad para las conexiones remotas mediante el cifrado seguro de todos los datos transmitidos entre los dispositivos. En esta actividad, protegerá un switch remoto con el cifrado de contraseñas y SSH.

 Configuración de SSH
![[1.3.6-packet-tracer---configure-ssh_es-XL.pka]]

---
## Configuración básica de un router

1.4.1

### Configuración de parámetros básicos del router

Hasta ahora, este módulo solo ha cubierto switches. Si desea que los dispositivos puedan enviar y recibir datos fuera de su red, deberá configurar routeres. En este tema se enseña la configuración básica del router y se proporcionan dos Comprobadores de sintaxis y una actividad de Rastreador de paquetes para que pueda practicar estas habilidades.

Los routers y switches Cisco tienen muchas similitudes. Admiten sistemas operativos modales y estructuras de comandos similares, así como muchos de los mismos comandos. Además, los pasos de configuración inicial son similares para ambos dispositivos. Por ejemplo, las siguientes tareas de configuración siempre deben realizarse. Asigne un nombre al dispositivo para distinguirlo de otros routeres y configure contraseñas, como se muestra en el ejemplo.

```js
Router# configure terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)# hostname R1
R1(config)# enable secret class
R1(config)# line console 0
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
R1(config)# line vty 0 4
R1(config-line)# password cisco
R1(config-line)# login
R1(config-line)# exit
R1(config)# service password-encryption
R1(config)#
```

Configure un banner para proporcionar notificaciones legales de acceso no autorizado, como se muestra en el ejemplo.

```js
R1(config)# banner motd #Authorized Access Only!#
R1(config)#
```

Guarde los cambios en un router, como se muestra en el ejemplo.

```js
R1# copy running-config startup-config
Destination filename [startup-config]? 
Building configuration...
[OK]
```

### Topología de doble pila

Una característica que distingue a los switches de los routers es el tipo de interfaces que admite cada uno. Por ejemplo, los switches de capa 2 admiten LAN; por lo tanto, tienen múltiples puertos FastEthernet o Gigabit Ethernet. La topología de pila dual de la figura se utiliza para demostrar la configuración de las interfaces IPv4 e IPv6 del router.

topología de red de doble pila que consta de múltiples hosts, switches y routeres con interfaces configuradas con direcciones IPv4 e IPv6

![[Pasted image 20241212105616.png]]

1.4.4

### Configurar interfaces de routers

Los routers admiten redes LAN y WAN, y pueden interconectar distintos tipos de redes; por lo tanto, admiten muchos tipos de interfaces. Por ejemplo, los ISR G2 tienen una o dos interfaces Gigabit Ethernet integradas y ranuras para tarjetas de interfaz WAN de alta velocidad (HWIC) para admitir otros tipos de interfaces de red, incluidas las interfaces seriales, DSL y de cable.

Para que una interfaz esté disponible, debe cumplir los siguientes requisitos:

- **Configurado con al menos una dirección IP:** - Utilice los comandos de configuración de **ip address** _ip-address subnet-mask_ y **ipv6 address** _ipv6-address/prefix_ interface.
- **Activado:** - Las interfaces LAN y WAN no están activadas de manera predeterminada (shutdown). Para habilitar una interfaz, esta se debe activar mediante el comando **no shutdown**. (Es como encender la interfaz.) La interfaz también debe estar conectada a otro dispositivo (un hub, un switch u otro router) para que la capa física se active.
- **Descripción** - Opcionalmente, la interfaz también se puede configurar con una breve descripción de hasta 240 caracteres. Es aconsejable configurar una descripción en cada interfaz. En las redes de producción, los beneficios de las descripciones de la interfaz se obtienen rápidamente, ya que son útiles para solucionar problemas e identificar una conexión de terceros y la información de contacto.

El siguiente ejemplo muestra la configuración de las interfaces en R1.

```js
R1(config)# interface gigabitethernet 0/0/0
R1(config-if)# ip address 192.168.10.1 255.255.255.0 
R1(config-if)# ipv6 address 2001:db8:acad:1::1/64 
R1(config-if)# description Link to LAN 1
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface gigabitethernet 0/0/1
R1(config-if)# ip address 192.168.11.1 255.255.255.0 
R1(config-if)# ipv6 address 2001:db8:acad:2::1/64 
R1(config-if)# description Link to LAN 2
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)# interface serial 0/0/0
R1(config-if)# ip address 209.165.200.225 255.255.255.252 
R1(config-if)# ipv6 address 2001:db8:acad:3::225/64 
R1(config-if)# description Link to R2
R1(config-if)# no shutdown
R1(config-if)# exit
R1(config)#
```

1.4.5
### Interfaces de bucle invertido IPv4

Otra configuración común de los routers Cisco IOS es la habilitación de una interfaz loopback.

La interfaz de bucle invertido es una interfaz lógica interna del router. No está asignado a un puerto físico y nunca se puede conectar a ningún otro dispositivo. Se la considera una interfaz de software que se coloca automáticamente en estado "up" (activo), siempre que el router esté en funcionamiento.

La interfaz loopback es útil para probar y administrar un dispositivo Cisco IOS, ya que asegura que por lo menos una interfaz esté siempre disponible. Por ejemplo, se puede usar con fines de prueba, como la prueba de procesos de routing interno, mediante la emulación de redes detrás del router.

Las interfaces de bucle invertido también se utilizan comúnmente en entornos de laboratorio para crear interfaces adicionales. Por ejemplo, puede crear varias interfaces de bucle invertido en un router para simular más redes con fines de práctica de configuración y pruebas. En este plan de estudios, a menudo usamos una interfaz de bucle invertido para simular un enlace a Internet.

El proceso de habilitación y asignación de una dirección de loopback es simple:

```js
Router(config)# **interface loopback** _number_ 

Router(config-if)# **ip address** _ip-address subnet-mask_ 
```

Se pueden habilitar varias interfaces loopback en un router. La dirección IPv4 para cada interfaz de bucle invertido debe ser única y no debe ser utilizada por ninguna otra interfaz, como se muestra en la configuración de ejemplo de la interfaz de bucle invertido 0 en R1.

```js
R1(config)# interface loopback 0
R1(config-if)# ip address 10.0.0.1 255.255.255.0
R1(config-if)# exit
R1(config)#
%LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up
```

1.4.7

### Packet Tracer- Configurar Interfaces de Router

En esta actividad Packet Tracer, configurará `routeres` con direccionamiento IPv4 e IPv6.

 Configure interfaces de routers

![[1.4.7-packet-tracer---configure-router-interfaces_es-XL.pka]]

---
## Verificar redes conectadas directamente

1.5.1

### Comandos de verificación de interfaz

No tiene sentido configurar el router a menos que verifique la configuración y la conectividad. En este tema se describen los comandos que se van a utilizar para comprobar las redes conectadas directamente. Incluye dos verificadores de sintaxis y un trazador de paquetes.

Hay varios comandos **show** que se pueden usar para verificar el funcionamiento y la configuración de una interfaz. La topología de la figura se utiliza para demostrar la verificación de la configuración de la interfaz del router.

![[Pasted image 20241212105900.png]]


Los siguientes comandos son especialmente útiles para identificar rápidamente el estado de una interfaz:

- **show ip interface brief** y **show ipv6 interface brief** -Estos muestran un resumen de todas las interfaces, incluida la dirección IPv4 o IPv6 de la interfaz y el estado operativo actual.
- **show running-config interface** _interface-id_ -Esto muestra los comandos aplicados a la interfaz especificada.
- **show ip route** y **show ipv6 route** - Este muestra el contenido de la tabla IPv4 o IPv6 almacenada en la memoria RAM. En Cisco IOS 15, las interfaces activas deben aparecer en la tabla de ruteo con dos entradas relacionadas identificadas con el código '**C**' (Conectado) o '**L**' (Local). En versiones anteriores de IOS, solo aparece una entrada con el código '**C**'.

1.5.2

### Verificación del estado de una interfaz

La salida de los comandos **show ip interface brief** y **show ipv6 interface brief** y se puede usar para revelar rápidamente el estado de todas las interfaces en el router. Puede verificar que las interfaces están activas y operativas como se indica en el estado de «up» y el protocolo de «up», como se muestra en el ejemplo. Un resultado distinto indicaría un problema con la configuración o el cableado.

```js
R1# show ip interface brief
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   192.168.10.1    YES manual up                    up
GigabitEthernet0/0/1   192.168.11.1    YES manual up                    up
Serial0/1/0            209.165.200.225 YES manual up                    up
Serial0/1/1            unassigned      YES unset  administratively down down
R1# show ipv6 interface brief
GigabitEthernet0/0/0   [up/up]
    FE80::7279:B3FF:FE92:3130
    2001:DB8:ACAD:1::1
GigabitEthernet0/0/1   [up/up]
    FE80::7279:B3FF:FE92:3131
    2001:DB8:ACAD:2::1
Serial0/1/0            [up/up]
    FE80::7279:B3FF:FE92:3130
    2001:DB8:ACAD:3::1
Serial0/1/1            [down/down]     Unassigned
```

1.5.3

### Verificar direcciones locales y multidifusión de vínculos IPv6

El resultado del comando  **show ipv6 interface brief** show ipv6 interface brief **show ipv6 interface brief**  muestra dos direcciones IPv6 configuradas por interfaz. Una de las direcciones es la dirección de unidifusión global de IPv6 que se introdujo manualmente. La otra, que comienza con FE80, es la dirección de unidifusión link-local para la interfaz. La dirección link-local se agrega automáticamente a una interfaz cuando se asigna una dirección de unidifusión global. Las interfaces de red IPv6 deben tener una dirección link-local, pero no necesariamente una dirección de unidifusión global.

El comando **show ipv6 interface gigabitethernet 0/0/0** muestra el estado de la interfaz y todas las direcciones IPv6 que pertenecen a la interfaz. Junto con la dirección local del enlace y la dirección de unidifusión global, la salida incluye las direcciones de multidifusión asignadas a la interfaz, comenzando con el prefijo FF02, como se muestra en el ejemplo.

```js
R1# show ipv6 interface gigabitethernet 0/0/0
GigabitEthernet0/0/0 is up, line protocol is up
  IPv6 is enabled, link-local address is FE80::7279:B3FF:FE92:3130
  No Virtual link-local address(es):
  Global unicast address(es):
    2001:DB8:ACAD:1::1, subnet is 2001:DB8:ACAD:1::/64
  Joined group address(es):
    FF02::1
    FF02::1:FF00:1
    FF02::1:FF92:3130
  MTU is 1500 bytes
  ICMP error messages limited to one every 100 milliseconds
  ICMP redirects are enabled
  ICMP unreachables are sent
  ND DAD is enabled, number of DAD attempts: 1
  ND reachable time is 30000 milliseconds (using 30000)
  ND advertised reachable time is 0 (unspecified)
  ND advertised retransmit interval is 0 (unspecified)
  ND router advertisements are sent every 200 seconds
  ND router advertisements live for 1800 seconds
  ND advertised default router preference is Medium
```

1.5.4

### Verificar la configuración de la interfaz

Junto con la dirección local del enlace y la dirección de unidifusión global, **show running-config interface** la salida incluye las direcciones de multidifusión asignadas a la interfaz, comenzando con el prefijo FF02, como se muestra en el ejemplo.

```js
R1 show running-config interface gigabitethernet 0/0/0
Building configuration...
Current configuration : 158 bytes
!
interface GigabitEthernet0/0/0
    description Link to LAN 1
    ip address 192.168.10.1 255.255.255.0
    negotiation auto
    ipv6 address 2001:DB8:ACAD:1::1/64
end
R1#
```

Los dos comandos siguientes se usan para recopilar información más detallada sobre la interfaz:

- **show interfaces** - Muestra la información de la interfaz y el recuento de flujo de paquetes para todas las interfaces en el dispositivo.
- **show ip interface** and **show ipv6 interface** -Muestra la información relacionada con IPv4 e IPv6 para todas las interfaces en un router.

1.5.5

### Verificar rutas

La salida de los **show ip route** comandos **show ipv6 route** y muestra las tres entradas de red conectadas directamente y las tres entradas de interfaz de ruta de host local, como se muestra en el ejemplo. La ruta de host local tiene una distancia administrativa de 0. También tiene una máscara /32 para IPv4 y una máscara /128 para IPv6. La ruta del host local es para rutas en el router que posee la dirección IP. Estas se usan para permitir que el router procese los paquetes destinados a esa dirección IP.

```js
R1# show ip route
Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
       
Gateway of last resort is not set
      192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.10.0/24 is directly connected, GigabitEthernet0/0/0
L        192.168.10.1/32 is directly connected, GigabitEthernet0/0/0
      192.168.11.0/24 is variably subnetted, 2 subnets, 2 masks
C        192.168.11.0/24 is directly connected, GigabitEthernet0/0/1
L        192.168.11.1/32 is directly connected, GigabitEthernet0/0/1
      209.165.200.0/24 is variably subnetted, 2 subnets, 2 masks
C        209.165.200.224/30 is directly connected, Serial0/1/0
L        209.165.200.225/32 is directly connected, Serial0/1/0
R1# show ipv6 route
IPv6 Routing Table - default - 7 entries
Codes: C - Connected, L - Local, S - Static, U - Per-user Static route
       
C   2001:DB8:ACAD:1::/64 [0/0]
     via GigabitEthernet0/0/0, directly connected
L   2001:DB8:ACAD:1::1/128 [0/0]
     via GigabitEthernet0/0/0, receive
C   2001:DB8:ACAD:2::/64 [0/0]
     via GigabitEthernet0/0/1, directly connected
L   2001:DB8:ACAD:2::1/128 [0/0]
     via GigabitEthernet0/0/1, receive
C   2001:DB8:ACAD:3::/64 [0/0]
     via Serial0/1/0, directly connected
L   2001:DB8:ACAD:3::1/128 [0/0]
     via Serial0/1/0, receive
L   FF00::/8 [0/0]
     via Null0, receive
R1#
```

Una ‘**C**’ junto a una ruta dentro de la tabla de enrutamiento indica que se trata de una red conectada directamente. Cuando la interfaz del router está configurada con una dirección de unidifusión global y está en el estado "arriba / arriba", el prefijo IPv6 y la longitud del prefijo se agregan a la tabla de enrutamiento IPv6 como una ruta conectada.

La dirección de unidifusión global IPv6 aplicada a la interfaz también se instala en la tabla de enrutamiento como una ruta local. La ruta local tiene un prefijo /128. La tabla de routing utiliza las rutas locales para procesar eficazmente los paquetes cuyo destino es la dirección de la interfaz del router.

El **ping** comando para IPv6 es idéntico al comando usado con IPv4, excepto que se usa una dirección IPv6. Como se muestra en el ejemplo, el **ping** comando se usa para verificar la conectividad de Capa 3 entre R1 y PC1.

```js
R1# ping 2001:db8:acad:1::10
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 2001:DB8:ACAD:1::10, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/1 ms
```

1.5.6

### Filtrado de los resultados del comando show

Los comandos que generan varias pantallas de resultados se pausan al cabo de 24 líneas de manera predeterminada. Al final del resultado detenido, se muestra el texto --More--. Al presionar **Enter** se muestra la siguiente línea y al presionar la barra espaciadora se muestra el siguiente conjunto de líneas. Use el **terminal length** comando para especificar el número de líneas que se mostrarán. Un valor 0 (cero) evita que el router haga una pausa entre las pantallas de resultados.

Otra característica muy útil que mejora la experiencia del usuario en la CLI es el **show** filtrado de salida. Los comandos de filtrado se pueden utilizar para mostrar secciones específicas de los resultados. Para habilitar el comando de filtrado, ingrese una barra vertical partida (**|**) después del **show** comando y luego ingrese un parámetro de filtrado y una expresión de filtrado.

Hay cuatro parámetros de filtrado que se pueden configurar después de la tubería.

Haga clic en cada botón para obtener información sobre los comandos de filtrado.

#### section
Muestra la sección completa que comienza con la expresión de filtrado, como se muestra en el ejemplo.

```js
R1# show running-config | section line vty
line vty 0 4
 password 7 110A1016141D
 login
 transport input all
```

**Nota**: Los filtros de salida se pueden usar en combinación con cualquier **show** comando.

#### include

Incluye todas las líneas de salida que coinciden con la expresión de filtrado, como se muestra en el ejemplo.

```js
R1# show ip interface brief
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0 / 0/0 192.168.10.1 SÍ manual arriba
GigabiteThernet0/0/1 192.168.11.1 SÍ manual arriba
Serie0 / 1/0 209.165.200.225 SÍ manual arriba
Serial0/1/1 unassigned NO unset down down
R1#
R1# show ip interface brief | include up
GigabitEthernet0 / 0/0 192.168.10.1 SÍ manual arriba
GigabiteThernet0/0/1 192.168.11.1 SÍ manual arriba
Serie0 / 1/0 209.165.200.225 SÍ manual arriba
```

**Nota**: Los filtros de salida se pueden usar en combinación con cualquier **show** comando.
#### exclude

Excluye todas las líneas de salida que coinciden con la expresión de filtrado, como se muestra en el ejemplo.

```js
R1# show ip interface brief
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0 / 0/0 192.168.10.1 SÍ manual arriba
GigabiteThernet0/0/1 192.168.11.1 SÍ manual arriba
Serie0 / 1/0 209.165.200.225 SÍ manual arriba
Serial0/1/1 unassigned NO unset down down
R1#
R1# show ip interface brief | exclude unassigned
Interface IP-Address OK? Method Status Protocol
GigabitEthernet0 / 0/0 192.168.10.1 SÍ manual arriba
GigabiteThernet0/0/1 192.168.11.1 SÍ manual arriba
Serie0 / 1/0 209.165.200.225 SÍ manual arriba
```

**Nota**: Los filtros de salida se pueden usar en combinación con cualquier **show** comando.

#### begin

Muestra todas las líneas de salida desde un punto determinado, comenzando con la línea que coincide con la expresión de filtrado, como se muestra en el ejemplo.

```js
R1# show ip route | begin Gateway
Gateway of last resort is not set
      192.168.10.0/24 is variably subnetted, 2 subnets, 2 masks
C 192.168.10.0/24 está directamente conectado, GigabitEthernet0/0/0
L 192.168.10.1/32está directamente conectado, GigabitEthernet0/0/0
      192.168.11.0/24 is variably subnetted, 2 subnets, 2 masks
C 192.168.10.0/24 está directamente conectado, GigabitEthernet0/0/0
L 192.168.10.1/32está directamente conectado, GigabitEthernet0/0/0
      209.165.200.0/24 is variably subnetted, 2 subnets, 2 masks
C 209.165.200.224/30está directamente conectado, Serial0/1/0
L 209.165.200.225/32 está conectado directamente, Serie0 / 1/0
```

**Nota**: Los filtros de salida se pueden usar en combinación con cualquier **show** comando.

1.5.7
### Historial de comandos

La función de historial de comandos es útil porque almacena temporalmente la lista de comandos ejecutados para recuperar.

Para recuperar comandos en el búfer de historial, presione **Ctrl**+**P** o la **Up Arrow** tecla. El resultado de los comandos comienza con el comando más reciente. Repita la secuencia de teclas para recuperar sucesivamente los comandos más antiguos. Para volver a los comandos más recientes en el búfer de historial, presione **Ctrl**+**N** o la **Down Arrow** tecla. Repita la secuencia de teclas para recuperar sucesivamente los comandos más recientes.

De manera predeterminada, el historial de comandos está habilitado, y el sistema captura las últimas 10 líneas de comandos en el búfer de historial. Utilice el **show history** comando EXEC privilegiado para mostrar el contenido del búfer.

También es práctico aumentar la cantidad de líneas de comandos que registra el búfer de historial solamente durante la sesión de terminal actual. Use el **terminal history size** comando EXEC del usuario para aumentar o disminuir el tamaño del búfer.

Un ejemplo de los comandos **terminal history size** y **show history** se muestra en la figura.

```js
R1# terminal history size 200
R1# show history
  show ip int brief
  show interface g0/0/0
  show ip route
  show running-config
  show history
  terminal history size 200
  
```

1.5.9
### Packet Tracer: verificar redes conectadas directamente

En esta actividad Packet Tracer, los routers R1 y R2 tienen dos LAN. Su tarea es verificar el direccionamiento en cada dispositivo y verificar la conectividad entre las LAN.

 Verificar redes conectadas directamente

 ![[1.5.10-packet-tracer---verify-directly-connected-networks_es-XL.pka]]

---

1.5.11

### Compruebe su comprensión - Verificar las redes conectadas directamente

Verifique su comprensión de verificar las redes conectadas directamente eligiendo la MEJOR respuesta a las siguientes preguntas.

1. ¿Qué comando mostrará un resumen de todas las interfaces habilitadas para IPv6 en un router que incluya la dirección IPv6 y el estado operativo?
    
    **show ip interface brief**
    
    **show ipv6 route**
    
    **show running-config interface**
    
    **show ipv6 interface brief**
    
2. Al verificar rutas, ¿qué código se utiliza para identificar rutas conectadas directamente en la tabla de enrutamiento?
    
    C
    
    D
    
    L
    
    R
    
3. ¿Qué comando mostrará recuentos de flujo de paquetes, colisiones y fallas de búfer en una interfaz?
    
    **show interface**
    
    **show ip interface**
    
    **show running-config interface**
    
4. Se requiere una interfaz habilitada para IPv6 para tener qué tipo de dirección?
    
    Bucle invertido
    
    Unidifusión global
    
    Link-local
    
    estática
    
5. ¿Qué carácter se utiliza para habilitar el filtrado de comandos?
    
    tubería |
    
    coma ,
    
    Dos puntos (:)
    
    (punto y coma) ;
    
6. ¿Qué expresión de filtrado mostrará todas las líneas de salida a partir de la línea que coincida con la expresión de filtrado?
    
    sección
    
    empezar
    
    incluir

---

## Práctica del módulo y cuestionario

1.6.1

### Packet Tracer - Implementar una red pequeña

En esta actividad de Packet Tracer, los routers R1 y R2 tienen dos LAN cada uno. Su tarea es verificar el direccionamiento en cada dispositivo y verificar la conectividad entre las LAN.

 Implementar una red pequeña

 ![[1.6.1-packet-tracer---implement-a-small-network_es-XL.pka]]
 

1.6.2

### Laboratorio: configuración del router básico

Esta es una práctica de laboratorio integral para revisar comandos de router de IOS que se abarcaron anteriormente. Cableará el equipo y completará las configuraciones básicas y la configuración de la interfaz IPv4 en el router. Luego usará SSH para conectarse al router de forma remota y utilizará los comandos IOS para recuperar información del dispositivo para responder preguntas sobre el router.

 Configure los parámetros básicos del router - Modo Físico

 ![[1.6.2-packet-tracer----configure-basic-router-settings---physical-mode_es-XL.pka]]

**Equipo de Laboratorio**

 Configuración del router básico

1.6.3

### ¿Qué aprenderé en este módulo?

**Configuración de parámetros iniciales de un switch**

Después de encender un switch Cisco, pasa por una secuencia de arranque de cinco pasos. La variable de entorno BOOT se establece utilizando el **boot system** comando del modo de configuración global. El IOS se encuentra en una carpeta distinta y se especifica la ruta de la carpeta. Utilice los LED del interruptor para supervisar la actividad y el rendimiento del interruptor: SYST, RPS, STAT, DUPLX, SPEED y PoE. El cargador de arranque proporciona acceso al switch si no se puede usar el sistema operativo debido a la falta de archivos de sistema o al daño de estos. El cargador de arranque tiene una línea de comando que proporciona acceso a los archivos almacenados en la memoria flash. Para el acceso a la administración remota de un switch, este se debe configurar con una dirección IP y una máscara de subred. Para administrar el switch desde una red remota, el switch debe configurarse con una puerta de enlace predeterminada. Para configurar el switch SVI, primero debe configurar la interfaz de administración, luego configurar la puerta de enlace predeterminada y, finalmente, verificar la configuración.

**Configuración de puertos de un switch**

La comunicación en dúplex completo aumenta el ancho de banda eficaz al permitir que ambos extremos de una conexión transmitan y reciban datos simultáneamente. La comunicación semidúplex es unidireccional. Los puertos de switch se pueden configurar manualmente con parámetros específicos de dúplex y de velocidad. Utilice la negociación automática cuando la configuración de velocidad y dúplex del dispositivo que se conecta al puerto sea desconocida o pueda cambiar. Al habilitar la característica auto-MDIX, la interfaz detecta automáticamente el tipo de conexión de cable requerido (directo o cruzado) y configura la conexión conforme a esa información. Hay varios **show** comandos que se pueden utilizar al verificar las configuraciones del switch. Utilice el **show running-config** comando y el **show interfaces** comando para verificar la configuración de un puerto de switch. El resultado del **show interfaces** comando también es útil para detectar problemas comunes de capa de acceso a la red, ya que muestra el estado del protocolo de línea y vínculo de datos. Los errores de entrada reportados desde el **show interfaces** comando incluyen: tramas runt, gigantes, errores CRC, junto con colisiones y colisiones tardías. Utilícelo **show interfaces** para determinar si la red no tiene conexión o una conexión incorrecta entre un switch y otro dispositivo.

**Acceso remoto seguro**

Telnet (que usa el puerto TCP 23) es un protocolo más antiguo que utiliza la transmisión de texto sin formato segura tanto de la autenticación de inicio de sesión (nombre de usuario y contraseña) como de los datos transmitidos entre los dispositivos de comunicación. SSH (utilizando el puerto TCP 22) es un protocolo seguro que proporciona una conexión de administración cifrada a un dispositivo remoto. SSH proporciona seguridad para las conexiones remotas mediante el cifrado seguro cuando se autentica un dispositivo (nombre de usuario y contraseña) y también para los datos transmitidos entre los dispositivos que se comunican. Utilice el **show version** comando del switch para ver qué IOS está ejecutando el switch. Un nombre de archivo de IOS que incluye la combinación «k9» admite características y capacidades criptográficas. Para configurar SSH, debe verificar que el switch lo admita, configurar el dominio IP, generar pares de claves RSA, configurar la autenticación de uso, configurar las líneas VTY y habilitar SSH versión 2. Para verificar que SSH esté operativo, use el **show ip ssh** comando para mostrar la versión y los datos de configuración de SSH en el dispositivo.

**Configuración básica de un router**

Siempre se deben realizar las siguientes tareas de configuración inicial: nombrar el dispositivo para distinguirlo de otros routeres y configurar contraseñas, configurar un banner para proporcionar notificación legal de acceso no autorizado y guardar los cambios en un router. Una característica que distingue a los switches de los routers es el tipo de interfaces que admite cada uno. Por ejemplo, los switches de capa 2 admiten redes LAN y, por lo tanto, tienen varios puertos FastEthernet o Gigabit Ethernet. La topología de pila dual se utiliza para demostrar la configuración de las interfaces IPv4 e IPv6 del router. Los routers admiten redes LAN y WAN, y pueden interconectar distintos tipos de redes; por lo tanto, admiten muchos tipos de interfaces. Por ejemplo, los ISR G2 tienen una o dos interfaces Gigabit Ethernet integradas y ranuras para tarjetas de interfaz WAN de alta velocidad (HWIC) para admitir otros tipos de interfaces de red, incluidas las interfaces seriales, DSL y de cable. La interfaz de bucle invertido IPv4 es una interfaz lógica interna del router. No está asignado a un puerto físico y nunca se puede conectar a ningún otro dispositivo.

**Verificar redes conectadas directamente**

Utilice los siguientes comandos para identificar rápidamente el estado de una interfaz: **show ip interface brief** y **show ipv6 interface brief** para ver un resumen de todas las interfaces (direcciones IPv4 e IPv6 y estado operativo), **show running-config interface interface-id** para ver los comandos aplicados a una interfaz especificada **show ip route** y **show ipv6 route** para ver el de la tabla de enrutamiento IPv4 o IPv6 almacenada en la RAM. La salida de los **show ip interface brief** comandos **show ipv6 interface brief** y se puede usar para revelar rápidamente el estado de todas las interfaces en el enrutador. El **show ipv6 interface gigabitethernet 0/0/0** comando muestra el estado de la interfaz y todas las direcciones IPv6 que pertenecen a la interfaz. Junto con la dirección local del enlace y la dirección de unidifusión global, la salida incluye las direcciones de multidifusión asignadas a la interfaz. La salida del **show running-config interface** comando muestra los comandos actuales aplicados a una interfaz específica. El **show interfaces** comando muestra la información de la interfaz y el recuento de flujo de paquetes para todas las interfaces en el dispositivo. Verifique la configuración de la interfaz mediante **show ip interface** los comandos **show ipv6 interface** y, que muestran la información relacionada con IPv4 e IPv6 para todas las interfaces de un router. Compruebe las rutas mediante los **show ip route** comandos **show ipv6 route** y. Filtrar la salida del comando show usando el carácter pipe (|). Usar expresiones de filtro: sección, inclusión, exclusión y comienzo. De forma predeterminada, el historial de comandos está habilitado y el sistema captura las últimas 10 líneas de comando en su búfer de historial. Utilice el **show history** comando EXEC privilegiado para mostrar el contenido del búfer.

1.6.4

### Prueba del módulo: configuración básica del dispositivo

1. ¿Qué tareas se pueden realizar mediante la función de historial de comandos? (Escoja dos opciones).
    
    Guarde las líneas de comando en un archivo de registro para futuras referencias.
    
    Recuérdese los comandos introducidos anteriormente.
    
    Ver una lista de comandos introducidos en una sesión anterior.
    
    Recuperar hasta 15 líneas de comando de forma predeterminada.
    
    Establece el tamaño del búfer del historial de comandos.
    
2. ¿Qué declaración describe el funcionamiento del LED del sistema en los switches Catalyst de Cisco?
    
    Si el LED es de color ámbar, el sistema recibe energía pero no funciona correctamente.
    
    Si el LED parpadea en ámbar, el interruptor está realizando la POST (POST).
    
    Si el LED es ámbar, el sistema no está encendido.
    
    Si el LED parpadea en verde, el sistema está funcionando normalmente.
    
3. ¿Qué tipo de cable Ethernet se utilizaría para conectar un switch a otro cuando ninguno de los dos admite la función Auto-MDIX?
    
    Coaxial
    
    De conexión cruzada
    
    De consola (rollover)
    
    Directo
    
4. ¿Qué ventajas brinda SSH en comparación con Telnet?
    
    Más líneas de conexión
    
    Cifrado
    
    Servicios orientados a la conexión
    
    Autenticación de nombre de usuario y de contraseña
    
5. Un administrador de red ha configurado VLAN 99 como VLAN de administración y la ha configurado con una dirección IP y una máscara de subred. El administrador emite el **show interface vlan 99** comando y observa que el protocolo de línea está inhabilitado. ¿Qué acción puede cambiar el estado del protocolo de línea a arriba?
    
    Conecte un host a una interfaz asociada con VLAN 99.
    
    Configure un gateway predeterminado.
    
    Elimine todos los puertos de acceso de la VLAN 99.
    
    Configure un método de entrada de transporte en las líneas vty.
    
6. ¿Qué enunciado describe los SVI?
    
    Se crea automáticamente un SVI para cada VLAN en un switch multicapa.
    
    Al crear un SVI se crea automáticamente una VLAN asociada.
    
    Sólo se puede crear un SVI para la VLAN de administración.
    
    Se crea un SVI predeterminado para la VLAN 1 para la administración del switch.
    
7. ¿Qué mensaje se muestra cuando un administrador de red accede correctamente al gestor de arranque en un switch para recuperarse de un fallo del sistema?
    
    Switch>
    
    system:
    
    switch#
    
    Sistema.
    
8. ¿Qué secuencia de arranque del router es correcta?
    
    1 - realiza la POST y carga el programa bootstrap  
    Se ubica y se carga el archivo de configuración de inicio, o se ingresa al modo de configuración.  
    3 - ubique y cargue el software Cisco IOS
    
    1 - realiza la POST y carga el programa bootstrap  
    2: ubique y cargue el software Cisco IOS  
    3: ubica y carga el archivo de configuración de inicio o ingresa al modo de configuración
    
    1 - realiza la POST y carga el archivo de configuración de inicio  
    2 - localizar y cargar el programa de arranque  
    3 - ubique y cargue el software Cisco IOS
    
    1: realice la POST y cargue el software Cisco IOS  
    Se ubica y se carga el archivo de configuración de inicio, o se ingresa al modo de configuración.  
    3 - localizar y cargar el programa de arranque
    
9. ¿Cuál es la primera acción en la secuencia de arranque cuando un switch está encendido?
    
    cargar un programa de autoprueba de encendido
    
    cargar el software del cargador de arranque
    
    inicialización de CPU de bajo nivel
    
    cargar el software Cisco IOS predeterminado
    
10. ¿Con qué debe contar un administrador para restablecer una contraseña olvidada en un router?
    
    Acceso físico al router
    
    Cable cruzado
    
    Servidor TFTP
    
    Acceso a otro router
    
11. Al configurar un switch para el acceso SSH, ¿qué otro comando asociado con el **login local** comando es necesario ingresar en el switch?
    
    **enable secret** _password_
    
    **login block-for** _seconds_ **attempts** _number_ **within** _seconds_
    
    **username** _username_ **secret** _secret_
    
    **password** _password_
    
---

1. ¿Qué comando proporcionará información sobre el estado de todas las interfaces, incluyendo el número de gigantes, runts y colisiones en la interfaz?
    
    **show ip interface brief**
    
    **show interfaces**
    
    **show history**
    
    **show running-config**

