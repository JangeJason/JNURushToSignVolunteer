from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# 设置WebDriver路径
driver_path = os.path.join(os.getcwd(), 'chromedriver-mac-arm64', 'chromedriver')  # 获取当前目录下的chromedriver路径
service = Service(driver_path)
#----------------------------------------------------------------------------------------
# 输入的数据可以通过这些变量进行修改，不能删掉引号''
name = '姓名'     #输入姓名
student_id = '学号'      #输入学号
phone_number = '电话'    #输入电话
department = '信息科学技术学院'     #输入学院
dropdown_value = 'T1'  #修改楼栋，比如 'T1' 到 'T12'，必须是大写T

field_6_index = 0  # 修改此来选择生源：0=内招生，1=外招生
field_7_index = 2  # 修改此来选择政治面貌：0=正式党员，1=预备党员，2=积极分子，3=共青团员，4=其他

# 启动浏览器
driver = webdriver.Chrome(service=service)

# 修改打开的问卷链接
driver.get('https://xscjnu.jinshuju.com/f/SWT3Ky')
#----------------------------------------------------------------------------------------
# 等待输入框加载完成
try:
    # 等待直到输入框（ID为TextInputfield_1）可用
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'TextInputfield_1'))
    )

    # 查找到输入框并输入姓名
    input_field.send_keys(name)  # 输入姓名

    # 等待第二个输入框加载完成
    input_field_2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'TextInputfield_2'))
    )
    # 输入学号
    input_field_2.send_keys(student_id)  # 输入学号
    # 等待手机号输入框加载完成（name='field_3'）
    input_field_3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'field_3'))
    )
    # 输入手机号
    input_field_3.send_keys(phone_number)  # 输入手机号

    # 等待class="ant-select-selection-search-input" 输入框加载完成
    input_field_4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'ant-select-selection-search-input'))
    )
    # 点击下拉框打开选项
    input_field_4.click()

    # 等待下拉菜单显示
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ant-select-item-option'))
    )

    # 使用 ActionChains 模拟鼠标悬停并点击动态选择的下拉项（通过name选择）
    option_to_click = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, dropdown_value))  # 使用dropdown_value变量来动态选择
    )
    actions = ActionChains(driver)
    actions.move_to_element(option_to_click).click().perform()  # 鼠标悬停并点击所选项

    # 点击name="field_4" 元素
    field_4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'field_4'))
    )
    field_4.click()

    # 等待学院输入框加载完成（name='field_5'）
    input_field_5 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'field_5'))
    )
    # 输入学院
    input_field_5.send_keys(department)  # 输入学院

    # 等待 `name="field_6"` 的元素加载完成，并选择指定索引的元素
    field_6_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.NAME, 'field_6'))
    )
    # 选择指定索引的 `field_6` 元素
    field_6_elements[field_6_index].click()

    # 等待 `name="field_7"` 的所有元素加载完成，并选择指定索引的元素
    field_7_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.NAME, 'field_7'))
    )
    # 选择指定索引的 `field_7` 元素
    field_7_elements[field_7_index].click()

    # 等待提交按钮（class='form-theme--submit-button'）加载并点击
    submit_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'form-theme--submit-button'))
    )
    # 点击提交按钮
    submit_button.click()

    # 保持浏览器打开，直到手动关闭
    input("按Enter键关闭浏览器...")

finally:
    # 关闭浏览器
    driver.quit()  # 当你按下回车键时，关闭浏览器
