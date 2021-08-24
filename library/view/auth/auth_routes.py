from flask import render_template

from library.view.auth.auth_controller import AuthController


def auth_routes(app, controller: AuthController):
    @app.route("/login", methods=['POST'])
    def login():
        return controller.login()

    @app.route("/login", methods=['GET'])
    def login_page():
        return render_template("login.html")
