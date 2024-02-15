from dotenv import load_dotenv
load_dotenv()
from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os

# models.database モジュールから Base をインポート
from models.database import Base

# Alembic の設定を読み込む
config = context.config

config.set_main_option("sqlalchemy.url", os.environ.get("DB_CONNECTION_STRING"))

fileConfig(config.config_file_name)

# ここで target_metadata を設定
target_metadata = Base.metadata

def run_migrations_offline():
    # この関数内で context.configure() を呼び出す際に target_metadata を使用
    url = config.get_main_option("sqlalchemy.url")
    print(url)
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": 'named'},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    # この関数内でも context.configure() を呼び出す際に target_metadata を使用
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

#migrationsを実行
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
