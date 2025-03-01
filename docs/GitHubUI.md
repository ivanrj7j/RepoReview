# GitHubUI Documentation

## Overview

`GithubUI` is a Python class designed to facilitate interaction with GitHub repositories using the PyGitHub library. It provides functionalities for retrieving repository structures, descriptions, README files, and specific file contents.

---

## Class: `GithubUI`

### **Initialization**
```python
GithubUI(apiKey: str)
```
**Parameters:**
- `apiKey` *(str)*: The API key for authenticating with GitHub.

**Description:**
Initializes the class with GitHub authentication.

---

## **Methods**

### **Private Method**

#### `_getRepoStructure`
```python
_getRepoStructure(repo: Repository, path: str = "") -> dict
```
**Parameters:**
- `repo` *(Repository)*: The GitHub repository object.
- `path` *(str, optional)*: The path within the repository. Defaults to "".

**Returns:**
- `dict`: The repository structure represented as a nested dictionary.

**Description:**
Recursively retrieves the structure of a repository, including directories and files.

---

### **Public Methods**

#### `getRepo`
```python
getRepo(repoPath: str) -> Repository
```
**Parameters:**
- `repoPath` *(str)*: The path to the GitHub repository (e.g., "username/repository").

**Returns:**
- `Repository`: A PyGitHub `Repository` object.

**Description:**
Fetches a GitHub repository using the provided path.

---

#### `getRepoStructure`
```python
getRepoStructure(repoPath: str) -> dict
```
**Parameters:**
- `repoPath` *(str)*: The path to the GitHub repository.

**Returns:**
- `dict`: A nested dictionary representing the repository structure.

**Description:**
Returns the repository structure by recursively listing its files and directories.

---

#### `getDescription`
```python
getDescription(repoPath: str) -> str
```
**Parameters:**
- `repoPath` *(str)*: The path to the GitHub repository.

**Returns:**
- `str`: The repository description.

**Description:**
Fetches the description of the given GitHub repository. Returns an empty string if no description is available.

---

#### `getReadme`
```python
getReadme(repoPath: str) -> str
```
**Parameters:**
- `repoPath` *(str)*: The path to the GitHub repository.

**Returns:**
- `str`: The content of the README file.

**Description:**
Retrieves the content of the README file in the repository. If no README file is found, returns an empty string.

---

#### `getFileContents`
```python
getFileContents(repo: str, file: str) -> str
```
**Parameters:**
- `repo` *(str)*: The path to the GitHub repository.
- `file` *(str)*: The file name.

**Returns:**
- `str`: The content of the specified file.

**Description:**
Fetches the content of a specific file in the repository. Returns an empty string if the file does not exist.

---

#### `getRelevantFiles`
```python
getRelevantFiles(repo: str, files: list[str]) -> dict
```
**Parameters:**
- `repo` *(str)*: The path to the GitHub repository.
- `files` *(list[str])*: A list of file names.

**Returns:**
- `dict`: A dictionary mapping filenames to their content.

**Description:**
Retrieves the content of multiple specified files in the repository. Uses a generator to yield file contents one by one.

---

## **Usage Example**
```python
apiKey = "your_github_api_key"
githubUI = GithubUI(apiKey)

repoPath = "username/repository"
structure = githubUI.getRepoStructure(repoPath)
print("Repository Structure:", structure)

description = githubUI.getDescription(repoPath)
print("Repository Description:", description)

readmeContent = githubUI.getReadme(repoPath)
print("README Content:", readmeContent)

fileContent = githubUI.getFileContents(repoPath, "main.py")
print("main.py Content:", fileContent)

files = ["main.py", "config.py"]
for content in githubUI.getRelevantFiles(repoPath, files):
    print("File Content:", content)
```

---

## **Notes**
- Uses the **PyGitHub** library to interact with GitHub's API.
- Handles missing files gracefully, returning empty strings when necessary.
- Implements efficient retrieval using recursion for repository structure.
- Uses a generator in `getRelevantFiles` for optimized memory usage.

---

## **Dependencies**
Make sure to install the required library before using this class:
```bash
pip install pygithub
```

