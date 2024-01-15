from flask import Flask     # 載入 Flask
from flask import request   # 載入 Request 物件
app=Flask(__name__) # 建立 Application 物件

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
        return "妳好,歡迎光臨"
    else:
        return "Hello Flask"

#建立路徑 /data 對應的處理函式
@app.route("/data")
def getData():
    return "My Data"

#動態路由:建立路徑 /user/使用者名稱 對應的函式
@app.route("/user/<name>")
def getUser(name):
    return "Hello "+name


#啟動網站伺服器
app.run(port=3000)