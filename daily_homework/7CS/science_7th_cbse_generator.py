import random 
"""
program to generate science questions ( level 1 )
>>requires>> ./7CS.txt
"""
f = open("./7CS.txt" , "r") 
questions = f.readlines()
cnt  = len(questions)

nQuesRequired = input("how many questions do you want ? ")
nQ = random.sample(range(0,cnt) , (int)(nQuesRequired) )        #no. of questions , change here if required 

out = ''
n = "\n"
################SUBPARTS OF THE DOC################
headingNo = "7CS"
documentClass = "\\documentclass[12pt, a4paper]{article}" 
packages = "\\usepackage[margin=0.5in]{geometry} "
title = "\\title{\\underline{" + headingNo + "}}"
tileExtended = "\\date{} " 
beginDocument = " \\begin{document} \
\\maketitle "

minipage = "\\small {\\underline{ F.M. 20} \\hfill \\underline{time : 20 min} } \n\
\\\\ \n\
\\linebreak \n \
\\large { \\bf \\textit {Answer in one word or one line}} " + n
closing = "\\end{document}\n"
######################################################

out = documentClass + n + packages + n + title + n + tileExtended + n + beginDocument + n + minipage + n  

out = out + "\n\\begin{enumerate}\n"
for i  in range(0,len(nQ)):                          
    index = nQ[i]
    out = out + "   \item " + questions[index]

out= out + "\\end{enumerate}\n"

out = out + closing

o = open("./7CSquestions.txt" , "w+")
print(out, file=o) 
print(out)
f.close()


a= 'z'
while a == 'z' :
    a = input()