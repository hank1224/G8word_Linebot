# G8word_Linebot
雞八話機器人，郭睿桓的惡夢

稽查並記錄你與素質朋友間Line群組內的G8話，共創綠色聊天環境。

## 本專案尚未完成!!
收到line訊息後需要在一秒內回覆200，否則line就會關連線造成Broken pipe，message.reply.token時效應該有十分鐘，處理完再慢慢回

分支可在docker環境建置，要改成本地的話要處理環境變數引入(預計最終會讓兩方法通用)

使用docker-compose建置，第一次可能celery和django開不起來，手動再按一次即可(判定db初始化完成與否的程式待優化)

/bin/docker_star.sh sh檔案用mac存檔會有問題，若遇到開不了，用Notepad>編輯>換行格式>Unix格式存檔即可

## 使用技術
1.  django的celery套件處理任務，需要注意的是他是掛在Django內但是要分兩個終端開
2.  celery使用radis作為任務儲存資料庫，但redis是用RAM去裝的，並不可靠
3.  使用postgresql作為Django資料庫，有ORM支援
4.  dockerflie和dockercompose建置，僅有Django可對外網，模式host

## 本地部署
記得調整env檔案

**redis**
1. 安裝redis windows版: https://marcus116.blogspot.com/2019/02/how-to-install-redis-in-windows-os.html
2. 到 服務 啟動Redis
3. cmd執行 `redis-cli` 然後 `ping` 看有沒有回應 `PONG`

**celery**
1. 記得先啟動redis
2. cd manage.py同層目錄
3. cmd執行 `celery -A G8word worker -l info` 啟動celery


**PostgreSQL**
1. 注意新建資料庫的密碼要符合.env檔案設定

## Docker部署
你加油