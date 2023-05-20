import requests as req
import json
import schedule
import time
from matplotlib import pyplot as pyp

TOKEN = 'your token'
api_url = 'https://notify-api.line.me/api/notify'

def main_night():
    hourly_time=[]
    hourly_rain=[]
    weather_json=req.get("https://api.open-meteo.com/v1/forecast?latitude=35.30&longitude=136.80&timezone=Asia%2FTokyo&daily=temperature_2m_max&daily=temperature_2m_min&daily=precipitation_probability_mean&daily=weathercode&daily=windspeed_10m_max&daily=winddirection_10m_dominant&hourly=rain",verify=False)
    weather_json=weather_json.json()

    rain_mm=weather_json["hourly_units"]["rain"]
    temp_sym=weather_json["daily_units"]["temperature_2m_max"]
    rain_sym=weather_json["daily_units"]["precipitation_probability_mean"]
    wind_sym=weather_json["daily_units"]["windspeed_10m_max"]
    for i in range(24,49):
        hourly_time.append(weather_json["hourly"]["time"][i])
        tmp=hourly_time[i-24]
        tmp=tmp.replace("2023-","")
        hourly_time[i-24]=tmp.replace("T"," ")
        hourly_rain.append(weather_json["hourly"]["rain"][i])
    fig=pyp.figure(figsize=[12,5])
    ax=fig.add_subplot(111)
    fig.tight_layout()
    ax.bar(hourly_time, hourly_rain,width=1,align="edge")
    ax.set_xlabel("Data")
    ax.set_ylabel("mm/h")
    pyp.xticks(rotation=15)
    fig.savefig("graph.png")
    pyp.cla()

    day=weather_json["daily"]["time"][1]
    temp_max=weather_json["daily"]["temperature_2m_max"][1]
    temp_min=weather_json["daily"]["temperature_2m_min"][1]
    humi_mean=weather_json["daily"]["precipitation_probability_mean"][1]
    weather_code=weather_json["daily"]["weathercode"][1]
    wind_max=weather_json["daily"]["windspeed_10m_max"][1]
    wind_di=weather_json["daily"]["winddirection_10m_dominant"][1]
    wind_str="None"
    weather_str="None"
    if wind_di >=0 and wind_di <22.4:
        wind_str="北"
    elif wind_di >= 22.5 and wind_di < 44.9:
        wind_str="北北東"
    elif wind_di >= 22.5 and wind_di < 44.9:
        wind_str="北東"
    elif wind_di >= 45 and wind_di < 67.4:
        wind_str="東北東"
    elif wind_di >= 67.5 and wind_di < 89.9:
        wind_str="東"
    elif wind_di >= 90 and wind_di < 112.4:
        wind_str="東南東"
    elif wind_di >= 112.5 and wind_di < 134.9:
        wind_str="南東"
    elif wind_di >= 135 and wind_di < 157.4:
        wind_str="南南東"
    elif wind_di >= 157.5 and wind_di < 179.9:
        wind_str="南"
    elif wind_di >= 180 and wind_di < 202.4:
        wind_str="南南西"
    elif wind_di >= 202.5 and wind_di < 224.9:
        wind_str="南西"
    elif wind_di >= 225 and wind_di < 247.4:
        wind_str="西北西"
    elif wind_di >= 247.5 and wind_di < 269.9:
        wind_str="西"
    elif wind_di >= 270 and wind_di < 292.4:
        wind_str="西北西"
    elif wind_di >= 292.5 and wind_di < 314.9:
        wind_str="北西"
    elif wind_di >= 315 and wind_di < 337.4:
        wind_str="北北西"
    elif wind_di >= 337.5 and wind_di <= 360:
        wind_str="北"

    if weather_code == 0 :
        weather_str = "快晴"
    elif weather_code >= 1 and weather_code <=3:
        weather_str = "晴れ時々曇り、曇り"
    elif weather_code == 45 or weather_code == 48:
        weather_str = "小雨"
    elif weather_code == 51 or weather_code == 53 or weather_code == 55:
        weather_str = "霧雨"
    elif weather_code >= 56 and weather_code <=57:
        weather_str = "氷結霧雨"
    elif weather_code == 61 or weather_code == 63 or weather_code == 65:
        weather_str = "雨"
    elif weather_code >= 66 and weather_code <=67:
        weather_str = "冷たい雨"
    elif weather_code == 71 or weather_code == 73 or weather_code == 75:
        weather_str = "雪"
    elif weather_code >= 77:
        weather_str = "にわか雪"
    elif weather_code >= 80 and weather_code <=82:
        weather_str = "にわか雨"
    elif weather_code >= 85 and weather_code <=86:
        weather_str = "雪"
    elif weather_code == 95:
        weather_str = "強雨"
    elif weather_code == 96 or weather_code == 99:
        weather_str = "雷雨"

    wind_max=(wind_max/3600)*1000

    send_contents=f"{day}の天気\n最高気温:{temp_max}{temp_sym} 最低気温:{temp_min}{temp_sym} \n天気:{weather_str} {humi_mean}{rain_sym}\n最大風速:{int(wind_max)}m/s 風向:{wind_str}"
    TOKEN_dic = {'Authorization': 'Bearer'+' '+TOKEN}
    send_dic = {'message': send_contents}
    image_dic = {'imageFile': open("graph.png", "rb")}
    try:
        req.post(api_url, headers=TOKEN_dic, data=send_dic,files=image_dic)
    except Exception as e:
        print(f"Error {e}")

