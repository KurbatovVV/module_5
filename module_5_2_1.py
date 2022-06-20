import json
class Module():

	title="Module_5"
	text="Python"
	author="Brunoyam"

	def __init__(self):
		self.title="name"
		self.tetx="Python"
		self.author="Brunoyam"

	def save(self):
		with open ('mod_5.json', 'w') as f:
			json.dump(o.__dict__, f)
			


o=Module()
print (o.__dict__)
o.save()




#json.dumps(self,default=lambda x: x.dict)