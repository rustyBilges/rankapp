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
