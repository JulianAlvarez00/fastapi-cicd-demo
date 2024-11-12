# FastAPI CI/CD Demo

Una aplicación FastAPI con CI/CD desplegada en Render.com

## Endpoints

- `/`: Mensaje de bienvenida
- `/health`: Health check
- `/docs`: Documentación OpenAPI (Swagger)

## Pipeline

El pipeline incluye:
1. Tests automatizados
2. Build de imagen Docker
3. Deploy automático en Render.com

## Desarrollo Local

```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
uvicorn src.main:app --reload