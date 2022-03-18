from time import sleep
from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge
from selenium.webdriver import ActionChains
from chaojiying import getCodeText
from PIL import Image

edge_options = EdgeOptions()
edge_options.use_chromium = True
# 实现规避检测(否则滑块验证后也无法登录)
edge_options.add_argument('--disable-blink-features=AutomationControlled')

# 实例化一个浏览器对象（传入浏览器的驱动程序）
browser = Edge(executable_path='./msedgedriver.exe', options=edge_options)
# 让浏览器发起一个指定url对应请求
browser.get('https://kyfw.12306.cn/otn/resources/login.html')
# 窗口最大化
browser.maximize_window()

# 定位到账号密码登录（默认时二维码登录）
a_tag = browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a')
a_tag.click()
sleep(2)

# 直接截屏验证码标签
codeImage_tag = browser.find_element_by_xpath('//*[@id="J-loginImg"]')
codeImage_screen = codeImage_tag.screenshot('code.png')

# 截屏保存
# browser.save_screenshot('screen.png')

# # 确定验证码图片对应的左上角和右下角坐标（确定裁剪区域）
# codeImage = browser.find_element_by_xpath('//*[@id="J-loginImg"]')
# # 获取左上角坐标
# location = codeImage.location
# print(location)
# # 获取图片尺寸
# size = codeImage.size
# print(size)
#
# rectangle = (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height'])
# Image.open('screen.png').crop(rectangle).save('./code.png')
sleep(3)
code_locations = getCodeText('code.png', 9004)

# 存储即将被点击的点的坐标
all_points_list = []
list1 = code_locations.split('|')
for i in range(len(list1)):
    point_list = []
    x = int(list1[i].split(',')[0])
    y = int(list1[i].split(',')[1])
    point_list.append(x)
    point_list.append(y)
    all_points_list.append(point_list)

print(all_points_list)

# 遍历列表，使用动作链对每一个列表元素对应的点坐标进行点击操作
action = ActionChains(browser)
for point in all_points_list:
    x = point[0]
    y = point[1]
    ActionChains(browser).move_to_element_with_offset(codeImage_tag, x, y).click().perform()
    sleep(0.5)

browser.find_element_by_xpath('//*[@id="J-userName"]').send_keys('15671378317')
browser.find_element_by_xpath('//*[@id="J-password"]').send_keys('panzerjkl520')
sleep(3)

# 点击登录按钮
browser.find_element_by_xpath('//*[@id="J-login"]').click()
sleep(3)

# 获取滑块
span_out = browser.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
span_in = browser.find_element_by_xpath('//*[@id="nc_1_n1z"]')
sleep(3)

# 滑块验证
action.click_and_hold(span_in)
action.move_by_offset(span_out.size['width'] - span_in.size['width'], 0).perform()

action.release().perform()

sleep(2)
browser.quit()