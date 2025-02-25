Jenkins, Terraform, Ansible, Docker y más (orientado a Java)

---

## Temario
### **1. Introducción a DevOps**

- ¿Qué es DevOps y por qué es importante?
- Ciclo de vida de desarrollo de software y su relación con DevOps.
- Principios y prácticas de DevOps.

---

### **2. Gestión de Proyectos con Jira**

- Introducción a Jira y sus características principales.
- Creación y gestión de proyectos y tareas en Jira.
- Uso de tableros Kanban y Scrum en Jira.
- Integración de Jira con otras herramientas de DevOps.

---

### **3. Infraestructura como Código con Terraform**

- Introducción a Terraform, instalación y configuración.
- Creación y gestión de recursos con Terraform.
- Trabajo con módulos y variables en Terraform.
- Uso de providers AWS, DigitalOcean, Linode.  
    _(Considerar para prácticas independientes aprox. $0.089 dólares por hora en AWS; si usas DigitalOcean o Linode podrás emplear el crédito gratuito que estas ofrecen)._

---

### **4. Automatización de Configuración con Ansible**

- Introducción a Ansible, instalación y configuración.
- Creación de playbooks y roles en Ansible.
- Gestión de configuración y despliegue de aplicaciones con Ansible.

---

### **5. Control de Versiones con Git**

- Introducción a Git, instalación y configuración.
- Uso de comandos.
- Resolución de conflictos.
- Gitflow para trabajo en equipo.
- Uso de GitHub, GitLab y Bitbucket.

---

### **6. Integración y Entrega Continua con Jenkins**

- Introducción a Jenkins, instalación y configuración.
- Creación de jobs freestyle project de CI/CD.
- Creación de pipelines de CI/CD.
- Uso de hooks, parameters, stages, global tool configuration, credentials y plugins.
- Arquitectura de maestro-esclavo.
- Integración de herramientas de control de versiones: GitHub, GitLab y Bitbucket.

---

### **7. Análisis de Código con SonarQube**

- Introducción a SonarQube, instalación y configuración.
- Ejecución de análisis de código.
- Uso de métricas para mejorar la calidad del código.
- Integración con Jenkins.

---

### **8. Gestión de Artefactos con Artifactory y Nexus**

- Introducción a Artifactory y Nexus, instalación y configuración.
- Gestión de artefactos y versiones.
- Tipos de repositorios: virtual, local, remote, group, proxy, hosted.
- Integración con Jenkins.

---

### **9. Contenedores y Virtualización con Docker**

- Introducción a Docker, instalación y configuración.
- Uso de comandos.
- Uso de Docker en un entorno de CI/CD.
- Integración con Jenkins.

---

### **10. Orquestación de Contenedores con Kubernetes**

- Introducción a Kubernetes, instalación y configuración.
- Creación y gestión de clústeres de Kubernetes.
- Uso de pods.
- Implementación de aplicaciones en un clúster de Kubernetes.
- Uso de Kubernetes en un entorno de CI/CD.
- Integración con Jenkins.

---

### **11. Pruebas Continuas**

- Pirámide Cohn.
- Introducción al desarrollo guiado por comportamiento.
- Escritura de especificaciones en Gherkin.
- Uso de Cucumber en pruebas.
- Integración con Jenkins.
- **Pruebas de Integración:**
    - Introducción a las pruebas de servicios REST.
    - Configuración de un proyecto de pruebas con Rest Assured.
    - Informes de resultados de pruebas con Serenity BDD.
- **Pruebas de E2E:**
    - Introducción a las pruebas de aceptación automatizadas.
    - Configuración de un proyecto de pruebas con Selenium Docker.
    - Informes de resultados de pruebas con Cucumber Reports.

---

## Temario Mejorado
---
### **1. Introducción a DevOps (Teoría y Práctica)**

- **Objetivo:** Comprender el impacto y las ventajas de DevOps en el desarrollo y la entrega de software.
- **Contenido:**
    - ¿Qué es DevOps y cómo transforma equipos?
    - _Framework CALMS:_ Cultura, Automatización, Lean, Métricas y Compartición.
    - Comparación de metodologías tradicionales y DevOps.
- **Mejora:** Incluye casos de estudio reales sobre empresas que implementaron DevOps (Netflix, Spotify).

---

### **2. Gestión de Proyectos con Jira (Integración con DevOps)**

- **Objetivo:** Usar Jira para gestionar proyectos ágiles con metodologías DevOps.
- **Contenido:**
    - Creación de epics, historias de usuario y tareas técnicas.
    - _Automatización en Jira:_ Configura reglas para flujos de trabajo repetitivos.
    - Integración con Bitbucket, GitHub o Jenkins.
