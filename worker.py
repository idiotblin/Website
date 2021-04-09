import datetime, time
import models
from models import Work
from database import SessionLocal, engine


db = SessionLocal()

models.Base.metadata.create_all(bind=engine)


def prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


while True:
    res = db.query(Work).filter_by(status='Queued').all()
    if len(res) > 0:
        task = res[0]
        task.status = 'Processing'
        db.add(task)
        db.commit()
        begin = datetime.datetime.now().second
        n = task.n
        for p in range(2, int(n ** 0.5) + 1):
            q = n // p
            if q * p == n and prime(p) and prime(q):
                end = datetime.datetime.now().second
                task.status = 'Done'
                task.p = p
                task.q = q
                task.elapsed = str(end - begin)
                db.add(task)
                db.commit()
                i = n
    time.sleep(5)
