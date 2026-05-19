# Urban Routes QA Automation Project

## Descripción

Este proyecto automatiza pruebas funcionales de la plataforma **Urban Routes** utilizando **Python, Selenium y Pytest**, aplicando el patrón **Page Object Model (POM)**.

El objetivo es validar de forma independiente los principales escenarios del flujo de solicitud de taxi.

---

## Tecnologías utilizadas

* Python 3.14
* Selenium WebDriver
* Pytest
* ChromeDriver
* Page Object Model (POM)

---

## Estructura del proyecto

```text
qa-project-Urban-Routes-es/
│
├── conftest.py
├── data.py
├── helpers.py
├── pages.py
│
├── tests/
│   ├── test_add_card.py
│   ├── test_add_phone.py
│   ├── test_confirm_code.py
│   ├── test_order_ice_cream.py
│   ├── test_request_blanket.py
│   ├── test_search_taxi.py
│   ├── test_select_comfort.py
│   ├── test_send_message.py
│   └── test_set_route.py
```

---

## Escenarios automatizados

### 1. Configuración de ruta

Valida que el usuario pueda ingresar dirección de origen y destino.

### 2. Selección de tarifa Comfort

Verifica la selección correcta de la tarifa Comfort.

### 3. Registro de número telefónico

Valida el ingreso y confirmación del teléfono.

### 4. Agregar método de pago

Verifica el registro exitoso de tarjeta bancaria.

### 5. Confirmación de código

Valida confirmación correcta del código recibido.

### 6. Envío de mensaje al conductor

Comprueba que el mensaje sea enviado correctamente.

### 7. Solicitud de manta y pañuelos

Verifica activación del servicio adicional.

### 8. Pedido de dos helados

Valida incremento correcto del contador.

### 9. Búsqueda y asignación de conductor

Verifica aparición del modal y asignación del conductor.

---

## Instalación

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual (Windows):

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install selenium pytest
```

---

## Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
pytest tests -v
```

Ejecutar una prueba específica:

```bash
pytest tests/test_add_phone.py -v
```

Ejecutar una función específica:

```bash
pytest tests/test_search_taxi.py::test_search_taxi -v
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

Proyecto desarrollado como parte del Sprint 9 de QA Automation en TripleTen.
