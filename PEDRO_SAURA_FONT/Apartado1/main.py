import argparse
from password_security import analyze_password, generate_password


def main():
    parser = argparse.ArgumentParser(
        description="Analizador y generador de contraseñas seguras (RA1 – Ciberseguridad)"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Subcomando: analizar contraseña
    analyze_parser = subparsers.add_parser("analizar", help="Analiza la seguridad de una contraseña")
    analyze_parser.add_argument("password", help="Contraseña a analizar")

    # Subcomando: generar contraseña
    gen_parser = subparsers.add_parser("generar", help="Genera una contraseña segura")
    gen_parser.add_argument("-l", "--length", type=int, default=16, help="Longitud de la contraseña (por defecto 16)")
    gen_parser.add_argument("--no-lower", action="store_true", help="No usar minúsculas")
    gen_parser.add_argument("--no-upper", action="store_true", help="No usar mayúsculas")
    gen_parser.add_argument("--no-digits", action="store_true", help="No usar dígitos")
    gen_parser.add_argument("--no-symbols", action="store_true", help="No usar símbolos")

    args = parser.parse_args()

    if args.command == "analizar":
        analysis = analyze_password(args.password)
        print("Análisis de contraseña")
        print("----------------------")
        print(f"Longitud: {analysis.length}")
        print(f"Tamaño del conjunto de caracteres: {analysis.charset_size}")
        print(f"Entropía aproximada: {analysis.entropy_bits:.2f} bits")
        print(f"Clasificación: {analysis.classification}")

    elif args.command == "generar":
        password = generate_password(
            length=args.length,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols,
        )
        print("Contraseña generada:")
        print(password)


if __name__ == "__main__":
    main()
