def generate_affiliation_link(url):
    parts = url.split('/')
    pybites_part = 'tag=pyb0f-20'
    result = f'http://www.amazon.com/dp/{parts[5]}/?{pybites_part}'
    return result