import pandas as pd
import matplotlib.pyplot as plt
import base64
import datetime

def graph():
    try:
        df = pd.read_csv(
            "大阪府_大阪_202209-202210_daily.csv",
            encoding = "utf-8",  # 文字コード
        )

        d = pd.to_datetime({
        "year":df['年月'],
        "day":df['日']
        })

        df["日付"] = d # 置換

        n_rainfall=df['日降水量'].values

        # 降水量のグラフ
        plt.plot(d, n_rainfall, color="lightblue")

        plt.gcf().autofmt_xdate()

        # x軸ラベル名
        plt.xlabel("Date")
        # y軸ラベル名
        plt.ylabel("Rainfall")
        # タイトルラベル名
        plt.title("2020/01/1 - 2021/12/31")
        # グリッド線
        plt.grid()

        # グラフ画像の保存
        plt.savefig("precipitation.png")

        plt.show()

        file_data = open("precipitation.png", "rb").read()
        b64_data = base64.b64encode(file_data).decode('utf-8')

        return b64_data
    except Exception as e:
        print(e)

graph()

