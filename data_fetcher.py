import requests
import wikipediaapi

def fetch_article_content(title):
    wiki_wiki = wikipediaapi.Wikipedia(user_agent='WikipediaArticleSummarizer (sylvesterchukwuahachie@gmail.com)', language='en')

    page_py = wiki_wiki.page(title)
    return page_py.summary

hello = fetch_article_content('boy')
print(hello)