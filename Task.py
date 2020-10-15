class Person():
    def __init__(self,name,bdate,tdate):
        self.name = name
        self.bdate = bdate
        self.tdate = tdate
        self.lst = []

    def vozrast(self):
        self.vozr = self.tdate - self.bdate

    def info(self):
        Person.vozrast(self)
        disc  = (' Имя: ' + self.name + ' Возраст: ' + str(self.vozr) ).title()
        print(disc)

    def add(self):
        self.lst.extend(self)

    def showlst(self):
        print(self.lst)

class abitur(Person):
    def __init__(self,name,bdate,tdate,fac):
        super().__init__(name,bdate,tdate)
        self.fac = fac

    def info(self):
        Person.info(self)
        disc = (" Факультет: " + self.fac)
        print(disc)


class Student(Person):
    def __init__(self,name,bdate,tdate,fac,kurs):
        super().__init__(name,bdate,tdate)
        self.fac = fac
        self.kurs = kurs

    def info(self):
        Person.info(self)
        disc = (" Факультет: " + self.fac + ' Курс: ' + str(self.kurs))
        print(disc)


class Prepod(Person):
    def __init__(self,name,bdate,tdate,fac,dolg, stag):
        super().__init__(name,bdate,tdate)
        self.fac = fac
        self.dolg = dolg
        self.stag = stag

    def info(self):
        Person.info(self)
        disc = (" Факультет: " + self.fac + ' Должность: ' + self.dolg + " Стаж: " + str(self.stag))
        print(disc)
