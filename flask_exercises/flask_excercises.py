from flask import Flask, request, jsonify, make_response


class FlaskExercise:
    users = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        @app.route("/user", methods=["POST"])
        def create_user():
            data = request.get_json()
            if "name" not in data:
                return make_response(jsonify({"errors": {"name": "This field is required"}}), 422)
            FlaskExercise.users[data["name"]] = data
            return make_response(jsonify({"data": f"User {data['name']} is created!"}), 201)

        @app.route("/user/<name>", methods=["GET"])
        def get_user(name: str):
            user = FlaskExercise.users.get(name)
            if not user:
                return make_response(jsonify({"error": "User not found"}), 404)
            return make_response(jsonify({"data": f"My name is {name}"}), 200)

        @app.route("/user/<name>", methods=["PATCH"])
        def update_user(name: str):
            data = request.get_json()
            if "name" not in data:
                return make_response(jsonify({"errors": {"name": "This field is required"}}), 422)
            if name not in FlaskExercise.users:
                return make_response(jsonify({"error": "User not found"}), 404)
            FlaskExercise.users[data["name"]] = data
            return make_response(jsonify({"data": f"My name is {data['name']}"}), 200)

        @app.route("/user/<name>", methods=["DELETE"])
        def delete_user(name: str):
            if name not in FlaskExercise.users:
                return make_response(jsonify({"error": "User not found"}), 404)
            del FlaskExercise.users[name]
            return "", 204
