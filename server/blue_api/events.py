import functools
from flask import (
    Blueprint, flash, g, redirect, request, url_for
)

from blue_api.db import get_db

bp = Blueprint('events', __name__, url_prefix='/events')

@bp.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
      title = request.form['title']
      start_time = request.form['start_time']
      end_time = request.form['end_time']
      content = request.form['content']
      db = get_db()
      error = None

      if error is None:
        try:
          db.execute(
            "INSERT INTO events (title, start_time, end_time, content (?, ?, ?, ?)",
            (title, start_time, end_time, content),
          ) 
          db.commit()
        except db.IntegrityError:
          error = f"Event {title} is already registered"
        else:
          return 200
    return "Successful"