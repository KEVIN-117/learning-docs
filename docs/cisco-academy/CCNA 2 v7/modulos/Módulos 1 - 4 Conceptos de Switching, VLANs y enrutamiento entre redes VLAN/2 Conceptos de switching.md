## Introducción

2.0.1

## ¿Por qué debería tomar este módulo?

¡Bienvenido a conceptos de Switching!

Puede conectar y configurar switches, ¡eso es genial!. Pero incluso una red con la tecnología más reciente desarrolla sus propios problemas eventualmente. Si tiene que solucionar problemas de la red, necesita saber cómo funcionan los switches. Este módulo le proporciona los fundamentos de los switches y su funcionamiento. Por suerte, el funcionamiento del switch es fácil de entender.

2.0.2

## ¿Qué aprenderé en este módulo?

**Título del módulo:** Conceptos de switching

**Objetivos del módulo**: Explique cómo los switches de capa 2 reenvían datos.


|**Título del tema**|**Objetivo del tema**|
|---|---|
|**Reenvío de tramas**|Explique la forma en la que las tramas se reenvían en una red conmutada.|
|**Dominios de switching**|Compare un dominio de colisión con un dominio de difusión.|

---
# Reenvío de tramas

2.1.1

## Switching en la red

El concepto de switching y reenvío de tramas es universal en la tecnología de redes y en las telecomunicaciones. En las redes LAN, WAN y en la red pública de telefonía conmutada (PSTN), se usan diversos tipos de switches.

La decisión sobre cómo un switch reenvía el tráfico se toma en relación con el flujo de ese tráfico. Hay dos términos asociados a las tramas que entran y salen de una interfaz:

- **Entrada** - Este término se usa para describir el puerto por donde una trama ingresa al dispositivo.
- **Salida** - Este término se usa para describir el puerto que las tramas utilizarán al salir del dispositivo.

Un switch LAN mantiene una tabla a la que hace referencia al reenviar tráfico a través del switch. La única inteligencia de un switch LAN es su capacidad de usar su tabla para reenviar tráfico. Un switch LAN reenvía tráfico basado en el puerto de entrada y la dirección MAC de destino de una trama Ethernet. Con un switch LAN, hay solamente una tabla de switching principal que describe una asociación estricta entre las direcciones MAC y los puertos; por lo tanto, una trama Ethernet con una dirección de destino determinada siempre sale por el mismo puerto de salida, independientemente del puerto de entrada por el que ingresa.

**Nota**: Una trama Ethernet nunca se reenviará fuera del mismo puerto en el que se recibió.

Haga clic en el botón Reproducir para ver una animación del proceso de switching.

![[Pasted image 20241212111012.png]]
Tabla de puertos

|Direcciones de destino|Puerto|
|---|---|
|EE|1|
|AA|2|
|BA|3|
|EA|4|
|AC|5|
|AB|6|

2.1.2

## Tabla de direcciones MAC del switch

Un switch se compone de circuitos integrados y del software complementario que controla las rutas de datos a través del switch. Los switches usan direcciones MAC de destino para dirigir las comunicaciones de red a través del switch, fuera del puerto apropiado, hacia el destino.

Para definir qué puerto usar para transmitir una trama, el switch primero debe saber qué dispositivos existen en cada puerto. A medida que el switch aprende la relación de los puertos con los dispositivos, construye una tabla llamada tabla de direcciones MAC. Esta tabla se almacena en la Memoria de Contenido Direccionable (Content-Addressable Memory, CAM), la cual es un tipo especial de memoria utilizada en aplicaciones de búsqueda de alta velocidad. Por esta razón, la tabla de direcciones MAC a veces también se denomina tabla CAM.

Los switches LAN determinan cómo manejar las tramas de datos entrantes manteniendo la tabla de direcciones MAC. Un switch llena su tabla de direcciones MAC al registrar la dirección MAC de origen de cada dispositivo conectado a cada uno de sus puertos. El switch hace referencia a la información en la tabla de direcciones MAC para enviar tramas destinadas a un dispositivo específico fuera del puerto que se ha asignado a ese dispositivo.

