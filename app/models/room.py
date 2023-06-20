import uuid

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy import TypeDecorator
from sqlalchemy.dialects import mysql
from sqlalchemy.dialects.mysql import BINARY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import sqltypes


Base = declarative_base()

class GUID(TypeDecorator):
    """Platform-independent GUID type."""

    impl = BINARY(16)

    def load_dialect_impl(self, dialect):
        if dialect.name == 'mysql':
            return dialect.type_descriptor(mysql.BINARY(16))
        else:
            return dialect.type_descriptor(sqltypes.CHAR(36))

    def process_bind_param(self, value, dialect):
        if value is not None:
            try:
                if not isinstance(value, uuid.UUID):
                    value = uuid.UUID(value)
                if dialect.name == "mysql":
                    return value.bytes
                else:
                    return str(value)
            except ValueError:
                raise ValueError(f"Invalid UUID value: {value}")

    def process_result_value(self, value, dialect):
        if value is not None:
            try:
                if dialect.name == "mysql":
                    return uuid.UUID(bytes=value)
                else:
                    return uuid.UUID(value)
            except ValueError:
                raise ValueError(f"Invalid UUID value: {value}")


class Room(Base):
    __tablename__ = "room"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    number = Column(Integer)
    available = Column(Boolean)

