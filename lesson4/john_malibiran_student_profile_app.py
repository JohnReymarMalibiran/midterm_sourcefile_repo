# Parent class for basic student information.
class Student:
    def __init__(self, name, course, year_level):
        self.name = name
        self.course = course
        self.year_level = year_level

    def get_profile(self):

        profile = "<h2>" + self.name + "</h2>\n"
        profile = profile + "<p>Course: " + self.course + "</p>\n"
        profile = profile + "<p>Year Level: " + str(self.year_level) + "</p>"
        return profile


# Child class for an IT student.
class ITStudent(Student):
    
    skill = "Python"

    def get_skill(self):
      
        return "<p>Programming Skill: " + self.skill + "</p>"


# Application class with Flask-inspired routes.
class StudentApp:
    def __init__(self, title, student):
        
        self.title = title
        self.student = student

    def route(self, path):
       
        if path == "/":
            return "<h1>" + self.title + "</h1>"
        elif path == "/profile":
            
            return self.student.get_profile() + "\n" + self.student.get_skill()
        else:
            return "<h1>404 - Page Not Found</h1>"

    def run(self):
        
        print("Running: " + self.title + "\n")
        
        print("GET /")
        print(self.route("/"))
        
        print("\nGET /profile")
        print(self.route("/profile"))
        
        print("\nGET /unknown")
        print(self.route("/unknown"))



student = ITStudent("John Malibiran", "BS Information Technology", 4)
app = StudentApp("PSU Student Profile App", student)


app.run()