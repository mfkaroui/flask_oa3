from .base import App
from flask import Flask, jsonify, request

class FlaskApp(App):
    def init_app(self) -> Flask:
        app = Flask(import_name=self.title)
        
        @app.route(self.get_route("openapi.json"), methods=["GET"])
        def oa3_spec_route():
            return jsonify(self.oa3_spec)

        @app.route(self.get_route("docs"), methods=["GET"])
        def docs_route():
            return """
<!DOCTYPE html>
<html>
  <head>
    <title>""" + self.title + """ API Documentation</title>
    <!-- needed for adaptive design -->
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css?family=Montserrat:300,400,700|Roboto:300,400,700" rel="stylesheet">

    <!--
    Redoc doesn't change outer page styles
    -->
    <style>
      body {
        margin: 0;
        padding: 0;
      }
    </style>
  </head>
  <body>
    <redoc spec-url='""" + self.get_route("openapi.json") + """'></redoc>
    <script src="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js"> </script>
  </body>
</html>
"""

        #initialize routes for views registered directly with the app
        for route, view in self.views.items():
            for method, method_properties in view.get_all_methods().items():
                @app.route(self.get_route(route), methods=[method.upper()])
                def view_route():
                    return method_properties["function"]()
        #initialize routes for namespaces registered with the app
        for _, namespace in self.namespaces.items():
            for route, view in namespace.views.items():
                methods = view.get_all_methods()
                if len(methods) > 0:
                    @app.route(self.get_route(namespace.get_route(route)), methods=[m.upper() for m in methods])
                    def namespaced_route():
                        request_view = view()
                        request.data
                        response = methods[request.method.lower()]["function"](request_view, {})
                        match type(methods[request.method.lower()]["type_hints"]["return"]).__name__:
                            case "_UnionGenericAlias":
                                pass
                            case _:
                                pass
        return app