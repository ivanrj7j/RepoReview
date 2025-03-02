import unittest
from src.ai.filePicker import generate

class TestFilePicker(unittest.TestCase):
    inp = {'README.md': 'file', 'index.html': 'file', 'styles.css': 'file'}
    def test_generation(self):
        output = generate(self.inp)
        self.assertIsNotNone(output)
        self.assertEqual(list(output.keys()), ["importantFiles", "justifications"])