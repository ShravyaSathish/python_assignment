# from .models import *
# from rest_framework_simplejwt.tokens import RefreshToken
# from datetime import datetime, timedelta, timezone


# def generateToken(user):
#     try:

#         checIfExists = Refresh_Token.objects.get(user=user)
#         if checIfExists.expiration_date > datetime.now(timezone.utc):
#             refresh = RefreshToken.for_user(user)
#             new_access_token = str(refresh.access_token)
#             return new_access_token
#         else:

#             checIfExists.delete()
#     except Refresh_Token.DoesNotExist:
#         pass

#     refresh = RefreshToken.for_user(user)
#     refresh_token = str(refresh)
#     expiration_date = datetime.now(timezone.utc) + timedelta(days=5)
#     access_token = str(refresh.access_token)
#     Refresh_Token.objects.create(user = user, refresh_token = refresh_token, expiration_date=expiration_date)
#     return access_token