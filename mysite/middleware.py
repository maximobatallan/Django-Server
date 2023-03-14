class VisitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.visits = 0
    
    def __call__(self, request):
        self.visits += 1
        response = self.get_response(request)
    
        return response
    
    def process_template_response(self, request, response):
       
        response.context_data['visit_counter'] = self.visits

        return response

