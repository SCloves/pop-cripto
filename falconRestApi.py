import json, falcon

class objRequestClass:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200
		data = json.loads(req.stream.read().decode('utf-8'))

		content = {
		'name': 'Cloves',
		'age': '28',
		'country': 'Brazil'
		}

		output = {}
		if 'method' not in data and 'name' not in data:
			resp.status = falcon.HTTP_501
			output['value'] = 'Error: none method found. Sorry!'
		elif 'name' in data:
			output['msg'] = 'Hello {0}'.format(data['name'])
		else:
			if data['method'] == 'get-name':
				output['value'] = content['name']
			else:
				resp.status = falcon.HTTP_404
				output['value'] = None
	
		resp.body = json.dumps(output)

	def on_post(self, req, resp):
		resp.status = falcon.HTTP_200
		data = json.loads(req.stream.read().decode('utf-8'))
		output = dict()
		equal = int(data['x']) + int(data['y'])
		output['msg'] = 'x: {0} + y: {1} is equal to {2}'.format(data['x'], data['y'], str(equal))
		resp.body = json.dumps(output)

api = falcon.API()
api.add_route('/test', objRequestClass())