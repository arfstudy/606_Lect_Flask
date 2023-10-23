from atexit import register

from sqlalchemy import Column, DateTime, Integer, String, create_engine, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройки подключения к базе данных
PG_DB = "app"
PG_USER = "app"
PG_PASSWORD = "1234"
PG_HOST = "127.0.0.1"
PG_PORT = 5431
PG_DNS = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

engine = create_engine(PG_DNS)    # Подключение к базе по заданному URL-базы (DNS)

register(engine.dispose)     # По окончании работы приложения наша БД должна отключиться

Session = sessionmaker(bind=engine)
Base = declarative_base(bind=engine)


class User(Base):
    __tablename__ = "app_users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())


print("\n  База данных создана...")    # BaseEmulator
# Выполняет миграции, подключается к базе данных
Base.metadata.create_all()
