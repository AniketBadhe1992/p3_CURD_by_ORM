from django.shortcuts import render

def gittest(request):
    pass
'''
1.cmd                                                     :create project name & app name
2.Installed app(settings.py)                  :'p3_app',
3.DATABASES  (settings.py)                   :add DB settings ==>'NAME': 'p3_curd_orm',     & check in console
4.models.py()                                          :add models ;(model name work as table name;model field work as table column)
                                                                terminal:QuerySet=<QuerySet [<Worker: Worker object (1)>]
                                                                to show fields instead of Worker object(1)  
                                                                write belows code after writing model class
                                                                def __str__(self):
                                                                        return self.ename
5.terminal                                               :python manage.py makemigrations
                                                                 python manage.py migrate
6.sql command prompt:                         :check table created or not



#CURD operation perform by using:         1.python shell/python console with ORM queries
                                                                    2.Admin side presentation
                                                                    3.Django template presentation
                                                                    4.mysqlDB.CURD command
#ID column can not be duplicate ;remaining be duplicate;deleted id not generate again.

7.CURD Operations by ORM (Object Relational Mapping) query Start:
    QuerySet=Database Record(process of accessing DB record or store data in DB)
    CURD(Create,Update,Read,Delete) in fields (column of table):
    
7.1.Create data in fields of Database table :-------->
        step1.python console(pycharm):           
         from <appname>.models import <modelname>       
        from p3_app.models inport Worker;
        
        step2.create object of model and save it;
       [ syntax:object name=<model name>(field1="value1",field2="value2",...........)]                                          
       - worker=Worker(ename="Aniket",salary=25000,city="Akola")     #create model name object
        worker.save()                                                                                   #by this above data save permanant in DB;after it showing in sqlcmd
         [by this backend side one query will execute insert into Worker(..)values(..)]
         worker.ename                                                                                #'Aniket'            
         worker.salary                                                                                  #25000       
         worker.city                                                                                      # 'Akola'   
        
        #OR
       [ syntax:<modelname>.objects.create(field1="value1",field2="value2",...........)]
        -Worker.objects.create(ename="Harsha",salary=50000,city="Hyderabad")     
7.2]Accessing of data-------------------->                                                                                                          #directly get saved
     count,Indexing,slicing--------->  
         Worker.objects.all()                                                                        #show all data@table
        
        emps=Worker.objects.all()
        len(emps)                                                                                           #or
        Worker.objects.all().count()                                                              #[in mysql prompt:select count(*) from p3_app]
        emps                                                                                                   #showing all key:value list
        emps[0]                                                                                               #indexing
        emps[1]
        emps[-1]                                                                                              #ValueError: Negative indexing is not supported.
        Worker.objects.all()[3]        
        
        emps[0:2]                                                                                            #slicing:[<Worker: Aniket>, <Worker: Vishal>]                                          
                                                                                                                    #[in mysql prompt:select * from p3_app_Worker limit 2]
        emps[1:3]                                                                                           #[<Worker: Vishal>, <Worker: Harsha>] index of 1st and 2nd get
                                                                                                                     #[in mysql prompt:select * from p3_app_Worker limit 2 offset 1]
       fetching data(get(),all(),values(),filter(),exclude()-------------->
        Worker.objects.all().last();
        Worker.objects.all().first();
        Worker.objects.get(id=3);                                                                   #to show specific record
                                                                                                                       #[in mysql prompt:select * from p3_app_Worker where id=3]
                                                                                                                        #get method for geting single record based on primary key.
        Worker.objects.filter(salary=80000)                                                    #filter method for getting multiple similar recoreds;
                                                                                                                            if wrong salary then through empty querySet
        Worker.objects.filter(salary=80000).count()                                         #how much worker having salary=80000==>2
        Worker.objects.exclude(salary=80000)                                                 show other entries without 80000 salary entry
                                                                                                                         #[in mysql prompt:select * from p3_app_Worker where not salary=80000]
         Worker.objects.values()                                                                         #showing all sets all key:values  one by one        
         Worker.objects.values('id','ename')                                                      #showing only  sets of id,name[ key:values]  one by one     
                                                                                                                         #[in mysql=>select id,ename from p3_app_worker;]
        Worker.objects.values_list()                                                                   #    querySet of values only
        Worker.objects.values_list('id','ename')                                                #    querySet of values (id,name)only
        
    #  lookup concept  : below explained look__up concept followed by two underscore.(__)
        [  __contains,__startswith,__istartswith,__endswith,__iendswith,__gt , __gte , __lt , __lte,__in,__range, ]
        
        Worker.objects.filter(id__gt=2)                                                             #showing ids details greter than 2nd id
        Worker.objects.filter(id__gte=2)                                                           #showing ids details >=2nd id
        Worker.objects.filter(id__lt=4)                                                             #showing ids details lower than 2nd id
        Worker.objects.filter(id__lte=4)                                                             #showing ids details <= 2nd id
    
    7.3Updating data in field:---------------->
        Worker.objects.filter(id=6).update(salary=10000)                                #id no.6 employ salary update as 10000
        Worker.objects.filter(id=6).update(ename="Rajesh")
        Worker.objects.all().update(salary=3000)                                             #all salary updated as 3000
        
        emp=Worker.objects.get(id=4)
        emp.salary=150000
        emp.save()
    
    7.3)deleting:------------------------>
        Worker.objects.filter(id=6).delete()                                                       #delete single recored
        Worker.objects.all().delete()                                                                   #delete all records    
         y = Worker.objects.get(sal = 40000)
         y.delete()
        Worker.objects.all()                                                                    #here Worker=model ;  objects=manager ; all():method
 Q. difference between get and filter ?
 Q.difference between filter and exclude?
 Q.difference between save and create method.       
        
        
#django by default provide 'objects' manager to each model;
#ORM?(object relational mapping concept):orm converting data between incompatible type system using  object orienting 
            programig language like:[DBdata --to--> python data--to-->json format--to-->python type--to--DB format  ]
            -sql(structured querry language) dealing with realational database likr mysql,oracleDB,
            -app1 to app2 communicate ti json module
            -application relate data ORM querries convert into sql code interact with  DB format
            app1----------------communicate by json module[mediator] to-------------------------------->app2
            APP2code-----------------------------------------------<sql code>---------------------------------------------------->mysql Database code
                                converting into                                                            interacting
            
            -by using sql:we can access and manipulate DB(MYSQL).
#why ORM: by using ORM ,developer can write python code instead of sql code to CURD operation
        Querryset :list of object of given models.   :querryset allow u to read data from DB.         
        MANAGER:DB is acessing thorugh manager:every model having manager called'objects'.so by manager we can handle model clsss.


-------------------------------------------------
from p3_app.models import Worker

# create data:
1.worker=Worker(ename='sopan',salary=40000,city='nashik')
    worker.save()
2.Worker.objects.create(ename='sunita',salary=70000,city='rampur')
3.Worker.objects.bulk_create([Worker(ename='ashwin',salary=80000,city='bhatinda'),
                                                    Worker(ename='suyog',salary=100000,city='muktainagar'),
                                                    Worker(ename='roshani',salary=75000,city='bhusawal') ] )


# read data:
1.Worker.objects.all()                                                                                                [select * from p3_app_Worker]
2.Worker.objects.all()[3]                                                            Indexing                                                   
3.Worker.objects.all()[3:5]                                                         slicing
3.1.Worker.objects.all().first()                                                   1st recored
3.2.Worker.objects.all().last()
3.3.print(Worker.objects.all().query)                                           sql code getting
4.Worker.objects.all().count()                                                    count
4.Worker.objects.count()                                                            count
5.Worker.objects.values()                                                           [(k:v),(k:v)]              
5.Worker.objects.values('id','ename')                                        [select id,ename from Worker]             
6.Worker.objects.filter(ename='sunita')                                    details of 'sunita' ename
7.Worker.objects.exclude(ename='sunita')                                all data except sunita ename
8.Worker.objects.get(ename='sunita'                                        object format getting/Worker.DoesNotExist
9.Djano loop_up concept:
9.1.Worker.objects.filter(ename__exact='sunita')
9.2.Worker.objects.filter(ename__contains='sunita')
9.2.Worker.objects.filter(ename__icontains='sunita')              i means case not matter
9.3Worker.objects.filter(ename__startswith='sunita')            [select * from p3_app_worker where ename like 's%';]
9.3Worker.objects.filter(ename__istartswith='sunita')            i means case not matter
9.4.Worker.objects.filter(ename__endswith='badhe')            [select * from p3_app_worker where ename like '%a';]
9.4.Worker.objects.filter(ename__iendswith='badhe')           i means case not matter
9.5.Worker.objects.filter(id__gt=4)                                             greater than                                                 
9.5.Worker.objects.filter(id__gte=4)                                           greater than  O equal to         
9.5.Worker.objects.filter(id__lt=4)                                              less than   
9.5.Worker.objects.filter(id__lte=4)                                            lessthan or equalto 
9.6.Worker.objects.filter(id__in=[2,4])                                         [select * from p3_app_worker where id in (2,6);]
9.7.Worker.objects.filter(id__range=[2,4])                                  [select * from p3_app_worker where id between 2 and 6;]
9.8.Worker.objects.filter(salary__gt=30000) & Worker.objects.filter(city__contains='nagpur')
9.9.Worker.objects.filter(Q(salary__gt=79000) |~Q(city__contains='Akola'))               [~   =except this contents]

10.from django.db.models import Q,Avg,Max,Min,Sum,Count
10.1.Worker.objects.filter(Q(salary__gt=30000) & Q(city__contains='nagpur'))        [SAME AS 9.8 POINT.]
10.2.Worker.objects.filter(Q(salary__gt=30000) | ~Q(city__contains='nagpur'))         [OR]

11.Aggrigation functions:
11.1.Worker.objects.all().aggregate(Sum('salary'))
11.1.Worker.objects.all().aggregate(Total_sum=Sum('salary'))
11.2.Worker.objects.all().aggregate(Max('salary'))
11.3.Worker.objects.all().aggregate(Min('salary'))
11.4.Worker.objects.all().order_by('salary')                                 [ low to high ][ select * from p3_app_worker order by salary;]
11.5.Worker.objects.all().order_by('-salary' '-ename')                   [ high to low][ select * from p3_app_worker order by -salary;][select * from p3_app_worker order by -salary desc]







# update data:
1.Worker.objects.update(salary=15000)
2.Worker.objects.filter(ename='raghu').update(salary=15000)

# delete data  :  
1.Worker.objects.delete()
2.Worker.objects.filer(ename='sunita').delete()    
    
    
    
    
    
                                                                 
'''
