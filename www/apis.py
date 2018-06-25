#coding=utf-8


import re,json,logging,functools

from transwarp.web import ctx

def dumps(obj):
	return json.dumps(obj)


class APIError(StandardError):
	"""docstring for APIError"""
	def __init__(self, error,data='',message=''):
		super(APIError, self).__init__(message)
		self.error = error
		self.data = data
		self.message = message



class APIValueError(APIError):
	"""docstring for APIValueError"""
	def __init__(self, field,message=''):
		super(APIValueError, self).__init__('value:invalid',field,message)



class APIResourceNotFoundError(APIError):
	"""docstring for APIResourceNotFoundError"""
	def __init__(self, field,message=''):
		super(APIResourceNotFoundError, self).__init__('value:notfound',field,message)


class APIPermissionError(APIError):
	"""docstring for APIPermissionError"""
	def __init__(self, arg):
		super(APIPermissionError, self).__init__('permission:forbidden','permission',message)


def api(func):

	@functools.wraps(func)

	def _wrapper(*args,**kw):
		try:
			r = dumps(func(*args,**kw))
		except APIError as e:
			r = json.dumps(dict(error=e.error,data=e.data,message=e.message))
		except Exception,e:
			logging.exception(e)
			r = json.dumps(dict(error='internalerror',data=e.__class__.__name__,message=e.message))
		ctx.response.content_type = 'application/json'
		return r 
	return _wrapper


if __name__ == '__main__':
	import doctest
	doctest.testmod()



		

		
		
