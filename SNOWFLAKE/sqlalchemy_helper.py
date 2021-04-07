#!/usr/bin/env python
from sqlalchemy import create_engine
import config
import pandas as pd


class SqlalchemyHelper:
    _instance = None
    _engine = None
    _connection = None

    def __init__(self):
        raise RuntimeError("Use SqlalchemyHelper.instance()")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance

    def create_engine(self):
        self._engine = create_engine('snowflake://{user}:{password}@{account}/'.format(
            user=config.user,
            password=config.password,
            account=config.account,))

        self._connection = self._engine.connect()

        try:
            # Starting with the connection
            results = self._connection.execute('select current_version()').fetchone()
            print(results[0])
            print('Sqlalchemy-SnowflakeConnection established!')
        except Exception as e:
            raise e

    def execute_query(self, sql):
        df = pd.read_sql_query(sql, self._engine)
        return df

    def close(self):
        # Close your connection and your engine.
        self._connection.close()
        self._engine.dispose()






