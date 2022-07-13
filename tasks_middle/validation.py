import unittest


def validation_name(name: str) -> bool:
    valid_name = name.isalpha() and name[0].isupper(
    ) and not name.isspace() and not name.isupper() and len(name) > 1
    return valid_name

# test_validation_name_lowercase


class TestValidationFun(unittest.TestCase):
    def test_validation_isalpha(self):
        self.assertTrue(validation_name("Nastya"))

    def test_validation_isnumbers(self):
        self.assertFalse(validation_name("123astya"))

    def test_validation_issuper(self):
        self.assertFalse(validation_name("nastya"))

    def test_validation_isspace(self):
        self.assertFalse(validation_name("N a stya"))

    def test_validation_all_filters(self):
        self.assertFalse(validation_name("n 1 stya"))

    def test_validation_name_empty_str(self):
        self.assertFalse(validation_name(''))

    def test_validation_name_all_uppercase(self):
        self.assertFalse(validation_name('RADIK'))

    def test_validation_name_only_one_letter(self):
        self.assertFalse(validation_name('R'))

    def test_validation_name_only_two_letters(self):
        self.assertTrue(validation_name('Ri'))


unittest.main()