- **Mejora:** Proporciona un proyecto de práctica para gestionar un pipeline completo con Jira.

---

### **3. Infraestructura como Código (IaC) con Terraform**

- **Objetivo:** Dominar la creación, modificación y destrucción de infraestructura usando código.
- **Contenido:**
    - Introducción a HCL (HashiCorp Configuration Language).
    - **Novedad:** Uso de _Terraform Cloud_ para colaboración.
    - Integración con proveedores más modernos: Azure, Google Cloud.
- **Mejora:** Propón un escenario de despliegue real (configurar una aplicación en AWS o DigitalOcean).

---

### **4. Automatización de Configuración con Ansible**

- **Objetivo:** Configurar sistemas y aplicaciones automáticamente.
- **Contenido:**
    - _Dynamic Inventory_ con proveedores como AWS o Azure.
    - Integración con Docker y Kubernetes.
    - Mejores prácticas para playbooks robustos.
- **Mejora:** Introduce prácticas con _Ansible Tower_ para la gestión centralizada.

---

### **5. Control de Versiones con Git**

- **Objetivo:** Aprovechar Git como herramienta colaborativa y de automatización.
- **Contenido:**
    - Configuración avanzada: hooks de pre-commit y plantillas de commit.
    - Flujos modernos: GitLab Flow, Trunk-Based Development.
    - Integración con CI/CD.
- **Mejora:** Incluye ejercicios de resolución de conflictos en escenarios reales.

---

### **6. Integración y Entrega Continua (CI/CD) con Jenkins**

- **Objetivo:** Automatizar pipelines desde el código hasta la producción.
- **Contenido:**
    - Integración con Docker, Kubernetes y herramientas de IaC.
    - Uso de _Blue Ocean_ para visualización moderna de pipelines.
    - **Novedad:** Alternativa moderna a Jenkins: GitHub Actions.
- **Mejora:** Diseña pipelines híbridos que incluyan pruebas, despliegues y análisis de calidad.

---

### **7. Análisis de Código con SonarQube**

- **Objetivo:** Mejorar la calidad del código y mantener estándares.
- **Contenido:**
    - Métricas críticas: _Code Smells_, deuda técnica y cobertura.
    - Configuración avanzada con Quality Gates.
    - Escaneo en múltiples lenguajes (Java, Python, JS).
- **Mejora:** Introduce _SonarCloud_ como alternativa en proyectos de código abierto.

---

### **8. Gestión de Artefactos con Artifactory y Nexus**

- **Objetivo:** Manejar artefactos y sus dependencias de manera eficiente.
- **Contenido:**
    - Creación de repositorios para Docker Images, Maven y NPM.
    - Optimización con _Caching Proxies_ para entornos CI/CD.
- **Mejora:** Introduce ejemplos prácticos de despliegues desde Nexus.

---

### **9. Contenedores y Virtualización con Docker**

- **Objetivo:** Dominar la contenedorización para facilitar el despliegue.
- **Contenido:**
    - Creación de imágenes optimizadas con multi-stage builds.
    - Uso avanzado: Docker Compose y Docker Swarm.
    - Configuración de redes y volúmenes.
- **Mejora:** Agrega prácticas con herramientas como _Podman_ o _Buildah_.

---

### **10. Orquestación de Contenedores con Kubernetes**

- **Objetivo:** Gestionar aplicaciones complejas y escalables.
- **Contenido:**
    - Introducción al ecosistema: Helm, Kubectl, Kustomize.
    - Implementación de aplicaciones en múltiples entornos (Dev, Prod).
    - **Novedad:** Uso de _K3s_ para aprender Kubernetes en máquinas locales ligeras.
- **Mejora:** Incluye configuración con _Service Mesh_ (Istio o Linkerd).

---

### **11. Pruebas Continuas**

- **Objetivo:** Automatizar pruebas para garantizar la calidad en cada entrega.
- **Contenido:**
    - Pruebas unitarias: Frameworks como JUnit, PyTest, Jest.
    - Pruebas de integración: REST Assured para APIs.
    - Pruebas E2E: Cypress o Playwright.
    - **Novedad:** Introduce _Mutation Testing_ para medir la efectividad de las pruebas.
- **Mejora:** Crea una práctica completa con un pipeline que incluya pruebas continuas.

---

### **12. Observabilidad y Monitoreo**

- **Objetivo:** Detectar y resolver problemas en tiempo real.
- **Contenido:**
    - Uso de Prometheus para métricas.
    - Visualización con Grafana.
    - Configuración de alertas.
    - **Novedad:** Introducción a OpenTelemetry para trazabilidad distribuida.
- **Mejora:** Añade ejercicios prácticos con simulaciones de fallos.

---

