# Urban Routes - Proyecto de Automatización QA

## Descripción del proyecto

Este proyecto automatiza pruebas funcionales de la aplicación **Urban Routes** utilizando **Selenium WebDriver** y **Pytest**.

El objetivo es validar el flujo principal de solicitud de taxi aplicando el patrón **Page Object Model (POM)** y ejecutando pruebas desacopladas e independientes para cada funcionalidad del sistema.

---

## Tecnologías utilizadas

- Python 3
- Selenium WebDriver
- Pytest
- ChromeDriver
- Page Object Model (POM)

---

## Estructura del proyecto

```bash
qa-project-Urban-Routes-es/

│── data.py
│── helpers.py
│── pages.py
│── README.md
│── __init__.py

└── tests/
    │── __init__.py
    │── test_urban_routes.py
```

---

## Escenarios automatizados

El proyecto contiene **9 pruebas independientes**:

- Configuración de dirección inicial
- Selección de tarifa Comfort
- Ingreso de número telefónico
- Agregado de tarjeta bancaria
- Confirmación de código
- Envío de mensaje al conductor
- Solicitud de manta y pañuelos
- Pedido de 2 helados
- Validación del modal de búsqueda de taxi

---

## Técnicas implementadas

- Automatización UI
- Localización de elementos:
  - XPath
  - CSS Selector
  - ID
  - Class Name
- Esperas explícitas (`WebDriverWait`)
- Manejo de overlays y modales
- Captura automática de código telefónico desde logs de red
- Patrón Page Object Model (POM)
- Pruebas desacopladas y reutilizables

---

## Instalación de dependencias

Instalar:

```bash
pip install selenium pytest
```

---

## Ejecutar todas las pruebas

```bash
python -m pytest tests/test_urban_routes.py -v
```

---

## Ejecutar una prueba específica

### Agregar tarjeta

```bash
python -m pytest tests/test_urban_routes.py::TestUrbanRoutes::test_add_card -v
```

### Seleccionar Comfort

```bash
python -m pytest tests/test_urban_routes.py::TestUrbanRoutes::test_select_comfort -v
```

### Validar modal final

```bash
python -m pytest tests/test_urban_routes.py::TestUrbanRoutes::test_search_taxi_modal -v
```

---

## Patrón de diseño aplicado

**Page Object Model (POM)**

Separación de responsabilidades:

- **data.py** → datos de prueba
- **helpers.py** → utilidades auxiliares
- **pages.py** → localizadores y acciones
- **tests/** → casos de prueba

---

## Resultado esperado

Ejecución exitosa:

```bash
============================= test session starts =============================
collected 9 items

9 passed
```

---

## Autor

Proyecto desarrollado como parte del Sprint de Automatización QA en TripleTen.