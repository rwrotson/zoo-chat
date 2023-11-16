from datetime import datetime

from pydantic import BaseModel, validator, root_validator


class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True


class Bestiary(ORMBaseModel):
    title: str
    password: str
    creator_tg_id: int


class BirthInfo(BaseModel):
    date_of_birth: datetime
    longitude: float
    lassitude: float
    #
    # @classmethod
    # @validator('date_of_birth', pre=True)
    # def parse_birthdate(cls, value):
    #     if isinstance(value, datetime):
    #         return value
    #     return datetime.strptime(value, '%d.%m.%Y %H:%M')
    #
    # @classmethod
    # @validator('longitude', 'lassitude')
    # def float_result(cls, v):
    #     return round(v, 6)
    #
    # @classmethod
    # @validator('longitude', 'lassitude')
    # def value_is_longitude(cls, v):
    #     if not (-180 <= v <= 180):
    #         raise ValueError('Longitude is between -180 and 180º')
    #     return v
    #
    # @classmethod
    # @validator('longitude', 'lassitude')
    # def value_is_latitude(cls, v):
    #     if not (-90 <= v <= 90):
    #         raise ValueError('Latitude is between -90 and 90º')
    #     return v


class User(ORMBaseModel):
    telegram_id: int
    username: str
    birth_info: BirthInfo | None
    totem_animal: str | None


class Score(ORMBaseModel):
    varna: float
    vashya: float
    dina: float
    yoni: float
    grahamaitri: float
    gana: float
    rashi: float
    nadi: float
    sum_score: float

    @classmethod
    @root_validator()
    def check_if_sum_is_correct(cls, values):
        fields = (
            'varna', 'vashya', 'dina', 'yoni',
            'gragamaitri', 'gana', 'rashi', 'nadi'
        )
        sum_of_fields = sum([values[field] for field in fields])
        if abs(sum_of_fields - values['sum_score']) > 0.1:
            raise ValueError('Sum score does not match other fields')
        return values


class Compatibility(ORMBaseModel):
    user_1_id: int
    user_2_id: int
    score: Score


class Pairing(ORMBaseModel):
    bestiary: str
    type: str
    pair_ref: int


class Triangle(ORMBaseModel):
    bestiary: str
    type: str
    pair_ref_1_2: int
    pair_ref_2_3: int
    pair_ref_1_3: int
