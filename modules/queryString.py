def parse(url):
    queryString = url.split('?')[1]
    keyvalues = queryString.split('&')
    queries = {}
    for keyvalue in keyvalues:
        key = keyvalue.split('=')[0]
        value = keyvalue.split('=')[1]
        queries[key] = value
    return queries
