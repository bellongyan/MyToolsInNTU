import requests
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1",
    "Referer": "",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
    "Origin": "http://jwxt.nit.net.cn",
    "Cache-Control": "max-age=0",
    "Content-Type": "application/x-www-form-urlencoded"
}

# cookies, 替换成自己的
cookies = {
    "ASP.NET_SessionId": ""
}
url = "http://jwxt.nit.net.cn/xscj_gc2.aspx"
params = {
    "xh": "",  # 学号
    "xm": "", # 姓名
    "gnmkdm": "N121632"
}
data = {
    "__VIEWSTATE": "",
    "__VIEWSTATEGENERATOR": "",
    "ddlXN": "",
    "ddlXQ": "",
    "Button1": ""
}


response = requests.post(url, headers=headers, cookies=cookies, params=params, data=data, verify=False)

html = response.text

# print(html)

response.close()

pattern = r'<td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td>(.*?)<\/td><td.*?>(.*?)<\/td><td.*?>(.*?)<\/td><td.*?>(.*?)<\/td>'
pattern_info = re.compile(r'<span id="pjxfjd" style="font-weight:bold;">(.*?)</span>(.*?)'
                          r'<span id="xfjdzh" style="font-weight:bold;">(.*?)</span>(.*?)'
                          r'<span id="xftj" style="font-weight:bold;">(.*?)</span>', re.S)

matches = re.findall(pattern, html)
match_info = pattern_info.search(html)

print("\t+---------------------------------+-------------+---------------+-------+")
print(f'\t|{"课程名称":<16}{" " * (16 - len("课程名称"))}', '|学分\t', '\t|\t绩点\t|', '成绩\t|')
print("\t+---------------------------------+-------------+---------------+-------+")
for match in matches:
    if match[3] == "课程名称":
        continue
    print(f"\t|{match[3]}{' ' * 2 * (16 - len(match[3]))}", '|', match[6], '\t|', match[7], '\t|', match[8], "\t|")

print("\t+---------------------------------+-------------+---------------+-------+")

if match_info:
    text = "\t|" + match_info.group(1).strip() + "；" + match_info.group(3).strip() + "\t\t\t\t|\n" \
           + "\t|" + match_info.group(5).strip() + "\t\t\t\t|"
    print(text)
print("\t+-----------------------------------------------------------------------+")
