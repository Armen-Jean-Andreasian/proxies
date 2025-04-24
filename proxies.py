import json


class ProxyGallery:
    def __init__(self, proxy_file: str):
        self.proxy_file = proxy_file
        self._proxies: list[dict[str, str]] = self._load_proxies()

    def _load_proxies(self):
        with open(self.proxy_file, encoding='utf-8') as jf:
            return json.load(jf)

    @property
    def generator(self):
        for proxy in self._proxies:
            yield proxy['IP'] + ':' + proxy['PORT']


class ProxyProvider:
    def __init__(self, proxy_file='proxies.json'):
        proxy_gallery = ProxyGallery(proxy_file)
        self._proxy_generator = proxy_gallery.generator
        self._current_proxy = None

    def _get_next_proxy(self):
        try:
            self._current_proxy = next(self._proxy_generator)
        except StopIteration:
            self._current_proxy = None

    @property
    def proxy(self):
        self._get_next_proxy()
        return self._current_proxy


if __name__ == '__main__':
    proxy_provider = ProxyProvider()
    while True:
        if proxy := proxy_provider.proxy is None:
            break
        else:
            print(proxy)
