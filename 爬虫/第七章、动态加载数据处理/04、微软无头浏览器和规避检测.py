from msedge.selenium_tools import EdgeOptions
from msedge.selenium_tools import Edge

edge_options = EdgeOptions()
edge_options.use_chromium = True
# 设置为无可视化界面
edge_options.add_argument('headless')
# 实现规避检测
edge_options.add_argument('--disable-blink-features=AutomationControlled')

# 实例化一个浏览器对象（传入浏览器的驱动程序）
bro = Edge(executable_path='./msedgedriver.exe', options=edge_options)
# 让浏览器发起一个指定url对应请求
bro.get('http://www.baidu.com')
print(bro.title)

bro.quit()