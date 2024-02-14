#!/usr/bin/python
import os
import re
import sys

def main():
    for line in sys.stdin:
        match = re.match(r'^#', line)

        fields = line.strip().split(':') #strip any whitespace and split into an array

        if match or len(fields) != 5: #This checks if the line starts with # or does not have exactly
            continue                  # 5 fields, then skips to next iteration if not.
                                      #I believe that this code skips the # because in code creation #
                                     #usually are for annotating or notes for the administrators. Also
                                     #skipping 5 lines to ensure it has a structured and predictable format
                                     #so the admins do not run into any problems in the future
        username = fields[0]
        password = fields[1]

        gecos = "%s %s,,," % (fields[3],fields[2])
        groups = fields[4].split(',') #Splits the last field into a list based on ',' to handle multiple
        #group assignments and so it can differ from each group assignment from eachother.
        print "==> Creating account for %s..." % (username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        #print cmd
        os.system(cmd) #This line executes the command in the shell
        print "==> Setting the password for %s..." % (username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        #print cmd
        os.system(cmd)
        
        for group in groups: #This for loop iterates through each item in groups list checks and ignores the place holders '-', and is also used to assign the user to multiple groups thats why the for loop is neccessary because they might be assigned to hundreds of groups and needs to process each group individually and - stops it because it is used to indicate that there is no additional groups to assign the user to.
            if group != '-':
                print "==> Assigning %s to the %s group..." % (username, group)
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                #print cmd
                os.system(cmd)
if __name__ == '__main__':
    main()

