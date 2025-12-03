from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Devolvemos HTML con CSS integrado para que se vea profesional
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Proyecto Final DevOps</title>
        <style>
            body {
                background-color: #0d1117; /* Fondo oscuro estilo GitHub */
                color: #c9d1d9;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background-color: #161b22;
                border: 1px solid #30363d;
                border-radius: 15px;
                padding: 40px;
                text-align: center;
                box-shadow: 0 10px 25px rgba(0,0,0,0.5);
                max-width: 400px;
            }
            h1 {
                color: #58a6ff; /* Azul estilo link */
                font-size: 24px;
                margin-bottom: 10px;
            }
            h2 {
                color: #7ee787; /* Verde éxito */
                font-size: 18px;
                margin-top: 0;
                margin-bottom: 20px;
            }
            .tag {
                background-color: #238636;
                color: white;
                padding: 5px 10px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
                display: inline-block;
                margin-top: 15px;
            }
            p { font-size: 16px; line-height: 1.5; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Proyecto Final DevOps</h1>
            <h2>George - Matrícula 20240001</h2>
            <p>Hola Mundo desde DevOps.</p>
            <p>Esta aplicación fue desplegada automáticamente con GitHub Actions y Docker.</p>
            <div class="tag">ESTADO: ONLINE 🚀</div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)