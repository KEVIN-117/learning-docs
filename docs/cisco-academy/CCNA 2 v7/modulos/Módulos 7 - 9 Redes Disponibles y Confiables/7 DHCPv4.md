
# Introducción

## ¿Por qué debería tomar este módulo?

## ¿Qué aprenderé en este módulo?
**Título del módulo**: DHCPv4

**Objetivos del módulo**: Implemente DHCPv4 para operar en varias LAN.

|**Título del tema**|**Objetivo del tema**|
|---|---|
|**Conceptos DHCPv4**|Explicar la forma en la que funciona DHCPv4 en la red de una pequeña o mediana empresa .|
|**Configurar un servidor DHCPv4 del IOS de Cisco**|Configure un router como servidor DHCPv4.|
|**Configurar un cliente DHCPv4**|Configure un router como cliente DHCPv4.|

# Conceptos DHCPv4

## Servidor y cliente DHCPv4
`DHCP` significa Protocolo de configuración dinámica de host v4, se encarga de asignar direcciones `ip` de forma dinámica esto permite el ahorro de mucho tiempo
Para esas configuraciones existen servidores DHCPv4 dedicados, o también un Router cisco, esto dependiendo del lugar donde se debe configurar se emplea el dispositivo correspondiente.
El router Cisco IOS cuenta con tecnología `DHVPv4` su uso y configuración se recomienda hacerlo en lugares pequeños.
Este servidor asigna direcciones Ip dinámicas para un perdido de tiempo especifico o hasta que el host ya no necesite la dirección `IP`
![[dhcpv4.png]]
## Funcionamiento de DHCPv4

DHCPv4 funciona en un modo cliente/servidor. Cuando un cliente se comunica con un servidor de DHCPv4, el servidor asigna o arrienda una dirección IPv4 a ese cliente. El cliente se conecta a la red con esa dirección IPv4 arrendada hasta que caduque el arrendamiento. El cliente debe ponerse en contacto con el servidor de DHCP periódicamente para extender el arrendamiento. Este mecanismo de arrendamiento asegura que los clientes que se trasladan o se desconectan no mantengan las direcciones que ya no necesitan. Cuando caduca un arrendamiento, el servidor de DHCP devuelve la dirección al conjunto, donde se puede volver a asignar según sea necesario.
## Pasos para obtener un arrendamiento

Cuando el cliente arranca (o quiere unirse a una red), comienza un proceso de cuatro pasos para obtener un arrendamiento:

1. Detección de DHCP (DHCP DISCOVER)
2. Oferta de DHCP (DHCP OFFER)
3. Solicitud de DHCP (DHCP REQUEST)
4. Acuse de recibo de DHCP (DHCP ACK)
**Paso 1. Detección DHCP (DHCP DISCOVER)**

El cliente inicia el proceso con un mensaje de difusión DHCPDISCOVER con su propia dirección MAC para detectar los servidores de DHCPv4 disponibles. Dado que el cliente no tiene información de IPv4 válida durante el arranque, utiliza direcciones de difusión de capa 2 y de capa 3 para comunicarse con el servidor. El propósito del mensaje `DHCP DISCOVER` es encontrar los servidores de DHCPv4 en la red.

**Paso 2. Ofrecimiento de DHCP (DHCP OFFER)**

Cuando el servidor de DHCPv4 recibe un mensaje DHCPDISCOVER, reserva una dirección IPv4 disponible para arrendar al cliente. El servidor también crea una entrada ARP que consta de la dirección MAC del cliente que realiza la solicitud y la dirección IPv4 arrendada del cliente. El servidor de DHCPv4 envía el mensaje `DHCP OFFER` asignado al cliente que realiza la solicitud.

**Paso 3. Solicitud de DHCP (DHCP REQUEST)**

Cuando el cliente recibe el mensaje `DHCP OFFER` proveniente del servidor, envía un mensaje `DHCP REQUEST`. Este mensaje se utiliza tanto para el origen como para la renovación del arrendamiento. Cuando se utiliza para el origen del arrendamiento, el mensaje `DHCP REQUEST` sirve como notificación de aceptación vinculante al servidor seleccionado para los parámetros que ofreció y como un rechazo implícito a cualquier otro servidor que pudiera haber proporcionado una oferta vinculante al cliente.

