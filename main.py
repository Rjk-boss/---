from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
import urllib.parse

for k in os.environ.keys():
    print(k)

today = datetime.now()
start_date = os.environ['START_DATE']
city = os.environ['CITY']
birthday = os.environ['BIRTHDAY']

app_id = os.environ["APP_ID"]
app_secret = os.environ["APP_SECRET"]

template_id = os.environ["TEMPLATE_ID"]

template_id1 = os.environ["TEMPLATE_ID1"]

user_rjk = os.environ["RJK"]

user_lc = os.environ["LC"]

user_gcm = os.environ["GCM"]

user_xyq = os.environ["XYQ"]

user_tcr = os.environ["TCR"]


def get_weather():
#   url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
#   res = requests.get(url).json()
#   weather = res['data']['list'][0]
#   return weather['weather'], math.floor(weather['temp'])
    url = "http://www.weather.com.cn/data/cityinfo/101010100.html"
    
    url = "https://api.yytianqi.com/observe?city=CH040100&key=nspuws4p7em6krcl"
    response = requests.get(url)
    response.encoding = 'utf-8'
    res = response.json()
    
#     res_str = res.decode('utf-8')
#     res_dict = json.loads(res_str)
#     result = urllib.parse.unquote(res.decode())
#     weather = urllib.parse.unquote(res_dict['weatherinfo'])
    weather = res['data']
    
    return urllib.parse.unquote(weather['tq']), urllib.parse.unquote(weather['qw']), urllib.parse.unquote(weather['sd']), urllib.parse.unquote(weather['cityName']), urllib.parse.unquote(weather['fl']), urllib.parse.unquote(weather['fx']);

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

# def get_birthday():
#  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
#  if next < datetime.now():
#    next = next.replace(year=next.year + 1)
#  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
wea, temperature, sd, cityName, fengli, fengxiang = get_weather()
data = {"weather":{"value":wea},"temperature":{"value":temperature},"words":{"value":get_words(), "color":get_random_color()}, "humidity":{"value":sd}, "CITY":{"value":cityName}, "FENG":{"value":fengli},"FENGXIANG":{"value":fengxiang}}

res = wm.send_template(user_rjk, template_id1, data)
# res5 = wm.send_template(user_rjk, template_id, data)

res1 = wm.send_template(user_lc, template_id1, data)
res2 = wm.send_template(user_gcm, template_id1, data)
res3 = wm.send_template(user_xyq, template_id1, data)
res4 = wm.send_template(user_tcr, template_id1, data)

print(">>>>>>>>>>>>>data" + str(data))
# print(res1)
