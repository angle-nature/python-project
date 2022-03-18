from time import sleep
from selenium import webdriver

# 实例化一个浏览器对象（传入浏览器的驱动程序）
browser = webdriver.Edge(executable_path='./msedgedriver.exe')
# 让浏览器发起一个指定url对应请求
browser.get('http://taobao.com')
# 窗口最大化
browser.maximize_window()

# 标签定位
search = browser.find_element_by_id('q')
# 标签交互
search.send_keys("娃娃")
sleep(1)

# 执行一组js程序
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
sleep(2)

# 点击搜索按钮 先定位到搜索按钮
btn = browser.find_element_by_css_selector('.btn-search')
btn.click()

# 回退 前进
browser.back()
browser.forward()

sleep(5)
browser.quit()