from aioapi.schemas import SchemaModel


class UserSchema(SchemaModel):
    name: str
    phone: int
