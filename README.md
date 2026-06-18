# Sistema de Gestión de Eventos

Aplicación de consola en Python para administrar eventos, asistentes y estadísticas mediante una arquitectura limpia basada en capas.

## Descripción

Este sistema permite:
- crear, modificar y cancelar eventos
- gestionar asistentes por evento
- consultar estadísticas de eventos abiertos, cerrados, cancelados y total de asistentes
- separar la lógica de negocio en servicios, el acceso a datos en repositorios y la interacción con el usuario en la interfaz de consola

## Características

- Registro y edición de eventos
- Validación de datos de fecha, hora, capacidad y edad mínima
- Control de estado de evento (`Abierto`, `Lleno`, `Cancelado`)
- Registro de asistentes con vinculación a eventos
- Menú de estadísticas con cálculos de indicadores de eventos
- Pruebas unitarias para servicios de negocio

## Arquitectura

El proyecto sigue una organización por capas:

- `Models/`: entidades del dominio (`Evento`, `Asistente`)
- `Repositories/`: almacenamiento en memoria y consultas básicas
- `Services/`: lógica de negocio y reglas de validación
- `ui/`: menús de consola y navegación del usuario
- `tests/`: casos de prueba unitarios para servicios

## Requisitos

- Python 3.10+ (o versión compatible)

## Instalación y ejecución

1. Clonar el repositorio:
   ```bash
   git clone <url_del_repositorio>
   cd Proyecto_LDP135_UES2026
   ```

2. Ejecutar la aplicación:
   ```bash
   python main.py
   ```

## Uso

Al ejecutar `main.py`, se muestra un menú principal desde el que se puede acceder a:
- Gestión de eventos
- Gestión de asistentes
- Menú de estadísticas

Cada opción guía al usuario para ingresar datos y realizar las operaciones correspondientes.

## Pruebas

Ejecutar las pruebas unitarias con:

```bash
python -m unittest discover -s tests
```

## Estructura de archivos

- `main.py`: punto de entrada de la aplicación
- `Models/Evento.py`: definición de la entidad evento
- `Models/Asistente.py`: definición de la entidad asistente
- `Repositories/Evento_repository.py`: almacenamiento y búsqueda de eventos
- `Repositories/Asistente_repository.py`: almacenamiento y búsqueda de asistentes
- `Services/Evento_service.py`: lógica de eventos
- `Services/Asistente_service.py`: lógica de asistentes
- `Services/Estadisticas_Service.py`: cálculos de estadísticas
- `ui/Menu_principal.py`: menú principal de la aplicación
- `ui/Menu_Evento.py`: menú de gestión de eventos
- `ui/Menu_Asistente.py`: menú de gestión de asistentes
- `ui/Menu_Estadisticas.py`: menú de estadísticas

## Integrantes

- Luis Antonio Ruiz Duran RD20014
- Edwin Eduardo Torres Perez TP21002
- William Eduardo Torres Serrano TS25003

