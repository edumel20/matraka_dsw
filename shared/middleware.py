import logging
import time

logger = logging.getLogger(__name__)


class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code execution before view calling ↓
        start_time = time.time()
        # View calling ↓
        response = self.get_response(request)
        # Code execution after view calling ↓
        duration = time.time() - start_time
        print(f'Request to {request.path} took {duration * 1000:.4f} miliseconds')
        return response