2.1.3

## El método Aprender y Reenviar del Switch

El siguiente proceso de dos pasos se realiza para cada trama de Ethernet que ingresa a un switch.

**Paso 1. Aprender - Examinando la dirección Origen MAC**

Se revisa cada trama que ingresa a un switch para obtener información nueva. Esto se realiza examinando la dirección MAC de origen de la trama y el número de puerto por el que ingresó al switch.

- Si la dirección MAC de origen no existe en la tabla de direcciones MAC, la dirección MAC y el número de puerto entrante son agregados a la tabla.
- Si la dirección MAC de origen existe, el switch actualiza el temporizador para esa entrada. De manera predeterminada, la mayoría de los switches Ethernet guardan una entrada en la tabla durante cinco minutos. Si la dirección MAC de origen existe en la tabla, pero en un puerto diferente, el switch la trata como una entrada nueva. La entrada se reemplaza con la misma dirección MAC, pero con el número de puerto más actual.

**Paso 2. Reenviar - Examinadno la dirección destino MAC**

Si la dirección MAC de destino es una dirección de unidifusión, el switch busca una coincidencia entre la dirección MAC de destino de la trama y una entrada de la tabla de direcciones MAC:

- Si la dirección MAC de destino está en la tabla, reenviará la trama por el puerto especificado.
- Si la dirección MAC de destino no está en la tabla, el switch reenviará la trama por todos los puertos, excepto por el de entrada. Esto se conoce como unidifusión desconocida. Si la dirección MAC de destino es de difusión o de multidifusión, la trama también se envía por todos los puertos, excepto por el de entrada.

2.1.4
## Métodos de reenvío del switch

Los switches toman decisiones de reenvío de capa 2 muy rápidamente. Esto se debe al software en los circuitos integrados para aplicaciones específicas (ASIC, por sus siglas en ingles). Los ASIC reducen el tiempo de manejo de paquetes dentro del dispositivo y permiten que el dispositivo pueda manejar una mayor cantidad de puertos sin disminuir el rendimiento.

Los switches de capa 2 utilizan uno de estos dos métodos para cambiar tramas:

- **Almacenamiento y reenvío de switching** - Este método toma una decisión de reenvío en una trama después de haber recibido la trama completa y revisada para la detección de errores mediante un mecanismo matemático de verificación de errores conocido como Verificación por Redundancia Cíclica (Cyclic Redundancy Check, CRC). El intercambio por almacenamiento y envío es el método principal de switching LAN de Cisco.
- **Método de corte** - Este método inicia el proceso de reenvío una vez que se determinó la dirección MAC de destino de una trama entrante y se estableció el puerto de salida.

2.1.6

## Intercambio de almacenamiento y reenvío

El intercambio de almacenamiento y reenvío, a diferencia del intercambio de corte, tiene laS siguientes características principales:

- **Verificación de errores** - Después de recibir la trama completa en el puerto de entrada, el switch compara el valor de Secuencia de Verificación de Trama (Frame Check Sequence, FCS) en el último campo del datagrama con sus propios cálculos de FCS. FCS es un proceso de verificación de errores que contribuye a asegurar que la trama no contenga errores físicos ni de enlace de datos. Si la trama no posee errores, el switch la reenvía. De lo contrario, se descartan las tramas.
- **Almacenamiento en búfer automático** - El proceso de almacenamiento en buffer que usan los switches de almacenamiento y envío proporciona la flexibilidad para admitir cualquier combinación de velocidades de Ethernet. Por ejemplo, manejar una trama entrante que viaja a un puerto Ethernet de 100 Mbps que debe enviarse a una interfaz de 1 Gbps, requeriría utilizar el método de almacenamiento y reenvío. Ante cualquier incompatibilidad de las velocidades de los puertos de entrada y salida, el switch almacena la trama completa en un buffer, calcula la verificación de FCS, la reenvía al buffer del puerto de salida y después la envía.

