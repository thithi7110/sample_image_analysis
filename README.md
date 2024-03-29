# sample_image_analysis
## 内容
特定の画像ファイルに対し、画像のClassなどを分析し、DB(mysql)に保存します

---

## 開発環境構築
## 1. mysqlインストールを使いますのでインストールしてください
```
brew install mysql
brew services start mysql
mysql_secure_installation
```
## 2. poetryを使うのでインストールしておいてください
例
```
curl -sSL https://install.python-poetry.org | python3 -

```

## 3. ライブラリ取得
ルートで以下を実行します。
```
poetry install
```

## 4. mysqlにDB構築（dockerで用意したいところ）
- 1.以下でDB作成、ユーザー作成、権限付与を実施
```
poetry shell 
mysql -u root -p
CREATE DATABASE sampledb;
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON sampledb.* TO 'user'@'localhost';
FLUSH PRIVILEGES;
```

- 2.接続確認
```
mysql -u user -p sampledb
```
## 5. migration実行
```
poetry shell
alembic upgrade head
```

## 6. サーバ起動
portはよしなに変えてください
```
poetry shell
uvicorn main:app --port 5000 --reload
```


## 7. mypyチェック
- mypyによるエラーチェック
```
poetry run mypy .
```

## 8. pytest
```
poetry run pytest .
```

## 9. 実行
サーバ起動させた状態で以下curl実行
```
curl -X POST \
  "http://127.0.0.1:5000/api/analyze-image/" \
  -H "Content-Type: application/json" \
  -d "{\"image_path\": \"/image/d03f1d36ca69348c51aa/c413eac329e1c0d03/test.jpg\"}"
```

実施成功で以下ai_analysis_logテーブルにデータが登録されます
![Alt text](image.png)