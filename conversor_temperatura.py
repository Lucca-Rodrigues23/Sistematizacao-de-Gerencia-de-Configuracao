"""
Conversor de Temperatura
------------------------
Versão inicial: converte Celsius para Fahrenheit.
"""


def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def main():
    print("=== Conversor de Temperatura (Celsius -> Fahrenheit) ===")

    while True:
        entrada = input("\nDigite a temperatura em Celsius (ou 'sair' para encerrar): ")

        if entrada.strip().lower() == "sair":
            print("Encerrando o conversor. Até mais!")
            break

        try:
            celsius = float(entrada)
        except ValueError:
            print("Valor inválido. Digite um número (ex: 25.5) ou 'sair'.")
            continue

        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F")


if __name__ == "__main__":
    main()
