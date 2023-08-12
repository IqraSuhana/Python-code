# the sys package contain the path list where the interpreter will look for the module/package that is imported in current module
import sys
print(sys.path)
#or print like this every separate path on separate line
for i in sys.path:
    print(i)

sys.path.insert(1,r'')  # insert the path of package you want interpreter to look for

import calendar
print(calendar.leapdays(2001,2023))
print(calendar.isleap(2024))