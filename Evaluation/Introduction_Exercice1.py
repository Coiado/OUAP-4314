import requests

class RequestHTTP:

    def __init__(self,url = "http://www.esiee.fr/"): 
        self.url = url
        self.header =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	
    def request(self,timeout):
        return requests.get(self.url, self.header, timeout = 10)

    def retry(self,timeout): 
        try:
             return requests.get(self.url, self.header, timeout = 10)
        except requests.exceptions.RequestException as e:  # This is the correct syntax
             print e
             return self.retry
		
		
		
r = RequestHTTP("http://www.esiee.fr/")
response = r.retry(5)
print(response.content[0:1000])
