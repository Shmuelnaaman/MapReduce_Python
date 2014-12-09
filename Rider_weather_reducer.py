import sys
import logging

from util import reducer_logfile
logging.basicConfig(filename=reducer_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def reducer():
    '''
    Given the output of the mapper, the reducer  print one row per weather type, 
    along with the average value of ENTRIESn_hourly for that weather type, 
    separated by a tab. 

    '''

    riders = 0      # The number of total riders for this key
    num_hours = 0   # The number of hours with this key
    old_key = None

    ENTRIESn_fpg_rain={}  
    weather_duration={}
    for line in sys.stdin:
        # your code here
            data = line.strip().split("\t")
#            logging.info(line)

            if data[1] not in ENTRIESn_fpg_rain:   
                ENTRIESn_fpg_rain[data[1]] = float(data[0])     
                weather_duration[data[1]] = 1

            else:              
                ENTRIESn_fpg_rain[data[1]] += float(data[0]) 
                weather_duration[data[1]] += 1                
    for i in ENTRIESn_fpg_rain:
            print '{0}\t{1}'.format(i, ENTRIESn_fpg_rain[i]/weather_duration[i])     

reducer()