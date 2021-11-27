import sys

import mysql.connector
import main
import time

from model import const


class SqlServer:
    host = "localhost"
    port = 3307
    conn = None

    def __init__(self, u, p):
        try:
            db = mysql.connector.connect(
                      host=self.host, port=self.port,
                      user=u, password=p)
            db.cursor().execute("CREATE DATABASE IF NOT EXISTS wechat_moments")
            self.conn = mysql.connector.connect(
                      host=self.host, port=self.port,
                      user=u, password=p,
                      database="wechat_moments")
        except Exception as e:
            print("database connect error:\n", e)
            sys.exit(2)

        cursor = self.conn.cursor()

        cursor.execute(const.CREATE_USER_LIST_TABLE)
        cursor.execute(const.CREATE_MOMENT_LIST_TABLE)
        cursor.execute(const.CREATE_LIKE_LIST_TABLE)
        cursor.execute(const.CREATE_COMMENT_LIST_TABLE)
        cursor.execute(const.CREATE_FRIENDSHIP_LIST_TABLE)

    def exec_select(self, sql, val):
        self.conn.cursor().execute(sql, val)
        result = self.conn.cursor().fetchall()
        return result

    def exec_insert(self, sql, val):
        self.conn.cursor().execute(sql, val)
        self.conn.commit()

    def login(self, account, password):
        cursor = self.conn.cursor()
        cursor.execute(const.LOGIN_SQL, (account,))
        result = cursor.fetchall()

        pair = (account, password)
        if pair in result:
            return True
        else:
            return False

    def register(self, account, name, gender, password):
        cursor = self.conn.cursor()
        cursor.execute(const.INSERT_USER_SQL, (account, name, gender, password))
        cursor.execute(const.INSERT_FRIENDSHIP_SQL, (account, account))
        self.conn.commit()
        print("insert %s success" % account)

    def get_all_moments(self, account):
        cursor = self.conn.cursor()
        cursor.execute(const.GET_ALL_MOMENTS, (account, ))
        result = cursor.fetchall()
        return result

    def check_like(self, index, account):
        cursor = self.conn.cursor()
        cursor.execute(const.CHECK_LIKE_SQL, (index, account))
        result = cursor.fetchall()
        if result:
            return True
        else:
            return False

    def like_confirm(self, index, account):
        cursor = self.conn.cursor()
        if self.check_like(index, account):
            cursor.execute(const.DELETE_LIKE_SQL, (index, account))
        else:
            val = (index, account, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            cursor.execute(const.INSERT_LIKE_SQL, val)
        self.conn.commit()

    def get_all_likes(self, index, account):
        cursor = self.conn.cursor()
        cursor.execute(const.GET_ALL_LIKES, (index, account))
        result = cursor.fetchall()
        return result

    def get_all_comments(self, index, account):
        cursor = self.conn.cursor()
        cursor.execute(const.GET_ALL_COMMENTS, (index, account))
        result = cursor.fetchall()
        return result

    def add_comment(self, index, content):
        cursor = self.conn.cursor()
        val = (index, main.USER, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), content)
        cursor.execute(const.INSERT_COMMENT_SQL, val)
        self.conn.commit()
        print("add Comment success")

    def delete_confirm(self, name, create_time):
        cursor = self.conn.cursor()
        cursor.execute(const.DELETE_COMMENT_SQL, (name, create_time))
        self.conn.commit()

    def add_moment(self, content):
        cursor = self.conn.cursor()
        val = (main.USER, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), content)
        cursor.execute(const.INSERT_MOMENT_SQL, val)
        self.conn.commit()
        print("add PYQ success")

    def add_friend(self, ID):
        cursor = self.conn.cursor()
        cursor.execute(const.SELECT_USER_LIST_SQL, (ID,))
        result = cursor.fetchall()
        if not result:
            return False

        cursor = self.conn.cursor()
        cursor.execute(const.SELECT_FRIENDSHIP_LIST_SQL, (main.USER, ID))
        result = cursor.fetchall()
        if result:
            return False

        cursor = self.conn.cursor()
        cursor.execute(const.INSERT_FRIENDSHIP_SQL, (main.USER, ID))
        cursor.execute(const.INSERT_FRIENDSHIP_SQL, (ID, main.USER))
        self.conn.commit()
        return True

