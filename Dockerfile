# 基本映像檔，必須是第一個指令 使用py3.8
FROM amd64/python:3.10-slim-buster

WORKDIR /app

# 複製requirements.txt(要安裝的函式庫)到docker裡面，然後安裝
COPY requirements.txt requirements.txt
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt

# 複製全部東西進docker
COPY . .

# 更新映像檔的指令
#RUN cd google-images-download && python3 setup.py install
# RUN mkdir downloads
# RUN apt-get update && apt-get install -y ffmpeg
# RUN pip3 list

# 建立新容器時要執行的指令
CMD [ "python3", "main.py"]