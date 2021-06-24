
from common import method   #从python包里导入
from testdata import data
from selenium import webdriver  #从selenium工具包导入webdriver库
import time    #导入等待时间的库
driver = webdriver.Chrome()  #webdriver与Chrome建立会话  赋值变量
driver.implicitly_wait(10)    #隐式等待 10s

#读取数据
url = data.data_1.get("url")
username = data.data_1.get("username")
password = data.data_1.get("password")
key = data.data_1.get("key")

result = method.search_fun(driver=driver,url=url,username=username,password=password,key=key)
print(result)
if key in result:
    print("搜索成功，这个单据编号是：{}".format(result))
else:
    print("搜索失败")






