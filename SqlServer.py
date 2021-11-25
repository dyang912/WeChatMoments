import pymssql
import main
import time


class SqlServer:
    server = "localhost:1433"
    user = "sa"
    password = "123456"
    database = "myPYQ"

    conn = None

    def __init__(self, ):
        pass

    def getConnect(self):
        self.conn = pymssql.connect(self.server, self.user, self.password, self.database)
        cursor = self.conn.cursor()

        return cursor

    def execSelect(self, sql):
        cursor = self.getConnect()
        cursor.execute(sql)
        result = cursor.fetchall()
        self.conn.close()
        return result

    def execInsert(self, sql):
        cursor = self.getConnect()
        cursor.execute(sql)
        self.conn.commit()
        self.conn.close()

    def login(self, account, password):
        sql = """
        select userID, uPassword
        from USERINFO
        """

        list = ("{:<10}".format(account), "{:<10}".format(password))
        result = self.execSelect(sql)
        if list in result:
            return True
        else:
            return False

    def register(self, account, name, gender, password):
        sql = """
        exec CREATEUSER_PROCEDURE @id = '%s', @name = '%s', @gender = '%s', @password= '%s' 
        """ % (account, name, gender, password)

        self.execInsert(sql)
        print("insert success")

    def search(self, account):
        sql = """
        select pCreator, pCreTime, pContent, pNumber
        from PYQLIST
        where pCreator in (select fU2 from FRIENDSHIP where fU1 = '%s') 
        order by pCreTime
        """ % account

        result = self.execSelect(sql)
        return result

    def checkLike(self, index, account):
        sql = """
        select *
        from LIKEINFO
        where lNumber = '%s' and lCreator = '%s'
        """ % (index, account)

        result = self.execSelect(sql)
        if result:
            return True
        else:
            return False

    def likeConfirm(self, index, account):
        if self.checkLike(index, account):
            sql = """
            delete
            from LIKEINFO
            where lNumber = '%s' and lCreator = '%s'
            """ % (index, account)

            self.execInsert(sql)
        else:
            sql = """
            SET IDENTITY_INSERT LIKEINFO ON
            insert into LIKEINFO(lNumber, lCreator, lCreTime) values ('%s', '%s', '%s')
            SET IDENTITY_INSERT LIKEINFO OFF
            """ % (index, account, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

            self.execInsert(sql)

    def searchLike(self, index, account):
        sql = """
        select lCreator
        from LIKEINFO
        where lNumber = '%s' and lCreator in (select fU2 from FRIENDSHIP where fU1 = '%s')
        """ % (index, account)

        result = self.execSelect(sql)
        return result

    def searchComment(self, index, account):
        sql = """
        select *
        from COMMENT
        where cNumber = '%s' and cCreator in (select fU2 from FRIENDSHIP where fU1 = '%s')
        order by cCreTime
        """ % (index, account)

        result = self.execSelect(sql)
        return result

    def addComment(self, index, content):
        sql = """
        exec ADDCOMMENT_PROCEDURE @index = '%s', @account = '%s', @time = '%s', @content = '%s' 
        """ % (index, main.USER, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), content)

        self.execInsert(sql)
        print("add Comment success")

    def deleteConfirm(self, name, ti):
        sql = """
        delete
        from COMMENT
        where cCreator = '%s' and cCreTime = '%s'
        """ % (name, ti)

        self.execInsert(sql)

    def addPYQ(self, content):
        sql = """
        exec ADD_PROCEDURE @creatorID = '%s', @time = '%s' ,@content = '%s' 
        """ % (main.USER, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), content)

        self.execInsert(sql)
        print("add PYQ success")

    def addFriend(self, ID):
        sql = """
        select *
        from USERINFO
        where userID = '%s'
        """ % (ID)

        result = self.execSelect(sql)
        if not result:
            return False

        sql = """
        select *
        from FRIENDSHIP
        where fU1 = '%s' and fU2 = '%s'
        """ % (main.USER, ID)
        result = self.execSelect(sql)

        if result:
            return False

        sql = """
        exec ADDFRIEND_PROCEDURE @id1 = '%s', @id2 = '%s' 
        """ % (main.USER, ID)

        self.execInsert(sql)
        return True

