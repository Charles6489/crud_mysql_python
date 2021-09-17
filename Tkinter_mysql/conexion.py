import mysql.connector

class Articulos:
    def Conectar(self):
        conexion1 = mysql.connector.connect(host="localhost",
                                            user="root",
                                            passwd="",
                                            database="articulo")

        return conexion1
    def alta(self,datos):
        cone=self.Conectar()
        cursor = cone.cursor()
        sql ="insert into articulos(descripcion, precio) values (%s,%s)"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

    def consultar(self,datos):
        cone=self.Conectar()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql,datos)
        cone.close()
        return cursor.fetchall()

    def recuperar(self):
        cone=self.Conectar()
        cursor = cone.cursor()
        sql="select codigo, descripcion, precio from articulos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()

    def eliminar(self,datos):
        cone =self.Conectar()
        cursor = cone.cursor()
        sql="delete from articulos where codigo=%s"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()

        return cursor.rowcount

    def actualizar(self,datos):
        cone = self.Conectar()
        cursor = cone.cursor()
        sql="UPDATE articulos SET descripcion =%s , precio =%s WHERE codigo=%s"
        cursor.execute(sql,datos)
        cone.commit()
        cone.close()







