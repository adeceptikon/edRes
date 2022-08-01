import random 
"""
program to generate map questions ( level 1 )
>>requires>> ./map_level_1.txt
"""
################SUBPARTS OF THE DOC################
n= '\n'
headingNo = "MAP"
documentClass = "\\documentclass[12pt, a4paper]{article}" 
packages = "\\usepackage[margin=0.5in]{geometry} "
title = "\\title{\\underline{" + headingNo + "}}"
tileExtended = "\\date{} " 
beginDocument = " \\begin{document} \
\\maketitle "

minipage = "\\small {\\underline{ F.M. 20} \\hfill \\underline{time : 20 min} } \n\
\\\\ \n\
\\linebreak \n \
\\large { \\bf \\textit {On a map locate the following: }} " + n
closing = "\\end{document}\n"
######################################################

# a  = 'sd.flkfsdl'
f = open("./map_level_1.txt" , "r") 
questions = f.readlines()
cnt  = len(questions)

noOfQuestions = input("how many questions do you want ? ")
nQ = random.sample(range(0,cnt) , (int)(noOfQuestions) )        #no. of questions , change here if required 

# print(questions)
# print(n)
out = documentClass + n + packages + n + title + n + tileExtended + n + beginDocument + n + minipage + n  

out = out + "\n\\begin{enumerate}\n"

for i  in range(0,len(nQ)):                          
    index = nQ[i]
    out = out + "\item " + questions[index]

out= out + "\\end{enumerate}\n"

out = out + closing

o = open("./mapOut.txt" , "w+")
print(out, file=o) 
print(out)
f.close()


a = input()
