import unittest
from src.ai.filePicker import pickFiles
from src.interface import GithubUI
from src.ai.scorer import generateScore
from src.env import API_KEY

class TestAI(unittest.TestCase):
    inp = {'README.md': 'file', 'index.html': 'file', 'styles.css': 'file'}
    repo = "ivanrj7j/GAN-Based-Super-resolution"
    git = GithubUI(API_KEY)
    def test_filePicking(self):
        output = pickFiles(self.inp)
        self.assertIsNotNone(output)
        self.assertEqual(list(output.keys()), ["importantFiles", "justifications"])

    def test_scoring(self):
        structure = self.git.getRepoStructure(self.repo)
        files = pickFiles(structure)
        inp = self.git.getAIInput(self.repo, files)
        score = generateScore(inp)

        self.assertIsNotNone(score)
        self.assertEqual(list(score.keys()), ["summary", "evaluation", "total"])