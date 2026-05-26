from data_fetcher import fetch_article_content
def clean_text(title):
    text = fetch_article_content(title)
    if text:
        # Remove extra whitespace and newlines
        cleaned_text = ' '.join(text.split())
        # return cleaned_text
        references_index = cleaned_text.find('References')
        if references_index != -1:
            cleaned_text = cleaned_text[:references_index]
        else:
            cleaned_text = cleaned_text

    return cleaned_text

def chunk_text(text, chunk_size=1000):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks
