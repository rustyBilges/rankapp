import pandas as pd
import json

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
    df = pd.DataFrame()
    df['Name'] = ['Paul Stephenson', 'Princess Campbell', 'Guy Bailey', 'Roy Hackett']
    df['Bed'] = [1,3,5,11]
    df['T_number'] = ['T38746', 'T18346', 'T32985', 'T23190']
    df['Age'] = ['61', '52', '81', '77']
    df['Admission'] = ['2019/01/25', '2019/03/01', '2019/02/18', '2019/02/22']
    table_d = json.loads(df.to_json(orient='index'))
    columns = df.columns
                
    return render_template('tables/table1.html', columns=columns, 
                            table_data=table_d)

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
        prodId = request.form["Guy Bailey"]
        print(prodId)
        prodId = request.form["Princess Campbell"]
        print(prodId)
    return redirect(url_for('tables.table2'))

@bp.route('/submit_table2', methods=('GET', 'POST'))
@login_required
def submit_table2():
    return redirect(url_for('tables.finish'))
