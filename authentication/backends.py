# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model
# from keycloak import KeycloakOpenID


# class KeycloakAuthenticationBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         keycloak_openid = KeycloakOpenID(
#             server_url='http://localhost:8080/auth/',
#             client_id='myapp',
#             realm_name='myrealm',
#             client_secret_key='myappsecret',
#         )

#         token = keycloak_openid.token(username, password)

#         if token:
#             User = get_user_model()
#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 user = User(username=username)
#                 user.set_unusable_password()
#                 user.save()

#             return user

#     def get_user(self, user_id):
#         User = get_user_model()
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None
