from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} already exists'.format(name)}

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {'message': 'Was not possible save to db'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_to_db()
        return {'message': 'Store was successfully deleted'}


class StoreList(Resource):
    def get(self):
        return {'stores': list(map(lambda x : x.json(), StoreModel.query.all()))}
