#test file
from unittest import TestCase
import main
from collections import Counter
class Test(TestCase):
    def test_kid_safe(self):
        words = Counter(["hello","world"])
        self.assertAlmostEqual(main.kid_safe(words),1)
        words = Counter(["hello", "sex"])
        self.assertAlmostEqual(main.kid_safe(words), 0.9)