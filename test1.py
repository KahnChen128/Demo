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
            result = cursor.execute(
                'insert into tb_dept values (50, "信息部", "广州")')
            if result == 1:
                print('添加成功')
            # 4. 操作成功执行提交
            conn.commit()
    except pymysql.MySQLError as error:
        print(error)
        # 4. 操作失败执行回滚
        conn.rollback()
    finally:
        # 5. 关闭连接释放资源
        conn.close()


if __name__ == '__main__':
    main()
