import requests


class HTTP:

    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url, timeout=5)
        # print(r.encoding)
        if r.status_code== 200:
            return r.json() if return_json else r.text
        else:
            return {} if return_json else ''


def is_isbn(query):
    if len(query) == 13 and query.isdigit():
        return True
    if len(query) == 10 and ('-' in query) and query.relace('-', '').isdigit():
        return True
    return False


def search_book(q, page, return_json=True):
    isbn_url = "https://api.douban.com/v2/book/isbn/{}"
    name_url = "https://api.douban.com/v2/book/search?q={}&start={}&count={}"
    count = 15
    start = (page-1) * count
    if is_isbn(q):
        return HTTP.get(isbn_url.format(q), return_json)
    else:
        return HTTP.get(name_url.format(q, start, count), return_json)


if __name__ == '__main__':
    test_url = 'https://api.douban.com/v2/book/search?q=test'
    print(HTTP.get(test_url))