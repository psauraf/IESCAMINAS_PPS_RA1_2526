# Apartado 1 – Aplicación en Python: Analizador y Generador de Contraseñas Seguras

## 📌 Descripción General

En este apartado se desarrolla una aplicación en Python relacionada con la ciberseguridad que permite:

- **Analizar la fortaleza de una contraseña** mediante el cálculo de su entropía.
- **Generar contraseñas seguras** ajustando longitud y tipos de caracteres.
- **Clasificar** la seguridad de una contraseña en:
  - Muy débil
  - Débil
  - Media
  - Fuerte
  - Muy fuerte

La herramienta utiliza conceptos reales de ciberseguridad y matemáticas aplicadas, ofreciendo un análisis sólido basado en la entropía.  
Incluye además **4 tests unitarios**, cumpliendo con los objetivos del RA1.

---

## 📁 Estructura del Apartado

```
PEDRO_SAURA_FONT/
  Apartado1/
    main.py
    password_security.py
    tests/
      test_password_security.py
    README.md
```

### Archivos principales

- **password_security.py** → Lógica de análisis, cálculo de entropía y generación de contraseñas.  
- **main.py** → Interfaz de línea de comandos (CLI) usando `argparse`.  
- **tests/test_password_security.py** → Contiene 4 tests unitarios que validan el correcto funcionamiento del sistema.

---

## ▶️ Requisitos

- Python 3.9 o superior  
- No requiere librerías externas

---

## ▶️ Uso de la aplicación

Situarse dentro del directorio del apartado:

```bash
cd PEDRO_SAURA_FONT/Apartado1
```

---

## 🔍 1. Analizar una contraseña

```bash
python3 main.py analizar "MiPassw0rd!"
```

Salida de ejemplo:

```
Análisis de contraseña
----------------------
Longitud: 11
Tamaño del conjunto de caracteres: 94
Entropía aproximada: 72.10 bits
Clasificación: Fuerte
```

---

## 🔐 2. Generar una contraseña segura

Generar contraseña estándar de 16 caracteres:

```bash
python3 main.py generar
```

Generar una contraseña de 20 caracteres:

```bash
python3 main.py generar -l 20
```

Generar una contraseña sin símbolos:

```bash
python3 main.py generar --no-symbols
```

Ejemplo real:

```
Contraseña generada:
.!5KkLZ:v|GSC+lMN&V2
```

---

## 🧪 Tests Unitarios

Ejecutar los tests:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

Salida esperada:

```
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

### Los tests validan:

- El cálculo del tamaño del conjunto de caracteres.  
- Que la entropía aumenta con la longitud.  
- Diferenciación entre contraseñas débiles y fuertes.  
- Que la contraseña generada cumple la longitud solicitada.

---

## 🔒 Relación con la Ciberseguridad (RA1)

Este apartado demuestra conocimientos esenciales del RA1:

- Cálculo de **entropía**, métrica real usada para evaluar contraseñas.  
- Generación de credenciales seguras.  
- Desarrollo seguro mediante **tests unitarios**.  
- Modularidad y buenas prácticas en Python.  
- Interacción mediante CLI para un uso profesional.

---

## ✔️ Conclusión

Este apartado integra ciberseguridad, programación y pruebas unitarias en una herramienta funcional que permite analizar y generar contraseñas seguras. El resultado es una solución sólida, clara y totalmente funcional, adecuada para su aplicación en contextos reales de seguridad informática.
