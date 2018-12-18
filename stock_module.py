import twstock
import requests

def get_setting():
    res = []
    try:
        with open('stock.txt') as f:
            slist = f.readlines()
            # print('讀入', slist)
            for line in slist:
                s = line.split(',')
                res.append([s[0].strip(), float(s[1]), float(s[2])])
    except:
        print('讀取失敗')
    
    return res

def get_price(stockid):
    rt = twstock.realtime.get(stockid)
    if(rt['success']):
        return (rt['info']['name'], float(rt['realtime']['latest_trade_price']))
    else:
        return (False, False)
            
def get_best(stockid):
    stock = twstock.Stock(stockid)
    bp = twstock.BestFourPoint(stock).best_four_point()
    if(bp):
        return('買進' if bp[0] else '賣出', bp[1])
    else:
        return(False, False)
def send_ifttt(v1, v2, v3):
    url = ('https://maker.ifttt.com/trigger/toline/with/key/da2-R6WO4CJ3gIAdQlj9vF' + '?value1=' + str(v1)  + '&value2=' + str(v2) + '&value3=' + str(v3))
    r = requests.get(url)
    if(r.text[:5] == 'Congr'):
        print('已傳送')
    

send_ifttt('台積電', 99, '建議買進')