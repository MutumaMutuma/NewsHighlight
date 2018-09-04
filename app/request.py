import urllib.request,json
from .models import source
Source =source.Source
Articles = source.Articles

# Getting api key
api_key = None
base_url = None
articles_url = None
def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']
def get_sources(name):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(name, api_key)


    with urllib.request.urlopen(get_sources_url) as url:
        print("ew")
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        print(get_sources_response)
        source_results = None
        if get_sources_response["sources"]:
            source_results_list = get_sources_response["sources"]
            source_results = process_results(source_results_list)
    return source_results

def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        source_results: A list of source objects
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')

        
        source_object = Source (id, name, description)
        source_results.append(source_object)

    return source_results

def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''

    get_articles_url = articles_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        print(get_articles_response)
        articles_results = None

        
        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = receive_results(articles_results_list)
    return  articles_results
        

def receive_results(articles_list):
    '''
    Function that processes the articles result and transform them to a list of Objects

    Args:
        articles_list: A list of dictionaries that contain source details

    Returns :
        articles_results: A list of articles objects
    '''

    articles_results = []
    for articles_item in articles_list:
        id = articles_item.get('id')
        blue = articles_item.get('blue')
        title = articles_item.get('title')
        author = articles_item.get('author')
        description = articles_item.get('description')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        url = articles_item.get('url')
        
        articles_object = Articles ( blue, id, title , author, description, urlToImage, publishedAt, url)
        articles_results.append(articles_object)
    return articles_results