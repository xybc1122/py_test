#质检
import time

#打开质检
def open_quality(op):
    print("打开质检")
    # 左键仓库管理
    w_x = "//*[@id='djweb-console']/div/div[1]/div/div[2]/div[2]/div/div[1]/div/div[1]/div/div[7]"
    op.left_click(w_x)
    time.sleep(1)
    # 左键质检记录
    q_x = "//*[@id='djweb-console']/div/div[1]/div/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[1]/div/div[2]/div[1]"
    op.left_click(q_x)

#新增质检
def save_quality(op):
    print("打开新增质检")
    #点击打开新增质检
    q_s_x = "//*[@id='router']/div[2]/div/div[1]/div[1]/div/button[1]/span"
    op.left_click(q_s_x)
    #输入订单号
    q_in="//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[1]/div[1]/div/div/div/div/div/input"
    q_ord="12345678910" #错误订单
    op.input_in(q_in,q_ord)
    time.sleep(2)
    #开始各种逻辑验证
    #获取弹框消息
    q_ord_v="/html/body/div[3]/p"
    q_text_msg=op.get_text(q_ord_v) #获取错误msg消息框
    if('请输入正确的订单编号'!=q_text_msg):
        print("-----此条不符合需求用列 记录日志")
    q_ord="CGRN201910172359145591" #正确订单号
    #清空文本消息
    op.clear_text(q_in)
    # 输入正确订单号
    op.input_in(q_in, q_ord)
    time.sleep(1)
    #点击不良原因
    b_r_x="//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[2]/div[1]/div/div/div/div/span/span/i"
    op.left_click(b_r_x)
    time.sleep(1)
    #选择下拉框选项
    b_r_o_x="/ html / body / div[3] / div[1] / div[1] / ul / li[1] / span"
    op.left_click(b_r_o_x)
    time.sleep(1)
    #输入不良数量
    b_r_q="// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[3] / " \
                               "div[1] / div / div / div / div / div / input"
    op.input_in(b_r_q, 10)
    time.sleep(1)
    #点击处理方案
    t_p_x="//*[@id='router']/div[3]/div/div/div[2]/div/div/div/form/div/div[5]/div[1]/div/div/div/div/input"
    op.left_click(t_p_x)
    time.sleep(1)
    #选择处理方案
    t_p_o_x = "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span"
    op.left_click(t_p_o_x)
    time.sleep(1)
    #输入备注
    r_x="// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[6] " \
         "/ div / div / div / div / div / div[1] / textarea"
    op.input_in(r_x, "自动化测试")
    time.sleep(1)
    #选择责任人
    res_x="// *[ @ id = 'router'] / div[3] / div / div / div[2] / div / div / div / form / div / div[5] " \
          "/ div[ 2] / div / div / div / div / div / div / input"
    op.left_click(res_x)
    time.sleep(1)
    #选择公司
    res_c="// *[ @ id = 'router'] / div[4] / div / div / div[2] / div / div / div / div[1] / div / span[2] / span"
    op.left_click(res_c)
    time.sleep(1)
    #选择人
    res_p="// *[ @ id = '914aec1426fa444ba226ccf8ad95031e']"
    op.left_click(res_p)
    time.sleep(1)
    #点击确认
    c_conf="// *[ @ id = 'router'] / div[4] / div / div / div[3] / div / div / button[2] / span"
    op.left_click(c_conf)
    time.sleep(1)
    #点击最终的确认
    c_conf="// *[ @ id = 'router'] / div[3] / div / div / div[3] / div / button[2] / span"
    op.left_click(c_conf)