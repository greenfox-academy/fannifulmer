import unittest
import extend

class TestExtend(unittest.TestCase):
    def setUp(self):
        pass

    def test_add_2_and_3_is_5(self):
        self.assertEqual(extend.add(2, 3), 5)

    def test_add_4_and_1_is_5(self):
        self.assertEqual(extend.add(4, 1), 5)

    def test_max_of_three_first(self):
        self.assertEqual(extend.max_of_three(3, 4, 18), 18)

    def test_max_of_three_third(self):
        self.assertEqual(extend.max_of_three(8, 4, 5), 8)

    def test_median_four(self):
        self.assertEqual(extend.median([7,5,3,5]), 5)

    def test_median_five(self):
        self.assertEqual(extend.median([1,2,3,4,5]), 3)

    def test_is_vovel_a(self):
        self.assertEqual(extend.is_vovel('a'), True)
    
    def test_is_vovel_r(self):
        self.assertEqual(extend.is_vovel('r'), False)

    def test_translate_bemutatkozik(self):
        self.assertEqual(extend.translate('hungarian'), 'huvungavariviavan')

if __name__ == '__main__':
    unittest.main()
