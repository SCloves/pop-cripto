import json, falcon

class objRequestClass:
	def on_get(self, req, resp):
		content = {
		'name': 'Cloves',
		'age': '28',
		'country': 'Brazil'
		}

		resp.body = json.dumps(content)


api = falcon.API()
api.add_route('/test', objRequestClass())