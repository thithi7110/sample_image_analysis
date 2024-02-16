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


## mypyチェック
- mypyによるエラーチェック
```
poetry run mypy .
```

## pytest
```
poetry run pytest .
```