"""
    You can do a lot of things with Python, even read the news. You
    can access the news using the Python newspapers module. You
    can use this module to scrape newspaper articles. First, install the module "pip install newspaper3k".
"""
# pip install newspaper3k
# Below we access the title of the article. All we need is the article URL.

from newspaper import Article

url = 'https://www.ndtv.com/india-news/haryana-assembly-polls-savitri-jindal-is-indias-richest-woman-savitri-jindal-bjps-b-team-in-haryana-what-she-told-ndtv-6640699#pfrom=home-ndtv_topstories_lastestImg'
news = Article(url)
news.download()
news.parse()
print(news.text)
print(news.title)
