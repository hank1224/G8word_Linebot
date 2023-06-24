FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /code/G8word/

# 安裝 libpq-dev 套件，它提供了 PostgreSQL 的 C 語言客戶端庫和相關的頭文件，使得 Python 程式能夠正確地讀寫 PostgreSQL 數據庫。
RUN  apt-get install libpq-dev -y && \
    ln -sf /usr/share/zoneinfo/Asia/Taipei  /etc/localtime

ADD requirements.txt requirements.txt

RUN pip install --upgrade pip  && \
        pip install -Ur requirements.txt
        
ADD . .
# 第一個點 "." 是指要複製的對象（源）所在的路徑，也就是 Dockerfile 所在的目錄；
# 第二個點 "." 則是指映像中的目的地或目錄，也就是將源複製到 Docker 長什麼樣子的空間。

RUN chmod +x /code/G8word/bin/docker_start.sh
# +x 給予執行權限

ENTRYPOINT ["/code/G8word/bin/docker_start.sh"]