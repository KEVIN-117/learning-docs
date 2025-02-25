## Captura de información

La captura de información en `bash` lo logramos usando la palabra reservada `read`
- **-p**: Permite ingresar una frase o _prompt_ antes de pedir el dato. 
- **-s**: Modo Sigiloso. No muestra ningún carácter en la terminal, util para contraseñas o información sensible. 
- **-n [num]**: Permite leer como máximo n caracteres. 
- **-r**: Toma el botón de retroceso o _backspace_ como un carácter y no borra ningún otro carácter previamente escrito.
```bash
echo 'Number a:'
read 
number=$REPLY
```

## Validar información
para validar información que llegamos a capturar podríamos utilizar los siguientes parámetros

- Para validar tamaños se utiliza el comando `read -n<numero de caracteres>`
- Para validar tipos de datos se utiliza expresiones regulares
```bash
# ! /bin/bash 
# Programa para ejemplificar como capturar la información del usuario utilizando el comando read 

option=0 
backupName="" 
echo "Programa Utilidades Postgres" 
read -p "Ingresar una opción:" option 
read -p "Ingresar el nombre del archivo del backup:" 
backupName 
echo "Opción:$option , backupName:$backupName"
```

## Arreglos 
```bash
# ! /bin/bash 
# Programa para ejemplificar el uso de los arreglos 

arregloNumeros=(1 2 3 4 5 6) 
arregloCadenas=(Marco, Antonio, Pedro, Susana) 
arregloRangos=({A..Z} {10..20}) 
#Imprimir todos los valores 
echo "Arreglo de Números:${arregloNumeros[*]}" 
echo "Arreglo de Cadenas:${arregloCadenas[*]}" 
echo "Arreglo de Números:${arregloRangos[*]}" 
#Imprimir los tamaños de los arreglos 
echo "Tamaño Arreglo de Números:${#arregloNumeros[*]}" 
echo "Tamaño Arreglo de Cadenas:${#arregloCadenas[*]}" 
echo "Tamaño Arreglo de Números:${#arregloRangos[*]}" 
#Imprimir la posición 3 del arreglo de números, cadenas de rango 
echo "Posición 3 Arreglo de Números:${arregloNumeros[3]}" 
echo "Posición 3 Arreglo de Cadenas:${arregloCadenas[3]}" 
echo "Posición 3 Arreglo de Rangos:${arregloRangos[3]}" 
#Añadir y eliminar valores en un arreglo 
arregloNumeros[7]=20 
unset arregloNumeros[0] # elimina 
echo "Arreglo de Números:${arregloNumeros[*]}" 
echo "Tamaño arreglo de Números:${#arregloNumeros[*]}"
```

## Menus 
```bash
#!/bin/bash
# Programa para validar procesos, memoria, recursos, variables.
# by: devp

echo ""
echo "**** PROGRAMA VALIDACIÓN RECURSOS ****"
echo ""

opcion=0

while :
do
    # Limpiar Pantalla
    clear
    echo " * Menú Principal * "
    echo ""
    echo "1) Procesos Actuales"
    echo "2) Memoria Disponible"
    echo "3) Espacio en disco"
    echo "4) Información Red"
    echo "5) Variables de entorno configuradas"
    echo "6) Información Programa"
    echo "7) Comprimir Archivos SH"
    echo "8) Salir"
    echo ""

    # Leer datos de usuario
    read -n1 -p "Ingrese la opción a seleccionar (1 - 8): " opcion
    echo ""

    # Validar opción ingresada
    case $opcion in
        1)
            echo -e "\n..Procesos Actuales.."
            ps axu
            sleep 3
            ;;
        2)
            echo -e "\n..Memoria Disponible.."
            free
            sleep 3
            ;;
        3)
            echo -e "\n..Espacio en disco.."
            df -h
            sleep 3
            ;;
        4)
            echo -e "\n..Información Red.."
            ifconfig -a
            sleep 3
            ;;
        5)
            echo -e "\n..Variables de Entorno Configuradas.."
            printenv
            sleep 3
            ;;
        6)
            echo -e "\n..Información Programa.."
            dpkg -l | more
            sleep 3
            ;;
        7)
            echo -e "\n..Comprimendo Archivos.."
            tar -czvf archivosComprimidos.tar.gz *.sh
            echo -e "\n ¡Éxito!"
            sleep 3
            ;;
        8)
            echo -e "\n..Saliendo, ¡¡Gracias!!"
            exit 0
            ;;
        *)
            echo -e "\nOpción no válida. Intente nuevamente."
            sleep 2
            ;;
    esac
done
```
## Archivos


