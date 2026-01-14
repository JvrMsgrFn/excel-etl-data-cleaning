# Excel ETL Data Cleaning Pipeline

Proyecto personal que implementa un pipeline ETL en Python orientado a la limpieza, validación y depuración progresiva de datos estructurados en archivos Excel, con el objetivo de generar una tabla paramétrica lista para su consumo en Power BI.

El proyecto simula un escenario habitual en entornos corporativos: el uso de ficheros de control con errores, duplicados y registros incompletos como base para construir una tabla paramétrica fiable dentro de un desarrollo evolutivo de reporting.

## Objetivo

Diseñar un proceso automatizado que permita transformar un Excel de control en una tabla paramétrica utilizable en un informe de Power BI, garantizando calidad del dato, trazabilidad y mantenibilidad.

Para ello, el pipeline:

- Utiliza el Excel de control original como capa **raw**
- Automatiza la limpieza y normalización de los datos
- Separa explícitamente los registros válidos de los inválidos
- Conserva los registros erróneos para su revisión y corrección

## Beneficios del enfoque

- Corrección progresiva del origen de datos
- Mejora continua de la calidad del Excel de control
- Pipeline extensible y mantenible
- Base sólida para desarrollos analíticos y de reporting

## Características principales

- Pipeline ETL desarrollado en Python
- Separación clara de capas: **raw / dirty / clean**
- Reglas de validación desacopladas y fácilmente ampliables
- Los datos inválidos no se eliminan, se aíslan para análisis
- Estructura modular orientada a escalabilidad

## Estructura de proyecto

```
data/
├── raw/
├── dirty/
└── clean/

src/
├── main.py
├── cleaning/
│   ├── __init__.py
│   └── cleaning_functions.py
├── rules/
│   ├── __init__.py
│   └── validation_rules.py
└── utils/
    ├── __init__.py
    └── excel_io.py
```

## Funcionamiento general

El script `main.py` actúa como orquestador del pipeline, ejecutando de forma secuencial las fases de carga, limpieza, validación y generación de salidas.

## Notas

Este proyecto no contiene datos reales ni información sensible. Los ficheros de entrada y la lógica de negocio se incluyen únicamente con fines demostrativos.
