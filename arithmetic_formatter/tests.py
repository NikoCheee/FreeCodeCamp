import unittest
from arithmetic_formatter.arithmetic_arranger import arithmetic_arranger


class MyTestCase(unittest.TestCase):
    def test_two_problems_arrangement1(self):
        test = arithmetic_arranger(['3801 - 2', '123 + 49'])
        self.assertEqual(test, '  3801      123\n''-    2    +  49\n''------    -----')

    def test_two_problems_arrangement2(self):
        test = arithmetic_arranger(['1 + 2', '1 - 9380'])
        self.assertEqual(test,  '  1         1\n'
                                '+ 2    - 9380\n'
                                '---    ------', 'Expected different output when calling '
                                                 '"arithmetic_arranger()" with ["1 + 2", "1 - 9380"]')

    def test_four_problems_arrangement(self):
        test = arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49'])
        self.assertEqual(test,  '    3      3801      45      123\n'
                                '+ 855    -    2    + 43    +  49\n'
                                '-----    ------    ----    -----',  'Expected different output when calling'
                                                                     ' "arithmetic_arranger()" with '
                                                                     '["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]')

    def test_five_problems_arrangement(self):
        test = arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380'])
        self.assertEqual(test,  '  11      3801      1      123         1\n'
                                '+  4    - 2999    + 2    +  49    - 9380\n'
                                '----    ------    ---    -----    ------',
                         'Expected different output when calling "arithmetic_arranger()" with'
                         ' ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]')

    def test_too_many_problems(self):
        with self.assertRaises(Exception):
            arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87'])

    def test_incorrect_operator(self):
        with self.assertRaises(Exception):
            arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49'])

    def test_too_many_digits(self):
        with self.assertRaises(Exception):
            arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])

    def test_only_digits(self):
        with self.assertRaises(Exception):
            arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49'])

    def test_two_problems_with_solutions(self):
        test = arithmetic_arranger(['3 + 855', '988 + 40'], True)
        self.assertEqual(test,   '    3      988\n'
                                 '+ 855    +  40\n'
                                 '-----    -----\n'
                                 '  858     1028',
                         'Expected solutions to be correctly displayed in output when '
                         'calling "arithmetic_arranger()" with ["3 + 855", "988 + 40"]'
                         ' and a second argument of `True`.')

    def test_five_problems_with_solutions(self):
        test = arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)
        self.assertEqual(test,
                         '   32         1      45      123      988\n'
                         '- 698    - 3801    + 43    +  49    +  40\n'
                         '-----    ------    ----    -----    -----\n'
                         ' -666     -3800      88      172     1028',
                         'Expected solutions to be correctly displayed in output when calling'
                         ' "arithmetic_arranger()" with five arithmetic problems and a second argument of `True`.')


if __name__ == '__main__':
    unittest.main()
