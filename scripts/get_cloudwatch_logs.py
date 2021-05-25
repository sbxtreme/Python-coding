#===========================================================================================================================================
# Description    : This lambda function parse CW logs for Finnair Custom lambda functions and write/visualize their Metrics in an Xls file
# Date           : 2021-04-09
# Version        : 1.0
# Python version : 3.7
#===========================================================================================================================================

import os
import io
import csv
import ast
import json
import boto3
import pandas as pd
from datetime import datetime, timedelta

def datetime_converter(o):
	""" This function converts datetime object to string for json date attribute value """
	if isinstance(o, datetime):
	   return o.__str__()

def get_cw_metrics_data(days,metrics_data_query):
	""" This function gets the CW logs for the date range where start_time is the "days" passed in the function and the endtime is today """
	try:
		cloudwatch_client = boto3.client('cloudwatch',region_name=os.environ['aws_region'])
		start_time=datetime.now(tz=None) - timedelta(days=days)
		end_time=datetime.now(tz=None)
		response = cloudwatch_client.get_metric_data(MetricDataQueries=metrics_data_query,StartTime=start_time,EndTime=end_time)
		return json.dumps(response, default = datetime_converter)

	except Exception as e:
		print("An error occured in the function get_cw_metrics_data:",e)
		raise e

def parse_json_logs(json_response,metrics):
	""" This function parse json response from CW logs and write it in a readable format in csv file """
	try:
		x_axis_list=[]
		y_axis_list=[]
	   
		if metrics=='duration':
		   json_index=0
		   columns_list=['Timestamps','Duration_in_milliseconds']
		   
		elif metrics=='invocation':
		   json_index=1
		   columns_list=['Timestamps','Invocations_Count']
		   
		else:
		   json_index=2
		   columns_list=['Timestamps','Error_Count']
		   
		for x_axis in json_response['MetricDataResults'][json_index]['Timestamps']:
		   x_axis_list.append(x_axis)
		   
		for y_axis in json_response['MetricDataResults'][json_index]['Values']:
		   y_axis_list.append(y_axis)
		   
		df = pd.DataFrame(list(zip(x_axis_list, y_axis_list)),columns = columns_list)
		df['Timestamps']=df['Timestamps'].str.split('+').str[0]
		df['Timestamps']=pd.to_datetime(df.Timestamps, format='%Y-%m-%d %H:%M:%S')
		df_final=df.sort_values(by='Timestamps')
		
		return df_final
      
	except Exception as e:
		print(e)
		raise e

