#操作html页面的类
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class operating(object):
    def __init__(self, driver):
        self.driver = driver

    # 操作输入登录用户名密码
    def html_login_input(self,u_name, pwd,x_u,x_p):
        # 输入账号
        self.input_in(x_u,u_name)
        # 输出密码
        self.input_in(x_p,pwd)
        return 0

    #点击登录操作
    def html_login(self,enter,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(enter)
            print("----------------登录成功")
            return 1
        except Exception:
             return 0
    #左键单击
    def left_click(self,xpath):
        self.driver.find_element_by_xpath(xpath).click()

    #输入框输入
    def input_in(self,xpath,content):
        self.driver.find_element_by_xpath(xpath).send_keys(content)

    # 获得文本消息
    def get_text(self,xpath):
        return self.driver.find_element_by_xpath(xpath).text

    #获取清空文本消息
    def clear_text(self, xpath):
        return self.driver.find_element_by_xpath(xpath).clear()


    # 获得消息弹框 未验证
    def get_alert_msg(self):
        return self.driver.switch_to_alert()