import tkinter as tk

import requests
import re

# 创建窗口
window = tk.Tk()

# 设置窗口大小
window.geometry("600x400")

# 设置窗口标题
window.title("小红书无水印图片下载")

# 创建标签和输入框
input_label = tk.Label(window, text="输入小红书笔记链接")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()


# 定义按钮的事件处理函数
def button_click():
    headers = {
        "authority": "t2.xiaohongshu.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "cache-control": "max-age=0",
        "sec-ch-ua": "^\\^Chromium^^;v=^\\^110^^, ^\\^Not",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
        "Referer": "https://www.xiaohongshu.com/",
        "Origin": "https://www.xiaohongshu.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63",
        "if-modified-since": "Tue, 28 Feb 2023 15:04:33 GMT",
        "if-none-match": "^\\^f3d61f43b5bcaca59803afc74eb22455^^",
        "referer": "https://www.xiaohongshu.com/",
        "content-type": "text/plain",
        "origin": "https://www.xiaohongshu.com",
        "x-b3-traceid": "6d63dc83520d7ba3",
        "x-s": "12sl1gFW1BaJOg4JOlvKOjvCsj5psjcis6TpZjwUsiT3",
        "x-t": "1678115684626",
        "access-control-request-headers": "x-b3-traceid,x-s,x-t",
        "access-control-request-method": "GET",
        "x-s-common": "2UQAPsHC+aIjqArjwjHjNsQhPsHCH0rjNsQhPaHCH0P1PshIHjIj2eHjwjQgynEDJ74AHjIj2ePjwjQhyoPTqBPT49pjHjIj2ecjwjHlN0H1PaHVHdWMH0ijP/W9G0q9GnHhP0+0q0WE4o4jq9IMPBH7+BTI80+DP9lEG0QTJdk0PfPMPeZIPeHh+0WU+aHVHdW9H0il+0qhP/rM+/DEweDMNsQh+UHCHSkszD+yy0SPqFHF4d+V4DTOcD8e/9il/oPUGppyySzNq9knaDRk4MLl87GAHjIj2eWjwjQQPAYUaBzdq9k6qB4Q4fpA8b878FSet9RQzLlTcSiM8/+n4MYP8F8LagY/P9Ql4FpUzfpS2BcI8nT1GFbC/L88JdbFyrSiafp/8DMra7pFLDDAa7+8J7QgabmFz7Qjp0mcwp4fanD68p40+fp8qgzELLbILrDA+9p3JpHlPDMMnLSi/9pr8fzAyDQ++LYl49IUqgcMc0mrJFShtMmozBD6qM8FyFSh8o+h4g4U+obFyLS3qDRQyaRAy9+02rSe/BzQPFRSPb8FJeHEqgbIaLkA8oZM8nkn4FMQynpAy7p7GDYl4BRP4gclLrSN8/8TzMmQ4dmLaLpB+f4n4AYtqgq7a/+C2fp/+npn4gzha/+DqAbc494QybzHanTiGfR687+/cLS3GdPMqFzM4okyz08S8S4BL7md8npgGFSSagYw8p+M4oSQyBpSngbFPB4VzDMOcD8oaL+9qAbn49zyze+A2rby/DSkzBbQypZFtASrpLS92dSla/YOanSCyjRM4e+Q2ecA+o+POaHVHdWEH0iMw/DMPArhPjIj2erIH0iUKc==",
        "x-sign": "X8efe40ac90c7df2a07c0c5a1ffa73c41"
    }
    cookies = {
        "webBuild": "",
        "xsecappid": "",
        "a1": "",
        "webId": "",
        "gid": "",
        "gid.sign": "",
        "web_session": "",
        "xhsTracker": "",
        "xhsTracker.sig": "",
        "websectiga": "",
        "sec_poison_id": "",
        "extra_exp_ids": "",
        "extra_exp_ids.sig": ""
    }
    # 获取输入框中的文本
    url = input_entry.get()
    response = requests.get(url, headers=headers, cookies=cookies)
    html = response.text

    # 从HTML文件中提取script标签的内容
    script_content = re.search("<script>window.__INITIAL_STATE__=({.*?})</script>", html, re.S).group(1)

    # 从script标签内容中找到所有的traceId
    trace_ids = re.findall(r'"traceId":"(.*?)"', script_content)

    # 将traceid和https://sns-img-bd.xhscdn.com/连接起来
    urls = ["https://sns-img-bd.xhscdn.com/" + trace_id for trace_id in trace_ids]

    # 下载图片
    for url in urls:
        response = requests.get(url)
        with open("./pic/" + url.split("/")[-1] + ".jpg", "wb") as f:
            f.write(response.content)
        response.close()

        # 在输出框中显示文本
        output_text.insert(tk.END, url + "下载完成\n")

        # 清空输入框
        input_entry.delete(0, tk.END)


# 创建确认按钮
confirm_button = tk.Button(window, text="开始下载", command=button_click)
confirm_button.pack()

# 创建输出框
output_label = tk.Label(window, text="下载结果")
output_label.pack()
output_text = tk.Text(window)
output_text.pack()

# 运行窗口
window.mainloop()
