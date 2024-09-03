import json
import string
import random
# from drf_yasg import openapi
from datetime import datetime
from django.conf import settings
from rest_framework import status
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
# from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view,permission_classes
from rest_framework.generics import GenericAPIView
from django.core.exceptions import ObjectDoesNotExist,ValidationError


from to_do_list.settings import *
from core.serializer import *
from core.models import *
from core.mixin import *


#================================================DEFAULT_VIEW=================================================

class DefaultAPIView(APIView):
    def get(self, request):
        data = {
            "Welcome to To_Do_List project."
        }
        return Response(data)