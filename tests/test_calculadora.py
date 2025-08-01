import unittest
from src.calculadora import soma

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(1, 2), 3)

    def test_soma_varias_entradas(self):
      x_y_saidas = (( 1, 2, 3),
                    (0, 0, 0),
                    (-1, 1, 0),
                    (2.5, 2.5, 5.0),
    )

      for x, y, saida in x_y_saidas:
          self.assertEqual(soma(x, y), saida)

unittest.main(verbosity=2)