La figura ilustra cómo almacenar y reenviar toma una decisión basada en la trama Ethernet.
![[Pasted image 20241212111113.png]]

2.1.7

## Switching por método de corte

El método de switching de almacenamiento y reenvío elimina las tramas que no pasan la comprobación FCS. Por lo tanto, no reenvía tramas no válidas.

Por el contrario, los switches que usan el método de corte pueden reenviar tramas no válidas, ya que no realizan la verificación de FCS. Sin embargo, el switching de corte tiene la capacidad de realizar un cambio de trama rápida. Esto significa que los switches que usan el método de corte pueden tomar una decisión de reenvío tan pronto como encuentren la dirección MAC de destino de la trama en la tabla de direcciones MAC, tal y como se muestra en la ilustración.
![[Pasted image 20241212111201.png]]
El switch no tiene que esperar a que el resto de la trama ingrese al puerto de entrada antes de tomar la decisión de reenvío.

El switching libre de fragmentos es una forma modificada de corte, en la que el switch solo comienza a reenviar la trama después de haber leído el campo Tipo. El switching libre de fragmentos proporciona una mejor verificación de errores que el método de corte, con prácticamente ningún aumento de latencia.

La velocidad de latencia más baja del switching por corte hace que resulte más adecuado para las aplicaciones mas demandantes de Tecnología Informática de Alto Rendimiento (High-Performance Computing, HPC) que requieren latencias de proceso a proceso de 10 microsegundos o menos.

El método switching de corte puede reenviar tramas con errores. Si hay un índice de error alto (tramas no válidas) en la red, el switching por método de corte puede tener un impacto negativo en el ancho de banda, de esta forma, se obstruye el ancho de banda con las tramas dañadas y no válidas.

---
# Dominios de switching

2.2.1

## Dominios de colisiones

En el tema anterior, obtuvo una mejor comprensión de lo que es un switch y cómo funciona. En este tema se explica cómo funcionan los switches entre sí y con otros dispositivos para eliminar colisiones y reducir la congestión de la red. Los términos colisiones y congestión se utilizan aquí de la misma manera que se utilizan en el tráfico callejero.

En segmentos Ethernet basados en hubs antiguos, los dispositivos de red compitieron por el medio compartido. Los segmentos de red que comparten el mismo ancho de banda entre dispositivos se conocen como dominios de colisión. Cuando dos o más dispositivos del mismo dominio de colisión tratan de comunicarse al mismo tiempo, se produce una colisión.

Si un puerto Ethernet de switch funciona en semidúplex, cada segmento está en su propio dominio de colisión. No hay dominios de colisión cuando los puertos del switch funcionan en dúplex completo. Sin embargo, podría haber un dominio de colisión si un puerto de switch funciona en semidúplex.

De manera predeterminada, los puertos de Ethernet del switch negociarán automáticamente el dúplex completo cuando el dispositivo adyacente también pueda funcionar en dúplex completo. Si el puerto del switch está conectado a un dispositivo que funciona en semidúplex, como por ejemplo un hub antiguo, el puerto de switch funcionará en modo semidúplex. En el caso de semidúplex, el puerto de switch formará parte de un dominio de colisión.

Como se muestra en la figura, se elige dúplex completo si ambos dispositivos cuentan con la funcionalidad, junto con su ancho de banda común más elevado.
![[Pasted image 20241212111546.png]]
2.2.2

## Dominios de difusión

Una serie de switches interconectados forma un dominio de difusión simple. Solo los dispositivos de capa de red, como los routers, pueden dividir un dominio de difusión de capa 2. Los routers se utilizan para segmentar los dominios de difusión, pero también segmentan un dominio de colisión.

Cuando un dispositivo desea enviar una difusión de capa 2, la dirección MAC de destino de la trama se establece solo en números uno binarios.

El dominio de difusión de capa 2 se denomina “dominio de difusión MAC”. El dominio de difusión MAC consta de todos los dispositivos en la LAN que reciben tramas de difusión de un host.

