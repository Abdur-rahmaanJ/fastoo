from fastoo.api.templates import render_template


class ReqMan:
    def __init__(self, module, request):
        self.module = module
        self.module.request = request

    def __enter__(self):
        return self.module 

    def __exit__(self, type, value, traceback):
        self.module.request = None

class Module:
    def __init__(self, path):
        self.path = path
        self.request = None 

    def set(self, request):
        return ReqMan(self, request)
    
    def render_template(self, path, template_vars):
        if self.request is None:
            raise Exception("Please call <with module.set(request) as m:> to set the current request")
        
        return render_template(path, template_vars, self.request)
        
    
