#!/bin/bash

# Detectar familia de sistema operativo usando uname
UNAME_OUT="$(uname -s)"
case "${UNAME_OUT}" in
    Linux*)     OS_FAMILY="Linux";;
    Darwin*)    OS_FAMILY="macOS";;
    MINGW*|MSYS*|CYGWIN*) OS_FAMILY="Windows (Git Bash / MSYS)";;
    *)          OS_FAMILY="Desconocido";;
esac

MAC=""
SO_DETALLE=""

if [ "$OS_FAMILY" = "Linux" ]; then
    # MAC en Linux (primer interfaz con MAC encontrada)
    if command -v ip >/dev/null 2>&1; then
        MAC=$(ip link 2>/dev/null | awk '/link\/ether/ {print $2; exit}')
    elif command -v ifconfig >/dev/null 2>&1; then
        MAC=$(ifconfig 2>/dev/null | awk '/ether/ {print $2; exit}')
    else
        MAC="No se ha podido obtener (sin ip ni ifconfig)"
    fi

    # Información detallada del SO
    if command -v lsb_release >/dev/null 2>&1; then
        SO_DETALLE=$(lsb_release -d | cut -f2)
    elif [ -f /etc/os-release ]; then
        SO_DETALLE=$(grep "^PRETTY_NAME=" /etc/os-release | cut -d= -f2 | tr -d '"')
    else
        SO_DETALLE=$(uname -a)
    fi

elif [ "$OS_FAMILY" = "macOS" ]; then
    # MAC en macOS
    if command -v ifconfig >/dev/null 2>&1; then
        MAC=$(ifconfig 2>/dev/null | awk '/ether/ {print $2; exit}')
    else
        MAC="No se ha podido obtener (sin ifconfig)"
    fi

    # Información detallada de macOS
    if command -v sw_vers >/dev/null 2>&1; then
        SO_DETALLE="$(sw_vers)"
    else
        SO_DETALLE=$(uname -a)
    fi

elif [[ "$OS_FAMILY" == "Windows (Git Bash / MSYS)" ]]; then
    # MAC en Windows usando getmac, si está disponible
    if command -v getmac >/dev/null 2>&1; then
        MAC=$(getmac | awk 'NR==4 {print $1}')
    else
        MAC="No se ha podido obtener con getmac"
    fi

    # Información del sistema operativo Windows usando wmic, si está disponible
    if command -v wmic >/dev/null 2>&1; then
        SO_DETALLE=$(wmic os get Caption,Version /value | sed '/^$/d')
    else
        SO_DETALLE="Windows (detalle no disponible con wmic)"
    fi

else
    MAC="No disponible"
    SO_DETALLE="SO no reconocido: $(uname -a)"
fi

HOST=$(hostname)
USER_ACTUAL=$(whoami)

echo "Información del sistema
------------------------------------
Familia de SO: $OS_FAMILY

Detalle de SO:
$SO_DETALLE

MAC: $MAC
Nombre del equipo: $HOST
Usuario actual: $USER_ACTUAL
------------------------------------"
