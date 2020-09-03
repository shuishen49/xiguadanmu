from selenium import webdriver
import json
import time
import win32com.client
# import win32com
# import key_Controller
# from playsound import playsound
# import traceback

old_list=[]

__danmu_num=1

def speak_text(text):
    #定义一个speak_text方法，并创建形参text，用于作为接下来读取的文字
    speak =  win32com.client.Dispatch("SAPI.SpVoice")
    #创建发声对象
    speak.Speak(text)
    #使用发生对象读取文字

#填写webdriver的保存目录
room_id = input("请输入房间号:")
driver = webdriver.Chrome()
#记得写完整的url 包括http和https
# driver.get('https://live.ixigua.com/1351108/')
driver.get('https://live.ixigua.com/%s'%(room_id))
info_string="本软件由西瓜视频up主小鑫学渣开发，想获取更多高级功能请联系我。"
print("西瓜视频____小鑫学渣")
speak_text(info_string)
#首先清除由于浏览器打开已有的cookies
driver.delete_all_cookies()

with open('cookies.txt','r') as cookief:
    #使用json读取cookies 注意读取的是文件 所以用load而不是loads
    cookieslist = json.load(cookief)

    # 方法1 将expiry类型变为int
    for cookie in cookieslist:
        #并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        driver.add_cookie(cookie)


def langdu_danmu(danmu):
    #for循环提取html字典中嵌套的子字典data中嵌套的子字典room的内容赋值给text变量
    #这个html字典来自于get_danmu方法传递
    danmu=danmu.split(":",1)
    # print(len(str1))
    # yidu = False
    if len(danmu) > 1 :
        danmu_name=danmu[0][-6:]
        # danmu_name=danmu_name[-6:]
        danmu_content=danmu[1]
        # print(danmu_content)
        danmu_string=danmu_name + "说:" + danmu_content
        print(danmu_string)
        speak_text(danmu_string)


    else :


        danmu_string="欢迎"+danmu[0]
        print(danmu_string)
        speak_text(danmu_string)

while True:
    a=driver.find_elements_by_class_name("chatroom__msg")
    try:
        langdu_danmu(a[__danmu_num].text)
        __danmu_num +=1
    except Exception as e:
        time.sleep(3)

