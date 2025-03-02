from github import Github
from github.Repository import Repository
from github.Auth import Token
from github import UnknownObjectException

class GithubUI:
    """
    # Github UI

    This class provides a simple UI for interacting with a GitHub repository.
    """
    def __init__(self, apiKey:str):
        self.git = Github(auth=Token(apiKey))

    def _getRepoStructure(self, repo:Repository, path:str=""):    
        """
        Recursively get the structure of a GitHub repository. (Should only be accessed from within the class.)
        
        Parameters:
        repo (Repository): The GitHub repository.
        path (str): The path within the repository. Defaults to "".
        
        Returns:
        dict: The repository structure as a nested dictionary.
        """
        contents = repo.get_contents(path)
        structure = {}
        
        for content in contents:
            if content.type == "dir":
                structure[content.name] = self._getRepoStructure(repo, content.path)  # Recurse into directories
            else:
                structure[content.name] = "file"
        
        return structure
    
    def getRepo(self, repoPath:str) -> Repository:
        """
        Get a GitHub repository by its path.
        
        Parameters:
        repoPath (str): The path to the GitHub repository.
        
        Returns:
        Repository: The GitHub repository.
        """
        repo = self.git.get_repo(repoPath)
        return repo
    
    def getRepoStructure(self, repoPath:str):
        """
        Get the structure of a GitHub repository.
        
        Parameters:
        repoPath (str): The path to the GitHub repository.
        
        Returns:
        dict: The repository structure as a nested dictionary.
        """
        repo = self.getRepo(repoPath)
        return self._getRepoStructure(repo)
    
    def getDescription(self, repoPath:str) -> str:
        """
        Get the description of a GitHub repository.
        
        Parameters:
        repoPath (str): The path to the GitHub repository.
        
        Returns:
        str: The description of the GitHub repository.
        """
        repo = self.getRepo(repoPath)
        return repo.description if repo.description else ""
    
    def getReadme(self, repoPath:str) -> str:
        """
        Get the README file content of a GitHub repository.
        If not found, return an empty string.
        
        Parameters:
        repoPath (str): The path to the GitHub repository.
        
        Returns:
        str: The content of the README file.
        """
        repo = self.getRepo(repoPath)
        
        # Look for README files in the specified order. If found, return its content.
        for fileName in ("README.MD", "README.md", "README", "README.TXT", "README.txt", "readme.md", "readme", "readme.txt"):
            try:
                repo = self.getRepo(repoPath)
                readmeFile = repo.get_contents(fileName)
                return readmeFile.decoded_content.decode("utf-8")
            except UnknownObjectException:
                pass

        return ""
    
    def getFileContents(self, repo:str, file:str):
        """
        Get the content of a specific file in a GitHub repository.
        Get the GitHub repository and check if the file exists. If not, return an empty string.
        
        Parameters:
        repo (str): The path to the GitHub repository.
        file (str): The file name.
        
        Returns:
        str: The content of the specified file.
        """
        # Also decode the content to handle potential encoding issues.
        try:
            repo = self.getRepo(repo)
            fileContent = repo.get_contents(file).decoded_content.decode("utf-8")
            return fileContent
        except UnknownObjectException:
            return ""
        
    def getRelevantFiles(self, repoPath:str, files:list[str]):
        """
        Get the content of relevant files in a GitHub repository.
        Get the GitHub repository and check if the files exist. If not, return an empty string.
        
        Parameters:
        repoPath (str): The path to the GitHub repository.
        files (list[str]): The list of file names.
        
        Returns:
        dict: The content of the relevant files.
        """
        for file in files:
            yield self.getFileContents(repoPath, file)

    def getAIInput(self, repoPath:str, files:list[str]):
        contents = self.getRelevantFiles(repoPath, files)
        readme = self.getReadme(repoPath)
        description = self.getDescription(repoPath)
        structure = self.getRepoStructure(repoPath)

        return {
            "readme": readme,
            "description": description,
            "contents": contents,
            "structure":structure
        }