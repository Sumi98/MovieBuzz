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

    # --------- Movie Database ------------
    # movie_data_0325.csv column name:
	# Movie_ID, Year, Rank, Title, Description, Duration, Genre, Rating, Metascore, Votes, Gross_Earning_in_Mil, Director, Actor
	
    sql_create_movie_table = """ CREATE TABLE IF NOT EXISTS movie_0325 (
                    -- Movie_ID integer PRIMARY KEY,
                    Year integer NOT NULL,
                    Rank integer,
                    Title text NOT NULL,
                    Description text,
                    Duration integer,
                    Genre text,
                    Rating real,
                    Metascore integer,
                    Votes integer,
                    Gross_Earning_in_Mil real,
                    Director text,
                    Actor text
                                    ); """
 
    # create a database connection
    conn = create_connection(database)
    cur = conn.cursor()
    if conn is not None:
        # create movie table
        create_table(conn, sql_create_movie_table)
    else:
        print("Error! cannot create the database connection.")

    # insert movie records 
    with open('Data/movie_data_0325.csv','r', encoding='utf8') as fin:
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # default delimiter: comma
        to_db = [(col['Movie_ID'], col['Year'], col['Rank'], col['Title'], col['Description'], col['Duration'], col['Genre'], col['Rating'], col['Metascore'], col['Votes'], col['Gross_Earning_in_Mil'], col['Director'], col['Actor']) for col in dr]

    cur.executemany("""INSERT INTO movie_0325 
    				(Movie_ID, Year, Rank, Title, Description, Duration, Genre, Rating, Metascore, Votes, Gross_Earning_in_Mil, Director, Actor) 
    				VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", to_db)
    conn.commit()
    conn.close()

    # --------- Other Database ------------ @ TODO

if __name__ == '__main__':
    main()



