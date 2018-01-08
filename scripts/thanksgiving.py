#!/usr/bin/env python

import datetime 
import json, os, numpy

dates = [
    datetime.date(2016,11,24),
    datetime.date(2015,11,26),
    datetime.date(2014,11,27)
]

def day_sales(date):
    txns =json.loads( open(os.path.join("data/taproom",date.strftime("%Y-%m-%d")+".json")).read())
    
    sales = [float(e['net_sales_money']['amount']) for e in txns]
    total_sales = sum(sales) / 100
    return total_sales
    

for i,d in enumerate(dates):

    print ""
    print d.year
    wed = d - datetime.timedelta(days=1)
    fri = d + datetime.timedelta(days=1)
    sat = d + datetime.timedelta(days=2)
    sun = d + datetime.timedelta(days=3)


    prev4_wed = [ wed - datetime.timedelta(weeks = i+1) for i in range(4)]
    next4_wed = [ wed + datetime.timedelta(weeks = i+1) for i in range(4)]

    prev_sales = [ day_sales(d) for d in prev4_wed]
    next_sales = [day_sales(d) for d in next4_wed]
    print "Thanksgiving {0}".format( d.year)
    print "On wednesday we made {0}".format(day_sales(wed))
    print "On the average in the surrounding 8 wks, we made ${0} on Wednesdays".format(numpy.array(prev_sales + next_sales).mean())
    print prev_sales
    print next_sales


    prev4_fri = [ fri - datetime.timedelta(weeks = i+1) for i in range(4)]
    next4_fri = [ fri + datetime.timedelta(weeks = i+1) for i in range(4)]

    prev_sales = [ day_sales(d) for d in prev4_fri]
    next_sales = [day_sales(d) for d in next4_fri]
    print "Thanksgiving {0}".format( d.year)
    print "On friday we made {0}".format(day_sales(fri))
    print "On the average in the surrounding 8 wks, we made ${0} on Fridays".format(numpy.array(prev_sales + next_sales).mean())
    print prev_sales
    print next_sales


    

    prev4_sat = [ sat - datetime.timedelta(weeks = i+1) for i in range(4)]
    next4_sat = [ sat + datetime.timedelta(weeks = i+1) for i in range(4)]

    prev_sales = [ day_sales(d) for d in prev4_sat]
    next_sales = [day_sales(d) for d in next4_sat]
    print "Thanksgiving {0}".format( d.year)
    print "On satday we made {0}".format(day_sales(sat))
    print "On the average in the surrounding 8 wks, we made ${0} on Satdays".format(numpy.array(prev_sales + next_sales).mean())
    print prev_sales
    print next_sales


