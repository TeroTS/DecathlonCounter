#####################################################################
#login page controller
#####################################################################
def login():
    form = FORM(TABLE(
        P('', INPUT(_type='decimal', _name='username', requires=IS_IN_DB(db, db.users.username, error_message='Vaara kayttajanimi !'))),
        P('', INPUT(_type='decimal', _name='password', requires=IS_IN_DB(db, db.users.password, error_message='Vaara salasana !'))),
        P('', INPUT(_type='submit', _value='OK'))
    ))

    if form.process().accepted:
        session.logged_in_user = True
        #initialize athletes list, has to be done here !
        session.athletes = []
        #age select for points calculation
        session.ageSelect = 'yleinen'
        redirect(URL('input', 'osallistujat2'))
    else:
        session.logged_in_user = False

    return dict(form=form)
