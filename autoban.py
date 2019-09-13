import subprocess
import datetime
import csv
import collections
'''
Author : Xia Hua 2019 Sep 12
'''
'''
Easy Add method for dictionary 
'''
class dicTemplate(dict): 
    # __init__ function 
    def __init__(self): 
        self = dict() 

    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
        
'''
Text Handling ,dealing with text data
'''
class text2Dic:
    def __init__(self):
        self.name = dicTemplate()
        self.ip = dicTemplate()
        self.orderedName = dicTemplate()
        self.orderedIP = dicTemplate()
        
        with open("btmp.txt") as f:
            '''
            In the case you are working with Big Data using readlines() 
            is not very efficient as it can result in MemoryError. 
            '''
            for lines in f:
                if (lines == '\n'):
                    break
                if (lines[:7].rstrip() in self.name.keys()):
                    self.name[lines[:7].rstrip()] += 1
                else:
                    self.name.add((lines[:7]).rstrip(),1)
                if (lines[60:].rstrip('\n') in self.ip.keys()):
                    self.ip[lines[60:].rstrip('\n')] += 1
                else:
                    self.ip.add((lines[60:].rstrip('\n')),1)
    def nameProcess(self):
        return self.name
    def ipProcess(self):
        return self.ip
    def printNamebyAlphabet(self):
        for key in sorted(self.name.keys()):
            print("%s: %s" % (key, self.name[key]))
    def printIPbyAlphabet(self):
        for key in sorted(self.ip.keys()):
            print("%s: %s" % (key, self.ip[key]))
            
    def sortNamebyValue(self):
        self.orderedName = collections.OrderedDict(sorted(self.name.items(), key=lambda kv: kv[1]))
        #return self.orderedName
    
    def sortIPbyValue(self):
        self.orderedIP = collections.OrderedDict(sorted(self.ip.items(), key=lambda kv: kv[1]))
        #return self.orderedIP
    
    def saveNametoCSV(self):
        self.sortNamebyValue()
        try:
            with open('NameOutput.csv', 'w') as f:
                for key in self.orderedName.keys():
                    f.write("%s,%s\n"%(key,self.orderedName[key]))
        except IOError:
            print("I/O error")  
            
    def saveIPtoCSV(self):
        self.sortIPbyValue()
        try:
            with open('IPoutput.csv', 'w') as f:
                for key in self.orderedIP.keys():
                    f.write("%s,%s\n"%(key,self.orderedIP[key]))
        except IOError:
            print("I/O error") 
'''
main function
'''

def main():
    startime = datetime.datetime.now()
    """
    create new jobs object to text2Dic
    """
    jobs = text2Dic()
    #jobs.printNamebyAlphabet()
    #jobs.printIPbyAlphabet()
    jobs.saveIPtoCSV()
    jobs.saveNametoCSV()
    #Time Calculator
    
    
    '''
    '''
    endtime = datetime.datetime.now()
    print("Total time used: ",endtime - startime)
    #Comment out for disable github push
    #subprocess.call(["git", "add", "."])
    #subprocess.call(["git", "commit", "-m", "auto import btmp snapshot " + str(datetime.datetime.now())])
    #subprocess.call(["git", "push"])
    
if __name__ == "__main__":
    main()
    
'''
Example TEXT
upload   ssh:notty    Thu Sep 12 21:58 - 21:58  (00:00)     113.134.211.228
upload   ssh:notty    Thu Sep 12 21:58 - 21:58  (00:00)     113.134.211.228
oracle   ssh:notty    Thu Sep 12 21:56 - 21:56  (00:00)     h213-21-67-184.cust.a3fiber.se
oracle   ssh:notty    Thu Sep 12 21:56 - 21:56  (00:00)     h213-21-67-184.cust.a3fiber.se
'''
