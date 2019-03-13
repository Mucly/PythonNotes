# Selenium 安装环境搭建
* python3
* pip install selenium
* <a href="https://npm.taobao.org/mirrors/chromedriver/"> chromedriver.exe</a> 下载合适的版本后，放至指定目录下，用于驱动chrome

# 简易代码demo
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    chrome_driver = webdriver.Chrome() # path形参缺省为环境变量 / 打包为exe后缺省为exe当前目录

    # S1 页面设置
    chrome_driver.maximize_window() # 最大化chrome窗口

    # S2 DOM操作
    chrome_driver.
            # 定位一个元素
                .find_element(type, "content") #
                .find_element_by_name("name")
                .find_element_by_id("id")
                .find_element_by_class_name("class")
                .find_element_by_tag_name("tag")  # 一般不用，因为重复太多
                .find_element_by_link_text("text")
                .find_element_by_partial_link_text("text") # 部分文字匹配
                .find_element_by_css_selector()
                .find_element_by_xpath()  # 万能  eg. "//div[@id='hd']/form/span/input" 也可以通过@name，@class等来查，这里的/代表路径
            # 定位一组元素
                ''' element加个s即可
                    例： .find_elements_by_name()
                    注： 返回一个数组
                '''
                # 定位后可进行操作的方法
                    .click() # 模拟鼠标点击
                    .text