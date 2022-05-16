from django.shortcuts import render
import mysql.connector as sql
NOM=''
PSEUDO=''
EMAILUSER=''
MDP=''
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='scameyes')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="NOM":
                fn=value
            if key=="PRENOM":
                ln=value
            if key=="EMAILUSER":
                em=value
            if key=="MDP":
                pwd=value
        
        c="insert into UTILISATEUR Values('{}','{}','{}','{}','{}')".format(NOM,PSEUDO,EMAILUSER,MDP)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
