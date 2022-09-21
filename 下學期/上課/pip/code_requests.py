import requests
data = {'lang':'tw','type':'2'}
r = requests.get("http://5b0988e595225.cdn.sohucs.com/images/20180731/87345ab1747a4cfba58ce7f0eccdaeb3.gif")
if r.status_code == 200:
    f = open('cut-cat.gif','wb')
    f.write(r.content)
    f.close
