from conexion import Conexion
from persona import Persona
from logger_base import  log


class PersonDAO:
    '''
    DAO (data access Object)
    CRUD (crud insert update delete)
    '''

    _SELECIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s , apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def selecionar(cls):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute(cls._SELECIONAR)
                registros = cursor.fetchall()
                personas = []
                for registro in registros:
                    persona = Persona(registro[0], registro[1], registro[2], registro[3])
                    personas.append(persona)
                return personas

    @classmethod
    def insertar(cls,persona):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (persona.nombre, persona.apellido, persona.email)
                cursor.execute(cls._INSERTAR,valores)
                log.debug(f'persona a insertada : {persona}')
                return  cursor.rowcount

    @classmethod
    def actualizar(cls,persona):
        with Conexion.obtenerCursor() as cursor:
            with Conexion.obtenerCursor() as cursor:
                valores =(persona.nombre,persona.apellido,persona.email,persona.id_persona)
                cursor.execute(cls._ACTUALIZAR,valores)
                log.debug(f'Persona actualizada : {persona}')
                return cursor.rowcount

    @classmethod
    def eliminar(cls,persona):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (persona.id_persona,)
                cursor.execute(cls._ELIMINAR,valores)
                log.debug(f'Objeto eliminado : {persona}')
                return  cursor.rowcount


if __name__=='__main__':

    #insertar iin regosro

    #persona1 = Persona(nombre="predro",apellido="Rios",email="hkhk@gmail.com")
    #persona1_insertadas=PersonDAO.insertar(persona1)
    #log.debug(persona1_insertadas)

    #selecionar registros


     #actualizar persona

    #persona1 = Persona(16,'miguel','Ramirez','hsad@gmail.com')
    #personas_actualizdas = PersonDAO.actualizar(persona1)
    #log.debug(f'Personas actualizadas :{personas_actualizdas}')

    persona1 = Persona(id_persona=20)
    personas_eliminadas = PersonDAO.eliminar(persona1)
    log.debug(f'personas eliminadas : {personas_eliminadas}')

    personas = PersonDAO.selecionar()
    for persona in personas:
       log.debug(persona)




