from __future__ import print_function
import eel
from views.models.login import login_user

eel.init('views')

@eel.expose
def btn_login(user_name, password):
    msg = login_user(user_name, password)
    eel.login_return(str(msg))

eel.start('index.html', size=(1366,743))