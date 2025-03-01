from github import Github
from github.Repository import Repository
from github.Auth import Token
from github import UnknownObjectException

class GithubUI:
    def __init__(self, apiKey:str):
        self.git = Github(auth=Token(apiKey))

    def _getRepoStructure(self, repo:Repository, path:str=""):    
        contents = repo.get_contents(path)
        structure = {}
        
        for content in contents:
            if content.type == "dir":
                structure[content.name] = self._getRepoStructure(repo, content.path)  # Recurse into directories
            else:
                structure[content.name] = "file"
        
        return structure
    
    def getRepo(self, repoPath:str) -> Repository:
        repo = self.git.get_repo(repoPath)
        return repo
    
    def getRepoStructure(self, repoPath:str):
        repo = self.getRepo(repoPath)
        return self._getRepoStructure(repo)
    
    def getDescription(self, repoPath:str) -> str:
        repo = self.getRepo(repoPath)
        return repo.description if repo.description else ""
    
    def getReadme(self, repoPath:str) -> str:
        for fileName in ("README.MD", "README.md", "README", "README.TXT", "README.txt", "readme.md", "readme", "readme.txt"):
            try:
                repo = self.getRepo(repoPath)
                readmeFile = repo.get_contents(fileName)
                return readmeFile.decoded_content.decode("utf-8")
            except UnknownObjectException:
                pass

        return ""
    
    def getFileContents(self, repo:str, file:str):
        try:
            repo = self.getRepo(repo)
            fileContent = repo.get_contents(file).decoded_content.decode("utf-8")
            return fileContent
        except UnknownObjectException:
            return ""