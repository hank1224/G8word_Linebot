# 選擇基礎映像檔
FROM python:3.10

# 設置工作資料夾
WORKDIR /app

# 安裝Django和其他依賴
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# 複製Django應用程式到工作資料夾
COPY ./G8word/ /app/

# 設置環境變數
ENV DEBUG=True

# 開放端口
EXPOSE 8000

# 啟動Django應用程式
CMD ["python", "G8word/manage.py", "runserver", "0.0.0.0:8000"]