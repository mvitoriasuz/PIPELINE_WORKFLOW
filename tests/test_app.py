from app import calcular_imc, classificar_imc
import pytest

def test_calcular_imc():
    assert calcular_imc(70, 1.75) == pytest.approx(22.86, rel=1e-2)  # Compara com tolerância
    assert calcular_imc(60, 1.60) == pytest.approx(23.44, rel=1e-2)
    assert calcular_imc(90, 1.80) == pytest.approx(27.78, rel=1e-2)

def test_classificar_imc():
    assert classificar_imc(22.86) == "Peso normal"
    assert classificar_imc(17.0) == "Abaixo do peso"
    assert classificar_imc(26.0) == "Sobrepeso"
    assert classificar_imc(30.0) == "Obesidade"
    assert classificar_imc(18.5) == "Peso normal"  # Limite inferior
    assert classificar_imc(25.0) == "Sobrepeso"     # Correto, 25.0 deve ser "Sobrepeso"

