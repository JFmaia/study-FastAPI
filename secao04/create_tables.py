from core.database import engine
from models import cursos_model

cursos_model.Base.metadata.create_all(bind=engine)