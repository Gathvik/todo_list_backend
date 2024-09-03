import os
import re
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator
from core.models import *