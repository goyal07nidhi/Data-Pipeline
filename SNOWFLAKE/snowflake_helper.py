import snowflake.connector
import config
from snowflake.connector.pandas_tools import write_pandas

class SnowflakeHelper:
    _instance = None
    _conn = None

    def __init__(self):
        raise RuntimeError("Use SnowflakeHelper.instance()")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)

        return cls._instance

    def create_connection(self):
        self._conn = snowflake.connector.connect(user=config.user,
                                                 password=config.password,
                                                 account=config.account)

        print('Snowflake Connection established!')

    def setup(self):
        try:
            if self._conn is None:
                self.create_connection()

            cur = self._conn.cursor()
            # Starting with the Role.
            sql = "USE ROLE SYSADMIN"
            cur.execute(sql)

            # Define warehouse and use it.
            sql = "CREATE WAREHOUSE IF NOT EXISTS MY_WH " \
                  "WITH WAREHOUSE_SIZE = SMALL"
            cur.execute(sql)
            sql = "USE WAREHOUSE MY_WH"
            cur.execute(sql)

            # Create database and use it
            sql = "CREATE DATABASE IF NOT EXISTS ASSIGNMENT_1"
            cur.execute(sql)
            sql = "USE DATABASE ASSIGNMENT_1"
            cur.execute(sql)

            # Create and use schema.
            sql = "CREATE SCHEMA IF NOT EXISTS PUBLIC"
            cur.execute(sql)
            sql = "USE SCHEMA PUBLIC"
            cur.execute(sql)

        except Exception as e:
            print(e)

        finally:
            cur.close()

    def write_dataframe(self, dataframe, table):
        if self._conn is None:
            self.setup()

        try:
            cur = self._conn.cursor()
            # Ensure warehouse is still running.
            sql = "ALTER WAREHOUSE MY_WH RESUME"
            cur.execute(sql)
        except Exception as e:
            print('Warehouse already active')
            pass

        finally:
            cur.close()

        success, nchunks, nrows, _ = write_pandas(self._conn, dataframe, table)

        if not success:
            print('Error writing dataframe to snowflake')
        else:
            print('Successfully pushed {0} rows to snowflake'.format(nrows))

    def close(self):
        cur = self._conn.cursor()
        # Turn off the warehouse.
        sql = "ALTER WAREHOUSE MY_WH SUSPEND"
        cur.execute(sql)
        print('Warehouse suspended')

        # Close your cursor and your connection.
        cur.close()
        self._conn.close()
