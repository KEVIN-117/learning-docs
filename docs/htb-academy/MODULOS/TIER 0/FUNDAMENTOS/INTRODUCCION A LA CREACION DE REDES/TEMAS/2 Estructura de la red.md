# Tipos de red

#### Terminología Común

| **Tipo de red**                                                    | **Definición**                              |
| ------------------------------------------------------------------ | ------------------------------------------- |
| Wide Area Network (WAN) `Red de área amplia`                       | Internet                                    |
| Local Area Network (LAN) `Red de área local`                       | Redes internas (Ej: Hogar u Oficina)        |
| Wireless Local Area Network (WLAN) `Red de área local inalámbrica` | Redes internas accesibles a través de Wi-Fi |
| Virtual Private Network (VPN) `Red privada virtual`                | Conecta varios sitios de red a una `LAN`    |
## WAN
La WAN (red de área amplia) se conoce comúnmente como Internet. Cuando se trata de equipos de red, a menudo tendremos una dirección WAN y una dirección LAN. La WAN es la dirección a la que generalmente se accede a través de Internet. Dicho esto, no incluye Internet; una WAN es simplemente una gran cantidad de redes LAN unidas. Muchas grandes empresas o agencias gubernamentales tendrán una "WAN interna" (también llamada Intranet, red Airgap, etc.). En términos generales, la forma principal en que identificamos si la red es una WAN es usar un protocolo de enrutamiento específico de WAN como BGP y si el esquema IP en uso no está dentro de RFC 1918 (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).

---
## LAN / WLAN
Las redes LAN (redes de área local) y las redes WLAN (redes de área local inalámbricas) normalmente asignan direcciones IP designadas para uso local (RFC 1918, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16). En algunos casos, como en el caso de algunas universidades u hoteles, es posible que se le asigne una dirección IP enrutable (de Internet) al unirse a su LAN, pero eso es mucho menos común. No hay ninguna diferencia entre una LAN y una WLAN, excepto que las WLAN introducen la capacidad de transmitir datos sin cables. Es principalmente una designación de seguridad.

---
## VPN
Hay tres tipos principales de redes privadas virtuales (VPN), pero las tres tienen el mismo objetivo: hacer que el usuario se sienta como si estuviera conectado a una red diferente.

#### Site-To-Site VPN
Tanto el cliente como el servidor son dispositivos de red, normalmente enrutadores o firewalls, y comparten rangos de red completos. Esto se utiliza con mayor frecuencia para unir redes de empresas a través de Internet, lo que permite que varias ubicaciones se comuniquen a través de Internet como si fueran locales.
#### VPN de acceso remoto
Esto implica que la computadora del cliente crea una interfaz virtual que se comporta como si estuviera en la red de un cliente. Hack The Box utiliza OpenVPN, que crea un adaptador TUN que nos permite acceder a los laboratorios. Al analizar estas VPN, un elemento importante a considerar es la tabla de enrutamiento que se crea al unirse a la VPN. Si la VPN solo crea rutas para redes específicas (por ejemplo, 10.10.10.0/24), esto se llama VPN de túnel dividido, lo que significa que la conexión a Internet no sale de la VPN. Esto es excelente para Hack The Box porque brinda acceso al laboratorio sin la preocupación de privacidad de monitorear su conexión a Internet. Sin embargo, para una empresa, las VPN de túnel dividido generalmente no son ideales porque si la máquina está infectada con malware, los métodos de detección basados ​​en la red probablemente no funcionarán ya que ese tráfico sale por Internet.

#### SSL VPN
Básicamente, se trata de una VPN que se ejecuta dentro de nuestro navegador web y que se está volviendo cada vez más común a medida que los navegadores web se vuelven capaces de hacer cualquier cosa. Por lo general, estos transmiten aplicaciones o sesiones de escritorio completas a su navegador web. Un gran ejemplo de esto sería `HackTheBox Pwnbox`.

## Términos del Libro

| Tipo de red                                                              | Definición                       |
| ------------------------------------------------------------------------ | -------------------------------- |
| Global Area Network (GAN) `Red de área global`                           | Global network (the Internet)    |
| Metropolitan Area Network (MAN) `Red del Área Metropolitana`             | Regional network (multiple LANs) |
| Wireless Personal Area Network (WPAN) `Red de área personal inalámbrica` | Personal network (Bluetooth)     |
#### GAN
Una red mundial como Internet se conoce como Red de Área Global (GAN, por sus siglas en inglés). Sin embargo, Internet no es la única red informática de este tipo. Las empresas que operan a nivel internacional también mantienen redes aisladas que abarcan varias WAN y conectan los ordenadores de la empresa en todo el mundo. Las GAN utilizan la infraestructura de fibra de vidrio de las redes de área amplia y las interconectan mediante cables submarinos internacionales o transmisión por satélite.

