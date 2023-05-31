Time_Input_Xpath = '/html/body/div[2]/div[3]/div/div[2]/table/tbody/tr/td[2]/input'
js = "document.getElementByXpath('{}').removeAttribute('readonly')".format(Time_Input_Xpath)

print(js)
