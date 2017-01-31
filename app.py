import connexion

def post_world():
    return "hello world"

app = connexion.App(__name__, 9090)
app.add_api('swagger.yaml')

if __name__ == '__main__':
    app.run()