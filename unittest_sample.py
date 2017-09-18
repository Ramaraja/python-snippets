# demonstrating unittest lib

import unittest

class TestSamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_upper(self):
        self.assertEqual('test'.upper(), 'TEST')

    def test_split(self):
        text = "hello world"
        self.assertEqual(text.split(), ['hello','world'])


if __name__ == '__main__':
    unittest.main()
