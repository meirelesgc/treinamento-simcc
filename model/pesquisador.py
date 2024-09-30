from pydantic import BaseModel, Field

class Pesquisador(BaseModel):
    lattes_id: str = Field(..., min_length=15, max_length=15)
    nome: str = Field(..., min_length=2, max_length=70)
    pesquisadores_id: str = Field(..., min_length=36, max_length=36)
    
