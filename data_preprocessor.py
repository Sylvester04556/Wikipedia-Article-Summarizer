def clean_text(fetched_content):
    if fetched_content:
        # Remove extra whitespace and newlines
        cleaned_text = ' '.join(fetched_content.split())
        # return cleaned_text
        references_index = cleaned_text.find('References')
        if references_index != -1:
            cleaned_text = cleaned_text[:references_index]
        else:
            cleaned_text = cleaned_text

    return cleaned_text

def chunk_text(cleaned_text, chunk_size=1000):
    words = cleaned_text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

