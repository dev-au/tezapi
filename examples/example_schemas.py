from tezapi.schemas import SchemaModel


class UserSchema(SchemaModel):
    username: str
    phone_number: str


class CarSchema(SchemaModel):
    name: str
    number: str




