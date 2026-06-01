import os
import argparse
from pathlib import Path

def crear_archivo(ruta: str, contenido: str):
    Path(ruta).parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido.strip() + "\n")

def init_ai_project(nombre_proyecto: str):
    base_dir = Path(nombre_proyecto)
    base_dir.mkdir(exist_ok=True)
    
    # Estructura principal de directorios
    directorios = ["src", "tests", "docs/ai", "infrastructure"]
    for d in directorios:
        (base_dir / d).mkdir(parents=True, exist_ok=True)

    # 1. Reglas Globales (Se lee automáticamente en cada prompt)
    reglas = """
# Reglas del Proyecto para la IA
- Escribe el código en Python usando tipado estricto (Type Hints).
- Prioriza FastAPI para el backend y mantén una estructuración modular y limpia.
- Todo servicio debe estar preparado para ejecutarse en Docker.
- ANTES de sugerir código nuevo o hacer modificaciones estructurales, lee OBLIGATORIAMENTE `docs/ai/03_current_task.md` para entender el contexto inmediato.
- Sé conciso en las explicaciones y céntrate en la implementación técnica.
"""

    # 2. Resumen del Proyecto
    overview = f"""
# Resumen del Proyecto: {nombre_proyecto}

## Propósito
Sistema de digitalización y automatización modular.

## Componentes Principales
- Módulo de Inventario.
- Módulo CRM / Gestión de Clientes.
- [Añadir otros módulos específicos aquí]
"""

    # 3. Arquitectura
    arquitectura = """
# Arquitectura y Stack Tecnológico

## Backend
- **Framework:** FastAPI
- **Lenguaje:** Python 3.11+
- **Base de Datos:** PostgreSQL (mediante SQLAlchemy / SQLModel)

## Infraestructura y Despliegue
- **Contenedores:** Docker y Docker Compose para entorno local y producción.
- **Red y Acceso:** Tailscale para acceso remoto a servidores (Mini PCs).
- **Control de Versiones:** Repositorio Git privado.
"""

    # 4. Estado Dinámico (El archivo más crítico para la eficiencia)
    tarea_actual = """
# Tarea Actual y Estado

**Estado Actual (Última actualización: Inicialización):**
- Proyecto recién inicializado. Estructura base generada.

**Objetivo de la Sesión Actual:**
- Definir modelos de base de datos base y configurar el contenedor de Docker.

**Problemas o Bugs Abiertos:**
- Ninguno por ahora.

*(Nota para la IA: Actualiza este archivo al finalizar cambios importantes para mantener el estado guardado para la siguiente interacción).*
"""

    # Generación de la estructura
    crear_archivo(base_dir / ".cursorrules", reglas)
    crear_archivo(base_dir / "docs/ai/01_overview.md", overview)
    crear_archivo(base_dir / "docs/ai/02_architecture.md", arquitectura)
    crear_archivo(base_dir / "docs/ai/03_current_task.md", tarea_actual)
    crear_archivo(base_dir / "README.md", f"# {nombre_proyecto}\n\nPara el contexto técnico de desarrollo, revisa la carpeta `docs/ai/`.")
    
    print(f"✅ Proyecto '{nombre_proyecto}' inicializado correctamente.")
    print("🧠 Contexto modular para la IA creado en 'docs/ai/'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Inicializa la estructura de un nuevo proyecto con contexto para IA.")
    parser.add_argument("nombre", help="Nombre del nuevo proyecto")
    args = parser.parse_args()
    init_ai_project(args.nombre)
