from flask import Flask
from flask_cors import CORS
from flask_graphql import GraphQLView

from app.schema import schema

app = Flask('api-marvel-comics')

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(port=5000,use_reloader=True)
