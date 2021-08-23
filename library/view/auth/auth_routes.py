from library.view.auth.auth_controller import AuthController


def auth_routes(app, controller: AuthController):
    @app.route("/login", methods=['POST'])
    def login():
        return controller.login()
