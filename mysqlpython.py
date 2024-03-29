# Roberta Pires - 02211057
#Avaliação SO
import mysql.connector


def insert_db(value1, value2, value3):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="pipo20012003",
            database="banco1"
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor()

            sql_query = "INSERT INTO prefArt(nomeUser,cpfUser, opcao_selec) VALUES (%s,%s,%s)"
            val = [value1, value2, value3]
            mycursor.execute(sql_query, val)

            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")
