from db_config import get_connection

def create_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (name, age) VALUES (%s, %s) RETURNING id;", (name, age))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"✅ Пользователь {name} добавлен с ID {user_id}")
    except Exception as e:
        conn.rollback()
        print("❌ Ошибка:", e)
    finally:
        cur.close()
        conn.close()

def read_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def read_one(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    return row

def update_user(user_id, new_name):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("UPDATE users SET name = %s WHERE id = %s;", (new_name, user_id))
        conn.commit()
        print(f"✅ Пользователь {user_id} обновлён")
    except Exception as e:
        conn.rollback()
        print("❌ Ошибка:", e)
    finally:
        cur.close()
        conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM users WHERE id = %s;", (user_id,))
        conn.commit()
        print(f"✅ Пользователь {user_id} удалён")
    except Exception as e:
        conn.rollback()
        print("❌ Ошибка:", e)
    finally:
        cur.close()
        conn.close()
