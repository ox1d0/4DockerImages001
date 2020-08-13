import pandas as pd
from application import app
from flask import render_template


df1 = pd.read_csv('../testlog_1/testlog_1', header = None, delimiter='\t', skiprows=[0,1])
columns1 = ['date','time','x_edge_location','sc_bytes','c_ip','cs_method','cs_Host','cs_uri_stem','sc_status','cs_Referer','cs_UserAgent)','csuriquery_cs_uri_query','cs_Cookie_cs_Cookie','x_edge_result_typex_edge_result_type','x_edge_request_id','x_host_header','cs_protocol','cs_bytes','time_taken','x_forwarded_for','ssl_protocol','ssl_cipher','x_edge_response_result_type','cs_protocol_version','fle_status','fle_encrypted_fields','c_port','time_to_first_byte','x_edge_detailed_result_type','sc_content_type','sc_content_len','sc_range_start','sc_range_end']
df1.columns = columns1

df2 = pd.read_csv('../testlog_2/testlog_2', header = None, delimiter='\t', skiprows=[0,1])
columns2 = ['date','time','x_edge_location','sc_bytes','c_ip','cs_method','cs_Host','cs_uri_stem','sc_status','cs_Referer','cs_UserAgent)','csuriquery_cs_uri_query','cs_Cookie_cs_Cookie','x_edge_result_typex_edge_result_type','x_edge_request_id','x_host_header','cs_protocol','cs_bytes','time_taken','x_forwarded_for','ssl_protocol','ssl_cipher','x_edge_response_result_type','cs_protocol_version','fle_status','fle_encrypted_fields','c_port','time_to_first_byte','x_edge_detailed_result_type','sc_content_type','sc_content_len','sc_range_start','sc_range_end']
df2.columns = columns2

df_agregate = pd.concat([df1,df2],axis=0, keys=['date','time','x-edge-location','sc-bytes','c-ip','cs-method','cs(Host)','cs-uri-stem','sc-status','cs(Referer)','cs(User-Agent)','cs-uri-querycs-uri-query','cs(Cous','fle-encrypted-fields','c-port','time-to-first-byte','x-edge-detailed-result-type','sc-content-type','sc-ontent-len','sc-range-start','sc-range-end'])
agg1 = ['date','time','x_edge_location','sc_bytes','c_ip','cs_method','cs_Host','cs_uri_stem','sc_status','cs_Referer','cs_UserAgent)','csuriquery_cs_uri_query','cs_Cookie_cs_Cookie','x_edge_result_typex_edge_result_type','x_edge_request_id','x_host_header','cs_protocol','cs_bytes','time_taken','x_forwarded_for','ssl_protocol','ssl_cipher','x_edge_response_result_type','cs_protocol_version','fle_status','fle_encrypted_fields','c_port','time_to_first_byte','x_edge_detailed_result_type','sc_content_type','sc_content_len','sc_range_start','sc_range_end']
df_agregate.columns = agg1

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", login=False)

@app.route("/log1/", methods=["GET"])
def log1():
    return (df1.describe().to_html())

@app.route("/log1/hits", methods=["GET"])
def log_hi1():
    return (df1.loc[df1.x_edge_detailed_result_type=='Hit'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())

@app.route("/log1/miss", methods=["GET"])
def log_mi1():
    return (df1.loc[df1.x_edge_detailed_result_type=='Miss'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())

@app.route("/log1/st", methods=["GET"])
def log_st1():
    return (df1.groupby(['sc_bytes','time','x_edge_detailed_result_type']).agg({'sc_bytes' : ['min', 'max', 'count']}).to_html())
            
@app.route("/all/", methods=["GET"])
def all():
    return (df_agregate.describe().to_html())

@app.route("/all/hits", methods=["GET"])
def all_hi():
    return (df_agregate.loc[df_agregate.x_edge_detailed_result_type=='Hit'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())
            
@app.route("/all/miss", methods=["GET"])
def all_mi():
    return (df_agregate.loc[df_agregate.x_edge_detailed_result_type=='Miss'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())
            
@app.route("/all/st", methods=["GET"])
def all_st():
    return (df_agregate.groupby(['sc_bytes','time','x_edge_detailed_result_type']).agg({'sc_bytes' : ['min', 'max', 'count']}).to_html())

@app.route("/log2/", methods=["GET"])
def log2():
    return (df2.describe().to_html())

@app.route("/log2/hits", methods=["GET"])
def log_hi2():
    return (df2.loc[df2.x_edge_detailed_result_type=='Hit'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())
            
@app.route("/log2/miss", methods=["GET"])
def log_mi2():
    return (df2.loc[df2.x_edge_detailed_result_type=='Miss'].groupby('x_edge_detailed_result_type').agg({'sc_bytes' :['min', 'max', 'count']}).to_html())
            
@app.route("/log2/st", methods=["GET"])
def log_st2():
    return (df2.groupby(['sc_bytes','time','x_edge_detailed_result_type']).agg({'sc_bytes' : ['min', 'max', 'count']}).to_html())

@app.route('/user/<name>')
def user(name):
        return '<h1>Hello, {}!</h1>'.format(name)
    
if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000, debug=False)
