from django.shortcuts import render
import mysql.connector as sql
PSEUDO=''
MPD=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='scameyes')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="PSEUDO":
                em=value
            if key=="MPD":
                pwd=value
        
        c="select * from users where PSEUDO='{}' and password='{}'".format(PSEUDO,MPD)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"welcome.html")

    return render(request,'login_page.html')
