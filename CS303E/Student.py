# File: Student.py
# Student: Maxwell Kretschmer
# UT EID: mtk739
# Course Name: CS303E
# 
# Date Created: 3/24/21
# Date Last Modified: 3/24/21
# Description of Program: A class, with properties name, exam1, and exam2, that represents a student object with their name and grades. A getAverage() method is used to average the exam grades.


class Student :
    def __init__ ( self, nam = "", exam1 = "None", exam2 = "None") :
        self.__Name = nam
        self.__Exam1 = exam1
        self.__Exam2 = exam2

    def getName ( self ) : 
        return self.__Name
    def setName ( self, nam ): 
        self.__Name = nam
    def getExam1Grade ( self ) : 
        if("None" in str(self.__Exam1)):
            return 
        else:
            return self.__Exam1
    def setExam1Grade ( self, exam1 ): 
        self.__Exam1 = exam1
    def getExam2Grade ( self ) : 
        if("None" in str(self.__Exam2)):
            return 
        else:
            return self.__Exam2
    def setExam2Grade ( self, exam2 ): 
        self.__Exam2 = exam2

    def getAverage(self):
        if( ("None" in str(self.__Exam1)) or ("None" in str(self.__Exam2)) ):
            return "Some exam grades not available."
        else:
            return ( (self.__Exam1 + self.__Exam2) / 2 )

    def __str__ (self) :
        return "Student: "+ str(self.__Name) +"\n  Exam1: "+ str(self.__Exam1) +"\n  Exam2: "+ str(self.__Exam2)