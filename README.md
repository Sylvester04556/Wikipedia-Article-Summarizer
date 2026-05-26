# Wikipedia Article Summarizer

An AI-powered CLI app that fetches a Wikipedia article and summarizes it using a local LLM via Ollama.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/download) installed

## Setup

1. Clone the repo and navigate into it
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the app

**Step 1 — Start Ollama** (do this once, in a separate terminal):
```
ollama serve
```

**Step 2 — Run the app:**
```
python main.py
```

Then enter any Wikipedia article title when prompted.

## How it works

1. Fetches and cleans the Wikipedia article text
2. Splits the text into chunks (~1000 words each)
3. Summarizes each chunk using `llama3.2:1b`
4. Merges all chunk summaries into one final summary
