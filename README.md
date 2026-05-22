# Urban Routes QA Automation Project

## Descripción

Este proyecto automatiza pruebas funcionales de la plataforma **Urban Routes** utilizando **Python, Selenium y Pytest**, aplicando el patrón **Page Object Model (POM)**.

El objetivo es validar de forma independiente los principales escenarios del flujo de solicitud de taxi, garantizando estabilidad, mantenibilidad y reutilización del código.

---

## Tecnologías utilizadas

- Python 3.14
- Selenium WebDriver
- Pytest
- ChromeDriver
- Page Object Model (POM)

---

## Técnicas implementadas

- Automatización funcional de interfaz web
- Page Object Model
- Esperas explícitas
- Assertions reales
- Pruebas independientes
- Uso de múltiples localizadores:
  - ID
  - XPATH
  - CLASS_NAME
  - CSS_SELECTOR

---

## Estructura del proyecto

```text
qa-project-Urban-Routes-es/
│
├── conftest.py
├── data.py
├── helpers.py
├── pages.py
├── test_urban_routes.py
├── README.md
└── .venv/
```

---

## Escenarios automatizados

### 1. Configuración de ruta
Valida el ingreso correcto de origen y destino.

### 2. Selección de tarifa Comfort
Verifica la selección correcta de la tarifa Comfort.

### 3. Registro de número telefónico
Valida el ingreso y confirmación del número telefónico.

### 4. Agregar método de pago
Verifica el registro correcto de tarjeta bancaria.

### 5. Confirmación de código
Valida la confirmación del código recibido.

### 6. Envío de mensaje al conductor
Comprueba que el mensaje se envíe correctamente.

### 7. Solicitud de manta y pañuelos
Verifica la activación del servicio adicional.

### 8. Pedido de dos helados
Valida el incremento correcto del contador.

### 9. Búsqueda y asignación de conductor
Verifica la aparición del modal de búsqueda y la asignación del conductor.

---

## Instalación

### Crear entorno virtual

```bash
python -m venv .venv
```

### Activar entorno virtual (Windows)

```bash
.venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install selenium pytest
```

---

## Ejecución de pruebas

### Ejecutar todas las pruebas

```bash
pytest test_urban_routes.py -v
```

### Ejecutar una prueba específica

```bash
pytest test_urban_routes.py::TestUrbanRoutes::test_add_card -v
```

### Ejecutar prueba de búsqueda de taxi

```bash
pytest test_urban_routes.py::TestUrbanRoutes::test_search_taxi_modal -v -s
```

---

## Resultados esperados

Todas las pruebas deben ejecutarse de forma independiente y finalizar exitosamente:

```text
9 passed
```

---

## Autor

**Dairon Manzo**

Proyecto desarrollado como parte del **Sprint 9 de QA Automation en TripleTen**.