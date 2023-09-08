# 使用官方Python基础映像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将当前目录的内容复制到工作目录
COPY . /app

# 安装项目依赖项
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com -r requirements.txt

# 设置环境变量
ENV PYTHONUNBUFFERED=1

# 暴露端口，如果你的应用需要
EXPOSE 8000

# 运行app.py
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]