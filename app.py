def calcular_imc(peso, altura):
    """Calcula o IMC a partir do peso (kg) e altura (m)."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC de acordo com os padrões da OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"  # Inclui 18.5 até 24.9
    elif 25 <= imc < 30:
        return "Sobrepeso"    # Inclui 25 até 29.9
    else:
        return "Obesidade"    # 30 ou mais


def main():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"Seu IMC é: {imc:.2f} - {classificacao}")

if __name__ == "__main__":
    main()