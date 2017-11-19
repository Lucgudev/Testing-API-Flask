from my_app import app
app.run(debug=True)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

