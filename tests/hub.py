import unittest
from src.interface import GithubUI
from src import env

class TestGithubUI(unittest.TestCase):
    spoonKnife = "octocat/Spoon-Knife"
    spoonKnifeContent = {'README.md': 'file', 'index.html': 'file', 'styles.css': 'file'}

    gan = "ivanrj7j/GAN-Based-Super-resolution"
    ganContent = {'.gitignore': 'file', 'LICENSE': 'file', 'README.md': 'file', 'config.py': 'file', 'main.py': 'file', 'src': {'__init__.py': 'file', 'blocks.py': 'file', 'discriminator.py': 'file', 'generator.py': 'file', 'loss.py': 'file'}, 'train': {'mseTrain.py': 'file', 'vggTrain.py': 'file'}, 'utils': {'__init__.py': 'file', 'dataloader.py': 'file', 'utils.py': 'file'}}

    content = {
        spoonKnife: (spoonKnifeContent, "This repo is for demonstration purposes only."),
        gan: (ganContent, "Implementation of Super resolution models using GANs"),
        # Add more repos here as needed...
    }

    testFiles = [
        "README.md",
        "train/vggTrain.py"
    ]
    
    git = GithubUI(env.API_KEY)

    def test_init(self):
        self.assertIsNotNone(self.git)

    def test_getRepo(self):
        repo = self.git.getRepo(self.spoonKnife)
        self.assertIsNotNone(repo)
        self.assertEqual(repo.name, 'Spoon-Knife')

    def test__getRepoStructure(self):
        for url, (content, description) in self.content.items():
            repo = self.git.getRepo(url)
            structure = self.git._getRepoStructure(repo)
            self.assertIsNotNone(structure)
            self.assertEqual(type(structure), dict)
            self.assertEqual(structure, content)

    def test_getRepoStructure(self):
        for url, (content, description) in self.content.items():
            structure = self.git.getRepoStructure(url)
            self.assertIsNotNone(structure)
            self.assertEqual(type(structure), dict)
            self.assertEqual(structure, content)

    def test_description(self):
        for url, (content, description) in self.content.items():
            desc = self.git.getDescription(url)
            self.assertEqual(desc, description)

    def test_readme(self):
        for url in self.content.keys():
            readme = self.git.getReadme(url)
            self.assertEqual(type(readme), str)

    def test_fileContent(self):
        for file in self.testFiles:
            content = self.git.getFileContents(self.gan, file)
            self.assertEqual(type(content), str)

    def test_relevantFiles(self):
        content = list(self.git.getRelevantFiles(self.gan, self.testFiles))
        self.assertGreater(len(content), 0)