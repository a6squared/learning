import unittest
import basics.basics as basics


class BasicsTests(unittest.TestCase):
    def test_string_formatting_matches_expected(self):
        self.assertEqual(
            'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are',
            basics.string_formatting())

    def test_current_version_gets_correct_version(self):
        self.assertIn('3.9', basics.current_version())

    def test_area_of_circle_is_correct(self):
        self.assertEqual(12.56, basics.area_of_circle(2))

    def test_file_extension_printer_is_correct(self):
        self.assertEqual('java', basics.file_extension('file.java'))
        self.assertEqual('doc', basics.file_extension('document.doc'))

    def test_get_builtin_docs_is_correct(self):
        self.assertEqual('Return the absolute value of the argument.', basics.get_builtin_docs())


if __name__ == '__main__':
    unittest.main()
