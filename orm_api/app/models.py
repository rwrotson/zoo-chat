from datetime import datetime as dt
from sqlalchemy import ForeignKey, DECIMAL, String, DateTime, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


association_table = Table(
    'bestiary_user_association',
    Base.metadata,
    Column('bestiary_id', ForeignKey('bestiary.id'), primary_key=True),
    Column('user_id', ForeignKey('user.id'), primary_key=True),
)


class Bestiary(Base):  # Isolated group of users
    __tablename__ = 'bestiary'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    creator_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    created_at: Mapped[dt] = mapped_column(DateTime, server_default=func.now())

    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    creator: Mapped['User'] = relationship(back_populates='creator_of')
    members: Mapped[list['User']] = relationship(
        secondary=association_table, back_populates='bestiaries'
    )

    def __repr__(self):
        return (
            f'<Bestiary: id {self.id}, '
            f'title {self.title}>'
        )


class BirthInfo(Base):
    __tablename__ = 'birth_info'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    date_of_birth: Mapped[dt] = mapped_column(DateTime, nullable=False)
    longitude: Mapped[float] = mapped_column(DECIMAL(8, 6), nullable=False)
    lassitude: Mapped[float] = mapped_column(DECIMAL(8, 6), nullable=False)

    user: Mapped['User'] = relationship(back_populates='birth_info')

    def __repr__(self):
        return (
            f'<BirthInfo: id {self.id}, '
            f'date_of_birth {self.date_of_birth}, '
            f'longitude {self.longitude}, '
            f'lassitude {self.lassitude}>'
        )


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[dt] = mapped_column(DateTime, server_default=func.now())

    telegram_id: Mapped[int] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(nullable=False)
    totem_animal: Mapped[str] = mapped_column(String(20), nullable=True)

    birth_info: Mapped[BirthInfo] = relationship(back_populates='user')
    creator_of: Mapped[Bestiary] = relationship(back_populates='creator')
    bestiaries: Mapped[list[Bestiary]] = relationship(
        secondary=association_table, back_populates='members'
    )

    def __repr__(self):
        return (
            f'<User: id {self.id}, '
            f'telegram_id {self.telegram_id}, '
            f'username {self.username}, '
            f'birth info: {self.birth_info}, '
            f'totem_animal {self.totem_animal}>'
        )


class Score(Base):
    __tablename__ = 'score'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    compatibility_id: Mapped[int] = mapped_column(ForeignKey('compatibility.id'))

    varna: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    vashya: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    dina: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    yoni: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    grahamaitri: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    gana: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    rashi: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    nadi: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)
    sum: Mapped[float] = mapped_column(DECIMAL(3, 1), nullable=False)

    compatibility: Mapped['Compatibility'] = relationship(back_populates='score')

    def __repr__(self):
        return (
            f'<Score: id {self.id}, '
            f'varna {self.varna}, '
            f'vashya {self.vashya}, '
            f'dina {self.dina}, '
            f'yoni {self.yoni}, '
            f'grahamaitri {self.grahamaitri}, '
            f'gana {self.gana}, '
            f'rashi {self.rashi}, '
            f'nadi {self.nadi}, '
            f'sum {self.sum}>'
        )


class Compatibility(Base):
    __tablename__ = 'compatibility'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    score: Mapped[Score] = relationship(back_populates='compatibility')

    user_1_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    user_2_id: Mapped[int] = mapped_column(ForeignKey('user.id'))

    def __repr__(self):
        return (
            f'<Compatibility: id {self.id}, '
            f'user_1 {self.user_1_id}, '
            f'user_2 {self.user_2_id}, '
            f'score: {self.score}>'
        )


class Pairing(Base):
    __tablename__ = 'pairing'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bestiary_id: Mapped[int] = mapped_column(ForeignKey('bestiary.id'))
    compatibility_id: Mapped[int] = mapped_column(ForeignKey('compatibility.id'))

    type: Mapped[str] = mapped_column(String(10), nullable=False)
    bestiary: Mapped[Bestiary] = relationship()

    def __repr__(self):
        return (
            f'<Pairing: id {self.id}, '
            f'bestiary {self.bestiary}, '
            f'type {self.type}, '
            f'compatibility_id {self.compatibility_id}>'
        )


class Triangle(Base):
    __tablename__ = 'triangle'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    bestiary_id: Mapped[int] = mapped_column(ForeignKey('bestiary.id'))
    pair_ref_1_2: Mapped[int] = mapped_column(ForeignKey('compatibility.id'))
    pair_ref_2_3: Mapped[int] = mapped_column(ForeignKey('compatibility.id'))
    pair_ref_1_3: Mapped[int] = mapped_column(ForeignKey('compatibility.id'))

    type: Mapped[str] = mapped_column(String(10), nullable=False)
    bestiary: Mapped[Bestiary] = relationship()

    def __repr__(self):
        return (
            f'<Triangle: id {self.id}, '
            f'bestiary {self.bestiary}'
            f'type {self.type}, '
            f'pair_ref_1_2 {self.pair_ref_1_2}, '
            f'pair_ref_2_3 {self.pair_ref_2_3}, '
            f'pair_ref_1_3 {self.pair_ref_1_3}>'
        )
