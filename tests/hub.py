import unittest
from src.interface import GithubUI
from src import env
from github.Auth import Token

class TestGithubUI(unittest.TestCase):
    spoonKnife = "octocat/Spoon-Knife"
    spoonKnifeContent = {'README.md': 'file', 'index.html': 'file', 'styles.css': 'file'}


    def setUp(self):
        self.git = GithubUI(Token(env.API_KEY))

    def test_getRepo(self):
        repo = self.git.getRepo(self.spoonKnife)
        self.assertIsNotNone(repo)
        self.assertEqual(repo.name, 'Spoon-Knife')

    def test__getRepoStructure(self):
        repo = self.git.getRepo(self.spoonKnife)
        structure = self.git._getRepoStructure(repo)
        self.assertIsNotNone(structure)
        self.assertEqual(type(structure), dict)
        self.assertEqual(structure, self.spoonKnifeContent)

    def test_getRepoStructure(self):
        structure = self.git.getRepoStructure(self.spoonKnife)
        self.assertIsNotNone(structure)
        self.assertEqual(type(structure), dict)