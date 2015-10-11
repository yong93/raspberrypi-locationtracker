import requests,re
import xml.etree.ElementTree as ET

def getCellTowerInfo():
    print 'Logging in to router home page'    
    baseurl = 'http://192.168.0.1/'
    url = baseurl + 'login.cgi'
    payload = {'ID':'admin','PASSWORD':'admin','REDIRECT':'index.asp','REDIRECT_ERR':'login.asp'}
    response = requests.post(url, data = payload)
    sessionPattern = re.compile('BID\d*')
    sessionId = sessionPattern.findall(response.text)[0]
    
    #get raw cell data
    payload ={'COUNT':'3','WWW_SID':sessionId,'ACTION_1':'function','NAME_1':'get_lac','VALUE_1':'','ACTION_2':'function','NAME_2':'get_cell_id','VALUE_2':'','ACTION_3':'function','NAME_3':'get_op_info','VALUE_3':''}
    rpcUrl = baseurl + 'rpc.cgi'
    response = requests.post(rpcUrl, data = payload)
    
    #parse data
    results = ET.fromstring(response.text).findall('rpc_result')
    lac = results[0].text
    cellid = results[1].text
    operator = results[2].text
    print 'Got tower location, logging out'
    print lac, cellid, operator
    
    logoutUrl = baseurl + 'logout.cgi'
    payload ={'WWW_SID':sessionId}
    requests.post(logoutUrl, data = payload)
    return (lac, cellid, operator)
