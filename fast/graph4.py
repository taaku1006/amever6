import pandas as pd
import matplotlib.pyplot as plt

class Graph:
    df = pd.read_csv(
            "data.csv",                
    )
    df2 = pd.to_datetime({
        "year":df['年'],
        "month":df['月'],
        "day":df['日'],
        
    })

    dt=pd.DataFrame({
        '日付':df2,      
    })

    d_f=df.drop(['年','月','日'],axis=1)

    df3 = pd.concat([dt, d_f],axis=1)

    n_temparacture=df3['平均気温'].values

    date=df3['日付'].values

    plt.plot(date, n_temparacture, color="red")

    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")

    plt.ylabel("")

    plt.grid()

    plt.savefig("temp.png")
