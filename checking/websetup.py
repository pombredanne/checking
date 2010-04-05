import logging
import transaction
from checking.model import meta
from checking import run

log = logging.getLogger(__name__)

def populateDatabase():
    from checking.model.account import Account
    session=meta.Session()
    admin=session.query(Account).filter(Account.login=="admin").first()
    if admin is None:
        log.info("Adding initial admin user")
        admin=Account(login="admin", password="admin",
                firstname=u"Admin", surname=u"Admin",
                email="discard@simplon.biz")
        session.add(admin)


def setup_app(command, conf, vars):
    run.app({}, **conf)
    meta.metadata.create_all()
    populateDatabase()
    transaction.get().commit()

