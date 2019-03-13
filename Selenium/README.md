# Selenium 安装环境搭建
- python3
- pip install selenium
- <a href="https://npm.taobao.org/mirrors/chromedriver/"> chromedriver.exe</a> 点击下载合适的版本后，放至指定目录下，用于驱动chrome
- <a href="https://selenium-python.readthedocs.io/api.html">selenium官方API</a>
- 推荐书籍:
 1. selenium2 python自动化测试

# 简易代码demo
    from selenium import webdriver
    from selenium.webdriver.common.by import By

    chrome_driver = webdriver.Chrome() # path形参缺省为环境变量 / 打包为exe后缺省为exe当前目录

    # 页面接口
    chrome_driver.maximize_window() # 最大化chrome窗口
                 .title             # 返回页面标题
                 .current_url       # 获取当前页面的URL
                 .page_source       # 返回页面源码

    # 元素定位接口
    chrome_driver.
            # 定位一个元素
                 .find_element(ByType, "content")            # 原始方式 eg. find_element(By.ID, "name")
                 .find_element_by_name("name")
                 .find_element_by_id("id")
                 .find_element_by_class_name("class")
                 .find_element_by_tag_name("tag")            # 一般不用，因为重复太多
                 .find_element_by_link_text("text")
                 .find_element_by_partial_link_text("text")  # 部分文字匹配
                 .find_element_by_css_selector()
                 .find_element_by_xpath()                    # xpath方式  eg. "//div[@id='hd']/form/span/input" div可以替换为*，也可以去掉; id可以替换为name、class等; 范例中的/代表路径;
            # 定位一组元素
            ''' 上面的element加个s即可
                注： 返回一个数组
            '''
            # 元素常规操作接口
            from selenium.webdriver.common.keys import Keys
                    # - 点击操作
                    .click() # 模拟鼠标点击
                    .double_click()
                    # - 其他
                    .clear()
                    .send_keys(k1[, k2]) # 送键值，文本范例：u"中文" ； 按键范例：Keys.RETURN == 回车按键，更多可参见官方API一章
                    .submit()
            # 接口获取值
                    .size
                    .text
                    .tag_name
                    .get_attribute("attr_name") # 获取属性值 eg. get_attribute('name')
                    .location                   # 获取元素坐标
                    .is_displayed()             # 设置该元素是否可见
                    .is_enabled()               # 是否被使用
                    .is_selected()              # 是否被选中
    # ActionChains动作链类 操作，主要用于复杂动作
    from selenium.webdriver.common.action_chains import ActionChains
    ActionChains(chrome_driver).
                                # - 点击
                                .context_click(elem)     # 右键elem
                                .click_and_hold(elem)    # 左键按住elem不松开
                                .double_click(elem)      # 双击elem
                                # - 移动
                                .move_to_element(elem)   # 鼠标移动到一个元素上
                                .drag_and_drop(source_elem, target_elem) # 将source元素拖动到target元素上
                                .drag_and_drop_by_offset(elem, x, y)
                                .move_by_offset(x, y)
                                # - 按键
                                .key_down(k, elem)
                                .key_up(k, elem)
                                # - 其他
                                .release()               # 释放鼠标
                                .perform()               # 按序执行ActionChains中的上述行为
