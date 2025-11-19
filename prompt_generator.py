import requests  # STEP 1: Library to send HTTP requests to the local Ollama API
import json  # STEP 1: Library to handle JSON input/output formatting

# STEP 2: Configuration Constants
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3"


# STEP 3: Define the function to call the local LLM
def generate_prompt(user_idea):
    """Sends the idea to Llama 3 and returns the engineered prompt."""

    # STEP 4: Prepare the API payload (using the "Chat" format)
    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are an expert image prompt engineer. Transform simple ideas into detailed, vivid technical prompts (8k, cinematic, lighting). Output ONE comma-separated sentence.",
            },
            {
                "role": "user",
                "content": f"Create a detailed image prompt based on this idea: '{user_idea}'",
            },
        ],
        "stream": False,
        "options": {"temperature": 0.7, "num_predict": 300},
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()  # Check for errors

        # Parse the JSON response
        result = response.json()
        return result["message"]["content"]  # Extract the actual text

    except Exception as e:
        return f"Error: {str(e)}"


# STEP 5: Main Execution Block
if __name__ == "__main__":
    print("\n--- Image Prompt Engineer (Local Llama 3) ---")
    idea = input("Enter a simple image idea (e.g., 'A cat on a roof'): ")

    print("\n--- Generating Detailed Prompt... ---")
    final_prompt = generate_prompt(idea)

    print(f"\n**Generated Image Prompt:**\n{final_prompt}")
