import psycopg2
import os
import re
from datetime import datetime

conn = psycopg2.connect(
    dbname='postgres',
    user='postgres',
    password='13072007Aa',
    host='localhost',
    port='5432'
)
cur = conn.cursor()

# Get all currently recorded migrations
cur.execute("SELECT app, name FROM django_migrations;")
recorded = set((row[0], row[1]) for row in cur.fetchall())
print(f"Total recorded migrations in DB: {len(recorded)}")

# Find all migration files in the project
base_dir = os.path.dirname(os.path.abspath(__file__))
apps = ['authentication', 'author', 'book', 'order']
inserted = 0

for app in apps:
    migrations_dir = os.path.join(base_dir, app, 'migrations')
    if not os.path.exists(migrations_dir):
        continue
    for filename in sorted(os.listdir(migrations_dir)):
        if filename.endswith('.py') and filename != '__init__.py':
            migration_name = filename[:-3]  # remove .py
            if (app, migration_name) not in recorded:
                cur.execute(
                    "INSERT INTO django_migrations (app, name, applied) VALUES (%s, %s, %s)",
                    (app, migration_name, datetime.now())
                )
                print(f"  FAKED: {app}.{migration_name}")
                inserted += 1
            else:
                print(f"  OK:    {app}.{migration_name}")

conn.commit()
cur.close()
conn.close()
print(f"\nDone! Inserted {inserted} missing migration records.")
