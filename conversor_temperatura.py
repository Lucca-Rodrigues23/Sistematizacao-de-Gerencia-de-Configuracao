"""
Conversor de Temperatura
------------------------
Converte Celsius para Fahrenheit e Fahrenheit para Celsius.
"""


def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def menu():
    print("\nEscolha a conversão desejada:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Sair")
    return input("Opção: ").strip()


def main():
    print("=== Conversor de Temperatura ===")

    try:
        while True:
            opcao = menu()

            if opcao == "3":
                print("Encerrando o conversor. Até mais!")
                break

            if opcao not in ("1", "2"):
                print("Opção inválida. Escolha 1, 2 ou 3.")
                continue

            entrada = input("Digite a temperatura (ou 'sair' para voltar ao menu): ")

            if entrada.strip().lower() == "sair":
                print("Voltando ao menu principal...")
                continue

            try:
                valor = float(entrada)
            except ValueError:
                print("Valor inválido. Digite um número (ex: 25.5).")
                continue

            if opcao == "1":
                resultado = celsius_para_fahrenheit(valor)
                print(f"{valor}°C equivalem a {resultado:.2f}°F")
            else:
                resultado = fahrenheit_para_celsius(valor)
                print(f"{valor}°F equivalem a {resultado:.2f}°C")

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Até mais!")


if __name__ == "__main__":
    main()
