
import time

import requests
from selenium import webdriver  # 网页自动化
from flask import Flask, request


app = Flask(__name__)

login_url = "https://auth.sztu.edu.cn/idp/authcenter/ActionAuthChain?entityId=jiaowu"  # 登录页面
base_url = "https://jwxt.sztu.edu.cn/jsxsd/framework/xsMain.jsp"  # 首页
course_url = "https://jwxt.sztu.edu.cn/jsxsd/xskb/xskb_list.do"  # 课表
headers = {
    "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/91.0.4472.124 Safari/537.36",
    "Origin": "https://jwxt.sztu.edu.cn"
}  # 用户代理，模拟机器类型
cookies = {}


@app.route("/login", methods=['POST'])
def login():
    print("request.json: ", request.json)

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(login_url)

        driver.find_element_by_id('j_username').clear()  # 清空输入框
        driver.find_element_by_id('j_username').send_keys(request.json['school_id'])  # 自动敲入用户名

        driver.find_element_by_id('j_password').clear()  # 清空输入框
        driver.find_element_by_id('j_password').send_keys(request.json['password'])  # 自动敲入密码

        driver.find_element_by_id('loginButton').click()

        time.sleep(1)
        driver.get(base_url)
        for cookie in driver.get_cookies():
            cookies[cookie['name']] = cookie['value']
        print("cookies: ", cookies)

    finally:
        driver.quit()

    if not cookies:
        return {
                   "error": "登录失败，账号或密码错误",
               }, 403

    return {
        "cookies": cookies
    }


def get(url):
    return requests.get(url, headers=headers, timeout=2, cookies=cookies, verify=False)


def post(url, data):
    return requests.post(url, headers=headers, timeout=2, cookies=cookies, verify=False, data=data)