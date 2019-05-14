def commit_to_db(data):
    from src import db
    db.session.add(data)
    db.session.commit()
