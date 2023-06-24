# G8word_Linebot
雞八話機器人，郭睿桓的惡夢

目前僅支援在docker環境建置，要改成本地的話要處理環境變數引入(預計最終會讓兩方法通用)

使用docker-compose建置，第一次可能celery和django開不起來，手動再按一次即可(判定db初始化完成與否的程式待優化)

/bin/docker_star.sh sh檔案用mac存檔會有問題，若遇到開不了，用Notepad>編輯>換行格式>Unix格式存檔即可

收到line訊息後需要在一秒內回覆200，否則line就會關連線造成Broken pipe，message.reply.token時效應該有十分鐘，處理完再慢慢回

使用技術:
1. django的celery套件處理任務，需要注意的是他是掛在Django內但是要分兩個終端開
2. celery使用radis作為任務儲存資料庫，但redis是用RAM去裝的，並不可靠
3. 使用postgresal作為Django資料庫，有ORM支援
4. dockerflie和dockercompose建置，僅有Django可對外網，模式host
