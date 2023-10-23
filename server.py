from typing import Type, Union

import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from auth import hash_password
from models import Session, User
from schema import CreateUser, UpdateUser

firstapp = Flask("server_app")


class HttpError(Exception):
    def __init__(self, status_code: int, message: Union[str, dict, list]):
        self.status_code = status_code
        self.message = message


def error_handler(er):
    # Перехватывает исключения и останавливает выполнение программы
    response = jsonify({"status": "error", "message": er.message})
    response.status_code = er.status_code
    return response


def validate(validation_schema: Union[Type[CreateUser], Type[UpdateUser]], json_data):
    try:
        pydantic_obj = validation_schema(**json_data)
        return pydantic_obj.model_dump(exclude_none=True)
    except pydantic.ValidationError as er:
        raise HttpError(400, er.errors())


def get_user(session: Session, user_id: int):
    user = session.get(User, user_id)
    if user is None:
        raise HttpError(404, "User not found")
    return user


class UserViews(MethodView):
    def get(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            return jsonify(
                {
                    "id": user_id,
                    "name": user.name,
                    "creation_time": user.creation_time.isoformat(),    # Преобразует дату в строчку, для JSON.
                }
            )

    def post(self):
        validated_data = validate(CreateUser, request.json)
        validated_data["password"] = hash_password(validated_data["password"])
        with Session() as session:
            new_user = User(**request.json)
            session.add(new_user)
            try:
                session.commit()
            except IntegrityError as er:
                raise HttpError(409, "User already exist")
            return jsonify({"id": new_user.id})

    def patch(self, user_id: int):
        validated_data = validate(UpdateUser, request.json)
        if "password" in validated_data:
            validated_data["password"] = hash_password(validated_data["password"])
        with Session() as session:
            user = get_user(session, user_id)
            for field, value in validated_data.items():
                setattr(user, field, value)
            session.add(user)
            try:
                session.commit()
            except IntegrityError as er:
                raise HttpError(409, "User already exist")
            return jsonify({"id": user.id})

    def delete(self, user_id: int):
        with Session() as session:
            user = get_user(session, user_id)
            session.delete(user)
            session.commit()
            return jsonify({"Status": "Delete"})


user_view = UserViews.as_view("users")


# def hello_world(some_id):
#     """ Простая вьюшка """
#     json_data = request.json                  # Получаем запрос
#     headers = request.headers
#     qs = request.args
#     print('  Получен запрос:')
#     print(some_id)
#     print(json_data)
#     print(headers)
#     print(qs)
#
#     response = jsonify({"hello": "world"})    # Формируем ответ
#     print(f'  Наш ответ: {response.json}')
#     return response
#     print(f'\n Hi, id = {some_id} !!!')
#
# firstapp.add_url_rule('/hello/world/<int:some_id>', view_func=hello_world, methods=['POST'])

firstapp.add_url_rule("/user/<int:user_id>", view_func=user_view, methods=["GET", "PATCH", "DELETE"])

firstapp.add_url_rule("/user", view_func=user_view, methods=["POST"])

if __name__ == "__main__":
    firstapp.run()
