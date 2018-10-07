from django.shortcuts import render
from . import models as tmd
from datetime import datetime
from tools import dbtest
# Create your views here.

def trade_report(request):
	
	data = {}
	
	# 当提交表单时
	st_date = None
	ed_date = None
	r_name =None
	stat_data = tmd.StatisticTradeData.objects.all().order_by('o_date')
	
	#时间大于等于st_date
	try:
		st_date = request.GET['st_date']
		if st_date != "":
			st_date_dtm = datetime.strptime(st_date, "%Y-%m-%d")
			stat_data = stat_data.filter(i_date__gte = st_date_dtm)
	except BaseException as e:
		print(e)
		
	try:
		ed_date = request.GET['ed_date']
		if ed_date != "":
			ed_date_dtm = datetime.strptime(ed_date, "%Y-%m-%d") 
			stat_data = stat_data.filter(i_date__lte = ed_date_dtm)
	except BaseException as e:
		print(e)
		
	try:
		r_name = request.GET['r_name']
		if r_name != "":
			stat_data = stat_data.filter(name = r_name)
	except BaseException as e:
		print(e)

	#保存页面数据
	data['st_date'] = st_date
	data['ed_date'] = ed_date
	data['r_name'] = r_name
	data['stat_data'] = stat_data;
	return render(request, 'tshare/trade_report.html',data)
	
def trade_detail(request,r_code):
	ori_data = tmd.OriginalTradeData.objects.filter(code = r_code)
	k_data = tmd.K_days.objects.filter(code = r_code)
	data = {}
	data['ori_data'] = ori_data;
	data['r_code'] = r_code
	data['k_data'] = k_data
	data['r_name'] = ori_data[1].name
	return render(request, 'tshare/trade_detail.html',data)
	
def echarts(request):
	return render(request, 'tshare/echarts.min.js')