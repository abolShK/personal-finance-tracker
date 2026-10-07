from database.db import get_connection


def get_transaction_types():

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT id, name
        FROM transaction_types
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

def get_transaction_types_category():
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
        SELECT id , name
        FROM transactions.categories
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result
    

def add_transaction(
    amount,
    type_id,
    category_id,
    description,
    transaction_date
):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO transactions
        (amount, type_id, category_id, description, transaction_date)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        amount,
        type_id,
        category_id,
        description,
        transaction_date
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()