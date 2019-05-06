# 常用库示例说明

## - urllib.request
### 范例
```python
    from urllib.request import urlopen
    url = 'http://zt.zjzs.net/xk2020/allcollege.html'

    # 将html转化为unicode，为防中文乱码
    html1 = urlopen(url).read().decode('utf-8') # html == url的html
    html2 = requests.get(MAIN_URL).content # bytes类型的html
    html2 = requests.get(MAIN_URL).text # 编码不完全准确
```

## -requests库 (pip3 install requests)
- get请求 - 百度搜索
```python
    url = "http://www.baidu.com/s"
    para = {"wd": "搜索的内容"}

    req = requests.get(url, params=para)
    print(req.url) # 返回url
```
- post请求 - form提交
```python
    url = 'http://pythonscraping.com/files/processing.php' # request url，通过浏览器Network处获取
    data = {'firstname': 'fff', 'lastname': 'lll'}

    req = requests.post(url, data=data)
    print(req.text) # Hello there, fff, lll !
```
- post请求 - 模拟登录
```python
    url = 'http://pythonscraping.com/pages/cookies/welcome.php'
    payload = {'username': 'user', 'password': 'password'}

    req = requests.post(url, data=payload)
    print(req.cookies.get_dict()) # {'username': 'user', 'loggedin': '1'}
```
- 下载图片范例一 (urlretrieve)
```python
    from urllib.request import urlretrieve
    IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
    urlretrieve(IMAGE_URL, './tmp/image1.png')
```
- 下载图片范例二 (request)
```python
    import requests
    req = requests.get(IMAGE_URL)
    with open('.image2.png', 'wb') as f:
        f.write(req.content)
```

## - bs4  (pip3 install beautifulsoup4, pip3 install lxml)
### 范例
```python
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, features="lxml")

    links = soup.find_all("a", {"target": "_blank", "href": re.compile(r"^[0-9]+$\.html")})
    links = [a["href"] for a in links] # links == html的href集合 (列表生成式)
```
