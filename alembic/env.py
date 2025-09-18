from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# -------------------------------
# Setup paths and import your models
# -------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app.db.session import Base  # SQLAlchemy Base
import app.models.user
import app.models.post

# -------------------------------
# Alembic Config
# -------------------------------
config = context.config

# Setup Python logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Point Alembic to SQLAlchemy models
target_metadata = Base.metadata

# -------------------------------
# Offline migrations
# -------------------------------
def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# -------------------------------
# Online migrations
# -------------------------------
def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# -------------------------------
# Run migrations depending on mode
# -------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
