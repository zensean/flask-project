from flask import Flask
app=Flask(__name__) # 建立 Application 物件

#建立路徑 / 對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 的處理函式
    return "Hello Flask" #回傳網站首頁<body>中的內容

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