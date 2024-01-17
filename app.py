from flask import Flask     # 載入 Flask
from flask import request   # 載入 Request 物件
from flask import redirect  # 載入 Redirect 函式
from flask import render_template # 載入 render_template 函式
import json
# 建立 Application 物件, 設定靜態檔案的資料夾名稱及路徑, 設定為預設值
app=Flask(__name__, static_folder="static", static_url_path="/static") 

#建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 的處理函式
    # print("請求方法", request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑", request.path)
    # print("完整的網址", request.url)
    # print("瀏覽器和作業系統", request.headers.get("user-agent"))
    print("語言偏好", request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    lang=request.headers.get("accept-language")
    if lang.startswith("zh"):
        return redirect("/zh") #導向到路徑 /zh
    else:
        return "<h2>hello</h2>"+ render_template("home.html")

@app.route("/zh")
def zh():
    return "我真的好累~, 你要的我都學不會"+render_template("index.html")

@app.route("/firstWeb")
def firstWeb():
    return render_template("index.html")

@app.route("/page")
def page():
    return render_template("page.html")

@app.route("/jsonDumps")
def jsonDumps():
    return json.dumps({
        "status":"OK",
        "text":"dumps dumps"+"我真的好累~"
    }, ensure_ascii=False) #指示不要用ASCII 編碼處理中文

#建立路徑 /data 對應的處理函式
@app.route("/data")
def getData():
    return "My Data"

#動態路由:建立路徑 /user/使用者名稱 對應的函式
@app.route("/user/<name>")
def getUser(name):
    return "Hello "+name

@app.route("/getSum")
def getSum(): #sum of m to n
    maxNumber=request.args.get("n", 100)
    maxNumber=int(maxNumber)
    minNumber=request.args.get("m", 1)
    minNumber=int(minNumber)
    result=0

    #時間複雜度O(n) 的運算
    # for n in range(minNumber, maxNumber+1):
    #     result += n

    #時間複雜度O(1) 的運算
    n=maxNumber # 最大值 n
    m=minNumber # 最小值 m
    m=m-1 # 為了減去m(最小值)以下的所有等差級數之合 m本身是需要的值
    result = int((n+1)*n/2-(m+1)*m/2)
    return "結果："+str(result)



#啟動網站伺服器
app.run(port=3000)