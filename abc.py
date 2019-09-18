
import subprocess
out = subprocess.Popen(['hadoop', 'fs','-ls','/hdfs/path'], 
   stdout=subprocess.PIPE, 
   stderr=subprocess.STDOUT)
stdout,stderr = out.communicate()
s = stdout.decode()
print(s)
print(type(s))
print('changes')
# test-repo
