from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cats = [
    {
        "name": "Гуся",
        "photo": "https://memepedia.ru/wp-content/uploads/2019/03/dxdaey6uuaakpup-kopiya.jpg",
        "description": "Любит вкусно поесть гусей.",
        "comments": [
            {
                "author": "Александр",
                "text": "*людей...)))",
                "date": "13.37.28"
            }
        ],
        "likes": 60
    }
]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', cats=cats)


@app.route('/add', methods=['GET'])
def add_form():
    return render_template('add.html')


@app.route('/add', methods=['POST'])
def add():
    fields = ['name', 'photo', 'description']
    for field in fields:
        if request.form.get(field, '') == '':
            return redirect('/add')
    cat = {
        "name": request.form['name'],
        "description": request.form['description'],
        "photo": request.form['photo']
    }
    cats.append(cat)
    return redirect('/cats/{0}'.format(len(cats)))


@app.route('/cats/<id>', methods=['GET'])
def details(id):
    cat = cats[int(id) - 1]
    return render_template('details.html', cat=cat)


@app.route('/like/<id>', methods=['GET'])
def like():
    pass


@app.route('/comment/<id>', methods=['POST'])
def comment():
    pass


app.run(debug=True, port=8080)
