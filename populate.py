from app import db, create_app
from app.models import *

from datetime import datetime

app = create_app('development')
app.app_context().push()



def scrap():
    Event.query.delete()
    Showing.query.delete()
    db.session.commit()


def main():
    for i in range(1, 5):
        e = Event(name='Event {}'.format(i), body='Event {} Body --------'.format(i))
        db.session.add(e)
        db.session.commit()

        s = Showing(
            event_id=e.id,
            date=datetime(2020, 7, i),
            num_tickets=i*3+1,
        )
        db.session.add(s)
        db.session.commit()


        for j in range(1, 3):
            tt = TicketType(
                name='Ticket type {}'.format(j),
                price=25.0,
                showing_id=s.id,
            )
            db.session.add(tt)
        db.session.commit()


scrap()
main()
    
    