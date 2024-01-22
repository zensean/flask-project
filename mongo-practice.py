# 載入 pymongo 套件
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

# 連線到 MongoDB 雲端資料庫
uri = "mongodb+srv://zensean00:root0123@cluster0.ja4dnzc.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# 把資料放進資料庫中
db=client.test # 選擇操作 test 資料庫
collection=db.users # 選擇操作 users 集合
# 篩選結果排序
cur=collection.find({ # find 尋找多筆資料 find_one 尋找一筆資料
    "$or":[ # 篩選條件 "$and":且條件 "$or":或條件
        {"gender":"female"},
        {"level":3}
    ]
}, sort=[ # 排序方式
    ("level", pymongo.DESCENDING) # ASCENDING:順序 DESCENDING:倒序
])
for doc in cur: # 取得多筆文件需使用for迴圈
    print(doc["name"], doc["level"])
# 複合篩選條件
# doc=collection.find_one({
#     "$and":[
#         {"name":"sean"},
#         {"gender":"male"}
#     ]
# })
# print("取得的資料", doc)

# 刪除集合中的多筆文件資料
# result=collection.delete_many({
#     "name":"mary"
# })
# print("實際上刪除的文件數量", result.deleted_count)

# 刪除集合中的一筆文件資料
# result=collection.delete_one({
#     "name":"sean"
# })
# print("實際上刪除的文件數量", result.deleted_count)

# 更新集合中的多筆文件資料
# result=collection.update_many({
#     "name":"sean"
# },{
#     "$mul":{
#         "level":0.25
#     }
# })
# print("符合條件的文件數量", result.matched_count)
# print("實際更新的文件數量", result.modified_count)

# 更新集合中的一筆文件資料
# result=collection.update_one({
#     "name":"mary"
# },{
#     "$inc":{ # $set:set&update $unset:remove $inc:+- $mul:*/
#         "level":1
#     }
# })
# print("符合條件的文件數量", result.matched_count)
# print("實際更新的文件數量", result.modified_count)

# 取得集合中的第一筆文件資料
# data=collection.find_one()
# print(data)
# 根據 ObjectId 取得文件資料
# data=collection.find_one(ObjectId("65ad3b37fc605a985b0e9d6e"))
# print(data)
# 取得文件資料中的欄位
# print(data["_id"])
# print(data["name"])
# print(data["gender"])
# 一次取得多筆文件資料
# cursor=collection.find()
# for doc in cursor:
#     print(doc["name"])

# 一次新增多筆資料,取得多筆資料的編號
# result=collection.insert_many([{
#     "name":"sean",
#     "gender":"male",
#     "level":1
# },{
#     "name":"mary",
#     "gender":"female",
#     "level":2
# },{
#     "name":"shelly",
#     "gender":"female",
#     "level":2
# },{
#     "name":"john",
#     "gender":"male",
#     "level":3
# }])
# print("資料新增成功")
# print(result.inserted_ids)