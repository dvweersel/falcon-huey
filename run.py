from app import create_app

if __name__ == '__main__':
    flaskapp_args = {"host": "0.0.0.0", "port": 5000}
    app = create_app()
    app.run(**flaskapp_args)