![[Pasted image 20241212111659.png]]
Cuando un switch recibe una trama de difusión, la reenvía por cada uno de sus puertos, excepto por el puerto de entrada en el que se recibió la trama de difusión. Cada dispositivo conectado al switch recibe una copia de la trama de difusión y la procesa.

En ocasiones, las difusiones son necesarias para localizar inicialmente otros dispositivos y servicios de red, pero también reducen la eficacia de la red. El ancho de banda de red se usa para propagar el tráfico de difusión. Si hay demasiadas difusiones y una carga de tráfico intensa en una red, se puede producir una congestión, lo que reduce el rendimiento de la red.

Cuando hay dos switches conectados entre sí, se aumenta el dominio de difusión, como se ve en la segunda mitad de la animación. En este caso, se reenvía una trama de difusión a todos los puertos conectados en el switch S1. El switch S1 está conectado al switch S2. Luego, la trama se propaga a todos los dispositivos conectados al switch S2.

2.2.3

## Alivio de la congestión en la red

Los switches LAN tienen características especiales que los hacen eficaces para aliviar la congestión de una red. De manera predeterminada, los puertos de switch interconectados tratan de establecer un enlace en dúplex completo y por lo tanto se eliminan los dominios de colisión. Cada puerto dúplex completo del switch ofrece el ancho de banda completo a los dispositivos conectados a dicho puerto. Las conexiones dúplex completas aumentaron notablemente el rendimiento de las redes LAN y se requieren para velocidades de Ethernet de 1 Gb/s y superiores.

Los switches interconectan segmentos LAN, usan una tabla de direcciones MAC para determinar los puertos de salida y pueden reducir o eliminar por completo las colisiones. Las características de los switches que alivian la congestión de la red incluyen las siguientes:

- **Velocidades de puertos rápidas** : las velocidades de los puertos del switch Ethernet varían según el modelo y el propósito. Por ejemplo, la mayoría de los switches de capa de acceso admiten velocidades de puerto de 100 Mbps y 1 Gbps. Los switches de capa de distribución admiten velocidades de puerto de 100 Mbps, 1 Gbps y 10 Gbps y los switches de nivel central y centro de datos admiten velocidades de puerto de 100 Gbps, 40 Gbps y 10 Gbps. Los switches con velocidades de puerto más rápidas cuestan más pero pueden reducir la congestión.
- **Cambio interno rápido** : los switches utilizan un bus interno rápido o memoria compartida para proporcionar un alto rendimiento.
- **Búferes de trama grande** : los switches utilizan búferes de memoria grande para almacenar temporalmente más tramas recibidas antes de tener que empezar a descartarlas. Esto permite que el tráfico de entrada desde un puerto más rápido (por ejemplo, 1 Gbps) se reenvíe a un puerto de salida más lento (por ejemplo, 100 Mbps) sin perder tramas.
- **Alta densidad de puertos** : un switch de alta densidad de puertos reduce los costos generales porque reduce el número de switches requeridos. Por ejemplo, si se necesitaran 96 puertos de acceso, sería menos costoso comprar dos switches de 48 puertos en lugar de cuatro switches de 24 puertos. Los switches de alta densidad de puertos también ayudan a mantener el tráfico local, lo que ayuda a aliviar la congestión.

2.2.4

## Verifique su comprensión - Cambiar dominios

Verifique su comprensión sobre dominios de switches eligiendo la MEJOR respuesta a las siguientes preguntas.

1. ¿Qué velocidad de puerto se negociará automáticamente entre un host con una NIC de 1 Gbps que se conecta a un switch Cisco Catalyst 2960 con un puerto de 100 Mbps?
    
    10 Mbps
    
    100 Mbps
    
    1 Gbps
    
    10 Gbps
    
2. ¿Qué dispositivo separa los dominios de difusión?
    
    punto de acceso
    
    hub
    
    router
    
    switch
    
