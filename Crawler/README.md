# 常用库

## - urllib.request.urlopen
### 范例
```python
    from urllib.request import urlopen
    url = 'http://zt.zjzs.net/xk2020/allcollege.html'

    # 将html转化为unicode，为防中文乱码
    html = urlopen(url).read().decode('utf-8') # html == url的html，
```

## - bs4  (pip3 install beautifulsoup4, pip3 install lxml)
### 范例
```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, features="lxml")

    links = soup.find_all("a", {"target": "_blank", "href": re.compile(r"^[0-9]+$\.html")})
    links = [a["href"] for a in links] # links == html的href集合 (列表生成式)
```
