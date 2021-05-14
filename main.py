import urllib, requests, sys

key = '42ad3755ae7d72e1b14416085c0c1838'
url = urllib.parse.quote(str(sys.argv[1]))
name  = ''
req = requests.get('http://cutt.ly/api/api.php?key={}&short={}&name={}'.format(key, url, name))
res = req.json()
if req.status_code == 200 and res['url']['status'] == 7:
    print(res['url']['title'] + ' - ' + res['url']['shortLink'])
else:
    print('Err: Connection or URL')
