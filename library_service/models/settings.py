import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://evans:local_silly@localhost:5432/library")
