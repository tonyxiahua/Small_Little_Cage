#!/usr/bin/env python
import subprocess
import datetime

subprocess.call(["lastb","-a",">","btmp.txt"])
subprocess.call(["git", "add", "."])
subprocess.call(["git", "commit", "-m", "auto import btmp snapshot " + str(datetime.datetime.now())])
subprocess.call(["git", "push"])
