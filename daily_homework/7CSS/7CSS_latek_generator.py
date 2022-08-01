import random 
from datetime import date
"""
program to generate 7CSS     questions ( level 1 )
>>requires>> ./map_level_1.txt
"""

#no. of questions , change here if required 
noOfGeoQuestions = 10
noOfMapQuestions = 10
noOfHistoryQuestions = 10
baseDate  = ""
headingNo  ="7CSS"  #take from input 


n = "\n"
################SUBPARTS OF THE DOC################
documentClass = "\\documentclass[10pt, a4paper]{article}" 
packages = "\\usepackage[margin=0.5in]{geometry} "
title = "\\title{\\underline{" + headingNo + "}}"
tileExtended = "\\date{} " 
beginDocument = " \\begin{document} \n\\maketitle "
minipage = "\\small {\\underline{ F.M. 20} \\hfill \\underline{time : 20 min} } \n\\vspace{5mm} " + n 
closing = "\\end{document}"

######################################################
out = documentClass + n + packages + n + title + n + tileExtended + n + beginDocument + n + minipage + n  #Connecting all the subparts 
# print(out)

#open files
fmap = open("./map_level_1.txt" , "r") 
fgeo = open("./7CSS_geography.txt" , "r") 
fhistory = open("./7CSS_history.txt" , "r") 

#read filecontents into ararys 
geoQuestions = fgeo.readlines()
mapQuestions = fmap.readlines()
historyQuestions = fhistory.readlines()


########################## for geography: create questions and add to output ###################################
cnt  = len(geoQuestions)
# noOfQuestions = input("how many questions do you want ? ")
n = random.sample(range(0,cnt) , (int)(noOfGeoQuestions) )  #sample index selection, use index to select questions       

out = out + '\\large \\underline{GEOGRAPHY}\n\\begin{enumerate}\n'
for i  in range(0,len(n)):                          
    index = n[i]
    out = out + "   \\item " + geoQuestions[index]
out = out + "   \\item On the map locate the following:"      #uncomment this line for renormalisation 
out = out + "\n   \\begin{enumerate}\n"                       #uncomment this line for renormalisation 


########################## for map: create questions and add to output ###################################
cnt  = len(mapQuestions)
# noOfQuestions = input("how many questions do you want ? ")
n = random.sample(range(0,cnt) , (int)(noOfMapQuestions) )        #no. of questions , change here if required , index of the random questions

for i  in range(0,len(n)):                          
    index = n[i]
    out = out + "       \\item " + mapQuestions[index]

out = out + "\n   \\end{enumerate} \n"#\\end{enumerate}"


########################## for history :create questions and add to output ###################################
out = out + "\\underline{HISTORY} \n\\begin{enumerate}\n"
cnt  = len(historyQuestions)
# noOfQuestions = input("how many questions do you want ? ")
n = random.sample(range(0,cnt) , (int)(noOfHistoryQuestions) )        #no. of questions , change here if required , index of the random questions

for i  in range(0,len(n)):                          
    index = n[i]
    out = out + "       \item " + historyQuestions[index]

out= out + "\\end{enumerate}"

out = out + closing

o = open("./out7CSS.txt" , "w+")
print(out, file=o)                              #print(content , file=(fileHandle))
print(out)                                      #output to screen 

o.close()
fmap.close()
fhistory.close()
fmap.close()


a= input()
