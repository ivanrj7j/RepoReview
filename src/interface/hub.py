from github import Github
from github.Repository import Repository
from github.Auth import Token

class GithubUI:
    def __init__(self, apiKey:str):
        self.git = Github(auth=Token(apiKey))

    def _getRepoStructure(self, repo:Repository, path:str=""):    
        contents = repo.get_contents(path)
        structure = {}
        
        for content in contents:
            if content.type == "dir":
                structure[content.name] = self.get_repo_structure(repo, content.path)  # Recurse into directories
            else:
                structure[content.name] = "file"
        
        return structure
    
    def getRepo(self, url:str) -> Repository:
        repo = self.git.get_repo(url)
        return repo
    
    def getRepoStructure(self, url:str):
        repo = self.getRepo(url)
        return self._getRepoStructure(repo)