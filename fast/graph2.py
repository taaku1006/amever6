import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
import datetime

def graph():
    try:
        df = pd.read_csv(
            "Osaka.csv",
            encoding = "utf-8",  # 文字コード
        )

        dates=[]
        for _date in df['date']:
            date = datetime.datetime.strptime(_date,'%Y/%m/%d').date()
            dates.append(date)

        n_temperature=df['temp'].values

        # 降水量のグラフ
        plt.plot(dates, n_temperature, color="lightsalmon")

        plt.gcf().autofmt_xdate()

        # x軸ラベル名
        plt.xlabel("Date")
        # y軸ラベル名
        plt.ylabel("Temperature")
        # タイトルラベル名
        plt.title("2020/01/1 - 2021/12/31")
        # グリッド線
        plt.grid()

        # グラフ画像の保存
        plt.savefig("temp.png")

        plt.show()

        file_data = open("temp.png", "rb").read()
        b64_data = base64.b64encode(file_data).decode('utf-8')

        return b64_data
    except Exception as e:
        print(e)

graph()

