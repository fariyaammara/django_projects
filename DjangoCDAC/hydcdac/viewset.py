from rest_framework.viewsets import ModelViewSet,ViewSet
from hydcdac.models import HydCdac,HydCdacemp
from hydcdac.serializer import HydCdacSerializer
from DjangoCDAC.settings import db
from rest_framework.response import Response
from rest_framework import status
from bson.objectid import ObjectId
import json
from DjangoCDAC.JsonEncoder import MongoJSONEncoder

class HydcdacViewset(ModelViewSet):
    queryset = HydCdac.objects.all()
    serializer_class= HydCdacSerializer

class HydcdacPost(ViewSet):
    queryset = HydCdac.objects.all()

class Hydcdacup(ModelViewSet):
    queryset = HydCdacemp.objects.all()
    serializer_class= HydCdacSerializer
    def update(self,request,*args, **kwargs):
        print("hiiii")
        data=request.data
        up=db.hydcdac_hydcdac.update_one({"_id":ObjectId("6396b6e6423705ae33d8e40b")},{'$set':{"employee_name":data["employee_name"]}})
        return Response({"req":"get_resp"}, status=status.HTTP_200_OK)

    def create(self,request,*args, **kwargs):
        data=request.data
        ins=db.hydcdac.insert_one({
            "em_id":data["em_id"],
            "pay":data["pay"],
            "emp_name":data["emp_name"],
            "emp_grp":data["emp_grp"]
        })
        return Response({"status":200,"Response":"Successfully inserted"})
    def list(self,args, **kwargs):
        dict_st={"status":200}
        lst=[]
        for get_val in db.hydcdac.find():
            lst.append(get_val)
        dict_st["data"]=lst
        return Response(str(dict_st))