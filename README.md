# Urban Routes - Proyecto de Automatización QA

## Descripción del proyecto
Este proyecto automatiza el flujo completo de solicitud de un taxi en la aplicación Urban Routes utilizando Selenium WebDriver y Pytest.

El objetivo es validar que el usuario pueda completar un pedido de taxi desde la selección de ruta hasta la confirmación del conductor.

---

## Tecnologías utilizadas
- Python 3
- Selenium WebDriver
- Pytest
- ChromeDriver
- Page Object Model (POM)

---

## Técnicas utilizadas
- Automatización de pruebas UI
- Localización de elementos (XPath, CSS Selector, ID, Class)
- Esperas explícitas con WebDriverWait
- Manejo de modales y overlays
- Patrones de diseño POM

---

## ▶ Cómo ejecutar las pruebas: pytest main.py -v

### 1. Instalar dependencias
```bash
pip install -r requirements.txt