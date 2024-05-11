from django.http import JsonResponse
from rest_framework.views import APIView
from bson import ObjectId, json_util
from pymongo.errors import PyMongoError
import json
import array
import datetime
from ..common.utils import get_endpoint, invalid_endpoint_response, encode_jwt, decode_jwt, serializerVal
from ..config import db

class LoginAPI(APIView):
    # GET METHOD
    def get(self, request):
        return self.commonEndpoint(request)
        
    # POST METHOD
    def post(self, request):
        return self.commonEndpoint(request)
       
    # COMMON API METHOD
    def commonEndpoint(self, request):
        endpoint = get_endpoint(request)
        if endpoint == 'GetLoginDetails':
            return self.login(request)
        elif endpoint == 'CreateUserAddress':
            return self.createUserAddress(request)
        else:
            return invalid_endpoint_response(request)
    
    # GET CURRENT TIME
    def currentTime(self):
        return datetime.datetime.now()
    
    # FUNCTION BEGIN
    # LOGIN FUNCTION BEGIN
    def login(self, request):
        decodeData = json.loads(request.body)
        decodeData = decode_jwt(decodeData.get("loginTokenData"), 'MemberCollectionBankStatementPDFKey')
        try:
            # Fetch the inserted document from MongoDB
            fetched_document =  serializerVal(db['tblUser'].find(filter = {'userPhone': '9094538125'}))
        
            return JsonResponse({'Response': 'Sucess', 'document': fetched_document}, status=201)
        except PyMongoError as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
        
    # LOGIN FUNCTION BEGIN
    def loginPost(self, request):
        data = json.loads(request.body)
        return JsonResponse({'UserPhone': data.get("UserPhone")}, status=200)
    
    def createUserAddress(self, request):
        resultArr = []
        responseMessage = 'CREATE ADDRESS FAILED'
        decodeData = json.loads(request.body)
        decodeData = decode_jwt(decodeData.get("loginTokenData"), 'MemberCollectionBankStatementPDFKey')
        try:
            # Fetch the inserted document from MongoDB
            fetched_document =  serializerVal(db['tblUser'].find(filter = {'userPhone': '9486740812'}))
            
            json_document = {
                # 'user_id': ObjectId(str(fetched_document[0]['_id']['$oid'])),
                'zipCode': '600130',
                'doorNo': '4/105',
                'line': 'Street',
                'createdOn': self.currentTime()
            }
            # # Insert the document into the collection
            # insert_result = db['tblAddress'].insert_one(json_document)
            # if str(insert_result.inserted_id) != '':
            #     responseMessage = 'CREATE ADDRESS SUCCESSFUL'

            key = 'ADDRESSKEY'
            resultArr.append(json_document)
            payload_info = {
                "data": resultArr,
                "message": responseMessage
            }
            encodeData = encode_jwt(payload_info, key)
            return JsonResponse({'Response': 'Sucess', 'document': payload_info}, status=201)
        except PyMongoError as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