### Escribiendo en archivos

```bash
#!/bin/bash
# Programa para ejemplificar cómo se escribe en un archivo.

echo "Escribir en un archivo"

# Escribir una línea en el archivo usando echo
echo "Valores escritos con el comando echo" >> "$1"

# Adición multilínea al archivo
cat <<EOM >>"$1"
$2
EOM
```

### Lectura de Archivos
```bash
#!/bin/bash
# Programa para ejemplificar cómo se lee en un archivo.
# Autor: Marco Toscano Freire - @martosfre

echo "Leer en un archivo"
cat "$1"

echo -e "\nAlmacenar los valores en una variable"
valorCat=$(cat "$1")
echo "$valorCat"

# Se utiliza la variable IFS (Internal Field Separator) para evitar que los espacios en blanco al inicio o al final se recorten.
echo -e "\nLeer archivos línea por línea utilizando while"
while IFS= read -r linea; do
    echo "$linea"
done < "$1"
```

### ¿Qué es IFS?

`IFS` (Internal Field Separator) es una variable de entorno en Bash que define los caracteres usados para dividir las palabras o líneas en los comandos de shell, especialmente cuando se procesan listas o archivos.

- **Por defecto, IFS incluye:**  
    Espacio ( ), tabulación (`\t`), y nueva línea (`\n`).
    
- **En este caso:**  
    Al asignar `IFS=` antes de `read`, estamos deshabilitando temporalmente su comportamiento predeterminado, asegurándonos de que las líneas del archivo se lean exactamente como están, sin recortar espacios al principio o al final.
### Ejemplo:

Si `archivo.txt` contiene:

```
	línea 1 
línea 2   
línea 3
```

Sin ajustar `IFS`, los espacios de las líneas serían ignorados:
```
línea 1 
línea 2   
línea 3
```

Con `IFS=`, se respetan los espacios en blanco:
```
	línea 1 
línea 2   
línea 3
```

### Empaquetamiento de archivos

El empaquetado y compresión de archivos con herramientas como `tar`, `gzip` y `pbzip` son tareas comunes en sistemas Unix/Linux. Cada herramienta tiene un propósito y se usa en diferentes etapas del proceso. Aquí te lo explico:

---

### 1. **`tar`: Empaquetado de archivos**

`tar` (Tape Archive) empaqueta varios archivos y directorios en un único archivo, llamado "tarball". Este archivo no está comprimido, pero agrupa el contenido para facilitar su manejo.

#### Comandos comunes:

- **Empaquetar archivos en un archivo `.tar`:**
    
    ```bash
    tar -cvf archivo.tar archivo1 archivo2 directorio/
    ```
    
    - `-c`: Crear un archivo.
    - `-v`: Modo detallado (muestra el progreso).
    - `-f`: Especificar el nombre del archivo resultante.
- **Extraer el contenido de un archivo `.tar`:**
    
    ```bash
    tar -xvf archivo.tar
    ```
    
    - `-x`: Extraer contenido.
- **Listar el contenido de un archivo `.tar`:**
    
    ```bash
    tar -tvf archivo.tar
    ```
    

---

### 2. **`gzip`: Compresión de archivos**

`gzip` comprime un archivo (puede ser un archivo tarball o cualquier archivo individual). La compresión se realiza de manera eficiente, aunque no aprovecha completamente procesadores multicore.

#### Comandos comunes:

- **Comprimir un archivo:**
    
    ```bash
    gzip archivo.tar
    ```
    
    Esto genera `archivo.tar.gz`.
    
