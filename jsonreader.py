import json

# def jsonReader(arg):
# # Opening JSON file
#   f = open('/home/pmillians/PycharmProjects/pythonProject1_readingJSONFiles/data.json')
#
# # returns JSON object as
# # a dictionary
#   data = json.load(f)
#
# # Iterating through the json
# # list
#   for i in data['emp_details']:
#     print(i)
#
# # Closing file
#   f.close()
#
#
# jsonReader('data.json')


myjsonfile=open('/home/pmillians/PycharmProjects/pythonProject1_readingJSONFiles/data.json','r')
jsondata=myjsonfile.read()
#obj =[]
obj=json.loads(jsondata)
print(str(obj['name']))
