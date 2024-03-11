from django.shortcuts import render
from .models import Topu
from .serializers import TopuSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


# Create your views here.
'''
def Topu_views(request):
    #complex_data
    topu_obj = Topu.objects.all()
    #python_dict
    serilizer = TopuSerializers(topu_obj,many= True)
    #render_json
    json_data = JSONRenderer().render(serilizer.data)
    
    return HttpResponse(json_data, content_type='application/json')

#model_instance

def Topu_instance(request, pk):
    #complex_data
    #topu_obj = Topu.objects.get(id=pk)
    topu_obj = get_object_or_404(Topu, id=pk)
    #python_dict
    serilizer = TopuSerializers(topu_obj)
    #render_json
    json_data = JSONRenderer().render(serilizer.data)
    
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def topu_create(request):
    if request.method == 'POST':
        json_data = request.body
        #json_data to covert stream
        stream = io.BytesIO(json_data)
        #stream to python 
        python_data = JSONParser().parse(stream)
        #python to complex
        serilizer = TopuSerializers(data=python_data)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'succesfully messaage data'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type= 'application/json')
        
        json_data = JSONRenderer().render(serilizer.errors)
        return HttpResponse(json_data, content_type= 'application/json')
    
    elif request.method == "PUT":
        json_data = request.body
        #json_data to covert stream
        stream = io.BytesIO(json_data)
        #stream to convert python
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        topu_id = Topu.objects.get(id=id)
        #python to complex
        serilizer=  TopuSerializers(topu_id, python_data, partial=True)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'succesfully Updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data)
        
    elif request.method == "DELETE":
        json_data = request.body
        #json data convert stream
        stream = io.BytesIO(json_data)
        #straem to convert python
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        topu_id = Topu.objects.get(id=id)
        topu_id.delete()
        res = {'msg': 'succesfully Updated'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data)
        
  /////////Function based view///////////      

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def topu_create(request, pk= None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            #complex_data
            topu_value = Topu.objects.get(id =id)
            #complex data to python dictionary
            serilizer = TopuSerializers(topu_value)
            return Response(serilizer.data)
        #complex_Data
        topu_value = Topu.objects.all()
        #complex data to python dictionary
        serilizer = TopuSerializers(topu_value, many=True)
        return Response(serilizer.data)
        
    if request.method == 'POST':
        serilizer= TopuSerializers(data= request.data)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'data save succesfully'}
            return Response(res)
        return Response (serilizer.errors)
    
    if request.method == 'PUT':
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        #complex data to python dictionary
        serilizer = TopuSerializers(topuvalue,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data updae successfully'})
        return Response(serilizer.errors)
    
    if request.method == 'PATCH':
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        #complex data to python dictionary
        serilizer = TopuSerializers(topuvalue,data=request.data,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'partial data update successfully'})
        return Response(serilizer.errors)
    
    if request.method == 'DELETE':
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        topuvalue.delete()
        return Response({'msg':'delete succesfully'})
        

     #class base view 

class Topuclassbaseview(APIView):
    def get(self,request,format= None,pk= None):
        id = pk
        if pk is not None:
            #complex data
            topu_value = Topu.objects.get(id=id)
            #complex data to python data
            serilizer = TopuSerializers(topu_value)
            return Response(serilizer.data)
        #complex data
        topu_value = Topu.objects.all()
        #complex data to python data
        serilizer = TopuSerializers(topu_value,many = True)
        return Response(serilizer.data)
    
    def post(self,request,format= None):
        serilizer= TopuSerializers(data= request.data)
        if serilizer.is_valid():
            serilizer.save()
            res = {'msg': 'data save succesfully'}
            return Response(res)
        return Response (serilizer.errors)
    
    def put(self,request,format= None,pk=None):
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        #complex data to python dictionary
        serilizer = TopuSerializers(topuvalue,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data updae successfully'})
        return Response(serilizer.errors)
    
    def patch(self,request,format= None,pk=None):
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        #complex data to python dictionary
        serilizer = TopuSerializers(topuvalue,data=request.data,partial=True)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'partial data update successfully'})
        return Response(serilizer.errors)
    
    def delete(self,request,format= None,pk=None):
        id =pk
        #complex_data
        topuvalue = Topu.objects.get(id=id)
        topuvalue.delete()
        return Response({'msg':'delete succesfully'})


class TopuListView(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Topu.objects.all()
    serializer_class = TopuSerializers
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
  
class TopuretriveView(GenericAPIView,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    
    queryset = Topu.objects.all()
    serializer_class = TopuSerializers
    lookup_field = 'pk'
    
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:  # If 'pk' is present in kwargs, it's a detail request
            return self.retrieve(request, *args, **kwargs)
        else:  # Otherwise, it's a list request
            return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
 '''    
 
 
class topushortlistcreate(ListCreateAPIView):
    queryset = Topu.objects.all()
    serializer_class = TopuSerializers
    
class topu_cre_up_del(RetrieveUpdateDestroyAPIView):
    queryset = Topu.objects.all()
    serializer_class = TopuSerializers
    
    