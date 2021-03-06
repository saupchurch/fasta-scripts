##################################
#                                #
# Last modified 06/11/2012       # 
#                                #
# Georgi Marinov                 #
#                                # 
##################################

import sys
from sets import Set

def main(argv):

    if len(argv) < 2:
        print 'usage: python %s inputfilename outfilename' % argv[0]
        sys.exit(1)

    inputfilename = argv[1]
    outputfilename = argv[2]

    outfile = open(outputfilename, 'w')

    SequenceList=[]

    lineslist = open(inputfilename)
    i=0
    for line in lineslist:
        i+=1
        if i % 10000000 == 0:
            print str(i/2000000) + 'M reads processed'
        if line.startswith('>'):
            continue
        else:
            SequenceList.append(line.strip())

    SequenceList=list(Set(SequenceList))

    i=0
    for read in SequenceList:
        i+=1
        outline = '>read' + str(i)
        outfile.write(outline + '\n')
        outfile.write(read + '\n')

    outfile.close()

if __name__ == '__main__':
    main(sys.argv)

