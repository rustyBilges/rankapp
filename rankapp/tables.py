from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from rankapp.auth import login_required, logout
from rankapp.db import get_db

bp = Blueprint('tables', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('tables/table1.html')

@bp.route('/table2')
@login_required
def table2():
    return render_template('tables/table2.html')

@bp.route('/logout_msg')
def finish():
    logout()
    return render_template('tables/logout_msg.html')

@bp.route('/submit_table1', methods=('GET', 'POST'))
@login_required
def submit_table1():
    if request.method == 'POST':
        prodId = request.form['prodId']
        print(prodId)
        prodId = request.form["myname"]
        print(prodId)
    return redirect(url_for('tables.table2'))

@bp.route('/submit_table2', methods=('GET', 'POST'))
@login_required
def submit_table2():
    return redirect(url_for('tables.finish'))
