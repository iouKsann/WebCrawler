import requests
import json

API_KEY = '[YOUR_API_KEY]'
OMDB_URL = 'http://www.omdbapi.com/?apikey=' + API_KEY


def get_data(url):
    data = json.loads(requests.get(url).text)
    if data['Response'] == 'True':
        return data
    else:
        return None


def search_ids_by_keyword(keywords):
    query = '+'.join(keywords.split())  
    url = OMDB_URL + '&s=' + query
    data = get_data(url)
    return data
    
if __name__ == '__main__':
    keyword = 'Black Panther' #輸入查詢的關鍵字
    data = search_ids_by_keyword(keyword)
    print(data)