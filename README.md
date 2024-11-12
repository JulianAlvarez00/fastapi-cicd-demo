# FastAPI DevOps Dashboard Demo

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)

Una aplicación dashboard moderna construida con FastAPI y desplegada en Render.com, implementando CI/CD con GitHub Actions.

## 🌟 Características

- ⚡ API REST con FastAPI
- 🎨 Dashboard moderno con Tailwind CSS
- 📊 Visualización de datos con Chart.js
- 🐳 Containerización con Docker
- 🚀 CI/CD automatizado
- 📈 Monitoreo de estado en tiempo real
- 🔄 Actualizaciones automáticas de datos

## 🚀 Demo

Visita la aplicación en vivo: [https://fastapi-cicd-demo.onrender.com](https://fastapi-cicd-demo.onrender.com)

## 🛠️ Stack Tecnológico

- **Backend**: FastAPI
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Charts**: Chart.js
- **CI/CD**: GitHub Actions
- **Containerización**: Docker
- **Hosting**: Render.com
- **Testing**: pytest

## 📋 Prerrequisitos

- Python 3.11+
- Docker
- Git

## 🚀 Instalación Local

1. Clonar el repositorio
```bash
git clone https://github.com/JulianAlvarez00/fastapi-cicd-demo.git
cd fastapi-cicd-demo
```

2. Crear y activar entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
```

3. Instalar dependencias
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación
```bash
uvicorn src.main:app --reload
```

La aplicación estará disponible en `http://localhost:8000`

## 🐳 Ejecutar con Docker

```bash
# Construir la imagen
docker build -t fastapi-app .

# Ejecutar el contenedor
docker run -p 8000:8000 fastapi-app
```

## 🔍 Endpoints API

- `GET /`: Dashboard principal
- `GET /api/health`: Health check endpoint
- `GET /api/stats`: Estadísticas del sistema
- `GET /docs`: Documentación OpenAPI (Swagger)

## 🧪 Tests

Ejecutar los tests con pytest:
```bash
pytest
```

## 📁 Estructura del Proyecto

```
fastapi-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── static/
│   │   └── css/
│   │       └── styles.css
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── Dockerfile
├── README.md
├── render.yaml
└── requirements.txt
```

## 🔄 CI/CD Pipeline

El pipeline incluye:
1. Ejecución automática de tests
2. Build de imagen Docker
3. Deploy automático en Render.com

## 📊 Características del Dashboard

- 🟢 Indicador de estado del sistema en tiempo real
- 📈 Métricas actualizadas automáticamente
- 📊 Gráfico interactivo de tiempo de respuesta
- 🔄 Actualización automática cada 30 segundos
- 📱 Diseño responsive para todos los dispositivos

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al Branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Variables de Entorno

| Variable | Descripción | Valor por defecto |
|----------|-------------|-------------------|
| PORT | Puerto para la aplicación | 8000 |


## ✨ Próximas Características

- [ ] Autenticación de usuarios
- [ ] Panel de administración
- [ ] Más visualizaciones y gráficos
- [ ] Filtros de fecha para métricas
- [ ] Sistema de alertas y notificaciones
- [ ] Exportación de datos
- [ ] Temas personalizables
- [ ] Integración con más servicios

## 🛠️ Tecnologías y Dependencias

```
fastapi==0.104.1
uvicorn==0.24.0
jinja2==3.1.2
pytest==7.4.3
requests==2.31.0
python-multipart==0.0.6
```

## 🔧 Configuración de Desarrollo

### Configuración del Entorno
```bash
# Instalación de dependencias de desarrollo
pip install -r requirements.txt

# Verificar instalación
python -c "import fastapi; print(fastapi.__version__)"
```

### Comandos Útiles
```bash
# Ejecutar tests
pytest

# Ejecutar con recarga automática
uvicorn src.main:app --reload

# Construir imagen Docker
docker build -t fastapi-app .

# Ejecutar contenedor Docker
docker run -p 8000:8000 fastapi-app
```

## 📘 Documentación API

La documentación completa de la API está disponible en:
- Swagger UI: `/docs`
- ReDoc: `/redoc`

## 🔍 Monitoreo y Logs

- Los logs del sistema están disponibles en el dashboard de Render
- Monitoreo de estado en tiempo real en el endpoint `/api/health`
- Métricas del sistema disponibles en `/api/stats`

## 🚀 Despliegue

El despliegue se realiza automáticamente en Render.com cuando se hace push a la rama main. El pipeline de CI/CD incluye:

1. Verificación de código
2. Ejecución de tests
3. Build de imagen Docker
4. Despliegue automático

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:
1. Revisa los [issues existentes](https://github.com/JulianAlvarez00/fastapi-cicd-demo/issues)
2. Abre un nuevo issue con detalles específicos
3. Incluye logs relevantes y pasos para reproducir el problema

## 👥 Contribuidores

- [Julian Alvarez](https://github.com/JulianAlvarez00) - Creador y mantenedor principal

## 📣 Agradecimientos

- FastAPI por el excelente framework
- Render por el hosting
- La comunidad open source

---
⌨️ con ❤️ por [Julian Alvarez](https://github.com/JulianAlvarez) | © 2024