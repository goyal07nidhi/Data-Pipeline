from sqlalchemy_helper import SqlalchemyHelper
import config

if __name__ == "__main__":

    SqlalchemyHelper.instance().create_engine()

    query_0 = 'select * from "ASSIGNMENT_1"."PUBLIC"."CATALOG" LIMIT 3'

    query_1 = 'SELECT year, sum(deaths_direct + deaths_indirect ) as total_deaths ' \
              'FROM "ASSIGNMENT_1"."PUBLIC"."STORM_EVENTS" ' \
              'group by year ' \
              'order by year limit 5'

    df = SqlalchemyHelper.instance().execute_query(query_0)
    print(df)

    SqlalchemyHelper.instance().close()
