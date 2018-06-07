import requests
url = 'http://apps.webofknowledge.com/full_record.do?product=UA&search_mode=GeneralSearch&qid=1&SID=7E8ocoeQDScVAjO5OzL&page=1&doc=7'

html = requests.get(url).text
print(html)