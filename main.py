import flask
import flask_oa3

class BaseRoute(flask_oa3.View):
    def get(self, **kwargs):
        pass

    def post(self, **kwargs):
        pass

    def put(self, **kwargs):
        pass

    def delete(self, **kwargs):
        pass
    
    def patch(self, **kwargs):
        pass

if __name__ == "__main__":
    app = flask.Flask(__name__)
    api = flask_oa3.API(app)
    api.set_spdx_license_info(flask_oa3.Licenses.license_gpl_3_0, "https://google.com")
    namespace = flask_oa3.Namespace("base", "/")
    namespace.register_view(BaseRoute)
    api.register_namespace(namespace)