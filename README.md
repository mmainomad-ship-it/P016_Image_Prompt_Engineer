# 🖼️ Project 16: API - Image Prompt Generator (Ollama Local AI)

This project utilizes a **Local Large Language Model (LLM)** via **Ollama** to transform simple, high-level ideas into highly detailed, production-ready technical prompts for text-to-image models (like Midjourney, DALL-E, or Stable Diffusion). This demonstrates constrained, creative prompt engineering using a local, private LLM setup.

### Key Features/Constraints

* **Creative Director Persona:** The LLM is governed by a strict System Prompt to act as a professional Creative Director and Prompt Engineer.
* **Technical Precision:** Generated prompts are constrained to include specific artistic styles, lighting conditions, resolutions (e.g., 8k), and moods.
* **Single Output Format:** The model is instructed to output a single, comprehensive, comma-separated sentence suitable for direct use in image generators.
* **Local AI Focus:** All processing is done locally via the Ollama service, ensuring data privacy and zero cost.
* **Direct Input:** Accepts simple user input directly via the terminal for quick iteration.

---

### Technology Stack

* Python 3.x
* `requests` library (For HTTP communication with the local Ollama API)
* Ollama Service (running locally on `http://localhost:11434`)
* LLM: Llama 3 (or other compatible models)

---

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/mmainomad-ship-it/P016_Image_Prompt_Engineer](https://github.com/mmainomad-ship-it/P016_Image_Prompt_Engineer)
    cd P016_Image_Prompt_Engineer
    ```
2.  **Ensure Ollama is running:**
    Make sure the Ollama application is installed and running on your machine. The script expects the API to be active at `http://localhost:11434`.
    ```bash
    ollama serve
    ```
3.  **Pull the required model:**
    The script defaults to using `llama3`. Pull it using the command:
    ```bash
    ollama pull llama3
    ```
4.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
5.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Since we are using `requests`, ensure it is in your requirements.txt)*

6.  **Run the script:**
    ```bash
    python prompt_generator.py
    ```
    The script will prompt you to enter a simple image idea (e.g., "A cat on a roof").

---

### Author

* **Author:** mmainomad-ship-it
* **GitHub:** https://github.com/mmainomad-ship-it