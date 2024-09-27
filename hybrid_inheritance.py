class student: 
    def getDetails(self,id,name):
        self.id=id
        self.name=name
class Marks(student):
    def getMarks(self,s1,s2,s3):
        self.s1=s1
        self.s2=s2
        self.s3=s3
class Sports(student):
    def getSportsMark(self,sm):
        self.sm=sm
class Result(Marks,Sports):
    def display(self):
        self.total=self.s1+self.s2+self.s3
        self.avg=self.total/3
        self.score=self.avg + self.sm
        print("Total Marks:", self.total)
        print("Average Marks:",self.avg);
        print("Total Score:",self.score);

res=Result()
res.getMarks(89,90,93)
res.getSportsMark(99)
res.display()
