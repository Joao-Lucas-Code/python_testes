def soma(a, b):
    """
    Função que soma dois números.
    >>> soma(5, 3)
    8
    """
    assert isinstance(a, (int, float)), "O primeiro argumento deve ser um número"
    assert isinstance(b, (int, float)), "O segundo argumento deve ser um número"
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    print("Todos os testes passaram!")