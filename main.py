from flask import Flask
from flask_cors import CORS
from config.database import Base, engine
from routes.route import menu_bp, transaction_bp

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Daftarkan blueprint
app.register_blueprint(menu_bp)
app.register_blueprint(transaction_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
