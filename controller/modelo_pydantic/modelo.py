from pydantic import BaseModel, Field

class PesquisadorSchema(BaseModel):
    nome: str = Field(..., min_length=2, max_length=70)
    lattes_id: str = Field(..., min_length=15, max_length=15)
    pesquisadores_id: str = Field(..., min_length=36, max_length=36)

    class Config:
        orm_mode = True
