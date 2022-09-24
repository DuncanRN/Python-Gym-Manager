from db.run_sql import run_sql
from models.class import Class
from models.member import Member

def save(class):
    sql = "INSERT INTO classes ( name ) VALUES ( %s ) RETURNING id"
    values = [class.name]
    results = run_sql( sql, values )
    class.id = results[0]['id']
    return class

