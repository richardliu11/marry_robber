from selenium import webdriver
import json
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import verificationDecode
from selenium.webdriver.common.keys import Keys

def browser_initial(url):
    """"
    浏览器初始化,并打开大麦界面（未登录状态）
    """
    browser = webdriver.Chrome()
    browser.get(
        url)
    browser.maximize_window()
    return browser

def browser_wait():
    time.sleep(30)


def input_verification(res):
    time.sleep(1)
    browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/span/span[1]/input').send_keys(res)
    browser.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[4]/input').click()
    time.sleep(3)
    browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/div[2]/a[1]/img').click()
    time.sleep(1)




def marry_book_robber_inputMessages():

    print('开始自动录入信息')
    ## 男方信息
    #市
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[4]/td[2]/select/option[4]').click()
    time.sleep(1)
    #区
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[5]/td[2]/select/option[4]').click()
    time.sleep(1)

    #街道
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[6]/td[2]/select/option[7]').click()
    time.sleep(1)

    #户籍地址
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[7]/td[2]/input').send_keys('广东省深圳市南山区东滨路10号东滨华苑14M')
    time.sleep(1)



    ##女方信息
    #市
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[4]/td[4]/select/option[4]').click()
    time.sleep(1)

    #区
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[5]/td[4]/select/option[4]').click()
    time.sleep(1)

    #街道
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[6]/td[4]/select/option[7]').click()
    time.sleep(1)

    #户籍地址
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[7]/td[4]/input').send_keys('广东省深圳市南山区东滨路10号东滨华苑14M')
    time.sleep(1)



    print('信息录入完毕')
    time.sleep(1)


    # 点击下一步
    browser.find_element(By.NAME,'Submit').click()
    time.sleep(3)

    ##选择办理网点
    # 日期
    # Time_Input_Xpath ='/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/input'
    # js = "document.getElementByXpath('{}').removeAttribute('readonly')".format(Time_Input_Xpath)
    js = 'document.getElementById("yyrq").removeAttribute("readonly")'
    print(js)
    browser.execute_script(js)
    print('执行')
    Time_Input = browser.find_element(By.ID,'yyrq')
    Time_Input.send_keys(Keys.CONTROL, 'a')
    Time_Input.send_keys('2023-06-15')
    #browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/input').click() #输入日期
    time.sleep(5)
    #browser.find_element(By.XPATH,'/html/body/div/div[3]/table/tbody/tr[6]/td[4]').click()#点击日期
    print('点击日期')
    time.sleep(5)
    #
    # 城市
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[4]/select/option[4]').click()
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[5]/a').click()

    # 点击查询 等待3秒
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[5]/a').click()
    time.sleep(3)

    # 选择龙岗区
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/table[1]/tbody/tr[5]/td[1]/input[1]').click()

    #选择下午时段
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/table[2]/tbody/tr[7]/td[1]/input').click()

    #下一步按钮
    browser.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div[5]/input[2]').click()

    time.sleep(1)
    ## 填写双方信息

    #男方
    #姓名
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[1]/td[2]/input').send_keys('刘雨辰')

    #身份证
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[4]/td[2]/input').send_keys('340302199706240435')

    #出生年月自动

    #文化程度
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[6]/td[2]/select/option[9]').click()

    #职业
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[7]/td[2]/select/option[10]').click()

    #手机号
    browser.find_element(By.XPATH,'/html/body/div[2]/form/div/div/table/tbody/tr[8]/td[2]/input').send_keys('15920017194')


    # 女方
    # 姓名
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/table/tbody/tr[1]/td[4]/input').send_keys('吴宇婷')

    # 身份证
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/table/tbody/tr[4]/td[4]/input').send_keys(
        '440882199706112743')

    # 出生年月自动

    # 文化程度
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/table/tbody/tr[6]/td[4]/select/option[9]').click()

    # 职业
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/table/tbody/tr[7]/td[4]/select/option[10]').click()

    # 手机号
    browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/table/tbody/tr[8]/td[4]/input').send_keys(
        '15817347490')
    # time.sleep(10000)
    time.sleep(1)
    for i in range(1,100):
        try:
            verificationDecode.getPageGIF(browser,
                                          '/html/body/div[2]/form/div/div/table/tbody/tr[9]/td[2]/span/span[2]/img',
                                          2)  # 保存验证码图片
            imgs = verificationDecode.getJpg("C:/Users/richard/Desktop/Common.gif")  # 验证码解码
            res = verificationDecode.ivd(verificationDecode.conflate(imgs))

            browser.find_element(By.XPATH,
                                 '/html/body/div[2]/form/div/div/table/tbody/tr[9]/td[2]/span/span[1]/input').send_keys(
                res)
            browser.find_element(By.XPATH, '/html/body/div[2]/form/div/div/div[4]/input[2]').click()

            break
        except:
            continue

    time.sleep(3)
    win = browser.switch_to.alert
    time.sleep(1)
    win.accept()
    print('完成')

    time.sleep(10000)


if __name__ == "__main__":
    #以2023年5月31日
    #龙岗区 /html/body/div[2]/div[3]/div/table[1]/tbody/tr[3]/td[1]/input[1]
    #15:30-16:00 为例子 /html/body/div[2]/div[3]/div/table[2]/tbody/tr[6]/td[1]/input

    # 南山区 /html/body/div[2]/div[3]/div/table[1]/tbody/tr[5]/td[1]/input[1]

    url = 'https://www.gdhy.gov.cn/'
    for i in range(0,100):
        try:
            print(i)
            browser = browser_initial(url)  # 重置浏览器
            verificationDecode.getPageGIF(browser,
                                      '/html/body/div[1]/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/span/span[2]/img',
                                      1)  # 保存验证码图片
            imgs = verificationDecode.getJpg("C:/Users/richard/Desktop/Common.gif")  # 验证码解码
            res = verificationDecode.ivd(verificationDecode.conflate(imgs))
            input_verification(res)
            time.sleep(1)
            break
        except:
            continue


    marry_book_robber_inputMessages()

    time.sleep(100)
