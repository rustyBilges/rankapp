import pandas as pd
import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from rankapp.auth import login_required, logout
from rankapp.db import get_db

bp = Blueprint('tables', __name__)

## using global variables for table data
##   A class would be more elegant but requires url endpoint rules
##   rather than decorators as currently used here.
df = pd.DataFrame()
df['Name'] = ['Paul Stephenson', 'Princess Campbell', 'Guy Bailey', 'Roy Hackett']
df['Bed'] = [1,3,5,11]
df['T_number'] = ['T38746', 'T18346', 'T32985', 'T23190']
df['Age'] = ['61', '52', '81', '77']
df['Admission'] = ['2019/01/25', '2019/03/01', '2019/02/18', '2019/02/22']

nrfd = {name:False for name in df['Name']}


@bp.route('/')
@login_required
def index():
    global df
    table_d = json.loads(df.to_json(orient='index'))
    columns = df.columns
                
    return render_template('tables/table1.html', columns=columns, 
                            table_data=table_d)

@bp.route('/table2')
@login_required
def table2():
    global df
    
    drop_rows = [i for i,name in enumerate(df['Name']) if nrfd[name]] 
    df_selected = df.drop(drop_rows, axis=0)
    table_d = json.loads(df_selected.to_json(orient='index'))
    columns = df_selected.columns
            
    return render_template('tables/table2.html', columns=columns, 
                            table_data=table_d)

@bp.route('/logout_msg')
def finish():
    logout()
    return render_template('tables/logout_msg.html')

@bp.route('/submit_table1', methods=('GET', 'POST'))
@login_required
def submit_table1():
    if request.method == 'POST':
        global df, nrfd
        for name in df['Name']:    
            selected = request.form[name]
            if selected=="selected":
                nrfd[name] = True
       
        print(nrfd)
    return redirect(url_for('tables.table2'))

@bp.route('/submit_table2', methods=('GET', 'POST'))
@login_required
def submit_table2():
    return redirect(url_for('tables.finish'))