Muchas redes empresariales utilizan varios servidores de DHCPv4. El mensaje `DHCP REQUEST` se envía en forma de difusión para informarle a este servidor de DHCPv4 y a cualquier otro servidor de DHCPv4 acerca de la oferta aceptada.

**Paso 4. Confirmación de DHCP (DHCP ACK)**

Al recibir el mensaje DHCPREQUEST, el servidor verifica la información del arrendamiento con un ping ICMP a esa dirección para asegurarse de que no esté en uso, crea una nueva entrada ARP para el arrendamiento del cliente y responde con un mensaje `DHCP ACK`. El mensaje `DHCP ACK` es un duplicado del mensaje `DHCP OFFER`, a excepción de un cambio en el campo de tipo de mensaje. Cuando el cliente recibe el mensaje `DHCP ACK`, registra la información de configuración y realiza una búsqueda de ARP para la dirección asignada. Si no hay respuesta al ARP, el cliente sabe que la dirección IPv4 es válida y comienza a utilizarla como propia.
![[arrendamiento.png]]

## Pasos para renovar un contrato de arrendamiento

Antes de la expiración de la concesión, el cliente inicia un proceso de dos pasos para renovar la concesión con el servidor DHCPv4, como se muestra en la figura:

**1. Detección DHCP (DHCP REQUEST)**

Antes de que caduque el arrendamiento, el cliente envía un mensaje `DHCP REQUEST` directamente al servidor de DHCPv4 que ofreció la dirección IPv4 en primera instancia. Si no se recibe un mensaje `DHCP ACK` dentro de una cantidad de tiempo especificada, el cliente transmite otro mensaje `DHCP REQUEST` de modo que uno de los otros servidores de DHCPv4 pueda extender el arrendamiento.

**2. Ofrecimiento de DHCP (DHCP ACK)**

Al recibir el mensaje `DHCP REQUEST`, el servidor verifica la información del arrendamiento al devolver un DHCPACK.

**Nota**: Estos mensajes (principalmente `DHCP OFFER` y `DHCP ACK`) se pueden enviar como unidifusión o difusión según la IETF RFC 2131.
![[renamearrendamiento.png]]

# Configure un servidor DHCPv4 del IOS de Cisco

## Pasos para configurar un servidor DHCPv4 del IOS de Cisco

Utilice los siguientes pasos para configurar un servidor DHCPv4 del IOS de Cisco:

**Paso 1**. Excluir direcciones IPv4  
**Paso 2**. Defina un nombre de grupo DHCPv4.  
**Paso 3**. Configure el grupo DHCPv4.

**Paso 1. Excluir direcciones IPv4**

El router que funciona como servidor de DHCPv4 asigna todas las direcciones IPv4 en un conjunto de direcciones DHCPv4, a menos que esté configurado para excluir direcciones específicas. Generalmente, algunas direcciones IPv4 de un conjunto se asignan a dispositivos de red que requieren asignaciones de direcciones estáticas. Por lo tanto, estas direcciones IPv4 no deben asignarse a otros dispositivos. La sintaxis del comando para excluir direcciones IPv4 es la siguiente:

```
Router(config)# ip dhcp excluded-address low-address [high-address]
```
Se puede excluir una única dirección o un rango de direcciones especificando la dirección más baja y la dirección más alta del rango. Las direcciones excluidas deben incluir las direcciones asignadas a los routers, a los servidores, a las impresoras y a los demás dispositivos que se configuraron o se configurarán manualmente. También puede introducir el comando varias veces.

**Paso 2. Defina un nombre de grupo DHCPv4**

La configuración de un servidor de DHCPv4 implica definir un conjunto de direcciones que se deben asignar.

Como se muestra en el ejemplo, el **ip dhcp pool** comando _pool-name_crea un conjunto con el nombre especificado y coloca al router en el modo de configuración de DHCPv4, que se identifica con el indicador Router(dhcp-config)#.

La sintaxis del comando para definir el grupo es la siguiente:

```
Router(config)# ip dhcp pool _pool-name_  
Router(dhcp-config)# 
```

