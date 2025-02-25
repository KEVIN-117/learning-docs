# Práctica del módulo y cuestionario

6.4.1

## Packet Tracer - Implementar EtherChannel

Se le ha encomendado diseñar una implementación de EtherChannel para una empresa que desee mejorar el rendimiento de los enlaces troncal del switch. Intentará varias formas diferentes de implementar los enlaces EtherChannel con el fin de evaluar cuál es el mejor para la empresa. Construirá la topología, configurará puertos troncales e implementará EtherChannels LACP y PAgP.

![[6.4.1-packet-tracer---implement-etherchannel_es-XL.pka]]


6.4.2

## Lab - Implementar EtherChannel

En esta práctica de laboratorio se cumplirán los siguientes objetivos:

- Parte 1: Armar la red y configurar los ajustes básicos de los dispositivos
- Parte 2: Crear redes VLAN y asignar puertos de switch
- Parte 3: Configurar un enlace troncal 802.1Q entre los switches
- Parte 4: Implementar y verificar un EtherChannel entre los switches

 Implementación de EtherChannel

6.4.3

## ¿Qué aprenderé en este módulo?

**Operación con EtherChannel**

Para aumentar el ancho de banda o la redundancia, se pueden conectar varios enlaces entre dispositivos. Sin embargo, el STP bloquea los enlaces redundantes para evitar los bucles de switching. EtherChannel es una tecnología de agregación de enlaces que permite enlaces redundantes entre dispositivos que no serán bloqueados por STP. EtherChannel agrupa varios enlaces Ethernet físicos en un único enlace lógico. Proporciona tolerancia a fallos, uso compartido de carga, mayor ancho de banda y redundancia entre conmutadores, enrutadores y servidores. Cuando se configura un EtherChannel, la interfaz virtual resultante se denomina “canal de puertos”. EtherChannel tiene varias ventajas, así como algunas restricciones a la implementación. Los EtherChannels se pueden formar por medio de una negociación con uno de dos protocolos: PAgP o LACP. Estos protocolos permiten que los puertos con características similares formen un canal mediante una negociación dinámica con los switches adyacentes. Cuando se configura un enlace EtherChannel mediante un propietario Cisco PAgP, se envían paquetes PAgP entre los puertos aptos para EtherChannel para negociar la formación de un canal. Los modos PAgP se encienden, PAgP deseable y PAgP automático. LACP realiza una función similar a PAgP con EtherChannel de Cisco. Debido a que LACP es un estándar IEEE, se puede usar para facilitar los EtherChannels en entornos de varios proveedores. Los modos LACP se encienden, LACP activo y LACP pasivo.

**Configurar EtherChannel**

Las siguientes pautas y restricciones son útiles para configurar EtherChannel:

- **Compatibilidad con EtherChannel** - Todas las interfaces Ethernet en todos los módulos deben admitir EtherChannel, sin necesidad de que las interfaces sean físicamente contiguas o estén en el mismo módulo.
- **Velocidad y dúplex** - Configure todas las interfaces en un EtherChannel para que funcionen a la misma velocidad y en el mismo modo dúplex.
- **VLAN match** - Todas las interfaces en el grupo EtherChannel se deben asignar a la misma VLAN o se deben configurar como enlace troncal.
- **Rango de VLAN** - Un EtherChannel admite el mismo rango permitido de VLAN en todas las interfaces de un EtherChannel de enlace troncal.

La configuración de EtherChannel con LACP requiere tres pasos:

**Paso 1.** Especifique las interfaces que conforman el grupo EtherChannel mediante el comando de modo de configuración global interface range.

**Paso 2.** Cree la interfaz de canal de puerto con el comando channel-group identifier mode active en el modo de configuración de rango de interfaz.

**Paso 3.** Para cambiar la configuración de capa 2 en la interfaz de canal de puertos, ingrese al modo de configuración de interfaz de canal de puertos mediante el comando interface port-channel, seguido del identificador de la interfaz.

**Verificar y resolver problemas de EtherChannel.**

Existe una variedad de comandos para verificar una configuración EtherChannel que incluye, **show interfaces port-channel**, **show etherchannel summary**, **show etherchannel port-channel** y **show interfaces etherchannel**. Entre los problemas comunes de EtherChannel se incluyen los siguientes:

- Los puertos asignados en el EtherChannel no son parte de la misma VLAN ni son configurados como enlace troncal. Los puertos con VLAN nativas diferentes no pueden formar un EtherChannel.
- La conexión troncal se configuró en algunos de los puertos que componen el EtherChannel, pero no en todos ellos. Si el rango permitido de VLAN no es el mismo, los puertos no forman un EtherChannel, incluso cuando PAgP se establece en modo automático o deseado. Las opciones de negociación dinámica para PAgP y LACP no se encuentran configuradas de manera compatible en ambos extremos del EtherChannel.

6.4.4

## Módulo Quiz - Etherchannel

1. Se formó un enlace EtherChannel  usando LACP entre dos switches, S1 y S2. Al verificar la configuración, ¿qué combinación de modos se podría utilizar en ambos switches?​
    
    S1-on and S2-passive
    
    S1-passive and S2-activo
    
    S1-on y S2-activo
    
    S1-passive and S2-passive​
    
