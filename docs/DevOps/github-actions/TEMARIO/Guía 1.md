# Creación de un flujo de trabajo con GitHub Actions

**En esta guía, aprenderemos**:

- Cómo crear un archivo de flujo de trabajo de GitHub Actions
    
- Cómo desencadenar un flujo de trabajo de acuerdo con eventos específicos de GitHub
    
- Cómo ejecutar una acción reutilizable en tu flujo de trabajo
    
- Cómo ejecutar un flujo de trabajo mediante un ejecutor hospedado en GitHub

# Pasos para la preparación del entorno
1. Abra el archivo [Repositorio actions-learning-pathway](https://github.com/github/actions-learning-pathway) en una nueva pestaña.
    
2. Haga clic en **Usar esta plantilla** encima de la lista de archivos y seleccione **Crear un nuevo repositorio**.
    
3. Utilice el menú desplegable **Propietario** para seleccionar la cuenta que desea que sea propietaria del repositorio.
    
4. Asigne un nombre a su repositorio y agregue una descripción simple para que sea más fácil de identificar más adelante.`actions-learning-pathway`
    
5. Establezca la visibilidad predeterminada para el repositorio en público, como repositorios privados [Usar minutos de acciones](https://docs.github.com/en/billing/managing-billing-for-github-actions/about-billing-for-github-actions), mientras que los repositorios públicos pueden usar ejecutores hospedados en GitHub de forma gratuita.
    
6. Haga clic en **Crear repositorio a partir de plantilla** y estaremos listos para crear nuestro primer flujo de trabajo de acciones.

# Preparar el entorno local
1. Clonar el repositorio
```bash
gh repo clone KEVIN-117/learning-github-actions
```
