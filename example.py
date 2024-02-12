#!/usr/bin/python3

import datetime,os



def add_log(script_path=os.path.dirname(os.path.abspath(__file__))):
    log_file = os.path.join(script_path,'log.txt')
    with open(log_file,'at') as o:
        line = [str(datetime.datetime.now()),'Hello world!']
        o.write('\t'.join(line) + "\n")
    return log_file

    
if __name__ == "__main__":
    log_file = add_log()

