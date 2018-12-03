from . import web




@web.route('/')
def index():
    return 'web.index'


@web.route('/personal')
def personal_center():
    pass
