"""
 * @Author: Jun Wu 
 * @Date: 2019-01-21 14:55:54 
 * @Last Modified by:  
 * @Last Modified time: 2019-01-21 15:08:15
 */
 """

def setTag(tag):  #定义装饰器，可能带参数
  def decorator(func):  #装饰器核心，以被装饰的函数对象为参数，返回装饰后的函数对象
    def wrapper(*args, **kvargs):  #装饰的过程，参数列表适应不同参数的函数
      sign = '<' + tag + '>'
      return sign + func(*args, **kvargs) +sign  #调用函数
    return wrapper
  return decorator
 
@setTag('tag')  #给函数加上装饰器
def hello(name):  #自己定义的功能函数
  helloName = 'hello' + name
  print(helloName)
  return helloName

