from django.urls import path
from core.views import *

urlpatterns = [
#================================================Login========================================================

    path("", DefaultAPIView.as_view()),


]
