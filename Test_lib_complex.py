import unittest
import complex_lib
import math


class TestLibComplex(unittest.TestCase):
    n1, n2= ((-3,2),(5,-8))
    n3, n4 = ((2.5,-9), (4,1))
    n5, n6 = ((5.25, 8), (6.8,2))

    def test_sumcomplex(self):
        pruba_1 = complex_lib.sum_complex(self.n1, self.n2)
        self.assertAlmostEqual(pruba_1[0], 2)
        self.assertAlmostEqual(pruba_1[1],-6)
        pruba_2 = complex_lib.sum_complex(self.n3, self.n4)
        self.assertAlmostEqual(pruba_2[0], 6.5)
        self.assertAlmostEqual(pruba_2[1],-8)
        pruba_3 = complex_lib.sum_complex(self.n5, self.n6)
        self.assertAlmostEqual(pruba_3[0], 12.05)
        self.assertAlmostEqual(pruba_3[1],10)

    def test_multcomplex(self):
        pruba_1 = complex_lib.mult_complex(self.n1, self.n2)
        self.assertAlmostEqual(pruba_1[0], 1)
        self.assertAlmostEqual(pruba_1[1],34)
        pruba_2 = complex_lib.mult_complex(self.n3, self.n4)
        self.assertAlmostEqual(pruba_2[0], 19)
        self.assertAlmostEqual(pruba_2[1],-33.5)
        pruba_3 = complex_lib.mult_complex(self.n5, self.n6)
        self.assertAlmostEqual(pruba_3[0], 19.7)
        self.assertAlmostEqual(pruba_3[1],64.9)

    def test_rescomplex(self):
        pruba_1 = complex_lib.res_complex(self.n1, self.n2)
        self.assertAlmostEqual(pruba_1[0], -8)
        self.assertAlmostEqual(pruba_1[1],10)
        pruba_2 = complex_lib.res_complex(self.n3, self.n4)
        self.assertAlmostEqual(pruba_2[0], -1.5)
        self.assertAlmostEqual(pruba_2[1],-10)
        pruba_3 = complex_lib.res_complex(self.n5, self.n6)
        self.assertAlmostEqual(pruba_3[0], -1.55)
        self.assertAlmostEqual(pruba_3[1],6)


    def test_divcomplex(self):
        pruba_1 = complex_lib.div_complex(self.n1, self.n2)
        self.assertAlmostEqual(pruba_1[0], -0.3483146067)
        self.assertAlmostEqual(pruba_1[1],-0.1573033708)
        pruba_2 = complex_lib.div_complex(self.n3, self.n4)
        self.assertAlmostEqual(pruba_2[0], 0.05882352941)
        self.assertAlmostEqual(pruba_2[1],-2.264705882)
        pruba_3 = complex_lib.div_complex(self.n5, self.n6)
        self.assertAlmostEqual(pruba_3[0], 1.02906051)
        self.assertAlmostEqual(pruba_3[1],0.8738057325)


    def test_modulo(self):
        self.assertAlmostEqual(complex_lib.modu_complex(self.n1), (3.605551275))
        self.assertAlmostEqual(complex_lib.modu_complex(self.n3), (9.340770846))
        self.assertAlmostEqual(complex_lib.modu_complex(self.n5), (9.568829605))

    def test_conju(self):
        pruba_1 = complex_lib.conju_complex(self.n1)
        self.assertAlmostEqual(pruba_1[0], -3)
        self.assertAlmostEqual(pruba_1[1],-2)
        pruba_2 = complex_lib.conju_complex(self.n3)
        self.assertAlmostEqual(pruba_2[0], 2.5)
        self.assertAlmostEqual(pruba_2[1], 9)
        pruba_3 = complex_lib.conju_complex(self.n5)
        self.assertAlmostEqual(pruba_3[0], 5.25)
        self.assertAlmostEqual(pruba_3[1],-8)



    def test_CartToPolar(self):
        pruba_1 = complex_lib.cart_to_polar(self.n1)
        self.assertAlmostEqual(pruba_1[0], 3.605551275)
        self.assertAlmostEqual(pruba_1[1], 2.55359005)
        pruba_2 = complex_lib.cart_to_polar(self.n3)
        self.assertAlmostEqual(pruba_2[0], 9.340770846)
        self.assertAlmostEqual(pruba_2[1], -1.299849476)
        pruba_3 = complex_lib.cart_to_polar(self.n5)
        self.assertAlmostEqual(pruba_3[0], 9.568829605)
        self.assertAlmostEqual(pruba_3[1], 0.9900399732)


    n7 = (8, math.pi/2)
    n8 = (-2, -math.pi/11)
    n9 = (5, -math.pi/6)
    def test_PolarToCart(self):
        pruba_1 = complex_lib.polar_to_cart(self.n7)
        self.assertAlmostEqual(pruba_1[0], 0)
        self.assertAlmostEqual(pruba_1[1], 8)
        pruba_2 = complex_lib.polar_to_cart(self.n8)
        self.assertAlmostEqual(pruba_2[0], -1.918985947)
        self.assertAlmostEqual(pruba_2[1], 0.5634651137)
        pruba_3 = complex_lib.polar_to_cart(self.n9)
        self.assertAlmostEqual(pruba_3[0], 4.330127019)
        self.assertAlmostEqual(pruba_3[1], -2.5)


    def test_fase(self):
        self.assertAlmostEqual(complex_lib.fase_complex(self.n1), 2.55359005)
        self.assertAlmostEqual(complex_lib.fase_complex(self.n3), -1.299849476)
        self.assertAlmostEqual(complex_lib.fase_complex(self.n5), 0.9900399732)

if __name__ == '__main__':
    unittest.main()