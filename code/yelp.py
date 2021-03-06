"""
Yelp Queries
------------
Uses Yelp Fusion Search API to query for businesses by a search term and
location, and the Business API to query additional information about the top
result from the search query.

Based on Yelp Fusion API code sample.
API documentation: https://www.yelp.com/developers/documentation/v3/get_started
"""
from __future__ import print_function

import functools
import pprint
import sys
from urllib.error import HTTPError
from urllib.parse import quote, urlencode
import argparse
import json
import requests
import urllib
import requests

API_KEY= 'ANhlvKgCi3WecIsQIolwYMD20ifqzhsPGsro5XLheEt_Wz8TtfxKYgImmAVTIhGuoXZzGnksvL0H38QEAtDMUQ3z-reqqlfONV6KjNrYedvBwu1I-e-m_2kKfZu7XnYx'

# API constants.
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Query constants.
SEARCH_LIMIT = 1




def request(host, path, api_key, url_params=None):
    """Given your API_KEY, send a GET request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, location, sort_by='distance'):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
        sort_by (str): How to filter search results.
    Returns:
        dict: The JSON response from the request.
    """
    try:
        term = term.replace(' ', '+')
    except AttributeError:  # if not str
        term = str(term)

    try:
        location = location.replace(' ', '+')
    except AttributeError:  # if not str
        location = str(location)

    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT,
        'sort_by':sort_by
    }
    return request(API_HOST, SEARCH_PATH, API_KEY, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.
    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, API_KEY)


def query_api(term, location):
    """Queries the API by the input values from the user.
    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, location)

    businesses = response.get('businesses')

    if not businesses:
        print(u'No businesses for {0} in {1} found.'.format(term, location))
        return

    business_id = businesses[0]['id']

    print(u'{0} businesses found, querying business info ' \
        'for the top result "{1}" ...'.format(
            len(businesses), business_id))
    response = get_business(API_KEY, business_id)

    print(u'Result for business "{0}" found:'.format(business_id))
    pprint.pprint(response, indent=2)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)')

    input_values = parser.parse_args()

    try:
        query_api(input_values.term, input_values.location)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )


if __name__ == '__main__':
    main()
