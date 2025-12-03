# Práctica Final DevOps: CI/CD con GitHub Actions y Docker

Este proyecto implementa un flujo de trabajo completo de **Integración Continua y Despliegue Continuo (CI/CD)** para una aplicación web simple hecha en Python con Flask.

## 👤 Datos del Alumno

- **Nombre:** George
- **Matrícula:** 20240001
- **Materia:** DevOps

---

## 🚀 Descripción del Proyecto

El objetivo de esta práctica es automatizar el ciclo de vida del software desde el desarrollo hasta producción.

### Flujo de Trabajo (Pipeline)

Cada vez que se hace un `push` a la rama `main`, GitHub Actions ejecuta automáticamente los siguientes pasos:

1.  **Test (CI):**
    - Descarga el código.
    - Instala las dependencias (`flask`, `pytest`).
    - Ejecuta pruebas unitarias para asegurar que la app funciona y muestra los datos correctos.
2.  **Build & Push (CD - Parte 1):**
    - Si las pruebas pasan, construye una imagen de Docker.
    - Sube la imagen a **Docker Hub** (`registry` público).
3.  **Deploy (CD - Parte 2):**
    - Utiliza un _Webhook_ para notificar a **Render**.
    - Render descarga la nueva imagen y actualiza el sitio web en producción automáticamente.

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.9 (Flask)
- **Contenedores:** Docker
- **Orquestación CI/CD:** GitHub Actions
- **Repositorio de Imágenes:** Docker Hub
- **Producción:** Render

---

## 📂 Estructura del Proyecto

- `app.py`: Código fuente de la aplicación web.
- `test_app.py`: Pruebas unitarias automatizadas.
- `Dockerfile`: Instrucciones para empaquetar la aplicación.
- `requirements.txt`: Dependencias del proyecto.
- `.github/workflows/pipeline.yml`: Configuración del pipeline de CI/CD.

---

## 🔗 Enlace del Proyecto En Produccion

- **Render:**
  (https://devops-practica-final-v0b2.onrender.com)
