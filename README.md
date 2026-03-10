# AI Sentiment Analyzer

AIを使って文章の感情（ポジティブ / ネガティブ）を分析する  
シンプルなWebアプリケーションです。

## デモ

入力文章：
"このラーメンは素晴らしい"

結果：
"result": "positive"

<img width="1420" height="862" alt="20260310" src="https://github.com/user-attachments/assets/88809fad-d203-4db9-bf34-6f4d6ab002bc" />

## セットアップ

### 1 仮想環境作成

python3 -m venv .venv

### 2 仮想環境起動

Linux / Mac
source .venv/bin/activate

Windows
.venv\Scripts\activate

### 3 依存関係インストール

pip install -r requirements.txt

## アプリ起動

uvicorn app.main:app --reload

ブラウザでアクセス
http://127.0.0.1:8000/docs
