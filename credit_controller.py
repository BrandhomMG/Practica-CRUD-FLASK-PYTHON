from db import get_db

def insert_credit(cliente, monto, tasa_interes, plazo, fecha_otorgamiento):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO CREDITOS(cliente, monto, tasa_interes, plazo, fecha_otorgamiento) VALUES(?,?,?,?,?)"
    cursor.execute(statement, [cliente, monto, tasa_interes, plazo, fecha_otorgamiento])
    db.commit()
    return True

def update_credit(id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE CREDITOS SET cliente = ?, monto = ?, tasa_interes = ?, plazo = ?, fecha_otorgamiento = ? WHERE id = ?"
    cursor.execute(statement, [cliente, monto, tasa_interes, plazo, fecha_otorgamiento, id])
    db.commit()     
    return {"success": True}

def delete_credit(id):
    db = get_db()
    cursor = db.cursor()
    statement  ="DELETE FROM CREDITOS WHERE id = ?"
    cursor.execute(statement,[id])
    db.commit()
    return True

def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento FROM CREDITOS WHERE id = ?"
    cursor.execute(statement,[id])
    return cursor.fetchone()

def get_credits():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, cliente, monto, tasa_interes, plazo, fecha_otorgamiento FROM CREDITOS"
    cursor.execute(query)
    credits = cursor.fetchall()

    credit_list = []
    for credit in credits:
        credit_dict = {
            "id": credit[0],
            "cliente": credit[1],
            "monto": credit[2],
            "tasa_interes": credit[3],
            "plazo": credit[4],
            "fecha_otorgamiento": credit[5],
        }
        credit_list.append(credit_dict)

    return credit_list

def get_credit_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT cliente, monto FROM CREDITOS")  # Ajusta la consulta si necesitas más datos
    data = cursor.fetchall()

    clientes = [row[0] for row in data]  # Lista de clientes
    montos = [row[1] for row in data]  # Lista de montos

    return {"clientes": clientes, "montos": montos}