#### MAN
Una `red de área metropolitana` (MAN) es una red de telecomunicaciones de banda ancha que conecta varias redes LAN en proximidad geográfica. Por lo general, se trata de sucursales individuales de una empresa conectadas a una MAN a través de líneas alquiladas. Se utilizan enrutadores de alto rendimiento y conexiones de alto rendimiento basadas en fibra de vidrio, que permiten un rendimiento de datos significativamente mayor que Internet. La velocidad de transmisión entre dos nodos remotos es comparable a la comunicación dentro de una LAN.
Los operadores de redes que operan a nivel internacional proporcionan la infraestructura para las redes de área metropolitana. Las ciudades conectadas como redes de área metropolitana pueden integrarse a nivel suprarregional en redes de área amplia (`WAN`) y a nivel internacional en redes de área global (`GAN`).

#### PAN / WPAN

Los dispositivos modernos, como teléfonos inteligentes, tabletas, computadoras portátiles o de escritorio, se pueden conectar ad hoc para formar una red que permita el intercambio de datos. Esto se puede hacer por cable en forma de `red de área personal` (PAN).
La variante inalámbrica Wireless Personal Area Network (WPAN) se basa en las tecnologías Bluetooth o Wireless USB. Una red de área personal inalámbrica que se establece a través de Bluetooth se denomina Piconet. Las PAN y las WPAN suelen tener una extensión de unos pocos metros y, por lo tanto, no son adecuadas para conectar dispositivos en habitaciones separadas o incluso en edificios.
En el contexto de la Internet de las cosas (IoT), las WPAN se utilizan para comunicar aplicaciones de control y monitorización con velocidades de datos bajas. Protocolos como Insteon, Z-Wave y ZigBee fueron diseñados explícitamente para hogares inteligentes y automatización del hogar. Anterior

# Topologías de red
La **topología de red** es la forma en la que se organizan y conectan `físicamente` o `lógicamente` los dispositivos en una red de comunicación. Describe cómo se interconectan los nodos (computadoras, routers, switches, etc.) y cómo se transmiten los datos entre ellos. Existen varias topologías de red, cada una con sus propias características, ventajas y desventajas. 
## Topologías físicas
Es el diseño de medio de transmisión lo cual es utilizado para conectar los dispositivos de la red
## Topologías lógicas
Es como estas actúan al momento de transmitir la información, com se transmiten los datos desde un dispositivo a otro

Toda la clasificación de las topologías podemos dividirlos en tres grupos:

## Conexiones
| `Conexiones cableadas`                            | `Conexiones inalámbricas` |
| ------------------------------------------------- | ------------------------- |
| Coaxial cabling (Cableado coaxial)                | Wi-Fi                     |
| Glass fiber cabling (Cableado de fibra de vidrio) | Cellular                  |
| Twisted-pair cabling (Cableado de par trenzado)   | Satellite                 |

## Nodos - Controlador de interfaz de red (NIC)

#### 2. Nodes - Network Interface Controller (NICs)

<div class="header"><p class="tag">Repetidores</p><p class="tag">Hubs</p><p class="tag">Bridges</p><p class="tag">Switches</p><p class="tag">Router/Modem</p><p class="tag">Puertas de enlace</p><p class="tag">Firewalls</p></div>

Los nodos de red son los `puntos de conexión del medio de transmisión` a los transmisores y receptores de señales eléctricas, ópticas o de radio en el medio. Un nodo puede estar conectado a una computadora, pero ciertos tipos pueden tener solo un microcontrolador en un nodo o pueden no tener ningún dispositivo programable.
## Clasificaciones
Podemos imaginar una topología como una forma o estructura virtual de una red. Esta forma no necesariamente corresponde a la disposición física real de los dispositivos en la red. Por lo tanto, estas topologías pueden ser `físicas` o `lógicas`. Por ejemplo, los ordenadores de una LAN pueden estar dispuestos en círculo en un dormitorio, pero es muy poco probable que tengan una topología de anillo real.
Las principales son:

