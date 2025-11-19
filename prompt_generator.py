import requests  # STEP 1: Library to send HTTP requests to the local Ollama API
import json  # STEP 1: Library to handle JSON input/output formatting
import csv  # STEP 1: Library to save data to CSV
import os  # STEP 1: Library to check file existence

# STEP 2: Configuration Constants
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"
CSV_FILE = "prompt_log.csv"


# STEP 3: Define the function to call the local LLM
def generate_prompt(user_idea):
    """Sends the idea to Llama 3 and returns the engineered prompt."""

    # STEP 4: Core Logic - The "Sophisticated" Persona
    # We force the model to use specific high-end artistic and technical keywords.
    system_instruction = (
        "You are an elite AI Visual Artist and Creative Director. "
        "Your task is to transmute simple concepts into hyper-realistic, production-grade image generation prompts. "
        "You MUST include specific technical details: camera type (e.g., Leica M6, Sony A7R IV), "
        "lens specifications (e.g., 35mm, f/1.8), film stock or render engine (e.g., Kodak Portra 400, Unreal Engine 5), "
        "complex lighting setups (e.g., volumetric, chiaroscuro, bioluminescent), and artistic style. "
        "The output must be a single, dense, comma-separated string optimized for diffusion models."
    )

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_instruction},
            {
                "role": "user",
                "content": f"Create a detailed image prompt based on this idea: '{user_idea}'",
            },
        ],
        "stream": False,
        "options": {
            "temperature": 0.8,  # Slightly higher for more artistic flair
            "num_predict": 400,  # Allowed it to be a bit longer
        },
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        result = response.json()
        return result["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"


# STEP 5: Define the Save Function
def save_to_csv(user_idea, generated_prompt):
    """Appends the idea and prompt to a CSV file."""

    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["User Idea", "Generated Prompt"])
        writer.writerow([user_idea, generated_prompt])

    print(f"   [Saved to {CSV_FILE}]")


# STEP 6: Main Execution Block (Continuous Loop)
if __name__ == "__main__":
    print("\n--- Image Prompt Engineer (Local Llama 3 | Pro Edition) ---")
    print("Type 'quit' or 'exit' to stop the program.\n")

    while True:
        idea = input("Enter a simple image idea (e.g., 'A cat on a roof'): ")

        if idea.lower() in ["quit", "exit"]:
            print("Exiting... Goodbye!")
            break

        print("\n--- Generating Detailed Prompt... ---")
        final_prompt = generate_prompt(idea)

        print(f"\n**Generated Image Prompt:**\n{final_prompt}\n")

        save_to_csv(idea, final_prompt)
        print("-" * 30 + "\n")
