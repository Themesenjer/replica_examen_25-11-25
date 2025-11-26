from flask import Flask
import random

app = Flask(__name__)

VERSION = "reyes-1.0.5"

tabla_posiciones = [
    {"pos": 1, "equipo": "Independiente del Valle", "puntos": 35, "pj": 15, "escudo": "🔵⚫"},
    {"pos": 2, "equipo": "LDU Quito", "puntos": 33, "pj": 15, "escudo": "⚪🔴"},
    {"pos": 3, "equipo": "Barcelona SC", "puntos": 31, "pj": 15, "escudo": "🟡⚫"},
    {"pos": 4, "equipo": "Universidad Católica", "puntos": 28, "pj": 15, "escudo": "🔵⚪"},
    {"pos": 5, "equipo": "Aucas", "puntos": 26, "pj": 15, "escudo": "🟡🔴"}
]

def predecir_campeon():
    candidatos = sorted(tabla_posiciones, key=lambda x: x['puntos'], reverse=True)[:3]
    ganador = random.choice(candidatos)
    probabilidad = random.randint(60, 95)
    return ganador['equipo'], probabilidad

@app.route('/')
def home():
    equipo_ia, prob_ia = predecir_campeon()

    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Liga Pro Ecuador - Réplica Examen</title>
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%); color: white; text-align: center; padding: 20px; }}
            .container {{ max-width: 800px; margin: 0 auto; background: rgba(255, 255, 255, 0.1); padding: 30px; border-radius: 15px; }}
            table {{ width: 100%; margin-top: 20px; background: rgba(255,255,255,0.9); color: black; border-radius: 10px; }}
            th, td {{ padding: 12px; border-bottom: 1px solid #ddd; }}
            th {{ background-color: #04AA6D; color: white; }}
            .ia-box {{ margin-top: 30px; padding: 20px; background: #ff9800; color: white; border-radius: 10px; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🇪🇨 Liga Pro - Tabla de Posiciones (Réplica Local)</h1>
            <table>
                <tr><th>Pos</th><th>Club</th><th>PJ</th><th>Puntos</th></tr>
                {''.join([f"<tr><td>{t['pos']}</td><td>{t['escudo']} {t['equipo']}</td><td>{t['pj']}</td><td>{t['puntos']}</td></tr>" for t in tabla_posiciones])}
            </table>

            <div class="ia-box">
                🤖 IA Predicción: <strong>{equipo_ia}</strong> ({prob_ia}%)
            </div>
            <p><em>Versión: {VERSION}</em></p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1002)
