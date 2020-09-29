from  flask import jsonify

def generateResponse(data,msg):
	response_data = {}
	data_list = []
	try:
		for i in data:
			temp = {}
			temp["name"] = i[0]
			temp["number"] = i[1]
			temp["address"] = i[2]
			temp["type"] = i[3]
			temp["size"] = i[4]
			temp["order_id"] = i[5]
			data_list.append(temp)
			response_data["data"]=data_list

		response_data["msg"]=msg
		print(f'Respone data : {response_data}')
		return jsonify(response_data)

	except IndexError as e:
		print(e)
		return ReturnInvalidData()


