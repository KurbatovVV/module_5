class StringVar:
    text: str
 
    def __init__(self, text: str):
        self.set(text)
 
    def get(self):
        return self.text
 
    def set(self, text: str):
      	self.text = text


p=StringVar('Hello')
print (p.get())
p.set('Hello world')
print (p.get())