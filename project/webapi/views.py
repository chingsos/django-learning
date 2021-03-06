#coding:utf-8
import datetime
import json
import traceback

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http.request import QueryDict
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render

# Create your views here.
from rest_framework import serializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import list_route
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ViewSet, ModelViewSet

from webapi.models import Application, Module, ApiDoc, DocumentResponse

from httputil import SuccCallReturn,FailCallReturn
from .exp_markdown import markdown_html

class EasyUiPagination(PageNumberPagination):
	# page_size = 10  # 真正的page_size由easyui.paginator传递过来
	page_query_param = 'page'

	page_size_query_param ='rows'

	def get_paginated_response(self,data):
		return Response(
				{'total':self.page.paginator.count,
				 'rows':data
				 })

class ApplicationSerializer(ModelSerializer):
	class Meta:
		model = Application
		read_only_fields=('create_date','user')
		# read_only_fields=('user',)
		# fields = '__all__'

	def create(self, validated_data):
		instance = Application(**validated_data)
		instance.user = User.objects.get(id=1)
		instance.create_date = datetime.datetime.now().date()
		instance.save()
		return instance





"""
虽然开启了csrf
 'django.middleware.csrf.CsrfViewMiddleware',
 但实际上django的response并没有产生csrftoken返回到前端，
 这会影响前端ajax程序在发送POST,UPDATE,DELETE,PATCH无法发送有效的csrftoken而请求无效.
 {% csrf_token %}通过form field传递的csrftoken另当别论。

 要解决这个问题，请见 django.middle.ware.csrf 的 process_response()处理函数，其检查
  request.META.get("CSRF_COOKIE_USED") 是否设置，未设置则不会返回csrf的cookie

 1. get_token(request) 函数可以生成新的csrftoken的cookie，所以只需要调用一下get_token()即可
 2. 编写新的middleware，从 CsrfViewMiddleware派生， process_response()中调用get_token()即可。

"""
class ApplicationViewSet(ModelViewSet):
	serializer_class = ApplicationSerializer
	queryset = Application.objects.all()
	pagination_class = EasyUiPagination
	parser_classes = (FormParser,)
	# authentication_classes = (SessionAuthentication,)
	def get_queryset(self):
		get_token(self.request)
		rs = Application.objects.all().order_by('name')
		return rs

	def create(self, request, *args, **kwargs):
		import json
		ser = ApplicationSerializer(data = request.data)
		if not ser.is_valid():
			return Response({'status':1})
		app = Application(**ser.validated_data)
		app.user = request.user # User.objects.get(id=1)
		app.create_date = datetime.datetime.now().date()
		app.save()
		# app = ser.save()
		r = json.dumps({'status':0,'result':app.id})
		# return HttpResponse(r,content_type='application/json')
		return Response({'status':0,'result':app.id})

	def retrieve(self, request, *args, **kwargs):
		app = self.get_object()
		ser = self.get_serializer(app)
		return Response(ser.data)

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		if not serializer.is_valid():
			return FailCallReturn().httpResponse()
		serializer.save()
		return SuccCallReturn().httpResponse()

	def destroy(self, request, *args, **kwargs):
		doc = self.get_object()
		doc.delete()
		return SuccCallReturn().httpResponse()

class ModuleSerializer(ModelSerializer):
	# app_id = serializers.IntegerField()
	class Meta:
		model = Module
		read_only_fields = ('app',)

	# def validate_app_id(self,value):
	# 	try:
	# 		self.app = Application.objects.get(id= value)
	# 	except:
	# 		raise serializers.ValidationError('application not existed')
	# 	return value

	# def create(self, validated_data):
	# 	module = Module(**validated_data)
	# 	module.app = self.app
	# 	module.save()
	# 	return module



class ModuleViewSet(ModelViewSet):
	serializer_class = ModuleSerializer
	pagination_class = EasyUiPagination
	# queryset = Module.objects.all()
	parser_classes = (FormParser,)

	def get_queryset(self):
		return Module.objects.filter(app__id = self.request.query_params.get('app_id')).order_by('name')



	def create(self, request, *args, **kwargs):
		ser = ModuleSerializer(data = request.data)
		if not ser.is_valid():
			return FailCallReturn().httpResponse()
		try:
			m = Module(**ser.validated_data)
			app = Application.objects.get( id= request.data['app_id'])
			m.app = app
			m.save()
			return SuccCallReturn().assign(m.id).httpResponse()
		except:
			traceback.print_exc()
		return FailCallReturn().httpResponse()


	def update(self, request, *args, **kwargs):
		# instance = self.get_object()
		instance = Module.objects.get(id=kwargs.get('pk'))
		ser = ModuleSerializer(instance,data = request.data)
		if not ser.is_valid():
			return FailCallReturn().httpResponse()
		ser.save()
		return SuccCallReturn().httpResponse()



class SheetSerializer(ModelSerializer):
	class Meta:
		model = ApiDoc

class SheetViewSet(ModelViewSet):
	serializer_class = SheetSerializer
	pagination_class = EasyUiPagination
	queryset = ApiDoc.objects.all()
	# parser_classes = (FormParser,JSONParser)
	parser_classes = (JSONParser,)

	def get_queryset(self):

		rs = ApiDoc.objects.all()
		if self.request.query_params.has_key('module_id'):
			rs = rs.filter(module__id=self.request.query_params.get('module_id',0) )
		return rs.order_by('name')

	@list_route()
	def headers(self,request):
		pass 


	def create(self, request, *args, **kwargs):
		try:
			module = Module.objects.get(id = request.data.get('module_id'))
			doc = ApiDoc()
			doc.module = module
			doc.name = request.data.get('name')
			doc.ver = request.data.get('ver')
			doc.description = request.data.get('description')
			doc.url = request.data.get('url')
			doc.method = request.data.get('method')
			doc.comment = request.data.get('comment')
			doc.headers = json.dumps( request.data.get('headers'))
			doc.paramters = json.dumps( request.data.get('parameters'))
			doc.resp_status = request.data.get('resp_status')
			doc.resp_headers =json.dumps( request.data.get('resp_headers'))
			doc.resp_data = json.dumps( request.data.get('resp_data'))
			doc.save()

			return SuccCallReturn().assign(doc.id).httpResponse()
		except:
			traceback.print_exc()

	def update(self, request, *args, **kwargs):
		doc = self.get_object()
		doc.name = request.data.get('name')
		doc.ver = request.data.get('ver')
		doc.description = request.data.get('description')
		doc.url = request.data.get('url')
		doc.method = request.data.get('method')
		doc.comment = request.data.get('comment')
		doc.headers = json.dumps( request.data.get('headers'))
		doc.paramters = json.dumps( request.data.get('parameters'))
		doc.resp_status = request.data.get('resp_status')
		doc.resp_headers =json.dumps( request.data.get('resp_headers'))
		doc.resp_data = json.dumps( request.data.get('resp_data'))
		doc.save()
		return SuccCallReturn().httpResponse()

	@list_route(methods=['post'])
	def markdown(self,request):
		# import pdfkit
		try:
			doc_ids = request.data
			html = markdown_html(doc_ids)
			# print html
			# pdfkit.from_string(html, 'out.pdf')
			return Response(html)
		except:
			traceback.print_exc()