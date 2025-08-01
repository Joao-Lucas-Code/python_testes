def soma(a, b):
    assert isinstance(a, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(b, (int, float)), "O segundo argumento deve ser um número"
    return a + b