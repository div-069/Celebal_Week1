from flask import Flask, render_template, request

app = Flask(__name__)

def generate_triangle(triangle_type, size):
    size = int(size)
    lines = []

    if triangle_type == "lower":
        for i in range(1, size + 1):
            lines.append("* " * i)
    elif triangle_type == "upper":
        for i in range(size, 0, -1):
            lines.append("* " * i)
    elif triangle_type == "pyramid":
        for i in range(1, size + 1):
            lines.append(" " * (size - i) + "* " * i)
    return lines

@app.route('/', methods=['GET', 'POST'])
def index():
    triangle = []
    triangle_type = None
    if request.method == 'POST':
        triangle_type = request.form['triangle_type']
        size = request.form['size']
        triangle = generate_triangle(triangle_type, size)
    return render_template('index.html', triangle=triangle, triangle_type=triangle_type)

if __name__ == '__main__':
    app.run(debug=True)
