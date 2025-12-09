import unittest
from password_security import (
    calculate_charset_size,
    calculate_entropy,
    analyze_password,
    generate_password,
)


class TestPasswordSecurity(unittest.TestCase):

    def test_charset_size_simple(self):
        # Solo minúsculas
        self.assertEqual(calculate_charset_size("abc"), 26)

    def test_entropy_increases_with_length(self):
        short = calculate_entropy("aaaaaa")      # 6 caracteres
        long = calculate_entropy("aaaaaaaaaa")   # 10 caracteres
        self.assertGreater(long, short)

    def test_analyze_password_classification(self):
        weak = analyze_password("1234")
        strong = analyze_password("A9$kzP!f3Qm2")
        self.assertNotEqual(weak.classification, strong.classification)

    def test_generate_password_length(self):
        pwd = generate_password(length=20)
        self.assertEqual(len(pwd), 20)


if __name__ == "__main__":
    unittest.main()
