# Import all the models, so that Base has them before being
# import by Alembic
from app.db.base_class import Base
from app.models.user import User
from app.models.recipe import Recipe