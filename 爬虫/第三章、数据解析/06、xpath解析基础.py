from lxml import etree

# 实例化好一个etree对象，且将被解析的源码加载到了该对象中
parser = etree.HTMLParser(encoding='utf-8')
tree = etree.parse('huazhuangping.html', parser=parser)

# ‘/’:表示从根节点开始定位，表示一个层级
# r = tree.xpath('/html/head/title')
# '//'：表示的是多个层级，可以表示从任意位置开始定位
# r = tree.xpath('/html//title')
# print(tree.xpath('//title'))

# 属性定位：//div[@class='hzbtabs'] tagName[@attrName='attrValue']
print(tree.xpath('//div[@class="hzbtabs"]'))
# 索引定位：索引从1开始定位
print(tree.xpath('//div[@class="hzbtabs"]/span[3]'))
# 取文本内容：/text()   //text()
print(tree.xpath('//div[@class="hzbtabs"]/span[3]/text()')[0])
# 取属性值：/@attrName
print(tree.xpath('//div[@class="hzbtabs"]/span[3]/@id')[0])
