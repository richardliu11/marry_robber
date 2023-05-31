#Richard
#20230517

from selenium import webdriver
import json
from selenium.webdriver.common.by import By
import time
import requests
from PIL import Image
import ddddocr
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from seleniumwire.webdriver import Chrome
import pyautogui as pag
import time

import os

#driver = Chrome(options=Options())


def browser_initial(url):
    """"
    浏览器初始化,并打开大麦界面（未登录状态）
    """
    browser = webdriver.Chrome()
    browser.get(
        url)
    browser.maximize_window()
    return browser

def getPageGIF(driver,xpath,yzm):
    # 定位搜索按钮
    button = driver.find_element(By.XPATH,xpath)

    ActionChains(driver).context_click(button).perform()#鼠标右键
    time.sleep(1)
    if yzm==1:
        pag.click(1104, 740)  # 左键：保存
        time.sleep(1)
        pag.click(113, 403)  # 选择桌面
        pag.click(1757, 1013)  # 保存
        time.sleep(3)
    if yzm==2:
        # time.sleep(1000)
        pag.click(1034, 828)  # 左键：保存
        time.sleep(1)
        pag.click(1757, 1013)  # 保存
        time.sleep(3)






# def get_verificationGIF(browser):#方法作废
#     # url = 'https://www.gdhy.gov.cn/'
#     # browser = browser_initial(url)  # 获取img标签的src属性值
#     time.sleep(1)
#     img_url = browser.find_element(By.XPATH,
#                                    '/html/body/div[1]/div[3]/div[1]/div[3]/table/tbody/tr/td[2]/span/span[2]/img').get_attribute(
#         'src')
#     headers = {
#         'Users-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
#     }
#     # 获取图片二进制数据
#     img_data = requests.get(url=img_url).content #, headers=headers
#     with open('./node1.gif', 'wb') as fp:
#         fp.write(img_data)
#     print('验证码图片保存成功')

# 获取GIF的各帧
def getJpg(img):
    im = Image.open(img)
    imgs = []

    try:
        while True:
            current = im.tell()
            img = im.convert('RGB')

             # 可以将各个帧图片保存出来观察一下
            img_path = 'gif-to-pic/' + str(current) + '.jpg'
            img.save(img_path)

            # 将获取的图片放到列表里面，给后面合成图片用
            imgs.append(img)
            #print(imgs)
            im.seek(current + 1)
    except:
        pass
    return imgs

def conflate(img_paths):

    cage = [] # 笼子，把图片放进来合并，如果有两张就合并，一笼不容二虎
    num = 0
    for img in img_paths:
        num += 1
        cage.append(img)
        if len(cage) == 2:
            merge = Image.blend(cage[0], cage[1], 0.5) # 合并两张图片，透明度0.5
            cage = [merge] # 合并完,重置笼子
    # 把合成完的图片保存出来，只是为了看看结果，后续直接用merge识别就行了

    merge.save("cage/intact.jpg")
    os.remove("C:/Users/richard/Desktop/Common.gif")
    return merge

#识别验证码
def ivd(img):
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(img)
    return res

if __name__ == '__main__':


    imgs = getJpg("C:/Users/richard/Desktop/Common.gif")
    #print(imgs)
    #conflate(imgs)
    res = ivd(conflate(imgs))
    print(res,len(res))