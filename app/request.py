from app import app
import urllib.request,json
from .models import source

# Getting api key
api_key = app.config['SOURCE_API_KEY']

#Getting api key
base_url = app.config['SOURCE_API_BASE_URL']

def get_sources(name):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url = base_url.format(name, api_key)


    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        movie_results = None

        if get_sources_response['results']:
            source_results_list = get_sources_response['results']
            movie_results = process_results(source_results_list)
    return source_results