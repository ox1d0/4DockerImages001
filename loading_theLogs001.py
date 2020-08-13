import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.read_csv('testlog_1/testlog_1', header = None, delimiter='\t', skiprows=[0,1])
df2 = pd.read_csv('testlog_2/testlog_2', header = None, delimiter='\t', skiprows=[0,1])

columns1 = ['date','time','x_edge_location','sc_bytes','c_ip','cs_method','cs_Host','cs_uri_stem','sc_status','cs_Referer','cs_UserAgent)','csuriquery_cs_uri_query','cs_Cookie_cs_Cookie','x_edge_result_typex_edge_result_type','x_edge_request_id','x_host_header','cs_protocol','cs_bytes','time_taken','x_forwarded_for','ssl_protocol','ssl_cipher','x_edge_response_result_type','cs_protocol_version','fle_status','fle_encrypted_fields','c_port','time_to_first_byte','x_edge_detailed_result_type','sc_content_type','sc_content_len','sc_range_start','sc_range_end']

columns2 = ['date','time','x_edge_location','sc_bytes','c_ip','cs_method','cs_Host','cs_uri_stem','sc_status','cs_Referer','cs_UserAgent)','csuriquery_cs_uri_query','cs_Cookie_cs_Cookie','x_edge_result_typex_edge_result_type','x_edge_request_id','x_host_header','cs_protocol','cs_bytes','time_taken','x_forwarded_for','ssl_protocol','ssl_cipher','x_edge_response_result_type','cs_protocol_version','fle_status','fle_encrypted_fields','c_port','time_to_first_byte','x_edge_detailed_result_type','sc_content_type','sc_content_len','sc_range_start','sc_range_end']


df1.columns = columns1
df2.columns = columns2

#count_data_null1 = df1.isnull().sum()
#print ('Null Data on Data frame Number 1:\n',count_data_null1)

#count_data_null2 = df2.isnull().sum()
#print ('Null Data on Data frame Number 2:\n',count_data_null1)

######################################
#Target info hits Holds  Categorical Info So
#option0: pandas factorizing: maps each category to a different integer = label encoder 
#create series for pandas

#hits1 =  df1.filter(like="x-edge-response-result-type")
hits1 = df1["x_edge_detailed_result_type"]
hits_encoded1, categories = pd.factorize(hits1)
print('Geting Result for the Categories For Logfile01\n', categories ) #original version 


missed_bytesdf1=df1.loc[df1.x_edge_detailed_result_type=='Miss'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']})
print('Getting Miss bytes for testlog_1', missed_bytesdf1) #testlog_1_bytes4Miss

hits_bytes4f1=df1.loc[df1.x_edge_detailed_result_type=='Hit'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']})
print('Getting Hits bytes for testlog_1', hits_bytes4f1) #testlog_1_bytes4Hits

bytes4Stdf1001=df1.groupby(['sc_bytes','time','x_edge_detailed_result_type']).agg({'sc_bytes' : ['min', 'max', 'count']})
print('Getting Hits and Miss bytes for testlog_1 on Periods of time', bytes4Stdf1001) #testlog_1_bytes4Hits


#print(hits1[:100]) #original version 
#print(hits_encoded1[:100]) #encoded numbers for categories 

factor_mapping = dict(zip(categories, hits_encoded1)) #mapping of encoded numbers and original categories. 
print('Factoritation for factor_mapping\n',factor_mapping) # print factor mapping
print('Counter For each Categories\n',hits1.value_counts()) # print factor mapping

#plt.plot(hits1)
#####################################

#print('the x-edge-detailed-result-type value On Log01 has Categorcal estates:\t', hits1)
#
#print('the x-edge-detailed-result-type value On Log02 has at leats 3 estates:\t', hits2) 

#########################################
#  Doing the Agregation of Logs1 + Logs2
# 
#########################################


#Agregated_stadistics =
#print ('Interesting Things About the A␇gregated DataFrame:\n', df_agregate.describe())
