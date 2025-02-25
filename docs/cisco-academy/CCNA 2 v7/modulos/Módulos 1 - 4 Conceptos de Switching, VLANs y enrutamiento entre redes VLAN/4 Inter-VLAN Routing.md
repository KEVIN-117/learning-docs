## Introducción

4.0.1

## ¿Por qué debería tomar este módulo?

Bienvenido a Inter-VLAN Routing!

Ahora sabe cómo segmentar y organizar su red en VLAN. Los hosts pueden comunicarse con otros hosts de la misma VLAN y ya no tiene hosts que envíen mensajes de difusión a cualquier otro dispositivo de la red, consumiendo el ancho de banda necesario. Pero, ¿qué pasa si un host de una VLAN necesita comunicarse con un host de otra VLAN? Si es administrador de red, sabe que las personas querrán comunicarse con otras personas fuera de la red. Aquí es donde el inter-VLAN routing puede ayudarle. El inter-VLAN routing utiliza un dispositivo de capa 3, como un router o un switch de capa 3. Vamos a llevar su experiencia VLAN y combinarla con sus habilidades de capa de red y ponerlos a prueba.

4.0.2

## ¿Qué aprenderé en este módulo?

**Título del módulo: Inter-VLAN Routing**

**Objetivo del módulo**: Solución de problemas de inter-VLAN routing en dispositivos de capa 3


|**Título del tema**|**Objetivo del tema**|
|---|---|
|**Funcionamiento del inter-VLAN routing**|Describa las opciones para configurar inter-VLAN routing|
|**Router-on-a-Stick Inter-VLAN Routing**|Configure router-on-a-Stick inter-VLAN Routing|
|**Inter-VLAN Routing usando switches de capa 3**|Configure inter-VLAN routing mediante un switch de capa&nbsp;3.|
|**Solución de problemas de Inter-VLAN Routing**|Solución de problemas comunes de configuración de inter-VLAN|

---

# Funcionamiento de Inter-VLAN Routing

4.1.1

## ¿Qué es Inter-VLAN Routing

Las VLAN se utilizan para segmentar las redes de switch de Capa 2 por diversas razones. Independientemente del motivo, los hosts de una VLAN no pueden comunicarse con los hosts de otra VLAN a menos que haya un router o un switch de capa 3 para proporcionar servicios de enrutamiento.

Inter-VLA routing es el proceso de reenviar el tráfico de red de una VLAN a otra VLAN.

Hay tres opciones inter-VLAN routing:

- **Inter-VLAN Routing heredado** - Esta es una solución antigua. No escala bien
- **Router-on-a-stick** - Esta es una solución aceptable para una red pequeña y mediana.
- **Switch de capa 3 con interfaces virtuales (SVIs)** : esta es la solución más escalable para organizaciones medianas y grandes.

4.1.2

## Inter-VLAN Routing heredado

La primera solución de inter-VLAN routing se basó en el uso de un router con múltiples interfaces Ethernet. Cada interfaz del router estaba conectada a un puerto del switch en diferentes VLAN. Las interfaces del router sirven como default gateways para los hosts locales en la subred de la VLAN.

Por ejemplo, consulte la topología donde R1 tiene dos interfaces conectadas al switch S1.

![[Pasted image 20241213005022.png]]
Observe que en el ejemplo la tabla de direcciones MAC de S1 se completa de la siguiente manera:

- El puerto Fa0/1 está asignado a la VLAN 10 y está conectado a la interfaz R1 G0/0/0.
- El puerto Fa0/11 está asignado a la VLAN 10 y está conectado a la PC1.
- El puerto Fa0/12 está asignado a la VLAN 20 y está conectado a la interfaz R1 G0/0/1.
- El puerto Fa0/24 está asignado a la VLAN 20 y está conectado a la PC2.

### Tabla de direcciones MAC para S1

|**Puerto**|**Dirección MAC**|**VLAN**|
|---|---|---|
|F0/1|R1 G0/0/0 MAC|10|
|F0/11|PC1 MAC|10|
|F0/12|R1 G0/0/1 MAC|20|
|F0/24|PC2 MAC|20|

Cuando PC1 envía un paquete a PC2 en otra red, lo reenvía a su puerta de enlace predeterminada 192.168.10.1. R1 recibe el paquete en su interfaz G0/0/0 y examina la dirección de destino del paquete. R1 luego enruta el paquete hacia fuera de su interfaz G0/0/1 al puerto F0/12 en la VLAN 20 en S1. Finalmente, S1 reenvía la trama a PC2.

Inter-VLAN routing heredado, usa las interfaces fisicas funciona, pero tiene limitaciones significantes. No es razonablemente escalable porque los routers tienen un número limitado de interfaces físicas. Requerir una interfaz física del router por VLAN agota rápidamente la capacidad de la interfaz física del router

