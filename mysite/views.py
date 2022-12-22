from ast import arg
from asyncio.windows_events import NULL
from statistics import multimode
from wsgiref.util import request_uri
from click import password_option
import cursor
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
import mysql.connector as sql
from datetime import datetime
from django.contrib import messages
import Content_based_recomendation as ml


now = datetime.now() # current date and time
date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

def delete_post_job(request):
    m = sql.connect(host='localhost', user='root', passwd='', database='JobShip')
    cursor = m.cursor()

    d = request.POST
    for key, value in d.items():
            if key == "deleted_job_id":
                deleted_job_id = value
            
    sql_delete_query = """DELETE FROM `job` WHERE job_id='{}'""".format(deleted_job_id)
    cursor.execute(sql_delete_query)
       
    m.commit()
    return redirect('/posted_job')
def posted_job(request):
    
    args={}
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    jai=request.session.get('domain')    
    # c3 = """select * from pinned_job where job_applicant_id=23 """.format(request.session.get('job_applicant_id'))
    c3 = """select * from job where domain='{}'""".format(jai)# jai means job application id
    cursor.execute(c3)
    t = tuple(cursor.fetchall())
    # #print("This is t: ",t)
    p = list(t)
    # #print("This is th evalue of p[0] ",p[0])
    l=[]
    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['job_id']=pt[0]
        comp['name']=pt[1]
        comp['jobdescription']=pt[2]
        comp['jobtitle']=pt[3]
        comp['skills']=pt[4]
        comp['joblocation_address']=pt[5]
        comp['vacencies']=pt[6]
        comp['domain']=pt[7]
        comp['linkedin']=pt[8]
        comp['time']=pt[9]
        comp['post']=pt[10]



        l.append(comp)
    args['jobs']=l  
    #print("this is l:",l)   
    args['jobs']=l
       
    return render(request,'posted_job.html',args)