- **Descomprimir un archivo:**
    
    ```bash
    gzip -d archivo.tar.gz
    ```
    

---

### 3. **`pbzip2`: Compresión paralela**

`pbzip2` es una variante de `bzip2` que permite aprovechar múltiples núcleos del procesador para acelerar la compresión. Es útil para archivos grandes en sistemas modernos.

#### Comandos comunes:

- **Comprimir un archivo:**
    
    ```bash
    pbzip2 archivo.tar
    ```
    
    Esto genera `archivo.tar.bz2`.
    
- **Descomprimir un archivo:**
    
    ```bash
    pbzip2 -d archivo.tar.bz2
    ```
    
- **Controlar el número de núcleos usados:**
    
    ```bash
    pbzip2 -p8 archivo.tar
    ```
    
    Usa 8 núcleos para la compresión.
    

---

### 4. **Usar `tar` con compresión integrada**

`tar` puede trabajar directamente con `gzip`, `bzip2`, o `pbzip2`, evitando pasos adicionales.

#### Empaquetar y comprimir:

- **Con `gzip`:**
    
    ```bash
    tar -cvzf archivo.tar.gz archivo1 archivo2 directorio/
    ```
    
    - `-z`: Usa `gzip` para comprimir.
- **Con `pbzip2`:**
    
    ```bash
    tar -cvjf archivo.tar.bz2 archivo1 archivo2 directorio/
    ```
    
    - `-j`: Usa `bzip2` o su variante `pbzip2`.

#### Extraer archivos comprimidos:

- **Con `gzip`:**
    
    ```bash
    tar -xvzf archivo.tar.gz
    ```
    
- **Con `pbzip2`:**
    
    ```bash
    tar -xvjf archivo.tar.bz2
    ```
    

---

### Comparación de herramientas

|Herramienta|Velocidad|Compresión|Multinúcleo|Extensión|
|---|---|---|---|---|
|`tar`|Rápido|No aplica|No|`.tar`|
|`gzip`|Rápido|Media|No|`.gz`|
|`pbzip2`|Más lento|Alta|Sí|`.bz2`|

---

### Ejemplo práctico

1. **Empaquetar y comprimir con `pbzip2`:**
    
    ```bash
    tar -cvjf archivos.tar.bz2 archivo1 archivo2 directorio/
    ```
    
2. **Extraer el archivo comprimido:**
    
    ```bash
    tar -xvjf archivos.tar.bz2
    ```

ahora para garantizar la seguridad de la compresión de archivos podemos utilizar `zip`, esto a traves del parámetro `-e` no permite darle un clave de seguridad.

