from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home/index.html")


@app.route("/about")
def about():
    return render_template("home/about.html")


@app.route("/questionnaire")
def questionnaire():
    return render_template("home/questionnaire.html")


@app.route("/result", methods=["GET", "POST"])
def result():

    if request.method == "POST":

        score = sum(int(request.form.get(f"q{i}", 0)) for i in range(1, 11))

        if score >= 85:
            nivel = "🌍 Eco Hero"
            color = "success"
            mensaje = "¡Excelente! Tus hábitos ayudan significativamente al planeta."
            recomendaciones = [
                "Continúa inspirando a otras personas.",
                "Participa en actividades ambientales.",
                "Comparte tus buenas prácticas."
            ]

        elif score >= 65:
            nivel = "🌱 Eco Explorer"
            color = "primary"
            mensaje = "Vas por muy buen camino. Aún puedes mejorar algunos hábitos."
            recomendaciones = [
                "Reduce el uso de plástico.",
                "Ahorra energía.",
                "Usa transporte sostenible."
            ]

        elif score >= 40:
            nivel = "♻️ Eco Learner"
            color = "warning"
            mensaje = "Puedes mejorar varios hábitos ambientales."
            recomendaciones = [
                "Recicla con mayor frecuencia.",
                "Reduce el consumo de agua.",
                "Apaga los aparatos eléctricos."
            ]

        else:
            nivel = "🌫 Eco Beginner"
            color = "danger"
            mensaje = "Es momento de comenzar a cuidar más el planeta."
            recomendaciones = [
                "Empieza separando residuos.",
                "Apaga las luces.",
                "Usa bolsas reutilizables."
            ]

        progress = f"width: {score}%;"

        return render_template(
            "home/result.html",
            score=score,
            nivel=nivel,
            color=color,
            mensaje=mensaje,
            recomendaciones=recomendaciones,
            progress=progress
        )

    return render_template("home/result.html", score=None)


if __name__ == "__main__":
    app.run(debug=True)