from django.test import TestCase
import json
# Create your tests here.
d = {'name':'jason','password':'123','hobby':'读书'}
print(json.dumps(d,ensure_ascii=False))