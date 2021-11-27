CREATE_USER_LIST_TABLE = """
                        CREATE TABLE IF NOT EXISTS user_list (uID VARCHAR(20) PRIMARY KEY, uName VARCHAR(20), 
                        uGender VARCHAR(10), uPassword VARCHAR(20))
                        """

CREATE_MOMENT_LIST_TABLE = """
                        CREATE TABLE IF NOT EXISTS moment_list (mID INT AUTO_INCREMENT PRIMARY KEY, 
                        mCreator VARCHAR(20), mCreTime VARCHAR(30), mContent VARCHAR(100))
                        """

CREATE_LIKE_LIST_TABLE = """
                        CREATE TABLE IF NOT EXISTS like_list (lID INT AUTO_INCREMENT PRIMARY KEY, 
                        lCreator VARCHAR(20), lCreTime VARCHAR(30), mID INT)
                       """

CREATE_COMMENT_LIST_TABLE = """
                        CREATE TABLE IF NOT EXISTS comment_list (cID INT AUTO_INCREMENT PRIMARY KEY, 
                        cCreator VARCHAR(20), cCreTime VARCHAR(30), cContent VARCHAR(100), mID INT)
                       """

CREATE_FRIENDSHIP_LIST_TABLE = "CREATE TABLE IF NOT EXISTS friendship_list (f1 VARCHAR(20), f2 VARCHAR(20))"

LOGIN_SQL = "SELECT uID, uPassword FROM user_list WHERE uID = %s"

INSERT_USER_SQL = "INSERT INTO user_list(uID, uName, uGender, uPassword) VALUES (%s, %s, %s, %s)"

INSERT_FRIENDSHIP_SQL = "INSERT INTO friendship_list(f1, f2) VALUES (%s, %s)"

GET_ALL_MOMENTS = """
                SELECT mCreator, mCreTime, mContent, mID FROM moment_list
                WHERE mCreator IN (SELECT f2 FROM friendship_list WHERE f1 = %s) 
                ORDER BY mCreTime
                """

INSERT_MOMENT_SQL = "INSERT INTO moment_list(mCreator, mCreTime, mContent) VALUES (%s, %s, %s)"

CHECK_LIKE_SQL = "SELECT * FROM like_list WHERE mID = %s AND lCreator = %s"

DELETE_LIKE_SQL = "DELETE FROM like_list WHERE mID = %s AND lCreator = %s"

INSERT_LIKE_SQL = "INSERT INTO like_list(mID, lCreator, lCreTime) values (%s, %s, %s)"

GET_ALL_LIKES = """
                SELECT lCreator FROM like_list
                WHERE mID = %s AND lCreator IN (SELECT f2 FROM friendship_list WHERE f1 = %s)
                """

GET_ALL_COMMENTS = """
                select * from comment_list
                where mID = %s and cCreator in (select f2 from friendship_list where f1 = %s)
                order by cCreTime
                """

INSERT_COMMENT_SQL = "INSERT INTO comment_list(mID, cCreator, cCreTime, cContent) VALUES (%s, %s, %s, %s)"

DELETE_COMMENT_SQL = "DELETE FROM comment_list WHERE cCreator = %s AND cCreTime = %s"

SELECT_USER_LIST_SQL = "SELECT * FROM user_list WHERE uID = %s"

SELECT_FRIENDSHIP_LIST_SQL = "SELECT * FROM friendship_list WHERE f1 = %s AND f2 = %s"
