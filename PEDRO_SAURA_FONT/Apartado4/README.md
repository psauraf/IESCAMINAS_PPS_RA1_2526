# Apartado 4 – Tutorial de Solidity y Smart Contract con Merkle Trees

## 📌 Descripción del apartado

Este apartado contiene:

1. Un pantallazo del progreso obtenido en el tutorial **“Solidity: Beginner to Intermediate Smart Contracts”** realizado en la práctica ACT_RA1_4.
2. La implementación de un **Smart Contract privado** desarrollado por el alumno.
3. La creación del **inicio de una cadena basada en Merkle Trees**, fundamental en sistemas blockchain para garantizar integridad y trazabilidad.

---

## 🖼️ Captura del tutorial de Solidity

La siguiente imagen demuestra que el tutorial fue completado por el alumno:

📷 `imagenes/solidity_tutorial.png`

---

## 🔐 Smart Contract Privado con Merkle Trees

El archivo `SmartMerkle.sol` contiene un contrato inteligente escrito en Solidity que cumple los requisitos solicitados:

### ✔ Privado  
Solo el propietario del contrato puede actualizar el Merkle Root.

### ✔ Inicio de una cadena  
Se define un **Merkle Root inicial**, que representa el nodo raíz del árbol de Merkle.

### ✔ Funciones criptográficas reales  
Se implementa la función `hashNodes()` que combina dos hashes hijos para formar nodos superiores del árbol.

### ✔ Actualización segura  
El owner puede modificar el Merkle Root de forma controlada, lo cual simula la evolución del árbol en un sistema real.

El contrato está documentado para facilitar su comprensión y su relación con el RA1.

---

## 🧠 ¿Qué es un Merkle Tree y por qué es relevante?

Un **árbol de Merkle** es una estructura criptográfica usada en:

- Blockchain (Bitcoin, Ethereum…)
- Sistemas de auditoría
- Control de integridad
- Redes distribuidas

Permite verificar grandes cantidades de datos comprobando únicamente un hash raíz (Merkle Root), lo que reduce costes y mejora la seguridad.

---

## 🎯 Relación con el RA1 de Puesta en Producción Segura

Este apartado cumple el objetivo del RA1 ya que:

- Aplica criptografía real (hashing, keccak256).
- Integra conceptos de integridad y verificación.
- Implementa buenas prácticas de seguridad en contratos inteligentes.
- Documenta correctamente el funcionamiento del sistema.

---

## ✅ Conclusión del Apartado 4

Se demuestra el dominio de conceptos clave de Solidity, estructuras criptográficas y control de acceso seguro mediante:

- Un smart contract privado.
- La implementación del inicio de una cadena con Merkle Trees.
- Evidencias gráficas del progreso formativo.

Este apartado completa con éxito los requisitos de la práctica.