En nuestro ejemplo, R1 requería dos interfaces Ethernet separadas para enrutar entre la VLAN 10 y la VLAN 20. ¿Qué ocurre si hubiera seis (o más) VLAN para interconectar? Se necesitaría una interfaz separada para cada VLAN. Obviamente, esta solución no es escalable.

**Nota**: Este método de inter-VLAN routing ya no se implementa en redes de switches y se incluye únicamente con fines explicativos.

4.1.3

## Router-on-a-Stick Inter-VLAN Routing

El método ‘router-on-a-stick’ inter-VLAN routing supera la limitación del método de enrutamiento interVLAN heredado. Solo requiere una interfaz Ethernet física para enrutar el tráfico entre varias VLAN de una red.

Una interfaz Ethernet del router Cisco IOS se configura como un troncal 802.1Q y se conecta a un puerto troncal en un switch de capa 2. Específicamente, la interfaz del router se configura mediante subinterfaces para identificar VLAN enrutables.

Las subinterfaces configuradas son interfaces virtuales basadas en software. Cada uno está asociado a una única interfaz Ethernet física. Estas subinterfaces se configuran en el software del router. Cada una se configura de forma independiente con sus propias direcciones IP y una asignación de VLAN. Las subinterfaces se configuran para subredes diferentes que corresponden a su asignación de VLAN. Esto facilita el enrutamiento lógico.

Cuando el tráfico etiquetado de VLAN entra en la interfaz del router, se reenvía a la subinterfaz de VLAN. Después de tomar una decisión de enrutamiento basada en la dirección de red IP de destino, el router determina la interfaz de salida del tráfico. Si la interfaz de salida está configurada como una subinterfaz 802.1q, las tramas de datos se etiquetan VLAN con la nueva VLAN y se envían de vuelta a la interfaz física.

Haga clic en Reproducir en la figura para ver una animación de la forma en que un router-on-a-stick desempeña su función de routing.

![[Pasted image 20241213005235.png]]

Como se ve en la animación, PC1 en la VLAN 10 se comunica con PC3 en la VLAN 30. El router R1 acepta el tráfico de unidifusión etiquetado en la VLAN 10 y lo enruta a la VLAN 30 mediante sus subinterfaces configuradas. El switch S2 elimina la etiqueta de la VLAN de la trama de unidifusión y reenvía la trama a PC3 en el puerto F0/23.

**Nota**: El método router-on-a-stick de inter-VLAN routing no escala mas allá de 50 VLANs.

4.1.4

## Inter-VLAN Routing en un switch de capa 3

El método moderno para realizar inter-VLAN routing es utilizar switches de capa 3 e interfaces virtuales del switch (SVI). Una SVI es una interfaz virtual configurada en un switch multicapa, como se muestra en la figura.

**Nota**: Un switch de capa 3 también se denomina switch multicapa ya que funciona en la capa 2 y la capa 3. Sin embargo, en este curso usamos el término switch de capa 3.

![[Pasted image 20241213005326.png]]
Los SVIs entre VLAN se crean de la misma manera que se configura la interfaz de VLAN de administración. El SVI se crea para una VLAN que existe en el switch. Aunque es virtual, el SVI realiza las mismas funciones para la VLAN que lo haría una interfaz de router. Específicamente, proporciona el procesamiento de Capa 3 para los paquetes que se envían hacia o desde todos los puertos de switch asociados con esa VLAN.

A continuación se presentan las ventajas del uso de switches de capa 3 para inter-VLAN routing:

- Es mucho más veloz que router-on-a-stick, porque todo el switching y el routing se realizan por hardware.
- El routing no requiere enlaces externos del switch al router. No se* limitan a un enlace porque los EtherChannels de Capa 2 se pueden utilizar como enlaces troncal entre los switches para aumentar el ancho de banda.
- La latencia es mucho más baja, dado que los datos no necesitan salir del switch para ser enrutados a una red diferente. Se* implementan con mayor frecuencia en una LAN de campus que en routers.

La única desventaja es que los switches de capa 3 son más caros.

4.1.5

## Verifique su comprensión- Operación de Inter-VLAN Routing

Esta actividad de verificación de su comprensión utiliza un escenario diferente para cada pregunta. Haga clic en cada botón para el escenario de operación de Inter-VLAN routing que corresponda a la pregunta.

### Escenario A
![[Pasted image 20241213005426.png]]

### Escenario B
![[Pasted image 20241213005451.png]]
### Escenario C
![[Pasted image 20241213005509.png]]

1. **Consulte cada una de las topologías de escenario.**. ¿Qué instrucciones describen mejor los diferentes tipos de soluciones de inter-VLAN routing? (Elija todas las opciones que correspondan).
    
    El escenario A es una solución interVLAN heredada.
    
    El escenario B es una solución interVLAN de capa 3.
    
    Los escenarios B y C son soluciones Router-on-a-stick inter-VLAN.
    
    El escenario A es una solución interVLAN de capa 3.
    
    El escenario B es una solución interVLAN heredada.
    
    El escenario C es una solución interVLAN de router-on-a-stick.

---

