# DB functions for the app

import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker


# Create a database connection to the database postres username: postgres password: admin
def create_db_connection():
    try:
        engine = sqla.create_engine(
            'postgresql://postgres:admin@localhost:5432/postgres')
        connection = engine.connect()
        return connection
    except Exception as e:
        print("Error connecting to the database:", str(e))
        return None
# Create a table called names in the database
conn = create_db_connection()

def create_table(engine):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(
            sqla.text("CREATE TABLE IF NOT EXISTS names (id SERIAL PRIMARY KEY, name VARCHAR(255))"))
        session.commit()
        return True
    except Exception as e:
        print("Error creating table:", str(e))
        return False
create_table(conn)

# Insert a name into the database
def insert_name(engine, name):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        session.execute(
        sqla.text("INSERT INTO names (name) VALUES ('{}')".format(name)))
        session.commit()
        return True
    except Exception as e:
        print("Error inserting name:", str(e))
        return False
# insert_name(conn, 'John')

# Get all the names from the database
def get_names(engine):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
        result = session.execute(sqla.text("SELECT * FROM names"))
        return result
    except Exception as e:
        print("Error getting names:", str(e))
        return None

# Delete a name from the database

def delete_name(engine, idno):
    """
    Delete a name from the database based on the given id.

    Args:
        engine: The database engine.
        idno: The id of the name to be deleted.

    Returns:
        True if the name is successfully deleted, False otherwise.
    """
    try:
        session = sessionmaker(bind=engine)()
        session.execute(sqla.text(f"DELETE FROM names WHERE id = {idno}"))
        session.commit()
        return True
    except Exception as e:
        print("Error deleting name:", str(e))
        return False

# Update a name in the database
def update_name(engine, id, name):
    """
    Update a name in the database based on the given id.

    Args:
        engine: The database engine.
        id: The id of the name to be updated.
        name: The new name value.

    Returns:
        True if the name is successfully updated, False otherwise.
    """
    try:
        session = sessionmaker(bind=engine)()
        session.execute(sqla.text(f"UPDATE names SET name = '{name}' WHERE id = {id}"))
        session.commit()
        return True
    except Exception as e:
        print("Error updating name:", str(e))
        return False



# Delete everything from the database
def delete_all(engine):
    """
    Delete all names from the database.

    Args:
        engine: The database engine.

    Returns:
        True if all names are successfully deleted, False otherwise.
    """
    try:
        session = sessionmaker(bind=engine)()
        session.execute(sqla.text("DELETE FROM names"))
        session.commit()
        return True
    except sqla.exc.SQLAlchemyError as e:
        print("Error deleting names:", str(e))
        return False
