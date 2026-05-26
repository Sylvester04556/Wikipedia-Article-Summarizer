import wikipediaapi

def fetch_article_content(title):
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='WikipediaArticleSummarizer (sylvesterchukwuahachie@gmail.com)', language='en')

    page_py = wiki_wiki.page(title)
    if page_py.exists():
        content = page_py.text
        return content
    else:
        raise ValueError(f"The article '{title}' does not exist.")


