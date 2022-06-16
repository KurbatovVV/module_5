import json
class Module():
	
	data={'title':'Python Course',
	      'text':'Module 5',
	      'author':'Brunoyam'
	      }

	
	def save(self):
		with open ('mod_5.json', 'w') as f:
			json.dump(self.data, f)


p=Module()
p.save()