import sqlite3 





def create_table_escuela():
    conn = sqlite3.connect("escuelas.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS escuelas (
            escuela_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            localidad TEXT ,
            provincia TEXT ,
            capacidad INTEGER 
            )
        """
    )
    conn.commit()
    conn.close()


def insert_escuela(nombre_escuela, localidad , provincia , capacidad):
    conn = sqlite3.connect("escuelas.db")
    cursor = conn.cursor()
    query = f"INSERT INTO escuelas (nombre, localidad, provincia, capacidad) VALUES( '{nombre_escuela}','{localidad}','{provincia}',{capacidad})"
    cursor.execute(query)
    conn.commit()
    conn.close()


def get_escuelas():
    conn = sqlite3.connect("escuelas.db")
    cursor = conn.cursor()    
    query = f"SELECT * FROM escuelas"
    cursor.execute(query)
    resultado = cursor.fetchall()
    conn.commit()
    conn.close()
    print(resultado)
   

def eliminar_escuela( id_escuela ):
    conn = sqlite3.connect("escuelas.db")
    cursor = conn.cursor() 
    query = f"DELETE FROM escuelas WHERE escuela_id = {id_escuela}"
    cursor.execute(query)
    conn.commit()
    conn.close()



def update_nombre_escuela(nombre , id_escuela):
    conn = sqlite3.connect("escuelas.db")
    cursor = conn.cursor() 
    query = f"UPDATE escuelas SET nombre = '{nombre}' where escuela_id = {id_escuela}"
    cursor.execute(query)
    conn.commit()
    conn.close()


#insert_escuela("Manuel Belgrano", "Carapachay","Buenos Aires", 100 )
#insert_escuela("Juan Manuel de Rosas", "Mataderos","CABA", 450 )
#create_table_escuela()

#eliminar_escuela(1)

#update_nombre_escuela("Manuel Belgrano", 2)
get_escuelas()


