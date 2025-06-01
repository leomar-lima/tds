import sqlite3
from repositories.__init__ import Usuario, Task, TaskCreate, DB

class TaskDAO():
    def __init__(self):
        pass

    def listar_tasks(self, user: Usuario, concluida: bool = None, limit: int = 10, offset: int = 0):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'SELECT * FROM Tarefa WHERE usuario_id=?'
            params = [user.id]
            if concluida != None:
                sql += " AND concluida=?"
                params.append(concluida)

            sql += " LIMIT ? OFFSET ?"
            params.extend([limit, offset])

            cursor.execute(sql, tuple(params))
            task_list = cursor.fetchall()

            tasks: list[Task] = []

            for t in task_list:
                task = Task(id = t[0],
                            titulo = t[1],
                            descricao = t[2],
                            concluida = t[3],
                            usuario_id = t[4])
                tasks.append(task)
            return tasks 

    def listar_tasks_id(self, id: int, user: Usuario):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'SELECT * FROM Tarefa WHERE id = ? AND usuario_id=?'
            cursor.execute(sql,(id,user.id))
            resultado = cursor.fetchone()

            if not resultado:
                return None
            
            task = Task(id=resultado[0],
                        titulo=resultado[1],
                        descricao=resultado[2],
                        concluida=resultado[3],
                        usuario_id=resultado[4])
            
                
            return task

    def criar_tarefa(self, task: TaskCreate, user: Usuario):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql =  '''INSERT INTO Tarefa(titulo, descricao, concluida, usuario_id) 
            VALUES (?,?,?,?)'''
            cursor.execute(sql,(task.titulo,
                                task.descricao,
                                task.concluida,
                                user.id))
            id = cursor.lastrowid
            return Task(id=id,usuario_id=user.id, **task.dict())
    
    def atualizar_tarefa(self, id: int, task: Task, user: Usuario):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = '''UPDATE Tarefa SET
                    titulo = ?,
                    descricao = ?,
                    concluida = ?,
                    usuario_id = ?
                    WHERE id = ?'''
            cursor.execute(sql,(task.titulo,
                                task.descricao,
                                task.concluida,
                                user.id,
                                id))
            c.commit()
            return self.listar_tasks_id(id, user)
        
    def remover_tarefa(self, id: int, user: Usuario):
        with sqlite3.connect(DB) as c:
            cursor = c.cursor()
            sql = 'DELETE from Tarefa WHERE id = ? AND usuario_id=?'
            cursor.execute(sql,(id, user.id))
            resultado = cursor.fetchone()
            if not resultado:
                return