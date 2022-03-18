from time import sleep
from selenium import webdriver

# 实例化一个浏览器对象（传入浏览器的驱动程序）
browser = webdriver.Edge(executable_path='./msedgedriver.exe')
# 让浏览器发起一个指定url对应请求
browser.get('http://qzone.qq.com')
# 窗口最大化
browser.maximize_window()

# 定位到标签的iframe中
browser.switch_to.frame('login_frame')
a_tag = browser.find_element_by_id('switcher_plogin')
a_tag.click()

# 定位到用户名和密码
userName_tag = browser.find_element_by_id('u')
userPwd_tag = browser.find_element_by_id('p')

userName_tag.send_keys('2458294937')
sleep(1)
userPwd_tag.send_keys('panzerjkl339')
sleep(1)

login_btn = browser.find_element_by_id('login_button')
login_btn.click()

sleep(5)
browser.quit()