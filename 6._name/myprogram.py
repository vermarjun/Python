#Importing my_func() from mymodule.py
from mymdule import my_func
#Calling that my_func*=() here now..
my_func()

#importing file from main folder
from mainfolder import report_main
report_main.mainfolder()
#importing file from subfolder inside main folder
from mainfolder.subfolder import report_sub
report_sub.subfolder()
