from data_fetcher import fetch_article_content
from data_preprocessor import clean_text, chunk_text
from summarizer import summarize_chunks, final_summary
class WikipediaArticleSummarizer:
    def __init__(self):
        print('Welcome to the Wikipedia Article Summarizer!')
        while True:
            title = input('Enter the title of the Wikipedia article you want to summarize (or type "exit" to quit): ').strip().lower()
            if title == 'exit':
                print('Goodbye!')
                break
            try:
                fetched_content = fetch_article_content(title)
                if fetched_content:
                    cleaned_text = clean_text(fetched_content)
                    chunks = chunk_text(cleaned_text)
                    chunk_summaries = summarize_chunks(chunks)
                    final_article_summary = final_summary(chunk_summaries)
                    print('\nFinal Summary:\n')
                    print(final_article_summary)
            except ValueError as ve:
                print(ve)
if __name__ == "__main__":
    summarizer = WikipediaArticleSummarizer()
    summarizer