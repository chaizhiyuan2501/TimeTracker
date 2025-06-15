FROM python:3.11-slim-bookworm

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係に必要なシステムパッケージをインストール
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Python依存パッケージをインストール
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# コードをコピー
COPY . .

# FastAPIアプリケーションを起動（uvicornを使用）
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
