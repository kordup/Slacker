from twill.commands import *

go('http://riseandshinemd.com:2082/')
setlocal('user','xyz')

setlocal('pass','123')
submit

#fv("1", "user", "blabla.com")
#fv("2", "pass", "testpass")
#submit()