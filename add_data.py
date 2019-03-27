import csv, sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = "db.sqlite3"

    # movie_data_0325.csv column name:
	# Movie_ID,Year,Rank,Title,Description,Duration,Genre,Rating,Metascore,Votes,Gross_Earning_in_Mil,Director,Actor

    sql_create_movie_table = """ CREATE TABLE IF NOT EXISTS movie_0325 (
                    Movie_ID integer PRIMARY KEY,
                    year integer NOT NULL,
                    rank integer NOT NULL,
                    Title text NOT NULL,
                    Description text,
                    Genre text NOT NULL,
                    Rating real,
                    Metascore integer,
                    Votes integer,
                    Gross_Earning_in_Mil real,
                    Director text,
                    Actor text
                                    ); """
 
    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create movie table
        create_table(conn, sql_create_movie_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()

with open('Data/movie_data_0325.csv','rb') as fin: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db = [(i['col1'], i['col2']) for i in dr]

cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
con.commit()
con.close()

