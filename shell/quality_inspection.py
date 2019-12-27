#质检
import time_util
import const


#打开质检
def open_quality(op):
    print("打开质检")
    # 左键仓库管理
    op.left_click(const.LEF_W_X)
    time_util.sleep_1()
    # 左键质检记录
    op.left_click(const.Q_LEF_Q_X)
    time_util.sleep_2()
    #新增质检
    save_quality(op)

#新增质检
def save_quality(op):
    q_ord = "12345678910"  # 初始错误订单
    print("打开新增质检")
    #点击打开新增质检
    op.left_click(const.Q_LEF_Q_S_X)
    time_util.sleep_2()
    #输入订单号
    op.input_in(const.Q_IN_O_X,q_ord)
    time_util.sleep_2()
    #开始各种逻辑验证
    #1第一个异常 获取错误msg消息框
    q_text_msg=op.get_text(const.Q_G_ORD_M_X)
    if('请输入正确的订单编号'==q_text_msg):
        print("-----此条不符合需求用列 记录日志:"+q_ord)

    q_ord="CGRN201910122359163457" #正确订单号
    #清空文本消息
    op.clear_text(const.Q_IN_O_X)
    # 输入正确订单号
    op.input_in(const.Q_IN_O_X, q_ord)
    time_util.sleep_2()
    #点击不良原因
    op.left_click(const.Q_LEF_B_X)
    time_util.sleep_2()
    #选择下拉框选项
    op.left_click(const.Q_LEF_O_X)
    time_util.sleep_2()
    #输入不良数量
    op.input_in(const.Q_IN_B_Q_X, 1)
    time_util.sleep_2()
    #点击处理方案
    op.left_click(const.Q_LEF_P_P_X)
    time_util.sleep_2()
    #选择处理方案
    op.left_click(const.Q_LEF_O_P_P_X)
    time_util.sleep_2()
    #输入备注
    op.input_in(const.Q_IN_R_X, "自动化测试")
    time_util.sleep_2()
    #点击责任人
    op.left_click(const.Q_LEF_RES_R_X)
    time_util.sleep_2()
    #选择公司
    op.left_click(const.Q_LEF_RES_C_X)
    time_util.sleep_2()
    #选择人
    op.left_click(const.Q_LEF_RES_P_X)
    time_util.sleep_2()
    #点击选择责任人确认
    op.left_click(const.Q_LEF_R_C_X)
    time_util.sleep_2()
    #点击最终的确认
    op.left_click(const.Q_C_X)
    time_util.sleep_2()
    #获取新增质检异常msg
    q_text_msg = op.get_text(const.Q_G_C_M_X)  # 获取错误msg消息框
    if ('请输入正确的订单编号' == q_text_msg):
        print("-----此条不符合需求用列 记录日志")
