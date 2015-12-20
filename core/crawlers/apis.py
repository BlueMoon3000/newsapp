import requests, anyconfig, os
import json

from core.models import Topic, Article
config = anyconfig.load(os.path.join(os.path.dirname(__file__), 'apis.json'))

class API(object):
    resource = ''
    responses = []

    def __init__(self, topics=None):
        self.api_config = config.get(self.resource)
        if topics:
            self.construct_urls()

    def build_params(self, subresource, params={}):
        # validates and constructs query params object

        query_params = {}
        for param, val in self.api_config.get(subresource).get('query').iteritems():
            if param in params.keys():
                query_params[param] = params[param]
            else:
                if val is not None:
                    query_params[param] = val
        print query_params
        return query_params

    def construct_url(self, subresource, params=None):
        # default no-op
        return self.api_config.get(subresource).get('url')

    def parse(self, response):
        # default no-op
        return response

    def read(self, subresource, params=None):
        params = self.build_params(subresource, params)
        url = self.construct_url(subresource, params)
        r = requests.get(url, params=params)
        self.responses.append(self.parse(r.json()))

class NYTimesAPI(API):
    resource = 'nytimes'
    
    def parse(self, response):
        print (json.dumps(response.get('response').get('docs')[:10],sort_keys=True, indent=4))
        return json.dumps(response.get('response').get('docs'), sort_keys=True, indent=4)