def post_job(request):
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    d = request.POST
    for key, value in d.items():
        if key == "jobtitle":
                jobtitle = value
        if key == "jobdescription":
                jobdescription = value
        if key == "skills":
                skills = value
        if key == "joblocation_address":
                joblocation_address = value
        if key == "vacencies":
                vacencies = value
        if key == "company":
                company = value
        if key == "domain":
                domain = value
        if key == "linkedin":
                linkedin = value
        if key == "post":
                post = value

               

    # c1 = """INSERT INTO pinned_job Values('{}','{}', '{}','{}');""".format(0,job_applicant_id,job_id,date_time)   
    
    c1 = """INSERT INTO job Values('{}','{}', '{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,company,jobdescription ,jobtitle,skills,joblocation_address,vacencies,domain,linkedin,date_time,post)    
    cursor.execute(c1)
    m.commit() 

    return redirect('/home/')


def delete_pinned_job(request):
    m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
    cursor = m.cursor()

    d = request.POST
    for key, value in d.items():
            if key == "deleted_job_id":
                deleted_job_id = value
            if key == "job_applicant_id":
                job_applicant_id = value
    sql_delete_query = """DELETE FROM `pinned_job` WHERE job_id='{}' and job_applicant_id='{}'""".format(deleted_job_id,job_applicant_id)
    cursor.execute(sql_delete_query)
       
    m.commit()

    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/pinned_job')
    elif request.method=="GET" and request.session.get('set')!='yes':
        return redirect('/')
    else:
        return redirect('/pinned_job')

    return redirect('/pinned_job')

def pinned_job(request):
    args={}
    m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
    cursor = m.cursor()
    jai=request.session.get('job_applicant_id')    
    # c3 = """select * from pinned_job where job_applicant_id=23 """.format(request.session.get('job_applicant_id'))
    c3 = """select * from pinned_job where job_applicant_id='{}'""".format(jai)# jai means job application id
    cursor.execute(c3)
    t = tuple(cursor.fetchall())
    p = list(t)
    #print(p)
    l=[]
    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['sno']=pt[0]
        comp['job_applicant_id']=pt[1]
        comp['job_id']=pt[2]
        comp['time']=pt[3]
        # here we fetched the job_id but we have to show the job description like home page
        # so we have to fetch the job from job id
        c4="""select * from job where job_id='{}'""".format(pt[2])
        cursor.execute(c4)
        t1 = tuple(cursor.fetchall())
        p1 = list(t1)
        pt1= list(p1[0])
        #print("this is job at job_id= ",pt[2]," is ",pt1)
        comp['comp_name']=pt1[1]
        comp['jobdescription']=pt1[2]
        comp['jobtitle']=pt1[3]
        comp['skills']=pt1[4]
        comp['joblocation_address']=pt1[5]
        comp['vacencies']=pt1[6]
        comp['domain']=pt1[7]
        comp['linkedin']=pt1[8]
        comp['time']=pt1[9]
        comp['post']=pt1[10]



        l.append(comp)
    # args['jobs']=l  
    #print("this is l:",l)   
    args['jobs']=l
       


    
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "job_applicant_id":
                job_applicant_id = value

            if key == "job_id":
                job_id = value
        #print('job applicant id is :',job_applicant_id)        
        c1 = """INSERT INTO pinned_job Values('{}','{}', '{}','{}');""".format(0,job_applicant_id,job_id,date_time)    
        cursor.execute(c1)
        m.commit() 
        return redirect('/home/')  

    
            
    return render(request,'pinned_job.html',args)


def index(request):
    return render(request, 'index.html')
def home(request):
    m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
    cursor = m.cursor()

    d = request.POST
    for key, value in d.items():
            if key == "email":
                em = value

            if key == "password":
                pwd = value
            if key =="q":
                q=value

    # c = "insert into job Values('job_id','company','jobdescription','jobtitle','skills','joblocation_address',current_timestamp(),'vacencies')"
    c = "select * from job order by job_id desc"
    # desc means it fetch the data in descending order

    cursor.execute(c)
    # m.commit() this is only for inserting the data
    t = tuple(cursor.fetchall())
    # for row in cursor:
    #     #print(row)
    # a=[""]*11
    # #print(t)
    p = list(t)
    args={'length':len(p)}

    # #print(p)
    #print("length of fetched data is :",len(p))
    # #print("this is second index: ",p[1])
    # #print("this is third index: ",p[2])
    # #print("this is third index: ",list(p[2]))
    l=[]

    for i in range (0,len(p)):
        comp={}
        pt =list(p[i])
        comp['job_id']=pt[0]
        comp['name']=pt[1]
        comp['jobdescription']=pt[2]
        comp['jobtitle']=pt[3]
        comp['skills']=pt[4]
        comp['joblocation_address']=pt[5]
        comp['vacencies']=pt[6]
        comp['domain']=pt[7]
        comp['linkedin']=pt[8]
        comp['time']=pt[9]
        comp['post']=pt[10]
        
        # #print(comp)
    # l.[i]=comp
        l.append(comp)
    #         #print(pt[j],end=" | ")
    #         args[f"d{i}{j}"]=pt[j] #if you want to take individual element of a row as a key in dictonary
    #     # args[f"d{i}"]=pt #if you want to take a row as an array in one key of dictonary
        # #print("it is pt :",pt)
            # it is pt : [4, 'company', 'jobdescription', 'jobtitle', 'skills', 'joblocation_address', datetime.datetime(2022, 3, 22, 18, 5, 21), 'vacencies']
# this is args:  {'length': 3}
    # #print("This is list of dictonories : ",l)
    args['jobs']=l
    # data={}
    #     # l.append(pt)
    #     #print('\n')

    # #print(l[1])
    # args['data':l]
    # data={'':''}

    # #print("this is args: ",args)
    
    # pt = p[0]
    # #print(p[0])
    # #print("hello")
    # ptp = list(pt)
    
    # #print(ptp) 
    # #print("this is first index: ",ptp[0])
    #how to pass list in dictonary
    #pehle hm list ki length pass karayege
    #phir loop ki help se args mai multiple element pass karayege
    # kyuki hme lenght pata hai to agle page (template) par bhi uski help se ek hi row ka data #print kar lenge
    return render(request, 'home.html',args)


def login(request):
    em = ''
    pwd = ''

    if request.method == "POST":
        m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
        cursor = m.cursor()

        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value

            if key == "password":
                pwd = value
            if key =="q":
                q=value

        c = "select id,firstname,lastname,college,degree,specialization,start_year,end_year from student where email='{}' and password='{}'".format(
            em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        # for row in cursor:
        #     #print(row)
        # a=[""]*11
        #print(t)
       

        if t == ():
            return HttpResponse(""" <script> 
            alert('Invalid Cridential');
            window.location='/login/'
            </script>""")
        else:
            p = list(t)
            pt = p[0]
            #print(p[0])
            #print("hello")
            ptp = list(pt)
            #print(ptp)  # it is a list of the data saved in database
            # #print(ptp[0])
            name = (ptp[1]+" "+ptp[2])
            # args = {'name': name, 'college': ptp[2], 'degree': ptp[3],
                    # 'specialization': ptp[4], 'start_year': ptp[5], 'end_year': ptp[6]}
            request.session['name']=name
            request.session['job_applicant_id']=ptp[0]
            request.session['email']=em
            request.session['password']=pwd
            request.session['set']='yes' #this is for setting the condition of session(session is set to yes)
#if session is clkeared then the value of request.session.get['set']is not equal to yes 😍
            return redirect('/user/')
    return render(request, 'login.html')


def login_company(request):
    em = ''
    pwd = ''
    gargs={'name':request.session.get('name')}
    if request.method == "POST":
        m = sql.connect(host='localhost', user='root',
                        passwd='', database='JobShip')
        cursor = m.cursor()

        d = request.POST
        for key, value in d.items():
            if key == "company_email":
                em = value

            if key == "company_password":
                pwd = value
            # if key =="q":
            #     q=value

        c = "select company_id,company_name,domain,establish_year,type_of_company,location,linkedin from company where email='{}' and password='{}'".format(em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        # for row in cursor:
        #     #print(row)
        # a=[""]*11
        #print(t)
       

        if t == ():
            return HttpResponse(""" <script> 
            alert('Invalid Cridential');
            window.location='/login/'
            </script>""")
        else:
            p = list(t)
            pt = p[0]
            #print(p[0])
            #print("hello")
            ptp = list(pt)
            #print(ptp)  # it is a list of the data saved in database
            # #print(ptp[0])
            request.session['name']=ptp[1]
            request.session['iscompany']='yes'
            request.session['login_id']=ptp[0]
            request.session['email']=em
            request.session['domain']=ptp[2]
            request.session['establish_year']=ptp[3]
            request.session['toc']=ptp[4]
            request.session['location']=ptp[5]
            request.session['linkedin']=ptp[6]
            request.session['set']='yes' #this is for setting the condition of session(session is set to yes)
#if session is clkeared then the value of request.session.get['set']is not equal to yes 😍
            return redirect('/company/')
    return render(request, 'login_company.html')


def company(request):
    id=request.session.get('email')
   
    def comp_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        # q = "Select * from company where email='{}'".format(id)
        q = """select name, location, email, domain, phone, summary,type_of_company , est_year ,about ,linkedin ,language_worked_with ,collab_tools ,opsys ,plateform_worked_with,honor_or_reward ,honor_or_reward_desc from comp_profile where email='{}'""".format(id)

        cursor.execute(q)
        #print(m1)
        t = tuple(cursor.fetchall())
        p = list(t)
        
        pt = p[0]
        ptp = list(pt)
        #print("The value of ptp is : ", ptp)

        kwargs = {'name':ptp[0],'location':ptp[1],'email':ptp[2],'domain':ptp[3],'phone':ptp[4],'summary':ptp[5],'type_of_company':ptp[6],'est_year':ptp[7],'about':ptp[8],'linkedin':ptp[9],'language_worked_with':ptp[10],'collab_tools':ptp[11],'opsys':ptp[12],'plateform_worked_with':ptp[13],'honor_or_reward':ptp[14],'honor_or_reward_desc':ptp[15],'cn':'cn'}
        return kwargs
        
    #print('you are:', request.session.get('name'))

    #print('your id:', request.session.get('email'))
    # request.session.set_expiry(1200) #this is to expire the session within 20 min of inactivity
    # this is the query function
    def query(fieldname,variable):
        c = """UPDATE comp_profile SET {}='{}' WHERE email='{}';""".format(fieldname,variable,id)
        cursor.execute(c)
        m.commit()

   
            
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key =="company_name":
                name = value
                query('name',name)
            if key=="location":
                location=value
                query('location',location)

            if key=="domain":
                domain=value
                query('domain',domain)

            if key=="phone":
                phone=value
                query('phone',phone)

            if key=="summary":
                summary=value
                query('summary',summary)

            if key=="toc":
                toc=value
                query('type_of_company',toc)

            if key=="est_year":
                est_year=value
                query('est_year',est_year)

                
            if key=="about":
                about=value
                query('about',about)

            if key=="honor_or_reward":
                honor_or_reward=value
                query('honor_or_reward',honor_or_reward)

            if key=="honor_or_reward_desc":
                honor_or_reward_desc=value
                query('honor_or_reward_desc',honor_or_reward_desc)

        # useer
        
        #print('your id within user post fxn',id)
        # post ewquest
        kwargs=comp_info(id)

        return render(request, 'company.html',kwargs)


    if  request.session.get('set')!='yes':
        return redirect('/')
    else: 
        # kwargs has to declare in else block if we call it before post request block it will throw an error
        kwargs=comp_info(id)    
        return render(request, 'company.html',kwargs)


def logout(request):
    request.session.clear()
    return redirect('/')    


def test(request):
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='test')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                name = value
            if key==   "password":
                password=value
            if key==   "email":
                email=value
            if key==   "dob":
                dob=value

        # INSERT INTO `test2` (`sno`, `name`, `email`, `password`) VALUES ('1', 'uh', 'kjhjg', 'jkjbkj');        
        c1 = """INSERT INTO test2  Values('{}','{}', '{}', '{}','{}');""".format('',name,password,email,dob)
        c2 = """INSERT INTO test Values('{}','{}', '{}', '{}');""".format('',name,password,'email')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()
    id=request.session.get('email')

    def company_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        q = "select name,place,email,website,phone,summary,experience,college,degree,timePeriod,certificate_name,certificate_desc,database_worked_with,language_worked_with,collab_tools,opsys,plateform_worked_with,honor_or_reward,honor_or_reward_desc from stud_profile where email='{}'".format(id)
        cursor.execute(q)
        t = tuple(cursor.fetchall())
        p = list(t)
        pt = p[0]
        #print(p[0])
        ptp = list(pt)
        #print(ptp)  # it is a list of the data saved in database
        # #print('length of ptp is: ',len(ptp))
        kwargs = {'name':ptp[0],'place':ptp[1],'email':ptp[2],'website':ptp[3],'phone':ptp[4],'summary':ptp[5],'experience':ptp[6],'college':ptp[7],'degree':ptp[8],'timePeriod':ptp[9],'certificate_name':ptp[10],'certificate_desc':ptp[11],'database_worked_with':ptp[12],'language_worked_with':ptp[13],'collab_tools':ptp[14],'opsys':ptp[15],'plateform_worked_with':ptp[16],'honor_or_reward':ptp[17],'honor_or_reward_desc':ptp[18],'cn':'cn'}
        return kwargs
    return render(request, 'company.html')


def settings(request):
    return render(request, 'settings.html')


def signup_company(request):
    args={'':''}
    name=''
    em=''
    pwd=''
    domain=''
    est_year=''
    toc=''
    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/')
    #  and request.session.get['set']!='yes'
    if request.method == "POST":
        
        m = sql.connect(host='localhost', user='root',passwd='', database='jobship')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "company_name":
                name = value
            if key == "email":
                em = value
            if key == "password":
                pwd = value
            if key == "domain":
                domain = value
            if key == "location":
                loc = value
            if key == "establish_year":
                est_year = value
            if key == "type_of_company":
                toc = value
            if key == "linkedin":
                linkedin = value
            
        c_auth="""Select *  from company where email='{}' """.format(em)
        cursor.execute(c_auth)
        t_auth=tuple(cursor.fetchall())
        if t_auth!=():
            return HttpResponse("""
            <script>
            alert('This Email is alredy register, Please Login')
            window.location='/signup_company'
            
            </script>
            
            """)

        
        
      
            #  INSERT INTO `company` (`company_id`, `company_name`, `email`, `password`, `domain`, `establish_year`, `type_of_company`, `location`) VALUES ('2', 'akdj', 'klhklh', 'lkjlk', 'lkj', '2022-03-02', 'lknk', 'lkn');
        c1="""INSERT INTO company Values('{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,name,em,pwd,domain,est_year,toc,loc,linkedin)    
        c2="""INSERT INTO comp_profile Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');""".format(0,name,loc,em,domain,'phone','summary',toc,est_year,'about your company',linkedin,'','','','','','')    
        
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()

        request.session['name']=name
        request.session['email']=em
        request.session['domain']=domain
        request.session['iscompany']='yes'
        request.session['linkedin']=linkedin
        request.session['set']='yes'
        args={'name':name,'email':em}

        return redirect('/company/')
    return render(request, 'signup_company.html')


def signup(request):
    # this is test branch
    fn = ''  # firstname
    ln = ''  # lastname
    em = ''  # email
    confem = ''  # confirmationemail
    pwd = ''  # password
    confpwd = ''  # confirmationpassword
    clg = ''  # college
    deg = ''  # degree
    spz = ''  # specialization
    sy = ''  # start_year
    ey = ''  # end_year
    
    if request.method=="GET" and request.session.get('set')=='yes':
        return redirect('/')
  
    #  and request.session.get['set']!='yes'
    if request.method == "POST":
        
        m = sql.connect(host='localhost', user='root',passwd='', database='jobship')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "firstname":
                fn = value
            if key == "lastname":
                ln = value
            if key == "email":
                em = value
            # if key == "confemail":
            #     confem = value
            if key == "password":
                pwd = value
            # if key == "password":
            #     confpwd = value
            if key == "college":
                clg = value
            if key == "degree":
                deg = value
            if key == "specialization":
                spz = value
            if key == "start_year":
                sy = value
            if key == "end_year":
                ey = value
                
            args = [fn, ln, em, pwd, clg, deg, spz, sy, ey]
            summary="This optional section can help you stand out to recruiters. If this section is empty, it will not appear on your resume."
            experience="This section is empty and won't appear in your resume."

        # this is to verify whether the email is already registered or not
        c_auth="""Select *  from student where email='{}' """.format(em)
        cursor.execute(c_auth)
        t_auth=tuple(cursor.fetchall())
        if t_auth!=():
            return HttpResponse("""
            <script>
            alert('This Email is alredy register, Please Login')
            window.location='/signup_company'
            
            </script>
            
            """)
        # this is to verify whether the email is already registered or not

        name=fn+" "+ln
        time_period=sy+"-"+ey
      
        c1 = """INSERT INTO student Values('{}','{}', '{}', '{}','{}','{}','{}','{}','{}','{}',current_timestamp());""".format(0, args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8])
        c2 = """INSERT INTO stud_profile Values('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}');""".format(0,name,'place',em,'wesite','phone','summary','experience',clg,deg,time_period,'cn','cd','dbs','lww','ct','opsys','pww','har','hard')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()

        request.session['name']=name
        request.session['email']=em
        request.session['set']='yes'
        request.session['issignup']='yes'

        return redirect('/user/')
        # request.session.['name']=name
    # elif request.session.get('set')=='yes':
    #     return redirect('/')
    
    return render(request, 'signup.html')    
    

