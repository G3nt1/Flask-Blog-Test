import sqlite3


def get_db():
    """
        Krijon nje lidhje me databazen dhe kthen connection dhe cursor per te ekzekutuar query
    """
    db = sqlite3.connect("blog.db3")
    db.row_factory = sqlite3.Row

    return db, db.cursor()


def get_db_cursor():
    return get_db()[1]
