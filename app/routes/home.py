from flask import render_template

from app import app
from app.forms.cutenessForm import cutenessForm


@app.route('/')  # Those decorators are used to associate the URL given as argument and the the function
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = cutenessForm()
    if form.validate_on_submit():
        plant_name = form.name.data
        plant_adjective = form.adjective.data

        return render_template('mypage.html', name=plant_name, adjective=plant_adjective)
    return render_template('home.html', title='Home', form=form)

