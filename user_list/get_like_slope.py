__author__ = 'yi-linghwong'

#############
# Get the slope of the linear equation for a list of user
# y = mx + c, where y is number of follower, x is epoch time
#############

import sys
import os
from matplotlib import *
import matplotlib.pyplot as plt
import pylab
import numpy as np
from scipy.stats import linregress
from scipy.interpolate import interp1d
from decimal import Decimal
import time


#------------------------------
# PART I: get slope for like count without interpolation


# lines = open('others/user_nonprofit.csv','r').readlines()
#
# user_list = []
#
# for line in lines:
#     spline = line.replace('\n','').split(',')
#     user_list.append(spline[0])
#
# user_slope_list = []
#
# for ul in user_list:
#
#     user_slope = []
#
#     lines = open('likes/'+ul+'.txt','r').readlines()
#
#     likecount_list = []
#     date = []
#
#
#     for line in lines:
#         spline = line.replace('\n','').split(',')
#
#         likecount_list.append(float(spline[1]))
#         date.append(spline[0])
#
#     date_split = []
#
#     for d in date:
#         d1 = d.replace('\n','').split(' ')
#
#         if len(d1) == 6:
#             d1.remove(d1[2])
#
#         date_split.append(d1)
#
#
#     date_epoch = []
#
#     for ds in date_split:
#
#         date_s = ds[1]+' '+ds[2]+' '+ds[4]
#
#
#         t1 = time.strptime(date_s,'%b %d %Y')
#         t_epoch = time.mktime(t1)
#         date_epoch.append(t_epoch)
#
#
#     x = date_epoch
#     y = likecount_list
#     mean_likecount = np.mean(y)
#
#     coefficients = np.polyfit(x, y, 1)
#     polynomial = np.poly1d(coefficients)
#     ys = polynomial(x)
#
#
#     # get standard deviation of like count
#
#     error = abs(ys-y)
#     mean_error = error.mean()
#     error_std = (ys-y).std()
#     error_std_percent = round(((error_std / mean_likecount) * 100),2)
#
#
#     #print ("Mean follcount for "+str(ul)+" is "+str(mean_likecount)+". Mean error is "+str(mean_error)+". Standard deviation is "+str(error_std)+"("+str(error_std_percent)+"%)")
#
#     plt.plot(x, y, '*', label=str(ul))
#     plt.xlabel('Epoch time')
#     plt.ylabel('Like count')
#
#     plt.errorbar(x,ys,error, label='std error '+str(error_std_percent)+'%')
#     pylab.legend(loc='upper left')
#     #plt.plot(x, ys)
#
#
#     #plt.show()
#
#     user_slope.append(ul)
#
#     # linregress method returns (slope, interception, etc)
#     # first item in the list returned is the slope of the linear line
#
#     slope = linregress(x, y)[0]
#
#     if slope < 0:
#
#         slope = 0.0
#
#     user_slope.append(str(slope))
#
#     user_slope_list.append(user_slope)
#
#
# # write results to a file
# f = open('slope/user_slope_nonprofit.txt','w')
#
# for usl in user_slope_list:
#     f.write(','.join(usl)+'\n')
#
# f.close()

#--------------------------------------
# PART II: get slope for like counts with interpolation

lines = open('others/user_nonprofit.csv','r').readlines()

user_list = []

for line in lines:
    spline = line.replace('\n','').split(',')
    user_list.append(spline[0])

user_list = ['NASA']

user_slope_list = []

for ul in user_list:

    user_slope = []

    lines = open('likes_interpolated/'+ul+'.csv','r').readlines()

    likecount_list = []
    date = []


    for line in lines:
        spline = line.replace('\n','').split(',')

        likecount_list.append(float(spline[1]))
        date.append(spline[0])

    date_split = []

    for d in date:
        d1 = d.replace('\n','').split('-')

        if int(d1[1]) < 10:
            d1[1] = '0' + d1[1]

        if int(d1[2]) < 10:
            d1[2] = '0' + d1[2]


        date_split.append(d1)


    date_epoch = []

    for ds in date_split:

        date_s = ds[2]+' '+ds[1]+' '+ds[0]


        t1 = time.strptime(date_s,'%d %m %Y')
        t_epoch = time.mktime(t1)
        date_epoch.append(t_epoch)


    x = date_epoch
    y = likecount_list
    mean_likecount = np.mean(y)

    coefficients = np.polyfit(x, y, 1)
    polynomial = np.poly1d(coefficients)
    ys = polynomial(x)


    # get standard deviation of like count

    error = abs(ys-y)
    mean_error = error.mean()
    error_std = (ys-y).std()
    error_std_percent = round(((error_std / mean_likecount) * 100),2)


    #print ("Mean follcount for "+str(ul)+" is "+str(mean_likecount)+". Mean error is "+str(mean_error)+". Standard deviation is "+str(error_std)+"("+str(error_std_percent)+"%)")

    plt.plot(x, y, '*', label=str(ul))
    plt.xlabel('Epoch time')
    plt.ylabel('Like count')

    plt.errorbar(x,ys,error, label='std error '+str(error_std_percent)+'%')
    pylab.legend(loc='upper left')
    #plt.plot(x, ys)


    plt.show()

    user_slope.append(ul)

    # linregress method returns (slope, interception, etc)
    # first item in the list returned is the slope of the linear line

    slope = linregress(x, y)[0]

    if slope < 0:

        slope = 0.0

    user_slope.append(str(slope))

    user_slope_list.append(user_slope)


# write results to a file
f = open('slope/interpolated_user_slope_space.txt','w')

for usl in user_slope_list:
    f.write(','.join(usl)+'\n')

f.close()

