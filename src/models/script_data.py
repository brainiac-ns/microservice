from pydantic import BaseModel


class ScriptData(BaseModel):
    input_data: str
    script_name: str
