from routes.__init__ import Annotated, Depends, HTTPException, status, router
from repositories.tasksDAO import TaskDAO, Task, TaskCreate, Usuario
from utils.auth_utils import get_current_user

taskDAO = TaskDAO()


@router.get("/tasks", status_code=status.HTTP_200_OK)
def listar_tarefas(user: Annotated[Usuario, Depends(get_current_user)], concluida: bool = None,limit: int = 10,offset: int = 0):
    tarefas = taskDAO.listar_tasks(user, concluida, limit, offset)
    return tarefas

@router.get("/task/{task_id}", status_code=status.HTTP_200_OK)
def tarefa_id(task_id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefa = taskDAO.listar_tasks_id(task_id, user)
    return tarefa

@router.post("/tasks", status_code = status.HTTP_201_CREATED)
def criar_tarefa(novo: TaskCreate, user: Annotated[Usuario, Depends(get_current_user)]):
    tarefa = taskDAO.criar_tarefa(novo, user)
    return tarefa

@router.put("/task/{task_id}", status_code=status.HTTP_200_OK)
def atualizar_tarefa(task_id: int, task_atualizada: Task, user: Annotated[Usuario, Depends(get_current_user)]):
    if tarefa_id(task_id, user):
        return taskDAO.atualizar_tarefa(task_id, task_atualizada, user)
    else:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
         detail=f'Não existe um tarefa eículo com id = {id}'
    )

@router.delete("/task/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(task_id:int, user: Annotated[Usuario, Depends(get_current_user)]):
    if tarefa_id(task_id, user):
        taskDAO.remover_tarefa(task_id, user)
        return {"message": "Tarefa excluida com sucesso!"}
    else:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Não existe um tarefa com id = {id}'
    )