Las topologías de red se dividen en los siguientes ocho tipos básicos:
<div class="header"><p class="tag">punto a punto</p><p class="tag">bus</p><p class="tag">estrella</p><p class="tag">anillo</p><p class="tag">mesh (malla)</p><p class="tag">arbol</p><p class="tag">hibrido</p><p class="tag">Daisy Chain</p></div>

### Punto a Punto
esta es una topología dedicada a la conexión directa de dos `hosts` , los hosts pueden utilizar esta conexión para una comunicación mutua.
![[Point-To-PointTopology.png]]
### Bus
Todos los dispositivos están conectados a un solo cable o línea principal (`bus`). Los datos viajan en ambas direcciones, y cada dispositivo recibe la señal. Es sencilla, pero sufre `colisiones de datos` y es difícil de expandir.
Dado que el medio se comparte con todos los demás, solo un host puede enviar, y todos los demás solo pueden recibir y evaluar los datos y ver si están destinados a ellos mismos.
![[BusTopology.png]]
### Estrella
Este tipo de topología mantiene una conexión con cada uno de los hosts, cada dispositivo se conecta a un nodo central, generalmente un switch o un hub. Es fácil de instalar y gestionar; si una conexión falla, solo afecta a un dispositivo, pero si el nodo central falla, toda la red se cae. El componente `central` se encargan de la función de reenvío de los paquetes de datos. Para ello, los paquetes de datos se reciben y se reenvían al destino. El tráfico de datos en el componente de red central puede ser muy alto, ya que todos los datos y conexiones pasan por él.
![[StarTopology.png]]
### Anillo
los dispositivos están conectados en un círculo, donde cada dispositivo tiene exactamente dos conexiones, una en cada lado. Los datos viajan en una dirección. Tiene buena capacidad de transmisión, pero si un dispositivo falla, la red entera puede verse afectada. Este tipo de topología permite que cada `host` o `nodo` este conectado al anillo con 2 cables:
- Uno para las señales entrantes *`incoming`*
- el otro para los salientes *`outgoing`*
Una topología de anillo lógico se basa en una topología de estrella física, donde un distribuidor en el nodo simula el anillo reenviando de un puerto al siguiente.
![[RingTopology.png]]
### Malla
cada dispositivo está conectado a varios otros dispositivos, creando múltiples rutas para los datos. Esto hace que sea muy confiable y tolerante a fallos, pero también costosa y compleja de instalar, utilizado principalmente en redes `WAN` o `MAN` para garantizar una alta fiabilidad y ancho de banda. Hay dos estructuras básicas a partir del concepto básico: la estructura `totalmente mallada` y la `estructura parcialmente mallada`.
- Cada nodo de una topología completamente en malla tiene las mismas funciones de enrutamiento y conoce los nodos vecinos con los que puede comunicarse en función de su proximidad a la puerta de enlace de la red y las cargas de tráfico.
- En la estructura parcialmente en malla, los puntos finales están conectados mediante una única conexión. En este tipo de topología de red, los nodos específicos están conectados a exactamente otro nodo, y algunos otros nodos están conectados a dos o más nodos mediante una conexión punto a punto.
![[MeshTopology.png]]
### Arbol
es una combinación de topologías en estrella y bus, donde los dispositivos están organizados en una jerarquía de nodos, similar a un árbol. Es flexible y fácil de expandir, pero depende de nodos de nivel superior; si uno de estos falla, afecta a sus nodos dependientes. Las topologías de árbol también se utilizan para redes de banda ancha y redes urbanas (MAN).
![[TreeTopology.png]]

### híbrida
combina dos o más de las topologías anteriores para aprovechar las ventajas de cada una, adaptándose mejor a redes más complejas.
Las redes híbridas combinan dos o más topologías, de modo que la red resultante no presenta ninguna topología estándar. Por ejemplo, una red en árbol puede representar una topología híbrida en la que las redes en estrella están conectadas a través de redes de bus interconectadas. Sin embargo, una red en árbol que está conectada a otra red en árbol sigue siendo topológicamente una red en árbol. Una topología híbrida siempre se crea cuando se interconectan dos topologías de red básicas diferentes.
![[HybridTopology.png]]
### Daisy Chain
Perite la conexión de multiples `hosts` por medio de un cable que pasa de un nodo a otro. Este tipo de redes se encuentra a menudo en la `tecnología de automatización` (CAN).
![[DaisyChainTopology.png]]

