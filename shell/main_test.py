#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from create_html import create_html_t
from operating_html import operating
from quality_inspection import open_quality,save_quality
import time
OPEN_URL = 'http://172.17.0.134/login'
U_NAME ="1000000"
PWD ="dj123456"

#创建谷歌对象
driver = webdriver.Chrome()
#打开url
create_html_t(driver,OPEN_URL)
#创建操作对象
op= operating(driver)
#输入input账号密码

in_u ="//*[@id='login']/div[2]/div[2]/div[2]/div[1]/input"
in_p ="//*[@id='pwd']"

op.html_login_input(U_NAME,PWD,in_u,in_p)
time.sleep(2)
#点击登录
log_x="//*[@id='login']/div[2]/div[2]/div[3]/button"
is_log=op.html_login(Keys.ENTER,log_x)
#判断是否登录
if(bool(is_log)):
    time.sleep(1)
    # 左键单击开始工作
    lef_x = "//*[@id='app']/div/div[2]/div[4]"
    op.left_click(lef_x)
    time.sleep(1)
    #功能选择做哪方面
    number=input("输入操作的脚本类型 1 质检记录:")
    if(number=='1'):
        open_quality(op)
        time.sleep(1)
        save_quality(op)
    elif(number=='2'):
        print("xxxxx")
    else:
        print("输入无效")
#driver.quit()