### Transfiriendo información por la `Red`
para esto utilizaremos [rzync]([Sincronización a fondo con rsync en Ubuntu, Linux Mint y derivados - atareao con Linux](https://atareao.es/software-linux/sincronizacion-a-fondo-con-rsync/))

### **`rsync`: Sincronización y Copia de Archivos**

`rsync` es una poderosa herramienta de línea de comandos en Linux/Unix para sincronizar y copiar archivos o directorios entre sistemas locales y remotos. Es eficiente porque solo transfiere los datos que han cambiado, minimizando el uso del ancho de banda y el tiempo de transferencia.

---

### **Principales características de `rsync`**

1. **Sincronización incremental**: Solo transfiere los cambios entre los archivos fuente y destino.
2. **Compresión**: Usa compresión durante la transferencia para ahorrar ancho de banda.
3. **Transferencias seguras**: Puede usar SSH para transferir datos de manera segura.
4. **Versatilidad**: Funciona localmente o entre servidores remotos.
5. **Preservación de atributos**: Conserva permisos, propietarios, marcas de tiempo, etc.

---

### **Comandos básicos**

1. **Sincronizar un directorio localmente:**
    
    ```bash
    rsync -av /ruta/origen/ /ruta/destino/
    ```
    
    - `-a`: Modo archivo, preserva atributos como permisos y marcas de tiempo.
    - `-v`: Modo detallado, muestra la salida.
2. **Sincronizar a un servidor remoto:**
    
    ```bash
    rsync -av /ruta/origen/ usuario@servidor:/ruta/destino/
    ```
    
3. **Sincronizar desde un servidor remoto:**
    
    ```bash
    rsync -av usuario@servidor:/ruta/origen/ /ruta/destino/
    ```
    
4. **Eliminar archivos en el destino que no estén en el origen:**
    
    ```bash
    rsync -av --delete /ruta/origen/ /ruta/destino/
    ```
    
5. **Comprimir datos durante la transferencia:**
    
    ```bash
    rsync -avz /ruta/origen/ usuario@servidor:/ruta/destino/
    ```
    
    - `-z`: Habilita la compresión.

---

### **Opciones útiles**

|**Opción**|**Descripción**|
|---|---|
|`-a`|Preserva permisos, propietarios, grupos, marcas de tiempo, y enlaces simbólicos.|
|`-v`|Muestra detalles de los archivos sincronizados.|
|`-z`|Comprime los datos durante la transferencia.|
|`--delete`|Elimina archivos en el destino que no existen en el origen.|
|`-e ssh`|Usa SSH para la transferencia segura.|
|`--progress`|Muestra el progreso de la transferencia.|
|`--exclude`|Excluye ciertos archivos o directorios (pueden usarse comodines).|

---

### **Ejemplos avanzados**

1. **Sincronizar con progreso y compresión:**
    
    ```bash
    rsync -avz --progress /ruta/origen/ usuario@servidor:/ruta/destino/
    ```
    
2. **Excluir ciertos archivos o directorios:**
    
    ```bash
    rsync -av --exclude="*.tmp" --exclude="carpeta_ignorar/" /ruta/origen/ /ruta/destino/
    ```
    
3. **Sincronizar entre servidores remotos:**
    
    ```bash
    rsync -av usuario1@servidor1:/ruta/origen/ usuario2@servidor2:/ruta/destino/
    ```
    
4. **Crear copias de respaldo incrementales:**
    
    ```bash
    rsync -av --delete /ruta/origen/ /ruta/backup/
    ```
    

---

### **Ventajas de `rsync` frente a otros métodos**

1. **Incremental**: Solo transfiere los cambios.
2. **Velocidad**: Usando compresión (`-z`), reduce el tiempo de transferencia.
3. **Versatilidad**: Compatible con copias locales y remotas.
4. **Seguridad**: Usa SSH (`-e ssh`) para transferencias seguras.

---

### **Casos de uso comunes**

1. **Hacer copias de seguridad locales o remotas.**
2. **Sincronizar datos entre servidores en tiempo real.**
3. **Migrar directorios grandes entre sistemas.**
4. **Mantener directorios espejo en múltiples ubicaciones.**

---

### **Comando práctico para respaldo completo**

```bash
rsync -avz --delete --progress -e ssh /home/usuario/ usuario@servidor:/backup/usuario/
```

Este comando:

1. **Sincroniza** el directorio `/home/usuario/` con la carpeta `/backup/usuario/` en el servidor remoto.
2. Usa **compresión** (`-z`) y **elimina** (`--delete`) archivos obsoletos en el destino.
3. Transfiere de forma **segura** mediante SSH (`-e ssh`).

---

### Ejemplo DB 
```bash
#!/bin/bash
# Programa que permite manejar las utilidades de Postgres

opcion=0
fechaActual=$(date +%Y%m%d)

# Función para instalar Postgres
instalar_postgres() {
    echo -e "\nVerificar instalación de Postgres..."
    verifyInstall=$(which psql)
    if [ $? -eq 0 ]; then
        echo -e "\nPostgres ya está instalado en el equipo."
    else
        echo -e "\n"
        read -s -p "Ingrese contraseña de sudo: " password
        echo -e "\n"
        read -s -p "Ingrese contraseña para Postgres: " passwordPostgres
        echo "$password" | sudo -S apt update
        echo "$password" | sudo -S apt-get -y install postgresql postgresql-contrib
        sudo -u postgres psql -c "ALTER USER postgres WITH PASSWORD '$passwordPostgres';"
        echo "$password" | sudo -S systemctl enable postgresql.service
        echo "$password" | sudo -S systemctl start postgresql.service
    fi
    read -n 1 -s -r -p "PRESIONE [ENTER] para continuar..."
}

# Función para desinstalar Postgres
desinstalar_postgres() {
    echo -e "\n"
    read -s -p "Ingrese contraseña de sudo: " password
    echo -e "\n"
    echo "$password" | sudo -S systemctl stop postgresql.service
    echo "$password" | sudo -S apt-get -y --purge remove postgresql\*
    echo "$password" | sudo -S rm -r /etc/postgresql
    echo "$password" | sudo -S rm -r /etc/postgresql-common
    echo "$password" | sudo -S rm -r /var/lib/postgresql
    echo "$password" | sudo -S userdel -r postgres
    echo "$password" | sudo -S groupdel postgresql
    read -n 1 -s -r -p "PRESIONE [ENTER] para continuar..."
}

# Función para sacar un respaldo
sacar_respaldo() {
    echo "Listar las bases de datos:"
    sudo -u postgres psql -c "\l"
    read -p "Elija la base de datos a respaldar: " bddRespaldo
    echo -e "\n"
    if [ -d "$1" ]; then
        echo "Estableciendo permisos al directorio..."
        echo "$password" | sudo -S chmod 755 $1
        echo "Realizando respaldo..."
        sudo -u postgres pg_dump -Fc $bddRespaldo > "$1/bddRespaldo_$fechaActual.bak"
        echo "Respaldo realizado correctamente en la ubicación: $1/bddRespaldo_$fechaActual.bak"
    else
        echo "El directorio $1 no existe."
    fi
    read -n 1 -s -r -p "PRESIONE [ENTER] para continuar..."
}

# Función para restaurar un respaldo
restaurar_respaldo() {
    echo "Listar respaldos disponibles:"
    ls -1 $1/*.bak
    read -p "Elija el respaldo a restaurar: " respaldoRestaurar
    echo -e "\n"
    read -p "Ingrese el nombre de la base de datos destino: " bddDestino
    verifyBdd=$(sudo -u postgres psql -lqt | cut -d \| -f 1 | grep -wq $bddDestino)
    if [ $? -eq 0 ]; then
        echo "Restaurando en la base de datos destino: $bddDestino"
    else
        sudo -u postgres psql -c "CREATE DATABASE $bddDestino"
    fi

    if [ -f "$1/$respaldoRestaurar" ]; then
        echo "Restaurando respaldo..."
        sudo -u postgres pg_restore -Fc -d $bddDestino "$1/$respaldoRestaurar"
        echo "Listando las bases de datos:"
        sudo -u postgres psql -c "\l"
    else
        echo "El respaldo $respaldoRestaurar no existe."
    fi
    read -n 1 -s -r -p "PRESIONE [ENTER] para continuar..."
}

# Menú principal
while :; do
    clear
    echo "_________________________________________"
    echo "PGUTIL - Programa de Utilidad de Postgres"
    echo "_________________________________________"
    echo "                MENÚ PRINCIPAL           "
    echo "_________________________________________"
    echo "1. Instalar Postgres"
    echo "2. Desinstalar Postgres"
    echo "3. Sacar un respaldo"
    echo "4. Restaurar respaldo"
    echo "5. Salir"
    echo "_________________________________________"

    read -n1 -p "Ingrese una opción [1-5]: " opcion
    echo -e "\n"

    case $opcion in
    1)
        instalar_postgres
        sleep 3
        ;;
    2)
        desinstalar_postgres
        sleep 3
        ;;
    3)
        read -p "Directorio para el respaldo: " directorioBackup
        sacar_respaldo $directorioBackup
        sleep 3
        ;;
    4)
        read -p "Directorio de respaldos: " directorioRespaldos
        restaurar_respaldo $directorioRespaldos
        sleep 3
        ;;
    5)
        echo "Saliendo del programa..."
        exit 0
        ;;
    *)
        echo "Opción no válida. Intente de nuevo."
        sleep 2
        ;;
    esac
done

```