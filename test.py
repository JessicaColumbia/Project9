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
        
#test love words
    def test_love(self):
        words = Counter(["hello", "world"])
        self.assertAlmostEqual(main.love(words), 0)
        words = Counter(["hello", "love"])
        self.assertAlmostEqual(main.love(words), 1.0/9)

#test mood function        
def test_mood(self):
        words = Counter(["hello", "happy"])
        self.assertAlmostEqual(main.mood(words), 1)
        words = Counter(["hello", "sad"])
        self.assertAlmostEqual(main.mood(words), 0)
        words = Counter(["hello", "world"])
        self.assertAlmostEqual(main.mood(words), 0.5)
