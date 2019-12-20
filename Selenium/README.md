# Selenium 安装环境搭建
- python3
- pip install selenium （若使用Anaconda，则cmd到 Anaconda/Scripts目录下使用该命令）
- <a href="https://npm.taobao.org/mirrors/chromedriver/"> chromedriver.exe</a> 点击下载合适的版本后，放至指定目录下，用于驱动chrome
- <a href="https://selenium-python.readthedocs.io/api.html">selenium官方API</a>
- 推荐书籍:
 1. selenium2 python自动化测试 - 虫师

# DEMO
```python
''' S1 driver > S2 WebElement '''
from selenium import webdriver
from selenium.webdriver import ChromeOptions

# 防浏览器前端语言通过检测window.navigator.webdriver的值，从而被封
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(options=option)

# executable_path default ：$PATH  / Chrome x86 = chrome程序所在文件夹
driver = webdriver.Chrome(executable_path="./Chrome x86/chromedriver.exe")

# S1 driver窗口方法
    .maximize_window()  # 最大化chrome窗口
    .set_window_size(w, h)
    .refresh()          # 刷新页面
    .back()             # 后退
    .forward()          # 前进
    .execute_script(js, *args) # eg. js = "window.scrollTo(w, h) // 滚动条滚动"
    .quit() 退出

# S1 driver窗口属性
    .title              # 返回页面标题
    .current_url        # 获取当前页面的URL
    .page_source        # 返回页面源码

# S1 driver焦点方法 https://blog.csdn.net/huilan_same/article/details/52200586
    .switch_to.
            .frame(ref) # ref可以是id、name、index和WebElement，ref无需加额外标识符
            .alert # 触发页面alert后，
