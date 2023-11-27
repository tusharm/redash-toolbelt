from pprint import pprint

from redash_toolbelt import Redash


def get_queries(client, tags=[]):
    queries = client.queries(tags=tags)
    return queries['results']


def get_dashboards(client, tags=[]):
    dashboards = client.dashboards(tags=tags)
    return dashboards['results']


if __name__ == '__main__':
    api_key = '...'
    base_url = '...'
    client = Redash(base_url, api_key)

    pprint(get_queries(client, ['dev']))
    # pprint(get_dashboards(client, ['sales']))
