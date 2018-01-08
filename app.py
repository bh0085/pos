#!/usr/bin/env python

from flask import Flask, flash, redirect, render_template, request, session, abort
import os,datetime
import json
import urllib2
import numpy

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=tmpl_dir)
 
def getExchangeRates():
    rates = []
    response = urllib2.urlopen('http://api.fixer.io/latest')
    data = response.read()
    rdata = json.loads(data, parse_float=float)
 
    rates.append( rdata['rates']['USD'] )
    rates.append( rdata['rates']['GBP'] )
    rates.append( rdata['rates']['HKD'] )
    rates.append( rdata['rates']['AUD'] )
    return rates
 
@app.route("/")
def index():

    startdate = datetime.date(2017, 06,01)
    dates = []
    for i in range(30):
        dates.append(startdate + datetime.timedelta(days = i))
        
        
    for d in dates:
        with open(os.path.join("data/taproom",d.strftime("%Y-%m-%d")+".json")) as f:
            txns = json.load(f)

    rates=getExchangeRates()

    
    arraydata = [['date', 'ticketsize', 'totalsales']]
    arraydata = arraydata +  [[d, i, i+1] 
                            for i, d in enumerate( dates )]
        
    
    return render_template('tickets.html',**locals())      
 
 
 
if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port = 5050)
