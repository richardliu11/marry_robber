# marry_robber
初始提交
> 本脚本基于selenium实现自动化结婚登记预约（深圳）
## 验证码解决方案
页面原验证码为GIF格式，由4帧图片构成，通过PIL库对图片进行拆分和重构为jpg格式
再基于ddddocr的api进行识别

## 日期选择框
日期框组件选择日期困难，send_keys无法直接使用。html描述中，可以看到readonly="readonly" ，说明日期控件不支持手动输入。
使用webdriver，驱动JS，对html页面属性进行更改，就可以不可录入的日期控件，录入日期格式数据了。

## web弹出提示框
web弹出提示框无法定位，需要使用switch_to.alert切换至提示框web组件
win = browser.switch_to.alert
time.sleep(1)
win.accept()
