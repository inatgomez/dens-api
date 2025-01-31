import logging
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djoser.social.views import ProviderAuthView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

logger = logging.getLogger(__name__)

class CustomProviderAuthView(ProviderAuthView):
    def post(self, request, *args, **kwargs):
        stored_state = request.session.get('oauth_state')
        incoming_state = request.data.get('state')
        
        if not stored_state or stored_state != incoming_state:
            return Response(
                {"detail": "Invalid state parameter"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            if 'oauth_state' in request.session:
                del request.session['oauth_state']
                
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            logger.debug(f"Access Token: {access_token}")
            logger.debug(f"Refresh Token: {refresh_token}")

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')
            refresh_token = response.data.get('refresh')

            logger.debug(f"Access Token: {access_token}")
            logger.debug(f"Refresh Token: {refresh_token}")

            response.set_cookie(
                'access',
                access_token,
                domain=settings.AUTH_COOKIE_DOMAIN,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
            response.set_cookie(
                'refresh',
                refresh_token,
                domain=settings.AUTH_COOKIE_DOMAIN,
                max_age=settings.AUTH_COOKIE_REFRESH_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )
        
        return response
    
class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh')

        logger.debug(f"Refresh Token from Cookie: {refresh_token}")

        if refresh_token:
            request.data['refresh'] = refresh_token

        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            access_token = response.data.get('access')

            response.set_cookie(
                'access',
                access_token,
                max_age=settings.AUTH_COOKIE_ACCESS_MAX_AGE,
                path=settings.AUTH_COOKIE_PATH,
                secure=settings.AUTH_COOKIE_SECURE,
                httponly=settings.AUTH_COOKIE_HTTP_ONLY,
                samesite=settings.AUTH_COOKIE_SAMESITE
            )

        return response

class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        access_token = request.COOKIES.get('access')

        logger.debug(f"Access Token from Cookie: {access_token}")

        if not access_token:
            return Response(
                {'detail': 'Missing access token in cookies'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        request.data['token'] = access_token
        return super().post(request, *args, **kwargs)
    
class Logoutview(APIView):
    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access')
        response.delete_cookie('refresh')

        logger.debug("Cookies deleted on logout")

        return response