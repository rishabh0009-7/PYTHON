# python inner working (behind the scenes in python)

#source code ====> byte code (hidden) ====> fetch into ====>python virtual machine ===> and then code run 
#1. compile to byte code 
# byte code is a low level code and it is platform independent
#byte code run faster 
#.pyc --> compiled python ( also known as frozen binaries )
#__pycache__ - this  system folder is created to organise frozen binaries versions deleetd updated in this folder, source code changes , python versions etc
# this pycache is created only when we import one file from another thats why  we imported basic func from hello.py to basic.py



#python virtual machine  is machine in which code loop to iterrate  byte code 
#also known as python interpreter

#byte code is not machine code 
#standard python implementation - cpython 
#there are other also jython. iron python,stackless,pypy