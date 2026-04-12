from src.config.db import get_db

def get_or_create_cart(user_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM carts WHERE user_id=%s", (user_id,))
    cart = cur.fetchone()

    if not cart:
        cur.execute(
            "INSERT INTO carts (user_id) VALUES (%s) RETURNING *",
            (user_id,)
        )
        cart = cur.fetchone()
        conn.commit()

    cur.close()
    conn.close()
    return cart

def get_cart_items(cart_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM cart_items WHERE cart_id=%s", (cart_id,))
    items = cur.fetchall()

    cur.close()
    conn.close()
    return items

def add_item(cart_id, product_id, quantity, price):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO cart_items (cart_id, product_id, quantity, price_at_add)
        VALUES (%s, %s, %s, %s)
        RETURNING *
    """, (cart_id, product_id, quantity, price))

    item = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return item

def update_item(item_id, quantity):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        UPDATE cart_items
        SET quantity=%s
        WHERE id=%s
        RETURNING *
    """, (quantity, item_id))

    item = cur.fetchone()
    conn.commit()

    cur.close()
    conn.close()
    return item

def delete_item(item_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM cart_items WHERE id=%s", (item_id,))
    conn.commit()

    cur.close()
    conn.close()

def get_total(user_id):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        SELECT SUM(quantity * price_at_add) AS total
        FROM cart_items ci
        JOIN carts c ON ci.cart_id = c.id
        WHERE c.user_id=%s
    """, (user_id,))

    total = cur.fetchone()

    cur.close()
    conn.close()
    return total

def get_all_carts():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("SELECT * FROM carts")
    carts = cur.fetchall()

    cur.close()
    conn.close()
    return carts