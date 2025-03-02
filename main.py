import gradio as gr
import time
import threading
import logging
import os
from src.ai.filePicker import pickFiles
from src.interface import GithubUI
from src.ai.scorer import generateScore
from src.env import API_KEY
from dotenv import load_dotenv

load_dotenv()

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging to both console & file
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),  # Log file
        logging.StreamHandler()  # Console output
    ]
)

# Global GitHub UI object
git = GithubUI(API_KEY)

def evaluateRepo(repoUrl: str):
    """
    Fetches repository data, processes files, generates a score,
    and returns formatted Markdown with total score, summary, evaluation scores, and elapsed time.
    """
    startTime = time.time()
    repo = "/".join(repoUrl.split("/")[-2:])
    if not repo:
        logging.error("Invalid repository URL provided.")
        return ("**Error:** Invalid repository URL", 0)

    logging.info(f"Starting evaluation for: {repo}")

    try:
        structure = git.getRepoStructure(repo)
        logging.info(f"Repo structure fetched for: {repo}")

        files = pickFiles(structure)
        inp = git.getAIInput(repo, files)

        score = generateScore(inp)
        elapsedTime = round(time.time() - startTime, 2)
        logging.info(
            f"Evaluation completed for {repo} in {elapsedTime} seconds.")

        # Build output text
        totalS = score["total"]
        totalScoreText = f"# {"🟢" if totalS >= 70 else "🟡" if totalS >= 40 else "🔴"}**Total Score:** {totalS}\n\n"
        summaryText = f"# **Summary:**\n{score['summary']}\n\n"
        evaluationText = "**Evaluation Scores:**\n"

        for category, details in score['evaluation'].items():
            s = details['score']
            emoji = "🟢" if s >= 70 else "🟡" if s >= 40 else "🔴"
            reason = details['reason']
            evaluationText += f"{emoji} **{category.capitalize().replace('_', ' ')}**: {s}\n> {reason}\n\n"

        finalOutput = totalScoreText + summaryText + evaluationText
        return (finalOutput, elapsedTime)

    except Exception as e:
        logging.error(f"Error during evaluation: {e}", exc_info=True)
        return ("**Error:** Something went wrong. Please try again!", 0)


def evaluateWithLoading(repoUrl: str):
    """
    Runs evaluateRepo in a background thread and displays loading updates (with a timer)
    until the evaluation is complete. Once done, it shows the final Markdown output.
    """
    result_container = [None]

    def worker():
        try:
            result_container[0] = evaluateRepo(repoUrl)
        except Exception:
            logging.error(
                "Unexpected error in background thread.", exc_info=True)
            result_container[0] = (
                "**Error:** Something went wrong. Please try again!", 0)

    thread = threading.Thread(target=worker)
    thread.start()
    startTime = time.time()

    # Yield loading message while processing
    while thread.is_alive():
        elapsed = round(time.time() - startTime, 2)
        yield ("<div>⌛ Evaluating...</div>", f"⏳ Time taken: {elapsed}s")
        time.sleep(0.5)
    thread.join()

    finalOutput, elapsedTime = result_container[0]
    yield (finalOutput, f"⏳ Time taken: {elapsedTime}s")


with gr.Blocks(title="RepoReview") as ui:
    gr.Markdown("# 🛠️ GitHub Repo Evaluator")
    gr.Markdown(
        "Enter a GitHub repository URL to analyze its structure and quality.")

    repoInput = gr.Textbox(label="GitHub Repo URL",
                           placeholder="https://github.com/user/repo", elem_id="repoInput")
    submitButton = gr.Button("Evaluate Repo", elem_id="submitButton")

    resultOutput = gr.Markdown()
    timerOutput = gr.Markdown()

    submitButton.click(evaluateWithLoading, inputs=repoInput,
                       outputs=[resultOutput, timerOutput])

    # Custom JS to trigger submit on Ctrl+Enter in the textbox
    gr.HTML("""
    <script>
    const repoInput = document.getElementById("repoInput");
    const submitButton = document.getElementById("submitButton");
    repoInput.addEventListener("keydown", function(event) {
      if (event.ctrlKey && event.key === "Enter") {
        submitButton.click();
      }
    });
    </script>
    """)

    gr.Markdown('<p style="text-align: center;"><a href="https://github.com/ivanrj7j" target="_blank" style="color: #007bff; text-decoration: none;">Made with 💖 Ivan Raphel Jaison</a></p>')

ui.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", 8080)))