def user(request):
    id=request.session.get('email')

    # args = {'name': request.session.get('name'),'email':request.session.get('email')}
    def user_info(id):
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        q = "select name,place,email,website,phone,summary,experience,college,degree,timePeriod,certificate_name,certificate_desc,database_worked_with,language_worked_with,collab_tools,opsys,plateform_worked_with,honor_or_reward,honor_or_reward_desc from stud_profile where email='{}'".format(id)
        cursor.execute(q)
        t = tuple(cursor.fetchall())
        p = list(t)
        pt = p[0]
        #print(p[0])
        ptp = list(pt)
        #print(ptp)  # it is a list of the data saved in database
        # #print('length of ptp is: ',len(ptp))
        kwargs = {'name':ptp[0],'place':ptp[1],'email':ptp[2],'website':ptp[3],'phone':ptp[4],'summary':ptp[5],'experience':ptp[6],'college':ptp[7],'degree':ptp[8],'timePeriod':ptp[9],'certificate_name':ptp[10],'certificate_desc':ptp[11],'database_worked_with':ptp[12],'language_worked_with':ptp[13],'collab_tools':ptp[14],'opsys':ptp[15],'plateform_worked_with':ptp[16],'honor_or_reward':ptp[17],'honor_or_reward_desc':ptp[18],'cn':'cn'}
        return kwargs
    # get request
    def recommended():
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        # this is for #printing recommendation
        if not  request.session.get('iscompany'):
            # #print("these are the recommendations :",ml.recommend(request.session.get('job_applicant_id')))
            # #print("This is your job applicant id :",request.session.get('job_applicant_id'))
            recj=ml.recommend(request.session.get('job_applicant_id'))
            
            # this will give us a list with recommended jobs
            rec_l=[]
            
            for i in range (0,5):
                rec_comp={}
                rec_c5= """select * from job where job_id='{}'""".format(recj[i])
                cursor.execute(rec_c5)
                rec_t=tuple(cursor.fetchall())
                rec_p=list(rec_t)
                rec_pt1=list(rec_p[0])
                rec_comp['comp_name']=rec_pt1[1]
                rec_comp['jobdescription']=rec_pt1[2]
                rec_comp['jobtitle']=rec_pt1[3]
                rec_comp['skills']=rec_pt1[4]
                rec_comp['joblocation_address']=rec_pt1[5]
                rec_comp['vacencies']=rec_pt1[6]
                rec_comp['domain']=rec_pt1[7]
                rec_comp['linkedin']=rec_pt1[8]
                rec_l.append(rec_comp)
    
            kwargs['recommended_jobs']=rec_l


    #print('you are:', request.session.get('name'))

    #print('your id:', request.session.get('email'))
    # request.session.set_expiry(1200) #this is to expire the session within 20 min of inactivity
    # this is the query function
    def query(fieldname,variable):
        c = """UPDATE stud_profile SET {}='{}' WHERE email='{}';""".format(fieldname,variable,id)
        cursor.execute(c)
        m.commit()

  
            
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='JobShip')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key =="name":
                name = value
                query('name',name)
            if key=="place":
                place=value
                query('place',place)

            # if key=="email":
            #     email=value
            #     query('email',email)
                # student_query('email', email)
                # email_change_query="""UPDATE student SET email='{}' WHERE email='{}';""".format(fieldname,variable,id)

            if key=="website":
                website=value
                query('website',website)

            if key=="phone":
                phone=value
                query('phone',phone)

            if key=="summary":
                summary=value
                query('summary',summary)

            if key=="experience":
                experience=value
                query('experience',experience)

            if key=="college":
                college=value
                query('college',college)

                
            if key=="degree":
                degree=value
                query('degree',degree)

                
            if key=="timePeriod":
                timePeriod=value
                query('timePeriod',timePeriod)

            if key=="certificate_name":
                certificate_name=value
                query('certificate_name',certificate_name)

            if key=="certificate_desc":
                certificate_desc=value
                query('certificate_desc',certificate_desc)

            if key=="database_worked_with":
                database_worked_with=value
                query('database_worked_with',database_worked_with)

            if key=="language_worked_with":
                language_worked_with=value
                query('language_worked_with',language_worked_with)

            if key=="collab_tools":
                collab_tools=value
                query('collab_tools',collab_tools)

            if key=="opsys":
                opsys=value
                query('opsys',opsys)

            if key=="plateform_worked_with":
                plateform_worked_with=value
                query('plateform_worked_with',plateform_worked_with)

            if key=="honor_or_reward":
                honor_or_reward=value
                query('honor_or_reward',honor_or_reward)

            if key=="honor_or_reward_desc":
                honor_or_reward_desc=value
                query('honor_or_reward_desc',honor_or_reward_desc)

        # useer
        
        #print('your id within user post fxn',id)
        # post ewquest
        kwargs=user_info(id)
        if not request.session.get('issignup'):
            recommended()

        return render(request, 'user.html',kwargs)


    if request.session.get('set')!='yes':
        return redirect('/')
    else: 
        kwargs=user_info(id)   
        if not request.session.get('issignup'):
            recommended()
        return render(request, 'user.html',kwargs)