**Paso 3. Configure el grupo DHCPv4**

La tabla indica las tareas para finalizar la configuración del pool de DHCPv4.

El conjunto de direcciones y el router de gateway predeterminado deben estar configurados. Use la **network** instrucción para definir el rango de direcciones disponibles. Use el **default-router** comando para definir el router de gateway predeterminado. Normalmente, el gateway es la interfaz LAN del router más cercano a los dispositivos clientes. Se requiere un gateway, pero se pueden indicar hasta ocho direcciones si hay varios gateways.

Otros comandos del pool de DHCPv4 son optativos. Por ejemplo, la dirección IPv4 del servidor DNS que está disponible para un cliente DHCPv4 se configura mediante el comando **dns-server**. El comando **domain-name** se utiliza para definir el nombre de dominio. La duración del arrendamiento de DHCPv4 puede modificarse mediante el comando **lease**. El valor de arrendamiento predeterminado es un día. El comando **netbios-name-server** se utiliza para definir el servidor WINS con NetBIOS.

Comando TaskiOS Definir la dirección pool.network network-number [mask | /prefix-length] Defina la dirección predeterminada del router o la puerta de enlace. default-router [address2.... address8] Definir una dirección DNS server.dns-server [address2... address8] Defina el nombre de dominio.domain-name domainDefinir la duración del arrendamiento DHCP.lease {days [hours [minutes]] | infinite} Definir la dirección del servidor WINS de NetBIOS. netbios-nombre-servidor [dirección2... dirección8]

| **Tarea**                                   | **Comando de IOS**                                         |
| ------------------------------------------- | ---------------------------------------------------------- |
| Definir el conjunto de direcciones.         | **network** _network-number_ [_mask_ \| / _prefix-length_] |
| Definir el router o gateway predeterminado. | **default-router** address [ _address2….address8_]         |
| Definir un servidor DNS.                    | **dns-server** _address_ [ _address2…address8_]            |
| Definir el nombre de dominio.               | **domain-name** _domain_                                   |
| Definir la duración de la concesión DHCP.   | **lease** {_days_ [_hours_ [ _minutes_]] \| **infinite**}  |
| Definir el servidor WINS con NetBIOS.       | **netbios-name-server** _address_ [ _address2…address8_]   |

**Nota**: Microsoft recomienda no implementar WINS, en su lugar configurar DNS para la resolución de nombres de Windows y retirar WINS.

## Comandos de verificación DHCPv4

Utilice los comandos de la tabla para verificar que el servidor DHCPv4 del IOS de Cisco esté funcionando.

CommandDescriptionshow running-config | section dhcpMuestra los comandos DHCPv4 configurados en el router.show ip dhcp bindingMuestra una lista de todos los enlaces de direcciones IPv4 a direcciones MAC proporcionados por el servicio DHCPv4. show ip dhcp server statisticsMuestra información de recuento relativa al número de mensajes DHCPv4 que se han enviado y recibido.

|**Comando**|**Descripción**|
|---|---|
|**show running-config \| section dhcp**|Muestra los comandos DHCPv4 configurados en el router.|
|**show ip dhcp binding**|Muestra una lista de todos los enlaces de direcciones IPv4 a direcciones MAC proporcionados por el servicio DHCPv4.|
|**show ip dhcp server statistics**|Muestra información de conteo con respecto a la cantidad de mensajes DHCPv4 que han sido enviados y recibidos.|
## Desactive el servidor DHCPv4 del IOS de Cisco

El servicio DHCPv4 está habilitado de manera predeterminada. Para desabilitar el servicio, use el comando **no service dhcp** del modo de configuración global. Use el comando del modo **service dhcp** de configuración global para volver a habilitar el proceso del servidor DHCPv4, como se muestra en el ejemplo. Si los parámetros no se configuran, habilitar el servicio no tiene ningún efecto.

**Nota**: Si se borra los enlaces DHCP o se detiene y reinicia el servicio DHCP, se pueden asignar temporalmente direcciones IP duplicadas en la red.

```
R1(config)# no service dhcp
R1(config)# service dhcp
R1(config)# 
```
