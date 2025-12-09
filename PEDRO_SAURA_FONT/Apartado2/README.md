# Apartado 2 – Script Bash Multiplataforma para Información del Sistema

## 📌 Descripción General

En este apartado se desarrolla un script en **Bash** capaz de obtener y mostrar, en un único mensaje, información esencial del equipo donde se ejecuta.  
El objetivo es demostrar conocimientos relacionados con la administración y puesta en producción segura, detectando el sistema operativo y extrayendo datos relevantes del entorno.

Este script es **multiplataforma**, funcionando correctamente en:

- **macOS**
- **Linux** (Ubuntu u otras distribuciones)
- **Windows 10/11** mediante **Git Bash** o **MSYS2**

---

## 📁 Estructura del Apartado

```
PEDRO_SAURA_FONT/
  Apartado2/
    info_equipo.sh
    README.md
```

---

## ▶️ ¿Qué información obtiene el script?

El script identifica automáticamente el entorno y muestra:

- **Familia del sistema operativo** (macOS, Linux, Windows/MSYS)
- **Detalle completo del sistema operativo**  
  - macOS → `sw_vers`  
  - Linux → `lsb_release` o `/etc/os-release`  
  - Windows → `wmic os get Caption,Version`
- **Dirección MAC** del equipo  
  - `ifconfig` / `ip` / `getmac`
- **Nombre del equipo** (`hostname`)
- **Usuario actual** (`whoami`)

Toda la información aparece en un **único mensaje**, cumpliendo con lo solicitado en el enunciado de la práctica.

---

## ▶️ Ejecución del script

### 1️⃣ Dar permisos de ejecución

Desde el directorio del apartado:

```bash
chmod +x info_equipo.sh
```

### 2️⃣ Ejecutarlo

```bash
./info_equipo.sh
```

---

## 📌 Ejemplo de salida real (macOS)

```
------------------------------------
Familia de SO: macOS

Detalle de SO:
ProductName:    macOS
ProductVersion: 15.6
BuildVersion:   24G84

MAC: e2:32:13:b1:fe:7c
Nombre del equipo: MacBook-Pro-de-Pedro.local
Usuario actual: pedrosaura
------------------------------------
```

Esta información demuestra claramente que el script ha sido ejecutado por el alumno en su propio equipo.

---

## 🧪 Ejecución en Linux (Ubuntu)

En una máquina virtual, ejecutar:

```bash
./info_equipo.sh
```

La salida mostrará algo como:

```
Familia de SO: Linux

Detalle de SO:
Ubuntu 22.04.4 LTS

MAC: 08:00:27:1c:aa:bb
Nombre del equipo: ubuntu-vm
Usuario actual: usuario
```

---

## 🪟 Ejecución en Windows (Git Bash)

Abrir **Git Bash**, situarse en el directorio del proyecto y ejecutar:

```bash
./info_equipo.sh
```

Salida típica:

```
Familia de SO: Windows (Git Bash / MSYS)

Detalle de SO:
Caption=Microsoft Windows 11 Pro
Version=10.0.22631

MAC: 3C-52-82-91-FA-10
Nombre del equipo: DESKTOP-12345
Usuario actual: pedro
```

---

## 🔒 Relación con la Ciberseguridad (RA1)

Este script demuestra conocimientos aplicados en el ámbito de la seguridad y la puesta en producción:

- Identificación automática del entorno del sistema.
- Uso de herramientas de administración en distintos sistemas operativos.
- Extracción de datos relevantes para auditoría y diagnóstico.
- Portabilidad y compatibilidad multiplataforma.
- Estructura clara y mantenible del código.

---

## ✔️ Conclusión

El script desarrollado cumple con todos los requisitos del apartado:

- Es **multiplataforma**  
- Muestra toda la información requerida  
- Proporciona un mensaje único y claro  
- Demuestra un conocimiento sólido del entorno del sistema y la ejecución segura de scripts  
- Facilita capturas y documentación para la memoria del RA1

