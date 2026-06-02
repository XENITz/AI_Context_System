import os
import argparse
from datetime import datetime
from pathlib import Path

def crear_archivo(ruta: Path, contenido: str):
    ruta.parent.mkdir(parents=True, exist_ok=True)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido.strip() + "\n")

def init_ai_universal_project(nombre: str, size: str):
    print(f"\n🚀 Iniciando configuración de IA para: {nombre}")
    print("Responde las siguientes preguntas (o presiona Enter para dejar en blanco)\n" + "-"*50)
    
    # --- PROMPTS INTERACTIVOS ---
    proposito = input("📝 ¿Cuál es el propósito del proyecto?: ") or "[Por definir]"
    audiencia = input("👥 ¿Quién es la audiencia/usuarios?: ") or "[Por definir]"
    frontend = input("🎨 Frontend / Interfaz (ej. React, CLI, Ninguno): ") or "No aplica"
    backend = input("⚙️  Backend (ej. Python/FastAPI): ") or "[Por definir]"
    db = input("🗄️  Base de Datos (ej. PostgreSQL): ") or "[Por definir]"
    infra = input("☁️  Infraestructura (ej. Docker, Vercel): ") or "[Por definir]"
    tarea_actual_input = input("🎯 ¿Cuál es la primera tarea de hoy?: ") or "Configurar el entorno base del proyecto"
    
    print("-" * 50)
    print("⏳ Generando tu Second Brain...\n")

    base_dir = Path(nombre)
    base_dir.mkdir(exist_ok=True)
    docs_dir = base_dir / "docs/ai"
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    fecha_actual = datetime.now().strftime("%Y-%m-%d")

    # 1. Reglas Globales
    reglas = """
# Reglas Globales de IA
1. LECTURA OBLIGATORIA: Lee `docs/ai/03_current_task.md` antes de sugerir código.
2. CERO EXPLICACIONES OBVIAS: Escribe código directamente.
3. MODULARIDAD: Si un archivo se vuelve demasiado grande, sugiere refactorizarlo.
4. LIMITACIÓN DE CONTEXTO: Si te falta información, detente y pídeme que te etiquete (@) el archivo.
"""

    # 0. MOC
    hub = f"""---
aliases: [Hub {nombre}]
tags: [project/hub, ai-context]
created: {fecha_actual}
status: active
---
# 🧠 Hub del Proyecto: {nombre}

Bienvenido al centro de control del proyecto. 

## 🧭 Navegación Principal
- **¿Qué es esto?** ➔ [[01_overview]]
- **¿Cómo está construido?** ➔ [[02_architecture]]
- **¿En qué estamos trabajando hoy?** ➔ [[03_current_task]]
"""

    # 2. Resumen (Ahora usa tus respuestas)
    overview = f"""---
aliases: [Overview {nombre}]
tags: [project/overview]
created: {fecha_actual}
---
# 01 - Overview del Proyecto: {nombre}

🔙 Volver al Hub: [[00_Project_Hub]]

**Propósito:** {proposito}
**Audiencia/Usuarios:** {audiencia}
**Estado:** Inicialización
"""

    # 3. Arquitectura (Ahora usa tus respuestas)
    arquitectura = f"""---
aliases: [Architecture {nombre}]
tags: [project/architecture]
created: {fecha_actual}
---
# 02 - Arquitectura y Stack

🔙 Volver al Hub: [[00_Project_Hub]]

**Frontend / Interfaz:** {frontend}
**Backend / Lógica Core:** {backend}
**Base de Datos / Almacenamiento:** {db}
**Infraestructura / Despliegue:** {infra}

## Reglas de Código Específicas
- [Añade aquí reglas exclusivas de este stack. Ej. "Usar Type Hints"]

## Conexiones
- Las tareas actuales están en [[03_current_task]].
"""

    # 4. Tarea Actual (Ahora usa tu respuesta)
    tarea_actual = f"""---
aliases: [Current Task {nombre}]
tags: [project/task-state]
last_updated: {fecha_actual}
---
# 03 - Tarea Actual (Punto de Guardado)

🔙 Volver al Hub: [[00_Project_Hub]]
⚙️ Basado en la arquitectura: [[02_architecture]]

**Objetivo Inmediato:**
- {tarea_actual_input}

**Contexto de Archivos (Tracked):**
- [Ninguno aún]

**Bugs/Problemas Actuales:**
- Ninguno.

*(Nota para la IA: Actualiza este archivo preservando el bloque YAML superior).*
"""

    # 5. README Simplificado (Ya no necesita el paso cero manual)
    readme_ai = f"""
# Sistema de Contexto IA para {nombre}

Este proyecto utiliza un sistema de contexto aislado para integrarse con MCP y tu Second Brain.

## 🔄 El Flujo de Trabajo

### 1. El Hábito de Inicio
Abre tu cliente IA (Roo Code / Aider) y envía:
> "Usa tu herramienta para leer `docs/ai/00_Project_Hub.md` y ejecuta el objetivo actual."

### 2. Aislamiento de Contexto
No dejes que la IA intente adivinar qué archivos editar. Guíala si es necesario, pero deja que el MCP lea los directorios.

### 3. El Hábito de Cierre (Punto de Guardado)
Antes de cerrar VS Code, dile a la IA:
> "Actualiza `docs/ai/03_current_task.md`. En 'Objetivo Inmediato' anota lo que haremos mañana."
"""

    crear_archivo(base_dir / ".cursorrules", reglas)
    crear_archivo(docs_dir / "00_Project_Hub.md", hub)
    crear_archivo(docs_dir / "01_overview.md", overview)
    crear_archivo(docs_dir / "02_architecture.md", arquitectura)
    crear_archivo(docs_dir / "03_current_task.md", tarea_actual)
    crear_archivo(base_dir / "README_AI_WORKFLOW.md", readme_ai)

    if size == "large":
        roadmap = f"""---
aliases: [Roadmap {nombre}]
tags: [project/roadmap]
created: {fecha_actual}
---
# 04 - Roadmap y Componentes Mayores

🔙 Volver al Hub: [[00_Project_Hub]]

## Fases del Proyecto
- [ ] Fase 1: {tarea_actual_input}
- [ ] Fase 2: Siguiente módulo
- [ ] Fase 3: Despliegue
"""
        crear_archivo(docs_dir / "04_roadmap.md", roadmap)

    print(f"✅ ¡Listo! Proyecto '{nombre}' inicializado con tu configuración específica.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera estructura universal de contexto IA")
    parser.add_argument("nombre", help="Nombre del proyecto")
    parser.add_argument("--size", choices=["mid", "large"], default="mid", help="Tamaño del proyecto")
    args = parser.parse_args()
    init_ai_universal_project(args.nombre, args.size)