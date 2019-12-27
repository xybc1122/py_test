#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from create_html import create_html_t
from operating_html import operating
from quality_inspection import open_quality
import const
import time_util
# import requests
#
# r = requests.get('http://172.17.0.134/djsupplier/firstPage/getWebFirstPageAll.do')
# print(type(r.cookies))
#
# cookies = requests.utils.dict_from_cookiejar(r.cookies)
# print(cookies)
#
#创建谷歌对象
driver = webdriver.Chrome()
#打开url
create_html_t(driver,const.OPEN_URL)
#创建操作对象
op= operating(driver)
#输入账号密码
op.html_login_input(const.U_NAME,const.PWD,const.IN_U_X,const.IN_P_X)
time_util.sleep_2()
#登录
is_log=op.html_login(Keys.ENTER,const.LOG_X)
#判断是否登录
if(bool(is_log)):
    #print(driver.get_cookies())
    # 左键单击开始工作
    op.left_click(const.LEF_S_X)
    time_util.sleep_1()
    #功能选择做哪方面
    number=input("输入操作的脚本类型 1 质检记录:")
    if(number=='1'):
        open_quality(op)
    elif(number=='2'):
        print("xxxxx")
    else:
        print("输入无效")
driver.close()



