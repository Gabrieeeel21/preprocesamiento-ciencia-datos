# DOCUMENTACIÓN.md

## Introducción

### Objetivo del proyecto:
El objetivo de este proyecto es aplicar herramientas y metodologías en Ciencia de Datos para realizar un preprocesamiento completo de datasets utilizando Pandas. Además, se busca implementar el uso de Git y GitHub para la gestión de versiones y la colaboración en proyectos de Ciencia de Datos.

### Funcionalidades implementadas:
1. **Preprocesamiento de datos**: Creación de un archivo `preprocesamiento.py` con funciones para la gestión de valores nulos, normalización de datos, codificación de variables categóricas y eliminación de duplicados en el dataset.
2. **Gestión de versiones**: Uso de Git y GitHub para versionar el código, gestionar ramas y fusionar cambios.
3. **Automatización**: Implementación de un workflow básico utilizando GitHub Actions para automatizar el flujo de trabajo de integración continua.

## Comandos Git Usados

A continuación se presentan los comandos de Git utilizados en el proyecto:

1. **`git init`**:
   - **Descripción**: Inicializa un nuevo repositorio de Git en el directorio actual.
   - **Propósito**: Se utiliza para comenzar a versionar el proyecto en Git.

2. **`git add .`**:
   - **Descripción**: Agrega todos los archivos modificados al área de staging.
   - **Propósito**: Preparar los archivos para ser confirmados en el repositorio.

3. **`git commit -m "mensaje"`**:
   - **Descripción**: Realiza un commit de los archivos en el área de staging.
   - **Propósito**: Registrar los cambios realizados en el repositorio con un mensaje descriptivo.

4. **`git push`**:
   - **Descripción**: Envía los cambios locales al repositorio remoto de GitHub.
   - **Propósito**: Subir los commits realizados al repositorio de GitHub para compartir los cambios con otros colaboradores.

5. **`git pull`**:
   - **Descripción**: Recupera los cambios del repositorio remoto y los fusiona con la rama local.
   - **Propósito**: Asegurarse de tener la versión más actualizada del proyecto antes de hacer nuevas modificaciones.

6. **`git branch nombre-de-rama`**:
   - **Descripción**: Crea una nueva rama para trabajar en nuevas funcionalidades.
   - **Propósito**: Permitir el trabajo en paralelo sin afectar la rama principal.

7. **`git merge nombre-de-rama`**:
   - **Descripción**: Fusiona los cambios de una rama en otra.
   - **Propósito**: Unir los cambios realizados en una rama con la rama principal.
  
## Automatización

### Explicación del workflow de GitHub Actions

El workflow de GitHub Actions creado en este proyecto tiene como propósito automatizar ciertas tareas como:

- **Integración continua**: Cada vez que se realiza un `push` al repositorio, el workflow se ejecuta para asegurarse de que los scripts de preprocesamiento funcionan correctamente en un entorno limpio.
- **Automatización de pruebas**: Si se agregan pruebas en el futuro, el workflow puede ejecutarlas automáticamente para verificar que no haya errores en el código.
- **Despliegue**: Este workflow podría ser extendido para automatizar el despliegue de scripts o resultados generados.

### Workflow básico de GitHub Actions:
- **Eventos**: Se activa cuando hay un `push` a cualquier rama del repositorio.
- **Acciones**: 
  - Configuración del entorno Python.
  - Instalación de dependencias necesarias (por ejemplo, `pandas`).
  - Ejecución de scripts de preprocesamiento.
  - Verificación de que el código se ejecute sin errores.
