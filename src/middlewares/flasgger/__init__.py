from src.controllers import app, base_folder
from flasgger import Swagger


openapi_path = base_folder + "/src/middlewares/flasgger/openapi/"
template = {
    "info": {
        "title": "My API",
        "description": "Swagger UI for My API",
        "contact": {
            "responsibleOrganization": "ImmaBe",
            "responsibleDeveloper": "App Developer",
            #"email": "appdeveloper@immabe.io",
            #"url": "https://immabe.io/developers",
        },
        "termsOfService": "https://immabe.io/?p=terms",
        "version": "1.0.0"
    },
    #   "host": "mysite.com",  
    "schemes": [
        "https"
    ],
    "components" : {
        "securitySchemes": {
            "bearerAuth": {
                "type": "http",
                "scheme": "bearer",
                "bearerFormat": "JWT"
                #"in": "header",
                #"name": "Authorization"
            }
        }
    },
    'uiversion': 3,
}
app.config['SWAGGER'] = {
    'openapi': '3.0.2',
    'title': 'VSuite API',
    'uiversion': 3,
}

swagger = Swagger(app, template=template)