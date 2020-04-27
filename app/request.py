import urllib.request,json
from .models import Articles
from .models import Source
# Getting api key
api_key = None
# Getting the movie base url
base_url = None
#
source_url =None


def configure_request(app):
    global api_key,base_url,source_url
    source_url = app.config['ARTICLE_API_BASE_URL']
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCES_URL']
    




def get_news(country,category):
    '''
    function of getting json response ro url
    '''
    get_news_url = base_url.format(country,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_result = None


        if get_news_response['sources']:
            news_result_list = get_news_response['sources']
            news_result = process_results(news_result_list)

    return news_result

def process_results(news_list):
    '''
    function that takes in the movie results and transform them to a list
    '''
    news_result =[]
 
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        print(id)
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        if url:
            news_object = Source(id,name,title,description,url,category,country)
            news_result.append(news_object)
    return news_result

def get_details(id):
    get_news_details_url = source_url.format(id,api_key)
    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)
        
        news_result = None

        if news_details_response['articles']:
           news_source_list = news_details_response['articles']
           news_result = process_sources(news_source_list)

    return news_result

def process_sources(articles_list):
    '''
    process dictionary and out out objects
    '''
    news_result = []
    source_dictionary ={}
    for result in articles_list:

        source_id = result['source']

        source_dictionary['id']= source_id['id']
        source_dictionary['name'] = source_id['name']

        id = source_dictionary['id']
        print(id)
        name = source_dictionary['name']

        author = result.get('author')
        title = result.get('title')
        description = result.get('description')
        url = result.get('url')
        urlToImage = result.get('urlToImage')
        publishedAt = result.get('publishedAt')

        if urlToImage:
            
            news_object = Articles(id,name,author,title,description,url,urlToImage, publishedAt)
            news_result.append(news_object)
    return news_result
