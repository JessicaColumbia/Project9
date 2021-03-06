#test file
import unittest 
import main
from collections import Counter
class Test(unittest.TestCase):
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
        self.assertTrue(main.love(words)>=0 )

#test mood function        
    def test_mood(self):
        words = Counter(["hello", "happy"])
        self.assertAlmostEqual(main.mood(words), 1)
        words = Counter(["hello", "sad"])
        self.assertAlmostEqual(main.mood(words), 0)
        words = Counter(["hello", "world"])
        self.assertAlmostEqual(main.mood(words), 0.5)
        words=Counter(['happy','sad'])
        self.assertAlmostEqual(main.mood(words), 0.5)
        words=Counter(['happy','sad','joy'])
        self.assertAlmostEqual(main.mood(words), 0.7)
        words=Counter(['happy','sad','weep'])
        self.assertAlmostEqual(main.mood(words), 0.3)
        words=Counter(['happy','sad','weep','cry'])
        self.assertAlmostEqual(main.mood(words), 1/4, delta=0.1)
        

#test length 
    def test_length(self):
        words = Counter(["hello", "world"])
        self.assertAlmostEqual(main.length(words), 0.00, delta=1e-4)
        words = Counter(['i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h'])
        self.assertAlmostEqual(main.length(words), 0.3, delta=1e-4)
        words = Counter(['i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h',
                        'i','j', 'a', 'b', 'c','d', 'e', 'f', 'g', 'h'])
        self.assertAlmostEqual(main.length(words), 1.0, delta=1e-4)
        

#test complexity
    def test_complexity(self):
        words = Counter(["hello", "world"])
        self.assertAlmostEqual(main.complexity(words), 0)
        words = Counter(["hello", "brandish"])
        self.assertAlmostEqual(main.complexity(words), 0.2)
        
        
#test read data        
    def test_read_data(self):
        data = main.read_data("./Lyrics")
        self.assertEqual(len(data["characterizations"]),1001)
        
        
suite = unittest.defaultTestLoader.loadTestsFromTestCase(Test)
# Run each test in suite
unittest.TextTestRunner().run(suite)
        