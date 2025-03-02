import argparse
from src.ai.filePicker import pickFiles
from src.interface import GithubUI
from src.ai.scorer import generateScore
from src.env import API_KEY
import colorama
from colorama import Fore, Style
# importing relevant libraries

colorama.init(autoreset=True)
# used for printing in color 

def printEvaluation(data):
    """
    This method is used to print the evaluation with colors

    Parameters:
    data (dict): Dictionary containing the evaluation data
    """
    print(f"{Fore.CYAN}{Style.BRIGHT}Summary:{Style.RESET_ALL} {data['summary']}\n")
    
    print(f"{Fore.MAGENTA}{Style.BRIGHT}Evaluation Scores:{Style.RESET_ALL}")
    
    for category, details in data['evaluation'].items():
        score = details['score']
        reason = details['reason']
        
        # Assign colors based on score
        if score >= 70:
            color = Fore.GREEN
        elif score >= 40:
            color = Fore.YELLOW
        else:
            color = Fore.RED
        
        print(f"{color}{category.capitalize().replace('_', ' ')}: {score}{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}{reason}{Style.RESET_ALL}\n")

    print(f"{Fore.BLUE}{Style.BRIGHT}Total Score:{Style.RESET_ALL} {data['total']}")


parser = argparse.ArgumentParser(description="Parse repo argument from CLI")
parser.add_argument("-r", "--repo", required=True, help="Repository name or URL")

args = parser.parse_args()
repo = "/".join(args.repo.split("/")[-2:])

if repo == "":
    print("Invalid repository name or URL")
    exit(1)
# getting the repository 

git = GithubUI(API_KEY)
structure = git.getRepoStructure(repo)
print("Getting structure... Please wait...")
files = pickFiles(structure)
print("Getting relevant files... Please wait...")
inp = git.getAIInput(repo, files)
print("Preparing files... Please wait...")
score = generateScore(inp)
print("Scoring files... Please wait...")

printEvaluation(score)