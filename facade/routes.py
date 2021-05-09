from flask import request

from facade.app import app
from facade.handlers import get_processed_post_request, \
    get_processed_get_request


@app.route('/facade-service', methods=['GET', 'POST'])
def facade_s():
    if request.method == 'POST':
        return get_processed_post_request()
    else:
        return get_processed_get_request()