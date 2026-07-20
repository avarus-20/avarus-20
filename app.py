from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
meals = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        food = request.form['food']
        calories = request.form['calories']
        try:
            calories = int(calories)
        except ValueError:
            calories = 0
        meals.append({'food': food, 'calories': calories})
        return redirect(url_for('index'))
    total_calories = sum(m['calories'] for m in meals)
    return render_template('index.html', meals=meals, total=total_calories)

if __name__ == '__main__':
    app.run(debug=True)
