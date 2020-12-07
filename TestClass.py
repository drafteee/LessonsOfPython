class Test:

  def __init__(self, name):
    self.name = name

  def run(self):
    print('run', self.name)

test = Test('name')
test.run() 
print(test.name)
