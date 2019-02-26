from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from rankapp.auth import login_required
from rankapp.db import get_db

bp = Blueprint('tables', __name__)

@bp.route('/')
@login_required
def index():
    return render_template('tables/table1.html')

@bp.route('/table2')
@login_required
def second():
    return render_template('tables/table2.html')

@bp.route('/submit_table1')
def submit_table1():
    print("Done.")
