from flask import Flask
import os
from flask_cors import CORS
from config.database import Base, engine
from routes.route import menu_bp, transaction_bp

Base.metadata.create_all(bind=engine)

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Daftarkan blueprint
app.register_blueprint(menu_bp)
app.register_blueprint(transaction_bp)

# Root route sederhana agar frontend/landing muncul saat domain dibuka
@app.get("/")
def index():
    return (
        """
        <html>
          <head>
            <meta name=viewport content="width=device-width, initial-scale=1" />
            <title>3AWAN Cafe & Resto API</title>
            <style>
              body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }
              .card { max-width: 680px; margin: 0 auto; padding: 20px; border: 1px solid #e5e7eb; border-radius: 12px; }
              h1 { font-size: 20px; margin: 0 0 8px; }
              p { margin: 8px 0; color: #374151; }
              code { background: #f3f4f6; padding: 2px 6px; border-radius: 6px; }
              a { color: #2563eb; text-decoration: none; }
            </style>
          </head>
          <body>
            <div class="card">
              <h1>3AWAN Cafe & Resto API</h1>
              <p>API berjalan. Gunakan endpoint yang tersedia pada aplikasi.</p>
              <p>Contoh endpoint: <code>/menu</code>, <code>/transaction</code></p>
            </div>
          </body>
        </html>
        """,
        200,
        {"Content-Type": "text/html; charset=utf-8"}
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
