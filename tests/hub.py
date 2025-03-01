import unittest
from src.interface import GithubUI
from src import env

class TestGithubUI(unittest.TestCase):
    spoonKnife = "octocat/Spoon-Knife"
    spoonKnifeContent = {'README.md': 'file', 'index.html': 'file', 'styles.css': 'file'}

    gan = "ivanrj7j/GAN-Based-Super-resolution"
    ganContent = {'.gitignore': 'file', 'LICENSE': 'file', 'README.md': 'file', 'config.py': 'file', 'main.py': 'file', 'src': {'__init__.py': 'file', 'blocks.py': 'file', 'discriminator.py': 'file', 'generator.py': 'file', 'loss.py': 'file'}, 'train': {'mseTrain.py': 'file', 'vggTrain.py': 'file'}, 'utils': {'__init__.py': 'file', 'dataloader.py': 'file', 'utils.py': 'file'}}

    content = {
        spoonKnife: spoonKnifeContent,
        gan: ganContent,
        # Add more repos here as needed...
    }


    def setUp(self):
        self.git = GithubUI(env.API_KEY)

    def test_init(self):
        self.assertIsNotNone(self.git)

    def test_getRepo(self):
        repo = self.git.getRepo(self.spoonKnife)
        self.assertIsNotNone(repo)
        self.assertEqual(repo.name, 'Spoon-Knife')

    def test__getRepoStructure(self):
        for url, content in self.content.items():
            repo = self.git.getRepo(url)
            structure = self.git._getRepoStructure(repo)
            self.assertIsNotNone(structure)
            self.assertEqual(type(structure), dict)
            self.assertEqual(structure, content)

    def test_getRepoStructure(self):
        for url, content in self.content.items():
            structure = self.git.getRepoStructure(url)
            self.assertIsNotNone(structure)
            self.assertEqual(type(structure), dict)
            self.assertEqual(structure, content)