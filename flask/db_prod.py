from notejam import db
from notejam import app as application
from notejam.config import ProductionConfig

application.config.from_object(ProductionConfig)

db.create_all(app=application)