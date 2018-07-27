from flask import jsonify, request

from forms.bookf import searchForm
from helper import search_book
from views import view


@view.route('/search')
def search():
    form = searchForm(request.args)

    if form.validate():
        return jsonify(search_book(form.data['q'], form.data['page']))
    else:
        return jsonify({'msg': form.errors})


@view.route('/')
def hello():
    return 'Hello'
