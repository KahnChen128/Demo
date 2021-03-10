import pymysql


class Dept(object):

    def __init__(self, no, name, location):
        self.no = no
        self.name = name
        self.location = location

    def __str__(self):
        return f'{self.no}\t{self.name}\t{self.location}'


def main():
    # 1. 创建连接对象
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='root', password='xX1285532325Xx',
                           db='hrs', charset='utf8',
                           cursorclass=pymysql.cursors.DictCursor)
    try:
        # 2. 获取游标对象 （上下文语法）
        with conn.cursor() as cursor:
            # 3. 执行SQL得到结果
            cursor.execute(
                'select dno as no, dname as name, dloc as location from tb_dept')
            for row in cursor.fetchall():
                dept = Dept(**row)
                print(dept)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