def write_and_plot_data(cw_response_data,lambda_name):
	try:
		""" This function writes and plot metrics data in an xls file """
		# Getting duration , invocation and error rates from CW logs for APIs
		metrics_list=['duration','invocation','errors']
		
		for metrics in metrics_list:
			if metrics =='duration':
				worksheet_duration='Duration'
				df_duration=parse_json_logs(cw_response_data,metrics)

			elif metrics == 'invocation':
				worksheet_invocation='Invocation'
				df_invocation=parse_json_logs(cw_response_data,metrics)

			else:
				worksheet_errors='Errors'
				df_errors=parse_json_logs(cw_response_data,metrics)


		# row counts for all 3 metric data
		row_count_dur=len(df_duration.index)
		row_count_inv=len(df_invocation.index)
		row_count_err=len(df_errors.index)

		with io.BytesIO() as output:
			with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
				df_duration.to_excel(writer,sheet_name=worksheet_duration,index=False)
				df_invocation.to_excel(writer,sheet_name=worksheet_invocation,index=False)
				df_errors.to_excel(writer,sheet_name=worksheet_errors,index=False)

				################ chart specific logic before writing to a single iostream ##############

				worksheet_dur = writer.sheets[worksheet_duration]
				worksheet_invo = writer.sheets[worksheet_invocation]
				worksheet_err = writer.sheets[worksheet_errors]
				
				str_val_dur=('=\'{0}\'!$B$2:$B$'+str(row_count_dur)).format(worksheet_duration)
				str_val_invo=('=\'{0}\'!$B$2:$B$'+str(row_count_inv)).format(worksheet_invocation)
				str_val_err=('=\'{0}\'!$B$2:$B$'+str(row_count_err)).format(worksheet_errors)
				
				str_cat_dur=('=\'{0}\'!$A$2:$A$'+str(row_count_dur)).format(worksheet_duration)
				str_cat_invo=('=\'{0}\'!$A$2:$A$'+str(row_count_inv)).format(worksheet_invocation)
				str_cat_err=('=\'{0}\'!$A$2:$A$'+str(row_count_err)).format(worksheet_errors)
				
				# Duration metrics plot
				workbook = writer.book
				chart = workbook.add_chart({'type': 'line'})
				chart.add_series({"values": str_val_dur,"categories":str_cat_dur,"name": "Duration","line": {'width': 2.00,'color':'blue'},})
				chart.set_x_axis({'name': 'Timestamps','major_unit': 1,'text_axis': True, 'date_axis': False})
				chart.set_y_axis({'name': 'Duration_in_milliseconds', 'major_gridlines': {'visible': False},'major_unit': 500})
				chart.set_legend({'position': 'top'})
				chart.set_size({'width': 1020, 'height': 750})
				worksheet_dur.insert_chart('F2', chart)
				
				# Invocation metrics plot
				workbook = writer.book
				chart = workbook.add_chart({'type': 'line'})
				chart.add_series({"values": str_val_invo,"categories":str_cat_invo,"name": "Invocation","line": {'width': 2.00,'color':'green'}})
				chart.set_x_axis({'name': 'Timestamps','major_unit': 1,'text_axis': True, 'date_axis': False})
				chart.set_y_axis({'name': 'Invocations', 'major_gridlines': {'visible': False},'major_unit': 100})
				chart.set_legend({'position': 'top'})
				chart.set_size({'width': 1020, 'height': 750})
				worksheet_invo.insert_chart('F2', chart)
				
				# Errors metrics plot
				workbook = writer.book
				chart = workbook.add_chart({'type': 'line'})
				chart.add_series({"values": str_val_err,"categories":str_cat_err,"name": "Errors","line": {'width': 2.00,'color':'red'}})
				chart.set_x_axis({'name': 'Timestamps','major_unit': 1,'text_axis': True, 'date_axis': False})
				chart.set_y_axis({'name': 'Errors', 'major_gridlines': {'visible': False}})
				chart.set_legend({'position': 'top'})
				chart.set_size({'width': 1020, 'height': 750})
				worksheet_err.insert_chart('F2', chart)

				############################ chart specific logic ends here ############################


			data = output.getvalue()
		s3 = boto3.resource('s3')
		s3.Bucket(os.environ['bucket_name']).put_object(Key='etl/api_metrics_report/{1}/{0}_metrics_{1}.xlsx'.format(lambda_name,datetime.now().strftime("%Y-%m-%d")), Body=data)
		print("API Metric Excel file generated for {} lambda".format(lambda_name))

	except Exception as e:
		print(e)
		raise e

def lambda_handler(event, context):
	try:
		metrics_data_query=[
									{
									  "Id":"getmetricsduration01",
									  "MetricStat":{
									     "Metric":{
									        "Namespace":"AWS/Lambda",
									        "MetricName":"Duration",
									        "Dimensions":[
									           {
									              "Name":"FunctionName",
									              "Value":"lambda_name"
									           }
									        ]
									     },
									     "Period":300,
									     "Stat":"Average",
									     "Unit":"Milliseconds"
									  }
									},
									{
									  "Id":"getmetricsinvocation01",
									  "MetricStat":{
									     "Metric":{
									        "Namespace":"AWS/Lambda",
									        "MetricName":"Invocations",
									        "Dimensions":[
									           {
									              "Name":"FunctionName",
									              "Value":"lambda_name"
									           }
									        ]
									     },
									     "Period":60,
									     "Stat":"Sum",
									     "Unit":"Count"
									  }
									},
									{
									  "Id":"getmetricserrors01",
									  "MetricStat":{
									     "Metric":{
									        "Namespace":"AWS/Lambda",
									        "MetricName":"Errors",
									        "Dimensions":[
									           {
									              "Name":"FunctionName",
									              "Value":"lambda_name"
									           }
									        ]
									     },
									     "Period":300,
									     "Stat":"Sum",
									     "Unit":"Count"
									  }
									}
									]
		
	
		list_of_lambdas=ast.literal_eval(os.environ['list_of_lambdas'])
		
		for lambda_name in list_of_lambdas:
			for dict in metrics_data_query:
				for v in dict['MetricStat']['Metric']['Dimensions']:
					v['Value']=lambda_name

			cw_response_data=get_cw_metrics_data(1,metrics_data_query) # here 1 is the days for which we need metric from CW.
			cw_response_data=json.loads(cw_response_data.replace("\'", '"'))
			write_and_plot_data(cw_response_data,lambda_name)

		return "API metrics report generated for all the lambda functions"
			
	except Exception as e:
		print("An error occured in the function lambda_handler:",e)
		raise e