#!/usr/bin/python3

import datetime,os



def add_log(script_path=os.path.dirname(os.path.abspath(__file__))):
    log_file = os.path.join(script_path,'log.txt')
    with open(log_file,'at') as o:
        line = [str(datetime.datetime.now()),'Hello world!']
        o.write('\t'.join(line) + "\n")
    return log_file

# def read_log(log_file):
#     with open(log_file) as i: last_entry = [elem.strip().split("\t")[0] for elem in i][-1]
#     old_date = datetime.datetime.fromisoformat(last_entry)
#     new_date = datetime.datetime.now()
#     print(f"It literally took me {(new_date - old_date).total_seconds()} seconds to switch branches.")
    
    
if __name__ == "__main__":
    log_file = add_log()
    #read_log(log_file)
