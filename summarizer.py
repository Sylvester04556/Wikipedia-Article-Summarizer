from openai import OpenAI
from data_preprocessor import clean_text, chunk_text
import subprocess
subprocess.run(["ollama", "pull", "llama3.2:1b"], check=True)
llama = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

system_prompt = """You are a precise summarization engine. Your ONLY job is to compress
text into shorter text. Rules you must follow:

1. Use ONLY facts stated in the provided text. Never add outside knowledge.
2. Never invent names, dates, numbers, or claims not explicitly present.
3. Write in neutral, encyclopedic tone — no opinions or commentary.
4. Output raw text only — no headings, bullet points, or markdown.
5. If the text is too vague to summarize, say: Insufficient content.
"""

chunk_prompt = """"
Summarize the following passage in exactly 3 to 5 sentences. Preserve
the most important facts, definitions, and relationships. Do not repeat
yourself.
"""

merge_prompt = """merge_prompt = (
    f"Below are partial summaries from different sections of the "
    f"Wikipedia article titled \"{title}\". Synthesize them into one "
    "unified, coherent summary of 4 to 7 sentences.\n\n"
    "Rules:\n"
    "- Merge overlapping points, do not repeat the same fact twice.\n"
    "- Maintain the original logical or chronological order.\n"
    "- Write as one flowing paragraph, not a list.\n"
    "- Do not add any information not present in the summaries below.\n\n"
    "---\n"
    f"{combined_summaries}\n"
    "---\n\n"
    "Final summary:"
).
"""
def summarize_chunks(chunks):
    summaries = []
    for chunk in chunks:
        response = llama.chat.completions.create(
            model = 'llama3.2:1b',
            messages = [
                {"role": "system", "content": "You are a helpful assistant that summarizes Wikipedia articles."},
                {"role": "user", "content": chunk_prompt + "\n\n" + chunk},
            ]
        )
        summaries.append(response.choices[0].message.content)
    return summaries

def final_summary(summaries):
    combined_summary = " ".join(summaries)
    response = llama.chat.completions.create(
        model = 'llama3.2:1b',
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": merge_prompt + "\n\n" + combined_summary},
        ]
    )
    return response.choices[0].message.content