3. ¿Qué dos características especiales utilizan los switches LAN para aliviar la congestión de la red? (Escoja dos opciones).
    
    velocidades de puertos rápidos
    
    switching interno rápido
    
    bajas densidades de puertos
    
    búferes de trama pequeña
    

---
# Práctica del módulo y cuestionario

2.3.1

## ¿Qué aprenderé en este módulo?

**Reenvío de trama**

La decisión sobre cómo un switch reenvía el tráfico se toma en relación con el flujo de ese tráfico. El término ingreso describe el puerto donde una trama ingresa a un dispositivo. El término salida describe el puerto que las tramas utilizarán al salir del dispositivo. Una trama Ethernet nunca será reenviada fuera del puerto donde ingresó. Para definir qué puerto usar para transmitir una trama, el switch primero debe saber qué dispositivos existen en cada puerto. A medida que el switch aprende la relación de los puertos con los dispositivos, construye una tabla llamada tabla de direcciones MAC. Cada trama que ingresa a un switch se comprueba para obtener información nueva examinando la dirección MAC de origen de la trama y el número de puerto donde la trama ingresó al switch. Si la dirección MAC de destino es una dirección de unidifusión, el switch busca una coincidencia entre la dirección MAC de destino de la trama y una entrada en la tabla de direcciones MAC. Los métodos de reenvío de switches incluyen almacenamiento y reenvío y corte. Almacenaje y reenvío utiliza la comprobación de errores y el almacenamiento en búfer automático. El corte no comprueba errores. En su lugar, realiza un cambio rápido de trama. Esto significa que el switch puede tomar una decisión de reenvío tan pronto como haya buscado la dirección MAC de destino de la trama en su tabla de direcciones MAC.

**Cambio de Dominio**

Si un puerto Ethernet de switch funciona en semidúplex, cada segmento está en su propio dominio de colisión. No hay dominios de colisión cuando los puertos del switch funcionan en dúplex completo. De manera predeterminada, los puertos de Ethernet del switch negociarán automáticamente el dúplex completo cuando el dispositivo adyacente también pueda funcionar en dúplex completo. Una serie de switches interconectados forma un dominio de difusión simple. Solo los dispositivos de capa de red, como los routers, pueden dividir un dominio de difusión de capa 2. El dominio de difusión de capa 2 se denomina “dominio de difusión MAC”. El dominio de difusión MAC consta de todos los dispositivos en la LAN que reciben tramas de difusión de un host. Cuando un switch recibe una trama de difusión, la reenvía por cada uno de sus puertos, excepto el puerto de entrada en el que se recibió la trama de difusión. Cada dispositivo conectado al switch recibe una copia de la trama de difusión y la procesa. Los switches pueden: interconectar segmentos LAN, usar una tabla de direcciones MAC para determinar los puertos de salida y pueden reducir o eliminar por completo las colisiones. Para ayudar a aliviar la congestión, los switches utilizan velocidades de puerto rápidas, cambio interno rápido, búferes de tramas grandes y densidades de puertos altas

2.3.2

## Prueba del módulo: conceptos de switches

1. ¿Qué declaración es verdadera sobre los dominios de difusión y colisión?
    
    Agregar un router a una red aumentará el tamaño del dominio de colisión.
    
    Agregar un switch a una red aumentará el tamaño del dominio de difusión.
    
    El tamaño del dominio de colisión se puede reducir agregando switches a una red.
    
    Cuantas más interfaces tenga un router, mayor será el dominio de difusión resultante.
    
2. ¿Cuál es una función de un switch de capa 2?
    
    reenvía datos basados en direccionamiento lógico
    
    aprende el puerto asignado a un host examinando la dirección MAC de destino
    
    determina qué interfaz se utiliza para reenviar una trama basado en la dirección MAC de destino
    
    duplica la señal eléctrica de cada trama a cada puerto
    
