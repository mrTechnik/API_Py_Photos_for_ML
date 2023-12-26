from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class PhotoMetadata(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    photo_type: Mapped[str] = mapped_column(String, nullable=False)
    path: Mapped[str] = mapped_column(String, nullable=False)
    datetime_: Mapped[str] = mapped_column(String, nullable=False)

    def to_dict(self):
        return {'id': self.id, 'photo_type': self.photo_type, 'path': self.path, 'datetime': self.datetime_}

