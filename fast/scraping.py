place_codeA = [62]
place_codeB = [47772]
place_name = ["Osaka"]   

import requests
from bs4 import BeautifulSoup 
import csv


base_url = "http://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php?prec_no=%s&block_no=%s&year=%s&month=%s&day=1&view=p1"

#取ったデータをfloat型に変える
def str2float(str):
  try:
    return float(str)
  except:
    return 0.0


if __name__ == "__main__":
  #都市を網羅します
  for place in place_name:
    #最終的にデータを集めるリスト
    All_list = [['date','rainfall','temp']]
    print(place)
    index = place_name.index(place)
    # for文で2020年~2021年までの2回。
    for year in range(2020,2022):
      print(year)
      # その年の1月~12月の12回を網羅する。
      for month in range(1,13):
        #2つの都市コードと年と月を当てはめる。
        r = requests.get(base_url%(place_codeA[index], place_codeB[index], year, month))
        r.encoding = r.apparent_encoding

        #　サイトごとスクレイピング
        soup = BeautifulSoup(r.text,'lxml')
        # findAllで条件に一致するものをすべて抜き出します。
        # 今回の条件はtrタグでclassがmtxになってるものです。
        rows = soup.findAll('tr',class_='mtx')

        rows = rows[4:]

        # 1日〜最終日までの１行を網羅し、取得します。
        for row in rows:
          # 今度はtrのなかのtdをすべて抜き出します
          data = row.findAll('td')

          #１行の中には様々なデータがあるので年度と降雨量のみをとりだす
          rowData = [] #初期化
          rowData.append(str(year) + "/" + str(month) + "/" + str(data[0].string))
          rowData.append(str2float(data[3].string))
          rowData.append(str2float(data[6].string))

          #次の行にデータを追加
          All_list.append(rowData)


def write_data():
    #都市ごとにデータをファイルを新しく生成して書き出す。(csvファイル形式。名前は都市名)
    with open(place + '.csv', 'w',encoding="utf_8_sig") as file:
      writer = csv.writer(file, lineterminator='\n')
      writer.writerows(All_list)

if __name__ == "__main__":
  write_data()



