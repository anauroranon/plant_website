from flask import render_template
from app import app


@app.route('/mypage', methods=['GET', 'POST'])
def mypage():
    return render_template('mypage.html', title='MyPage')
