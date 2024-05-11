from django.http import JsonResponse
import jwt
import json
from bson import json_util
    
    
# return Response("Login functionality goes here", status=status.HTTP_200_OK)
# TO GET API ENDPOINT
def get_endpoint(request):
    return request.path.split('/')[-1]

# INVALID API ENDPOINT
def invalid_endpoint_response(request):
    return JsonResponse({'Response': 'Invalid endpoint', 'Request': request}, status=500)

def encode_jwt(data, key):
    return jwt.encode(data, key, algorithm='HS256')

def decode_jwt(token, key):
    return jwt.decode(token, key, options={'verify_signature': False})
    # return jwt.decode(token, key,  algorithms=['HS256'])

def serializerVal(val):
       # Convert cursor to list of dictionaries
        listVal = list(val)
        
        # Convert BSON objects to JSON serializable format
        finalValues = json_util.dumps(listVal)
        return json.loads(finalValues)