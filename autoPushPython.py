#!/usr/bin/env python
import subprocess
import datetime

subprocess.call(["git", "add", "--all", "."])
subprocess.call(["git", "commit", "-m", "auto import btmp snapshot " + str(datetime.datetime.now())])
subprocess.call(["git", "push"])
