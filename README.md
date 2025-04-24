# Proxies

List of proxies to use for any purpose. 

Data is taken from open source. 

---
## Usage Example

```python
from proxy.proxies import ProxyProvider


class WebCrawler:
    def __init__(self):
        self._proxy_provider = ProxyProvider(proxy_file='path/to/proxies.json')

    def connect(self):
        proxy = self._proxy_provider.proxy

        if proxy is None:
            print('No more proxies available.')
        else:
            print(proxy)


c = WebCrawler()
c.connect()
c.connect()
c.connect()
c.connect()
c.connect()
```
---
