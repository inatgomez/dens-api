from django.utils.deprecation import MiddlewareMixin

class OAuthStateMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if '/o/google-oauth2/' in request.path:
            state = request.GET.get('state')
            if state:
                request.session['oauth_state'] = state