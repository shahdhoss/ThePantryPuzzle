from backend.complete import create_app
from os import urandom

app = create_app()
secret_key = urandom(24)
app.config["SECRET_KEY"] = secret_key
app.config["RECAPTCHA_USE_SSL"] = False
app.config["RECAPTCHA_PUBLIC_KEY"] = "6Lfer0kpAAAAAJnXGODihTewNcf3RDCXgc5FE7XY"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6Lfer0kpAAAAAEAtPP1igzvVEtUySFK8UpOCN57X"
app.config["RECAPTCHA_OPTIONS"] = {'theme' : 'black'}

if __name__ == '__main__':
    app.run(debug=True)