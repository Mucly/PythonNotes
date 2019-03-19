# Selenium 安装环境搭建
- python3
- pip install selenium
- <a href="https://npm.taobao.org/mirrors/chromedriver/"> chromedriver.exe</a> 点击下载合适的版本后，放至指定目录下，用于驱动chrome
- <a href="https://selenium-python.readthedocs.io/api.html">selenium官方API</a>
- 推荐书籍:
 1. selenium2 python自动化测试 - 虫师

# DEMO
```python
''' S1 driver > S2 WebElement '''
from selenium import webdriver

driver = webdriver.Chrome() # default $PATH  / exe_default: current path

# S1 driver窗口方法
    .maximize_window()  # 最大化chrome窗口
    .set_window_size(w, h)
    .refresh()          # 刷新页面
    .back()             # 后退
    .forward()          # 前进
    .execute_script(js, *args) # eg. js = "window.scrollTo(w, h) // 滚动条滚动"

# S1 driver窗口属性
    .title              # 返回页面标题
    .current_url        # 获取当前页面的URL
    .page_source        # 返回页面源码

# S1 driver焦点方法 https://blog.csdn.net/huilan_same/article/details/52200586
    .switch_to.
            .frame(ref) # ref可以是id、name、index和WebElement，ref无需加额外标识符
            .alert # 触发页面alert后，使用此方法会生成一个Alert类对象; 也可通过构造Alert类，eg. Alert(driver)
                .accept()                   # 确认
                .dismiss()                  # 取消
                .authenticate(usrn, pwd)    # 身份验证
                .send_keys(keysToSend)      # 发送文本
                .text                       # 返回alert文本内容
                .default_content()          # 切回主文档
                .parent_frame()             # 从子frame切到父frame

# S1 driver页面元素定位方法，并返回一个WebElement
from selenium.webdriver.common.by import By
    .find_element(By .ID / .NAME / .CLASS_NAME / .TAG_NAME / .LINK_TEXT / # 万能方式 eg. find_element(By.ID, id)
        .PARTIAL_LINK_TEXT / .XPATH / .CSS_SELECTOR, content)
    .find_element_by_name(name)
    .find_element_by_id(id)
    .find_element_by_class_name(class)
    .find_element_by_tag_name(tag)              # 一般不用，因为重复太多
    .find_element_by_link_text(text)
    .find_element_by_partial_link_text(text)    # 部分文字匹配
    .find_element_by_xpath(xpath)               # xpath，详见 http://www.runoob.com/xpath/xpath-tutorial.html
    .find_element_by_css_selector(css_selector) # css选择器，详见 http://www.runoob.com/cssref/css-selectors.html

# S1 driver元素定位一组元素，并返回一个WebElement数组
''' 上面的element加个s即可 '''

# S2 WebElement操作方法
    from selenium.webdriver.common.keys import Keys
    .click() # 模拟鼠标点击
    .double_click()
    .clear()
    .send_keys(k1[, k2]) # 送键值，文本范例：u"中文" ； 按键范例：Keys.RETURN
    .submit()

# S2 WebElement属性/方法
    .size
    .text
    .tag_name
    .get_attribute(attr_name) # 获取属性值 eg. get_attribute('name')
    .location                   # 获取元素坐标
    .is_displayed()             # 设置该元素是否可见
    .is_enabled()               # 是否被使用
    .is_selected()              # 是否被选中

# S0 ActionChains动作链类 操作，主要用于复杂动作
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).
                    .context_click(elem)     # 右键elem
                    .click_and_hold(elem)    # 左键按住elem不松开
                    .double_click(elem)      # 双击elem
                    .move_to_element(elem)   # 鼠标移动到一个元素上
                    .drag_and_drop(source_elem, target_elem) # 将source元素拖动到target元素上
                    .drag_and_drop_by_offset(elem, x, y)
                    .move_by_offset(x, y)
                    .key_down(k, elem)
                    .key_up(k, elem)
                    .release()               # 释放鼠标
                    .perform()               # 按序执行ActionChains中的上述行为
```
