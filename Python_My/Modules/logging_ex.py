#logging--> It is used to log details of records it is processing:
#logging --> is the module
import logging
logging.basicConfig(filename='log.txt',level=logging.INFO,format='%(asctime)s:%(name)s:%(message)s')
logging.info('processing new record')
try:
    x=int(input('Enter x:'))
    y=int(input('Enter y:'))
    print(x/y)
except ZeroDivisionError as msg:
    print("can't div by zero")
    logging.exception(msg)
except ValueError as msg:
    print("only int values are accepted")
    logging.exception(msg)
try:
    logging.info('processed for record {} & {}'.format(x,y))
except NameError as msg:
    print('log error')
    logging.exception(msg)
close('log.txt')
