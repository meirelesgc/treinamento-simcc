from pydantic import BaseModel, Field

class PesquisadorSchema(BaseModel):
    nome: str = Field(..., min_length=2, max_length=70)
    lattes_id: str = Field(..., min_length=1, max_length=50)
    pesquisadores_id: str = Field(..., min_length=1, max_length=50)

    class Config:
        orm_mode = True
