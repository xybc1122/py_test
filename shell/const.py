OPEN_URL = 'http://172.17.0.134/login'
U_NAME ="1000000"
PWD ="dj123456"




#输入账号密码
IN_U_X ="//*[@id='login']/div[2]/div[2]/div[2]/div[1]/input"
IN_P_X ="//*[@id='pwd']"
#点击登录
LOG_X="//*[@id='login']/div[2]/div[2]/div[3]/button"
# 左键单击开始工作
LEF_S_X = "//*[@id='app']/div/div[2]/div[4]"

# 左键仓库管理
LEF_W_X = "//*[@id='djweb-console']/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[7]"
###################################################质检#####################################################




# 左键质检记录
Q_LEF_Q_X = "//*[@id='djweb-console']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div[1]"

#点击打开新增质检
Q_LEF_Q_S_X = "//*[@id='router']/div[2]/div/div[1]/div[1]/div/button[1]/span"

# 输入订单号
Q_IN_O_X = "//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[1]/div[1]/div/div/div/div/div/input"

#获取质检输入订单号第一个异常消息
Q_G_ORD_M_X = "/html/body/div[3]/p"

# 点击不良原因
Q_LEF_B_X = "//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/div/div/div/span/span/i"

# 选择下拉框选项
Q_LEF_O_X = "/ html / body / div[3] / div[1] / div[1] / ul / li[1] / span"

# 输入不良数量
Q_IN_B_Q_X= "// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[3] / " \
        "div[1] / div / div / div / div / div / input"

# 点击处理方案
Q_LEF_P_P_X = "//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[5]/div[1]/div/div/div/div/input"
# 选择处理方案
Q_LEF_O_P_P_X = "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span"


#输入备注
Q_IN_R_X="// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[6] " \
         "/ div / div / div / div / div / div[1] / textarea"

# 点击责任部门/责任人
Q_LEF_RES_R_X = "// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[5] " \
        "/ div[ 2] / div / div / div / div / div / div / input"

# 选择公司
Q_LEF_RES_C_X = "// *[ @ id = 'router'] / div[4] / div / div / div[2] / div / div / div / div[1] / div / span[2] / span"

# 点击选择 人
Q_LEF_RES_P_X="// *[ @ id = '914aec1426fa444ba226ccf8ad95031e']"

#点击选择责任人确认
Q_LEF_R_C_X="// *[ @ id = 'router'] / div[4] / div / div / div[3] / div / div / button[2] / span"

# 点击质检新增确认
Q_C_X = "// *[ @ id = 'router'] / div[3] / div / div / div[3] / div / button[2] / span"

# 获取点击确定新增质检异常msg
Q_G_C_M_X = "/ html / body / div[5] / p"