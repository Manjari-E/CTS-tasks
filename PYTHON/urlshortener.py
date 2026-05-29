import hashlib

class URLShortener:
    def __init__(self):
        self.urls = {}

    def shorten(self, url):
        short = hashlib.md5(url.encode()).hexdigest()[:6]
        self.urls[short] = url
        return short

    def retrieve(self, short):
        return self.urls.get(short)

obj = URLShortener()

code = obj.shorten("https://google.com")

print("Short URL:", code)
print("Original URL:", obj.retrieve(code))