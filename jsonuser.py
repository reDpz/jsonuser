import json as j
class user:
    def __init__(self,username):
        self.username = username
    def store(self):
        with open('data.json', 'w+') as data:
            data.write(j.dumps({'username':self.username}), indent = 2)
        print('written')
    def load(self):
        with open('data.json','r') as data:
            self.dictionary = j.load(data)
        print(self.dictionary)
    def CheckContents(self):
        if 'username' not in self.dictionary:
            print('Username missing')
        else:
            print('username exists')
test = user('test')
test.load()
test.CheckContents()    