2. Cuando se configura un rango de puertos para EtherChannel, ¿qué modo configurará PAgP para que inicie la negociación EtherChannel?
    
    Automático
    
    passive
    
    desirable (deseable)
    
    activo
    
3. ¿Qué tres parámetros de interfaz deben coincidir para que se forme un EtherChannel? (Escoja tres opciones).
    
    VLAN permitidas
    
    EtherChannel mode
    
    estado de spanning-tree
    
    Modo PortFast
    
    modo de conexión troncal
    
    VLAN nativa
    
4. ¿Cuáles son las tres ventajas de utilizar la tecnología EtherChannel? (Escoja tres opciones).
    
    El protocolo de árbol de expansión cierra las interfaces no utilizadas en el paquete para evitar bucles.
    
    EtherChannel utiliza varios enlaces lógicos para proporcionar redundancia.
    
    El equilibrio de carga no es necesario con EtherChannel.
    
    No es necesario volver a calcular el árbol de expansión cuando se desactiva un único enlace dentro del canal.
    
    No es necesario actualizar enlaces a conexiones más rápidas para aumentar el ancho de banda.
    
    Las tareas de configuración se pueden realizar en la interfaz EtherChannel.
    
5. Un administrador de red está configurando un enlace EtherChannel entre dos puertos físicos de un switch. ¿Qué declaración describe el resultado cuando falla uno de los puertos físicos?
    
    El EtherChannel continúa transmitiendo datos con ancho de banda reducido.
    
    El EtherChannel falla.
    
    El EtherChannel deja de transmitir datos hasta que se reinicie.
    
    Se necesita un nuevo cálculo de STP.
    
6. Cuando se implementa EtherChannel, múltiples interfaces físicas se agrupan en qué tipo de conexión lógica?
    
    VLAN interface
    
    interface range
    
    Bucle invertido
    
    Canal de puertos
    
7. Cuando se configura un rango de puertos para EtherChannel mediante el uso de PAgP, ¿qué modo formará el canal agrupado sólo si el puerto recibe paquetes PAgP de otro dispositivo?
    
    desirable (deseable)
    
    Automático
    
    activo
    
    passive
    
8. ¿Qué dos métodos de equilibrio de carga se pueden implementar con la tecnología EtherChannel? (Escoja dos opciones).
    
    MAC de destino a IP de destino
    
    MAC de destino a MAC de origen
    
    IP de destino a IP de origen
    
    IP de destino a MAC de destino
    
    IP de origen a IP de destino
    
    MAC de origen a MAC de destino
    
9. ¿Qué función proporciona EtherChannel?
    
    habilitar el tráfico de varias VLAN para viajar a través de un único enlace de Capa 2
    
    dividir el ancho de banda de un único enlace en intervalos de tiempo separados
    
    propagar el tráfico a través de varios enlaces WAN físicos
    
    creación de un vínculo lógico mediante el uso de múltiples vínculos físicos entre dos switches LAN
    
10. ¿Cuáles dos afirmaciones sobre la tecnología EtherChannel son verdaderas?
    
    EtherChannel utiliza puertos de switch existentes.
    
    Todas las tareas de configuración deben realizarse en los puertos individuales del enlace EtherChannel.
    
    STP no se ejecuta en enlaces EtherChannel redundantes.
    
    Los enlaces deben actualizarse para que sean compatibles con EtherChannel.
    
11. ¿Cuáles dos combinaciones de modos resultarían en la negociación exitosa de un EtherChannel? (Escoja dos opciones).
    
    auto; auto
    
    deseable; deseable
    
    activo; encendido
    
    activo; pasivo
    
    deseable; activo
    
    pasivo; automático
    
12. ¿Qué dos protocolos son protocolos de agregación de enlaces? (Escoja dos opciones).
    
    RSTP
    
    STP
    
    PAgP
    
    802.3ad
    
    EtherChannel
    
13. Cuando se configura un rango de puertos para EtherChannel, ¿qué modo configurará LACP para que inicie la negociación EtherChannel?
    
    desirable (deseable)
    
    Automático
    
    activo
    
    passive
    
14. ¿Qué sucederá si un administrador de red coloca un puerto que forma parte de un paquete EtherChannel en una VLAN diferente a los otros puertos de ese paquete?
    
    El EtherChannel falla.
    
    El paquete EtherChannel se mantendrá en marcha solo si se utiliza LACP.
    
    El paquete EtherChannel se mantendrá en marcha solo si se utiliza PAgP.
    
    El paquete EtherChannel se mantendrá activado si los puertos se configuraron sin negociación entre los switches para formar el EtherChannel.
    
    El paquete EtherChannel se mantendrá en marcha si se utiliza PAgP o LACP.
    
15. Cuando se configura un rango de puertos para EtherChannel, ¿qué modo configurará LACP en un puerto sólo si el puerto recibe paquetes LACP de otro dispositivo?
    
    activo
    
    Automático
    
    passive
    
    desirable (deseable)