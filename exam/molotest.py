import urllib.request as ul

url = 'http://test-scis.skylife.co.kr/scis/ec'
request = ul.Request(url)
response = ul.urlopen(request)
