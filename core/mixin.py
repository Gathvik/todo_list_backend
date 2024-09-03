import os
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
from django.conf import settings
import environ
from django.conf import settings
from datetime import datetime
from core.models import *
from core.serializer import *
from django.core.exceptions import ObjectDoesNotExist
from datetime import date,datetime