### **Beneficios de la Versión Mejorada**

- **Actualización:** Se incorporan herramientas más modernas y prácticas del mercado actual.
- **Prácticas Reales:** Ejercicios basados en escenarios reales.
- **Escalabilidad:** Cubres herramientas avanzadas que te preparan para entornos empresariales complejos.

## Cronograma

### **Semana 1: Introducción a DevOps**

**Objetivo:** Comprender los fundamentos y la importancia de DevOps.

- ¿Qué es DevOps y por qué es importante?
- Ciclo de vida del desarrollo de software y su relación con DevOps.
- Principios y prácticas de DevOps.  
    **Tiempo estimado:** 8 horas.

---

### **Semana 2: Gestión de Proyectos con Jira**

**Objetivo:** Aprender a gestionar proyectos y tareas con Jira.

- Introducción a Jira y sus características principales.
- Creación y gestión de proyectos y tareas en Jira.
- Uso de tableros Kanban y Scrum en Jira.
- Integración de Jira con otras herramientas de DevOps.  
    **Tiempo estimado:** 10 horas.

---

### **Semana 3 y 4: Infraestructura como Código con Terraform**

**Objetivo:** Implementar y gestionar infraestructura como código.

- Introducción a Terraform, instalación y configuración.
- Creación y gestión de recursos con Terraform.
- Trabajo con módulos y variables.
- Uso de providers (AWS, DigitalOcean, Linode).  
    **Tiempo estimado:** 15 horas por semana.

---

### **Semana 5: Automatización de Configuración con Ansible**

**Objetivo:** Automatizar configuraciones y despliegues.

- Introducción a Ansible, instalación y configuración.
- Creación de playbooks y roles.
- Gestión de configuración y despliegue de aplicaciones.  
    **Tiempo estimado:** 12 horas.

---

### **Semana 6: Control de Versiones con Git**

**Objetivo:** Aprender Git y trabajo colaborativo.

- Introducción a Git, instalación y configuración.
- Uso de comandos básicos y avanzados.
- Resolución de conflictos.
- Gitflow para trabajo en equipo.
- Uso de GitHub, GitLab y Bitbucket.  
    **Tiempo estimado:** 10 horas.

---

### **Semana 7: Integración y Entrega Continua con Jenkins**

**Objetivo:** Configurar y trabajar con pipelines CI/CD.

- Introducción a Jenkins, instalación y configuración.
- Creación de jobs freestyle y pipelines de CI/CD.
- Uso de hooks, parámetros, stages, global tools, credentials y plugins.
- Arquitectura maestro-esclavo.
- Integración con herramientas de control de versiones.  
    **Tiempo estimado:** 15 horas.

---

### **Semana 8: Análisis de Código con SonarQube**

**Objetivo:** Mejorar la calidad del código mediante análisis.

- Introducción a SonarQube, instalación y configuración.
- Ejecución de análisis de código.
- Uso de métricas para mejorar la calidad del código.
- Integración con Jenkins.  
    **Tiempo estimado:** 10 horas.

---

### **Semana 9: Gestión de Artefactos con Artifactory y Nexus**

**Objetivo:** Administrar artefactos y repositorios.

- Introducción a Artifactory y Nexus, instalación y configuración.
- Gestión de artefactos y versiones.
- Tipos de repositorios: virtual, local, remote, group, proxy, hosted.
- Integración con Jenkins.  
    **Tiempo estimado:** 10 horas.

---

### **Semana 10: Contenedores y Virtualización con Docker**

**Objetivo:** Crear y gestionar contenedores.

- Introducción a Docker, instalación y configuración.
- Uso de comandos básicos y avanzados.
- Uso de Docker en un entorno de CI/CD.
- Integración con Jenkins.  
    **Tiempo estimado:** 12 horas.

---

### **Semana 11: Orquestación de Contenedores con Kubernetes**

**Objetivo:** Gestionar clústeres y aplicaciones con Kubernetes.

- Introducción a Kubernetes, instalación y configuración.
- Creación y gestión de clústeres.
- Uso de pods y despliegue de aplicaciones.
- Uso de Kubernetes en un entorno de CI/CD.
- Integración con Jenkins.  
    **Tiempo estimado:** 15 horas.

---

### **Semana 12: Pruebas Continuas**

**Objetivo:** Automatizar pruebas y mejorar la calidad de entrega.

- Pirámide Cohn y desarrollo guiado por comportamiento.
- Escritura de especificaciones en Gherkin.
- Uso de Cucumber y su integración con Jenkins.
- Pruebas de integración con Rest Assured y Serenity BDD.
- Pruebas E2E con Selenium Docker y Cucumber Reports.  
    **Tiempo estimado:** 15 horas.