from models.__init__ import *

class TaskBase(BaseModel):
    titulo: str
    descricao: Optional[str]
    concluida: bool = False

class Task(TaskBase):
  id: int | None = None
  usuario_id: int | None = None

class TaskCreate(TaskBase):
    pass
