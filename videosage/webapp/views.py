from django.shortcuts import render, redirect

from django.template.loader import render_to_string
from django.http import HttpResponse, HttpRequest
from django.template import Context, loader

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import salesforce_oauth2
#from simple_salesforce import Salesforce

import requests, json

from collections import OrderedDict

def home(request):
    # oauth workflow
    sf = salesforce_oauth2.SalesforceOAuth2('3MVG9fMtCkV6eLhdhn.bjVlF4Geczsr.0GUre6SnTGjCbCwXQUeQyaQRXi.cOEpYpzXTHWkYHCWFrVzJ6WM8i', '175569858642154718', 'http://localhost:8000/auth/salesforce/callback')
    return redirect(sf.authorize_url(scope='full'))

def redirecturl(request):
    sf = salesforce_oauth2.SalesforceOAuth2('3MVG9fMtCkV6eLhdhn.bjVlF4Geczsr.0GUre6SnTGjCbCwXQUeQyaQRXi.cOEpYpzXTHWkYHCWFrVzJ6WM8i', '175569858642154718', 'http://localhost:8000/auth/salesforce/callback')
    code = request.GET.get('code')
    response = sf.get_token(code)
    #sfa = Salesforce(instance_url=response['instance_url'], session_id=response['access_token'])
    #records = sfa.query("SELECT Id, Name FROM Opportunity")
    #for r in records['records']:
    #    print r.items()
    url = response['instance_url']+"/services/data/v33.0/query?q=SELECT+StageName,Name+from+Opportunity"
    res = requests.get(url, headers={"Authorization": "Bearer %s" % response['access_token']})
    personalOppDict = res.json()
    #for r in res.json()['records']:
    #     l = []
    #     l.append(r['Name'], r['StageName'])
    #     personalOppDict[]
    return render(request, 'redirect.html', {'personal':json.dumps(personalOppDict)})    

    '''
    url = "https://na16.salesforce.com/services/data/v33.0/sobjects/UserRole/00Ej0000000u5Wi"
    res = requests.get(url, headers={"Authorization": "Bearer %s" % sessionId})
    roleblob = res.json()
    userrole = roleblob['Name']
    {  
       u'access_token':u'00Dj00000029pgX!ARUAQPHyGqVfYEQ_MMUhaj5hAbBgrgiFH59.o5AfJThLHGF0UwLTz5QkQFEbt1WxP8MkI4MUNyMABkpf6sBOt7lRx6.L8o.v',
       u'id_token':u'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjE5NCJ9.eyJleHAiOjE0MzEwNDAyNzQsInN1YiI6Imh0dHBzOi8vbG9naW4uc2FsZXNmb3JjZS5jb20vaWQvMDBEajAwMDAwMDI5cGdYRUFRLzAwNWowMDAwMDBCd0lEVkFBMyIsImF0X2hhc2giOiJrdk1QMmVzaVJSMVVCRDhYQjcyaFNRIiwiYXVkIjoiM01WRzlmTXRDa1Y2ZUxoZGhuLmJqVmxGNEdlY3pzci4wR1VyZTZTblRHakNiQ3dYUVVlUXlhUVJYaS5jT0VwWXB6WFRIV2tZSENXRnJWeko2V004aSIsImlzcyI6Imh0dHBzOi8vbG9naW4uc2FsZXNmb3JjZS5jb20iLCJpYXQiOjE0MzEwNDAxNTR9.Qw97TjOW50Z97rYcBPjb4erbRkT4rq0h08NnvmAwonrg3jOF6ta_9wZc_oCiaRk5OEBKK6FQNwDRI2hGeDvtzuwhBhgHNcGwcx4e1NR85hqJVj6yOZNqeionp-PicEPv8INmBQn30kttDLUHD9QIEejqV01QlpFg0g00VY8po13wCaE3b25F8kg5ew42AQqXPuCg6oufd_fTSRaypWIhJcKa0t3TZwLAcENbYVxw1x7rFZNjN2n9ADxvST5LutUEFOhX94JxjvEWqWKTaWkqOzsyJWBhwvlfssrtNZoIRvDXEComt-xFAU-ZS_TkwJCWkSCF4u-WB1RP4u8JwJV2bTrSRCl4W-QBBiGDCkd57Tsq4S6EGXuXm5N5BnhF3SaMINqNdApwlAyAkvgoO1uycfUbepka3TBQq1lfZQvDFhMD28Qxw4uQ8sgaFcngJKxztpHYcrNMcwc7Qr8u6RSV1MXD6lljtCSkQJtU2ooW8jUGDc3JfFmtOFCw5OL0lH7g2yL9j65oCBog7DO3utcgLHb_oIxNKebQg3yNWR3-SjZs79RTl4C0XUlcdiZKra1eXhkDxyV8mfjuwMa5UK7U2Md_V8pIMXOgKSN56zxhQMNUJBspkMSOUF6h9fbANsN8V08SdpyjzuXtnOC1Cgtifrw8xjibZiNpQPei7zkQpFw',
       u'token_type':u'Bearer',
       u'signature':u'C0918HeLxSdmQVj6XDlMAICzB0CZFYmaDYUjcIWEttg=',
       u'issued_at':u'1431040154876',
       u'scope':u'full',
       u'instance_url':   u'https://na16.salesforce.com',
       u'id':   u'https://login.salesforce.com/id/00Dj00000029pgXEAQ/005j000000BwIDVAA3'
    }
    consumer_key = '3MVG9A2kN3Bn17hsWsLDatw._IVMEUBoPKv.7ksp0tz7xLX4tWDVgyzwTCA7i_yTfP.qYuNOsSoPNcdVH6DuE'
    consumer_secret = '8779811613588378217'
    request_token_url = 'https://login.salesforce.com/services/oauth2/token'
    access_token_url = 'https://login.salesforce.com/services/oauth2/token'
    redirect_uri = 'http://localhost/cgi-bin/python/oauth.py'
    authorize_url = 'https://login.salesforce.com/services/oauth2/authorize' #?response_type=token&client_id='+consumer_key+'&redirect_uri='+redirect_uri

    query = cgi.FieldStorage()
    req = None


    if 'login' in query:
        print "Location: https://login.salesforce.com/services/oauth2/authorize?response_type=code&client_id="+consumer_key+"&redirect_uri="+redirect_uri
        print

    if 'code' in query:
        code = query.getvalue('code')
        
        data = {
                    'grant_type': 'authorization_code',
                    'redirect_uri': redirect_uri,
                    'code': code,
                    'client_id' : consumer_key,
                    'client_secret' : consumer_secret
                }
        headers = {
                    'content-type': 'application/x-www-form-urlencoded'
                }
        req = requests.post(access_token_url,data=data,headers=headers)
        response = req.json()
        sf = Salesforce(instance_url=response['instance_url'], session_id=response['access_token'])
        records = sf.query("SELECT Id, Name, Email FROM Contact")
        records = records['records']

    #print web page
    print "Content-type: text/html"
    print

    print "<html><body>"
    print "<h1>SELECT Id, Name, Email FROM Contact</h1>"

    print "<table>"
    print "<tr><td><b>Name</b></td><td><b>Email</b></td></tr>"
    for record in records:
            print "<tr><td>"+record['Name']+"</td><td>"+record['Email']+"</td></tr>"

    print "</table>"

    print "</body></html>"
    '''