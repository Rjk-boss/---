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

template_id_baofu = os.environ["TEMPLATE_ID_BAOFU"]

template_id_friend = os.environ["TEMPLATE_ID_FRIEND"]

user_rjk = os.environ["RJK"]

user_lc = os.environ["LC"]

user_gcm = os.environ["GCM"]

user_xyq = os.environ["XYQ"]

user_tcr = os.environ["TCR"]


def get_cq_weather():
    # 重庆天气
    url_cq = "https://api.yytianqi.com/observe?city=CH040100&key=nspuws4p7em6krcl"
    response = requests.get(url_cq,verify=False)
    response.encoding = 'utf-8'
    res = response.json()
    weather = res['data']
    
    return urllib.parse.unquote(weather['tq']), urllib.parse.unquote(weather['qw']), urllib.parse.unquote(weather['sd']), urllib.parse.unquote(weather['cityName']), urllib.parse.unquote(weather['fl']), urllib.parse.unquote(weather['fx']);

def get_zj_weather():
    # 镇江
    url_zj = "https://api.yytianqi.com/observe?city=CH190301&key=nspuws4p7em6krcl"
    response = requests.get(url_zj,verify=False)
    response.encoding = 'utf-8'
    res = response.json()
    weather = res['data']
    
    return urllib.parse.unquote(weather['tq']), urllib.parse.unquote(weather['qw']), urllib.parse.unquote(weather['sd']), urllib.parse.unquote(weather['cityName']), urllib.parse.unquote(weather['fl']), urllib.parse.unquote(weather['fx']);

def get_xz_weather():
    # 徐州
    url_xz = "https://api.yytianqi.com/observe?city=CH190801&key=nspuws4p7em6krcl"
    response = requests.get(url_xz,verify=False)
    response.encoding = 'utf-8'
    res = response.json()
    weather = res['data']
    
    return urllib.parse.unquote(weather['tq']), urllib.parse.unquote(weather['qw']), urllib.parse.unquote(weather['sd']), urllib.parse.unquote(weather['cityName']), urllib.parse.unquote(weather['fl']), urllib.parse.unquote(weather['fx']);


def get_cs_weather():
    # 长沙
    url_cs = "https://api.yytianqi.com/observe?city=CH250101&key=nspuws4p7em6krcl"
    response = requests.get(url_cs,verify=False)
    response.encoding = 'utf-8'
    res = response.json()
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
#   words = requests.get("https://api.shadiao.pro/chp")
# 舔狗文学接口
#   words = requests.get("https://apis.tianapi.com/tiangou/index?key=a8a3b86b788884d47ec3436567ec073f")
#     if words.status_code != 200:
#         return get_words()
#       return words.json()['result']['content']
# 随机获取一句话
  words = requests.get("https://v1.hitokoto.cn/")
  if words.status_code != 200:
    return get_words()
  return words.json()['hitokoto']

def get_words1():
#   words = requests.get("https://api.shadiao.pro/chp")
# 舔狗文学接口
#   words = requests.get("https://apis.tianapi.com/tiangou/index?key=a8a3b86b788884d47ec3436567ec073f")
#     if words.status_code != 200:
#         return get_words1()
#       return words.json()['result']['content']
# 随机获取一句话
  words = requests.get("https://v1.hitokoto.cn/")
  if words.status_code != 200:
    return get_words()
  return words.json()['from']

def get_words2():
#   words = requests.get("https://api.shadiao.pro/chp")
# 舔狗文学接口
#   words = requests.get("https://apis.tianapi.com/tiangou/index?key=a8a3b86b788884d47ec3436567ec073f")
#     if words.status_code != 200:
#         return get_words()
#       return words.json()['result']['content']
# 随机获取一句话
  words = requests.get("https://v1.hitokoto.cn/")
  if words.status_code != 200:
    return get_words2()
  return words.json()['from_who']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

# 重庆
wm = WeChatMessage(client)
wea, temperature, sd, cityName, fengli, fengxiang = get_cq_weather()
data_cq = {"weather":{"value":wea},"temperature":{"value":temperature},"words":{"value":str(get_words()) +'--' +  str(get_words1()) +'('+str(get_words2()) + ')', "color":get_random_color()}, "humidity":{"value":sd}, "CITY":{"value":cityName}, "FENG":{"value":fengli},"FENGXIANG":{"value":fengxiang}}

# 镇江
wea, temperature, sd, cityName, fengli, fengxiang = get_zj_weather()
data_zj = {"weather":{"value":wea},"temperature":{"value":temperature},"words":{"value":str(get_words()) +'--' +  str(get_words1()) +'('+str(get_words2()) + ')', "color":get_random_color()}, "humidity":{"value":sd}, "CITY":{"value":cityName}, "FENG":{"value":fengli},"FENGXIANG":{"value":fengxiang}}

# 徐州
wea, temperature, sd, cityName, fengli, fengxiang = get_xz_weather()
data_xz = {"weather":{"value":wea},"temperature":{"value":temperature},"words":{"value":str(get_words()) +'--' +  str(get_words1()) +'('+str(get_words2()) + ')', "color":get_random_color()}, "humidity":{"value":sd}, "CITY":{"value":cityName}, "FENG":{"value":fengli},"FENGXIANG":{"value":fengxiang}}

# 长沙
wea, temperature, sd, cityName, fengli, fengxiang = get_cs_weather()
data_cs = {"weather":{"value":wea},"temperature":{"value":temperature},"words":{"value":str(get_words()) +'--' +  str(get_words1())  +'('+str(get_words2()) + ')', "color":get_random_color()}, "humidity":{"value":sd}, "CITY":{"value":cityName}, "FENG":{"value":fengli},"FENGXIANG":{"value":fengxiang}}

res = wm.send_template(user_rjk, template_id1, data_cq)
res1 = wm.send_template(user_lc, template_id1, data_cs)
res2 = wm.send_template(user_gcm, template_id1, data_cq)
res3 = wm.send_template(user_xyq, template_id_friend, data_zj)
res4 = wm.send_template(user_tcr, template_id_friend, data_xz)

