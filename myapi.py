from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel  

app=FastAPI()

students= {
    1:{
        "name":"John_Doe",
        "age":"17",
        "year":"10"
    },
    2:{
        "name":"Alina Chalk",
        "age":"19",
        "year":"10"
    },
    3:{
        "name":"Clark Kent",
        "age":"17",
        "year":"10"
    },
    4:{
        "name":"Strawberry Kurosaki",
        "age":"17",
        "year":"10"
    }
}

class Student(BaseModel):
     name:str
     age:int
     year:int

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

#GET : Get data from the DB / Program
@app.get("/")   
 
def index():
    return {"name": "First Data"} #json data

#Path Parameters

#originally you had to write Path(None,description...) it also has other 
#args like lt-less than le-less than or equal to, same with gt and ge 
@app.get("/get-students/{student_id}")
def student(student_id: int = Path(description="Enter Student ID")):
    if student_id not in students:
          return {"Error":"ID doesn't exist"}
    return students[student_id]

#Query Parameter
@app.get("/get-by-name/{student_ID}")
def get_student(student_ID: int,name: Optional[str] = None):
    if student_ID not in students:
          return {"Error":"ID doesn't exist"}
    if(student_ID<=len(students)):
            return students[student_ID]
    name = name.replace(" ","_").title()
    for student_id in students:
        if(students[student_id]["name"]==name):
            return students[student_id]
    return {"Data not found"}


#POST: Post data into the program/db 
@app.post("/create-stundent/{student_id}")
def create_student(student_id :int,student: Student):
     if(student_id in students):
          return{"Error: Already Exists"}
     
     students[student_id]=student
     return students[student_id]

#PUT : Update data
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students: 
        return {"Error": "ID not valid"}
    
    if student.age!=None:
         students[student_id]["age"] = student.age
    if student.name!=None:
         students[student_id]["name"] = student.name
    if student.year!=None:
         students[student_id]["year"] = student.year
    

    return students[student_id]

#DELETE : Delete data
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
     if student_id not in students:
          return {"Error":"ID doesn't exist"}
     del students[student_id]
     return {"Message":"Student Deleted Succesfully"}