def logout(request):
    request.session.clear()
    return redirect('/')    


def test(request):
    
    if request.method=="POST":
        m = sql.connect(host='localhost', user='root',passwd='', database='test')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "name":
                name = value
            if key==   "password":
                password=value
            if key==   "email":
                email=value
            if key==   "dob":
                dob=value

        # INSERT INTO `test2` (`sno`, `name`, `email`, `password`) VALUES ('1', 'uh', 'kjhjg', 'jkjbkj');        
        c1 = """INSERT INTO test2  Values('{}','{}', '{}', '{}','{}');""".format('',name,password,email,dob)
        c2 = """INSERT INTO test Values('{}','{}', '{}', '{}');""".format('',name,password,'email')
        cursor.execute(c1)
        cursor.execute(c2)
        m.commit()
   
    return render(request,'test.html')    

def job():
    pass

from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def pdfConvertor(template_src, context_dict={}):
    template= get_template(template_src)
    html= template.render(context_dict)
    result=BytesIO()
    pdf= pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None 

# class GeneratePDF(View):
def generate_view(request, *args, **kwargs):
    template= get_template('user.html')

    # fetching data from data-base
    m = sql.connect(host='localhost', user='root',passwd='', database='jobship')
    cursor = m.cursor()
    myList=[]
    args={'length':len(myList)}

    num=[1,2,3,4,5]

    d = request.POST
    for key, value in d.items():
        if key=='email':
            em_view=value
        

    c8="""SELECT * FROM stud_profile where email='{}'""".format(em_view)
    cursor.execute(c8)
    
    t = tuple(cursor.fetchall())

    p=list(t)
    args={'length':len(p)}
    #print(p)
    l=[]
    data={'':''}
    for i in range(0, len(p)):
        comp={}
        pt=list(p[i])
        comp['name']=pt[1]
        comp['place']=pt[2]
        comp['email']=pt[3]
        comp['website']=pt[4]
        comp['phone']=pt[5]
        comp['summary']=pt[6]
        comp['experience']=pt[7]
        comp['college']=pt[8]
        comp['degree']=pt[9]
        comp['timePeriod']=pt[10]
        comp['certificate_name']=pt[11]
        comp['certificate_desc']=pt[12]
        comp['database_worked_with']=pt[13]
        comp['language_worked_with']=pt[14]
        comp['collab_tools']=pt[15]
        comp['opsys']=pt[16]
        comp['plateform_worked_with']=pt[17]
        comp['honor_or_reward']=pt[18]
        comp['honor_or_reward_desc']=pt[19]
                                   
        #print("this is comp in generate view section ",comp)

        l.append(comp)
        
        #print("Testing the list: ",l)
        data={'student':l}
        #print(data)

    context=data
    #print("This is context from generate-view function(): ", context)
    html= template.render(context)
    pdf= pdfConvertor('user.html', context)

    return HttpResponse(pdf, content_type='application/pdf')
