fname = input('Please enter the name of the file: ')
# in case the entered name has spaces before or after
fname = fname.rstrip().lstrip()

# in case the entered name is causing the program to stop and producing an error.vim
try:
    fhand = open(fname, 'r')
except:
    print('The name you have entered is not readable by the program!!!\nFile can not be opened:', fname)
    exit()

spam_conf = 0
count = 0
for line in fhand:
    if 'X-DSPAM-Confidence' in line:
        # print(line.rstrip())
        index = line.find(':')
        # print(line[index+1:].rstrip())
        spam_conf = spam_conf + float(line[index+1:].rstrip())
        count = count + 1

avr_spam_conf = spam_conf/count
print('average spam confidence =', avr_spam_conf)
