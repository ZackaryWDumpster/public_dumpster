
from pydantic import BaseModel
from pydantic.main import ModelMetaclass

class UIDMeta(ModelMetaclass):
    _instances = {}

    def __call__(cls, **kwargs):
        id = kwargs.get("id")
        if id not in cls._instances:
            cls._instances[id] = super().__call__(**kwargs)
        return cls._instances[id]
    

class UIDItem(BaseModel, metaclass=UIDMeta):
    id : str