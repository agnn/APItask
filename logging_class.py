import logging as lg

# logging file to create basic config file.

lg.basicConfig(filename= "log.txt",
               level=lg.DEBUG,
               format='[%(asctime)s - %(levelname)s - "Function" %(funcName)s] : %(message)s')
lg.info("info")

