import atexit

from app import get_app
from errors import ApiError, error_handler
from views import UserView, login, register

from models import close_db, init_db

init_db()
atexit.register(close_db)

app = get_app()

app.add_url_rule("/register", view_func=register, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule(
    "/users/<int:user_id>",
    view_func=UserView.as_view("user"),
    methods=["GET", "PATCH", "DELETE"],
)

app.errorhandler(ApiError)(error_handler)
