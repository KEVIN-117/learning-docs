Este es un conjunto de pasos detallados para configurar un router en un entorno de red. Te proporcionaré una traducción directa de estos pasos a comandos ejecutables en el router:

### Configuración del Router

1. **Acceso al modo EXEC privilegiado:**
    
    ```plaintext
    enable
    ```
    
2. **Modo de configuración global:**
    
    ```plaintext
    configure terminal
    ```
    
3. **Asignar un nombre al router:**
    
    ```plaintext
    hostname R2
    ```
    
4. **Configurar una contraseña encriptada para el modo EXEC privilegiado:**
    
    ```plaintext
    enable secret c1sco1234
    ```
    
5. **Establecer el nombre de dominio:**
    
    ```plaintext
    ip domain-name ccna-lab.com
    ```
    
6. **Deshabilitar la búsqueda DNS:**
    
    ```plaintext
    no ip domain-lookup
    ```
    
7. **Cifrar todas las contraseñas de texto sin formato:**
    
    ```plaintext
    service password-encryption
    ```
    
8. **Configurar un usuario con privilegios y contraseña encriptada:**
    
    ```plaintext
    username SSHadmin privilege 15 secret 55Hadm!n
    ```
    
9. **Generar un conjunto de claves RSA para SSH (modulo de 1024 bits):**
    
    ```plaintext
    crypto key generate rsa
    modulus 1024
    ```
    
10. **Configurar la contraseña de consola y habilitar la desconexión automática:**
    
    ```plaintext
    line console 0
    password cisco
    login
    exec-timeout 5 0
    logging synchronous
    ```
    
11. **Configurar la contraseña para líneas VTY y habilitar SSH:**
    
    ```plaintext
    line vty 0 4
    password cisco
    login
    transport input ssh
    exec-timeout 5 0
    ```
    
12. **Configurar un mensaje de advertencia (banner):**
    
    ```plaintext
    banner motd #Acceso no autorizado está prohibido.#
    ```
    
13. **Habilitar el routing IPv6:**
    
    ```plaintext
    ipv6 unicast-routing
    ```
    
14. **Configurar las interfaces IPv4/IPv6, activarlas y añadir descripciones:**
    
    - **Ejemplo para una interfaz:**
        
        ```plaintext
        interface GigabitEthernet0/0
        ip address 192.168.1.1 255.255.255.0
        ipv6 address 2001:db8::1/64
        description Conexión a la red LAN
        no shutdown
        ```
        
15. **Guardar la configuración:**
    
    ```plaintext
    end
    write memory
    ```
    

Con estos comandos, completarías la configuración tal y como se indica en la guía proporcionada. Si necesitas detalles adicionales o tienes un entorno específico, avísame.


---

La **plantilla SDM (Switch Database Management)** de un switch Cisco es una funcionalidad que permite ajustar cómo se asignan los recursos de hardware del switch para optimizar su desempeño según el propósito o las necesidades de la red. En términos más simples, las plantillas SDM definen cómo el switch utiliza su memoria para manejar diferentes tipos de tráfico, como **rutas IPv4/IPv6**, **entradas de la tabla MAC**, **listas de acceso (ACLs)**, o **multicast**.

### Propósitos de las plantillas SDM

Dependiendo del entorno y los requisitos de la red, puedes elegir una plantilla SDM adecuada para maximizar la eficiencia en áreas específicas. Algunos ejemplos de plantillas SDM son:

1. **Default:**  
    Optimiza el switch para configuraciones estándar, donde el tráfico es principalmente de capa 2 (L2).
    
2. **Routing:**  
    Prioriza el manejo de rutas IPv4 y IPv6, útil para entornos donde el switch actúa como un router de capa 3.
    
3. **VLAN:**  
    Optimiza el switch para entornos con muchas VLANs, aumentando la capacidad para manejar sus bases de datos.
    
4. **Access:**  
    Diseñada para switches de acceso en redes empresariales, equilibrando los recursos entre capa 2 y capa 3.
    
5. **Dual IPv4 and IPv6:**  
    Prioriza el soporte para tráfico de rutas y ACLs tanto en IPv4 como en IPv6.
    
6. **Advanced:**  
    Proporciona capacidades adicionales, como mayor soporte para listas de acceso (ACLs) o tablas ARP.
    

---

### Cómo Ver y Configurar la Plantilla SDM

Puedes configurar y verificar la plantilla SDM de un switch con los siguientes comandos:

1. **Ver la plantilla actual:**
    
    ```plaintext
    show sdm prefer
    ```
    
2. **Configurar una nueva plantilla:** Cambia la plantilla SDM según tus necesidades (por ejemplo, para routing):
    
    ```plaintext
    sdm prefer routing
    ```
    
3. **Guardar los cambios y reiniciar:** Algunos cambios requieren un reinicio para aplicar la nueva configuración:
    
    ```plaintext
    reload
    ```
    

---

### Ejemplo Práctico

Si necesitas optimizar el switch para manejar más rutas IPv4 e IPv6 porque actuará como router, configurarías la plantilla SDM de la siguiente forma:

```plaintext
enable
configure terminal
sdm prefer dual-ipv4-and-ipv6 routing
end
reload
```

Al reiniciar, el switch asignará más recursos para gestionar rutas en lugar de tráfico de capa 2.

---

**Nota:** No todos los switches Cisco soportan todas las plantillas SDM. Esto depende del modelo y las capacidades del hardware. Si tienes dudas sobre las plantillas disponibles, ejecuta el comando `show sdm prefer` para verificar las opciones.


---

