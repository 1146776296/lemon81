import time

#打开网页函数
def open_page(driver,url):
    driver.get(url)   #打开URL网页地址
    driver.maximize_window()    #最大化窗口


#登录函数
def login_fun(driver,username,password):
    driver.find_element_by_id("username").send_keys(username)  #代码找到元素，进行输入内容的操作
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()  #通过id找到按钮，进行点击操作



#搜索函数
def search_fun(driver,url,username,password,key):
    open_page(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//div[@id='leftMenu']//span[text()='零售出库']").click()
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id") #通过定位零售出库的上一级，获取iframe的id
    id_iframe = id + "-frame"  #通过字符串的拼接，得到iframe的id
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()  #点击查询按钮
    time.sleep(1)   #隐式等待+强制等待--当隐式等待不生效时，可以再加一个强制等待
    #页面里的表格，标签语言：tr==行，td==列
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']").text
    return num



