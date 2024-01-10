from backend.complete import create_app
from os import urandom

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)