3. ¿Cuál es la diferencia mas significativa entre un hub y un switch LAN de capa 2?
    
    Un hub reenvía tramas y un switch reenvía sólo paquetes.
    
    Un hub divide los dominios de colisión y un switch divide los dominios de difusión.
    
    Un switch crea muchos dominios de colisión más pequeños y un hub aumenta el tamaño de un solo dominio de colisión.
    
    Cada puerto de un hub es un dominio de colisión, y cada puerto de un switch es un dominio de difusión.
    
4. ¿Qué hace un switch LAN de Cisco si recibe una trama entrante y la dirección MAC de destino no figura en la tabla de direcciones MAC?
    
    Envía la trama a la dirección de puerta de enlace predeterminada.
    
    Reenvía la trama a todos los puertos, excepto al puerto donde se recibe la trama.
    
    Utiliza el Protocolo de Resolución de Direcciones (Address Resolution Protocol, ARP) para resolver el puerto relacionado con la trama.
    
    Descarta la trama.
    
5. ¿Qué característica del switch ayuda a aliviar la congestión de la red cuando un puerto de 10 Gbps reenvía datos a un puerto de 1 Gbps?
    
    velocidad de puerto rápido
    
    Switching interno rápido
    
    búfer de trama
    
    Alta densidad del puerto
    
6. ¿Qué método de switching utiliza el valor FCS?
    
    búfer de trama grande
    
    Almacenamiento y envío
    
    difusión
    
    Método de corte
    
7. ¿Qué representa el término "densidad de puertos" para un switch Ethernet?
    
    el número de puertos disponibles
    
    la velocidad de cada puerto
    
    el número de hosts que están conectados a cada puerto del switch
    
    el espacio de memoria asignado a cada puerto del switch
    
8. ¿Qué información utiliza un switch para mantener actualizada la información de la tabla de direcciones MAC?
    
    las direcciones MAC de origen y destino y el puerto de entrada
    
    la dirección MAC de destino y el puerto de salida
    
    la dirección MAC de destino y el puerto de entrada
    
    la dirección MAC de origen y el puerto de salida
    
    las direcciones MAC de origen y destino y el puerto de salida
    
    la dirección MAC de origen y el puerto de entrada
    
9. ¿Qué dos afirmaciones son ciertas acerca de las comunicaciones semidúplex y dúplex completo? (Escoja dos opciones).
    
    Todas las NIC modernas admiten comunicación semidúplex y dúplex completo.
    
    El dúplex completo aumenta el ancho de banda efectivo.
    
    La mitad dúplex tiene un solo canal.
    
    El dúplex completo permite que ambos extremos transmitan y reciban simultáneamente.
    
    El dúplex completo ofrece un uso potencial del ancho de banda al 100%.
    
10. ¿Qué tipo de dirección utiliza un switch para generar la tabla de direcciones MAC?
    
    dirección IP de destino
    
    dirección MAC de destino
    
    dirección IP de origen
    
    dirección MAC de origen
    
11. ¿Qué opción describe correctamente un método de switching?
    
    Almacenamiento y reenvío: reenvía la trama inmediatamente después de examinar su dirección MAC de destino
    
    Método de corte: toma una decisión de reenvío después de recibir toda la trama
    
    Almacenamiento y reenvío: asegura que la trama está libre de errores físicos y de enlace de datos
    
    Método de corte: proporciona la flexibilidad necesaria para admitir cualquier combinación de velocidades Ethernet
    
12. ¿Qué dispositivo de red puede funcionar como límite para dividir un dominio de difusión de capa 2?
    
    Puente Ethernet
    
    Hub Ethernet
    
    punto de acceso
    
    router
    
13. ¿Cuál es el propósito de los búferes de trama en un switch?
    
    Proporcionan un análisis de seguridad básico en las tramas recibidas.
    
    Retienen el tráfico, aliviando así la congestión de la red.
    
    Proporcionan almacenamiento temporal de la suma de comprobación de la trama.
    
    Ejecutan valores de suma de comprobación antes de la transmisión.
    
14. ¿Qué dispositivo de red se puede usar para eliminar colisiones en una red Ethernet?
    
    firewall
    
    hub
    
    switch
    
    router

