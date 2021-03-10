import pymysql


def main():
    # 1. 创建连接对象
    conn = pymysql.connect(host='127.0.0.1', port=3306,
                           user='root', password='xX1285532325Xx',
                           db='hrs', charset='utf8')
    try:
        # 2. 获取游标对象 （上下文语法）
        with conn.cursor() as cursor:
            # 3. 执行SQL得到结果
            cursor.execute(
                'select dno, dname, dloc from tb_dept')
            for row in cursor.fetchall():
                print(f'部门编号：{row[0]}')
                print(f'部门名称：{row[1]}')
                print(f'部门所在地：{row[2]}')
                print('-' * 20)
    except pymysql.MySQLError as error:
        print(error)
    finally:
        # 5. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
