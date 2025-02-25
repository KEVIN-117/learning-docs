# Modelos de redes
En redes se conocen 2 tipos de topologías de red, las cuales estas se encargan de describir la comunicación  transferencia de datos de un `host` a otro `host`, esto son llamados como el modelo `OSI` y el modelo `TCP/IP`. Esta es una representación simplificada de las llamadas capas que representan bits transferidos en contenidos legibles para nosotros.
![[osiTcpIp.png]]
## El modelo OSI
El modelo OSI, es un modelo 7 de capas. cada uno con se encarga de realizar tareas especificas Es un modelos de referencia, al cual su uso permite describir la comunicación entre sistemas.
El termino OSI es `Open Systems Interconnection | Interconexion de sistemas abiertos` 

## El Modelo TCP/IP
El modelos `TCP/IP` por sus siglas en ingles `(Transmission Control Protocol/Internet Protocol | Protocolo de control de transmisión/Protocolo de Internet )`, se podría decir que es un termino genérico para muchas protocolos de redes. Esto protocolos son los responsables de la transferencia de paquetes de datos po de internet, como lo menciona el modelo `TCP/IP` no solo se basa enteramente en estos dos tipos de protocolos, sino que es un termino genérico que ase referencia a toda la familia de `protocolos` existentes. Tomaremos com ejemplo al protocolo `ICMP` y `UDP` 

## ISO/OSI vs. TCP/IP
TCP/IP es un protocolo de comunicación que permite a los hosts conectarse a Internet. Se refiere al Protocolo de control de transmisión utilizado en y por las aplicaciones de Internet.
Por otra parte, el modelo OSI es una puerta de enlace de comunicación entre la red y los usuarios finales. El modelo OSI suele denominarse modelo de referencia porque es más nuevo y se utiliza más ampliamente. También es conocido por su estricto protocolo y sus limitaciones.

## Transferencia de paquetes
En un sistema en capas, los dispositivos de una capa intercambian datos en un formato diferente llamado `protocol data unit | unidad de datos de protocolo` (PDU).  Es decir si queremos navegar por un sitió web, la petición es enviada y el servidor se encarga de procesar esa solicitud capa por capa , en este proceso cada cap se encarga de realizar sus propias tareas. A continuación, los datos se transfieren a través de la capa física de la red hasta que el servidor de destino u otro dispositivo los recibe.  Los datos se enrutan a través de las capas nuevamente, y cada capa realiza sus operaciones asignadas hasta que el software receptor utiliza los datos.

![[PacketTransfers.png]]
Durante la transmisión, cada capa se encarga de añadir su propio encabezado a la `PDU`.  y este encabezado le sirve com una identificación para su posterior control y a este proceso se le denomina encapsulación. El encabezado y los datos juntos forman la PDU para la siguiente capa. El proceso continúa hasta la capa física o capa de red, donde los datos se transmiten al receptor. El receptor invierte el proceso y descomprime los datos en cada capa con la información del encabezado. Después de eso, la aplicación finalmente utiliza los datos. Este proceso continúa hasta que se hayan enviado y recibido todos los datos.
![[packetTransfer.png]]
Ambos modelos de referencia son útiles. Con TCP/IP, podemos entender rápidamente cómo se establece toda la conexión, y con ISO, podemos descomponerla pieza por pieza y analizarla en detalle. Esto suele ocurrir cuando podemos escuchar e interceptar tráfico de red específico. Luego tenemos que analizar este tráfico en consecuencia, y lo explicamos con más detalle en el módulo Análisis de tráfico de red.

# El modelo OSI
