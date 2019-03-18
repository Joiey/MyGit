#import requests
def createGenerator():
  mylist = range(4)
  for i in mylist:
    yield i * i

mygenerator = createGenerator()
print(mygenerator)
for i in mygenerator:
  print(i)

def foo(end):
  previous, current = 1, 1
  while current < end:
    yield current
    previous, current = current, previous+current

fab = foo(200)
print(fab)
for i in fab:
  print(i)