def main_morning():
    hourly_time=[]
    hourly_rain=[]
    weather_json=req.get("https://api.open-meteo.com/v1/forecast?latitude=35.30&longitude=136.8125&timezone=Asia%2FTokyo&daily=temperature_2m_max&daily=temperature_2m_min&daily=precipitation_probability_mean&daily=weathercode&daily=windspeed_10m_max&daily=winddirection_10m_dominant&hourly=rain",verify=False)
    weather_json=weather_json.json()

    rain_mm=weather_json["hourly_units"]["rain"]
    temp_sym=weather_json["daily_units"]["temperature_2m_max"]
    rain_sym=weather_json["daily_units"]["precipitation_probability_mean"]
    wind_sym=weather_json["daily_units"]["windspeed_10m_max"]
    for i in range(0,24):
        hourly_time.append(weather_json["hourly"]["time"][i])
        tmp=hourly_time[i]
        tmp=tmp.replace("2023-","")
        hourly_time[i]=tmp.replace("T"," ")
        hourly_rain.append(weather_json["hourly"]["rain"][i])
    fig=pyp.figure(figsize=[12,5])
    ax=fig.add_subplot(111)
    fig.tight_layout()
    ax.bar(hourly_time, hourly_rain,width=1,align="edge")
    ax.set_xlabel("Data")
    ax.set_ylabel("mm/h")
    pyp.xticks(rotation=15)
    fig.savefig("graph.png")
    pyp.cla()

    day=weather_json["daily"]["time"][0]
    temp_max=weather_json["daily"]["temperature_2m_max"][0]
    temp_min=weather_json["daily"]["temperature_2m_min"][0]
    humi_mean=weather_json["daily"]["precipitation_probability_mean"][0]
    weather_code=weather_json["daily"]["weathercode"][0]
    wind_max=weather_json["daily"]["windspeed_10m_max"][0]
    wind_di=weather_json["daily"]["winddirection_10m_dominant"][0]
    wind_str="None"
    weather_str="None"
    if wind_di >=0 and wind_di <22.4:
        wind_str="北"
    elif wind_di >= 22.5 and wind_di < 44.9:
        wind_str="北北東"
    elif wind_di >= 22.5 and wind_di < 44.9:
        wind_str="北東"
    elif wind_di >= 45 and wind_di < 67.4:
        wind_str="東北東"
    elif wind_di >= 67.5 and wind_di < 89.9:
        wind_str="東"
    elif wind_di >= 90 and wind_di < 112.4:
        wind_str="東南東"
    elif wind_di >= 112.5 and wind_di < 134.9:
        wind_str="南東"
    elif wind_di >= 135 and wind_di < 157.4:
        wind_str="南南東"
    elif wind_di >= 157.5 and wind_di < 179.9:
        wind_str="南"
    elif wind_di >= 180 and wind_di < 202.4:
        wind_str="南南西"
    elif wind_di >= 202.5 and wind_di < 224.9:
        wind_str="南西"
    elif wind_di >= 225 and wind_di < 247.4:
        wind_str="西北西"
    elif wind_di >= 247.5 and wind_di < 269.9:
        wind_str="西"
    elif wind_di >= 270 and wind_di < 292.4:
        wind_str="西北西"
    elif wind_di >= 292.5 and wind_di < 314.9:
        wind_str="北西"
    elif wind_di >= 315 and wind_di < 337.4:
        wind_str="北北西"
    elif wind_di >= 337.5 and wind_di <= 360:
        wind_str="北"

    if weather_code == 0 :
        weather_str = "快晴"
    elif weather_code >= 1 and weather_code <=3:
        weather_str = "晴れ時々曇り、曇り"
    elif weather_code == 45 or weather_code == 48:
        weather_str = "小雨"
    elif weather_code == 51 or weather_code == 53 or weather_code == 55:
        weather_str = "霧雨"
    elif weather_code >= 56 and weather_code <=57:
        weather_str = "氷結霧雨"
    elif weather_code == 61 or weather_code == 63 or weather_code == 65:
        weather_str = "雨"
    elif weather_code >= 66 and weather_code <=67:
        weather_str = "冷たい雨"
    elif weather_code == 71 or weather_code == 73 or weather_code == 75:
        weather_str = "雪"
    elif weather_code >= 77:
        weather_str = "にわか雪"
    elif weather_code >= 80 and weather_code <=82:
        weather_str = "にわか雨"
    elif weather_code >= 85 and weather_code <=86:
        weather_str = "雪"
    elif weather_code == 95:
        weather_str = "強雨"
    elif weather_code == 96 or weather_code == 99:
        weather_str = "雷雨"

    wind_max=(wind_max/3600)*1000

    send_contents=f"今日の天気\n最高気温:{temp_max}{temp_sym} 最低気温:{temp_min}{temp_sym} \n天気:{weather_str} {humi_mean}{rain_sym}\n最大風速:{int(wind_max)}m/s 風向:{wind_str}"
    TOKEN_dic = {'Authorization': 'Bearer'+' '+TOKEN}
    send_dic = {'message': send_contents}
    image_dic = {'imageFile': open("graph.png", "rb")}
    try:
        req.post(api_url, headers=TOKEN_dic, data=send_dic,files=image_dic)
    except Exception as e:
        print(f"Error {e}")

schedule.every().day.at("19:00").do(main_night)
schedule.every().day.at("07:00").do(main_morning)
while True:
    schedule.run_pending()
    time.sleep(60)
