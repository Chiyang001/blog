import json
import requests
print("正在检查网站链接状态")
response = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg=")
response.status_code_str = str(response.status_code)
print("网站状态码："+response.status_code_str)

num = 200
if response.status_code == num:
 while True:
  input_text = input("我：")
  answer = requests.get('http://api.qingyunke.com/api.php?key=free&appid=0&msg='+input_text+"").text
  result = json.loads(answer)
  print("Robot:"+result["content"])
else:
 print("Error!网站状态码："+response.status_code_str)