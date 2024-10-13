use CMS
CREATE TABLE Department (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(100)
);

CREATE TABLE Teacher (
    TeacherID INT PRIMARY KEY Identity(1,1),
    TeacherName VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);
CREATE TABLE Student (
    StudentID INT PRIMARY KEY Identity(1,1),
    StudentName VARCHAR(100),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Department(DepartmentID)
);
CREATE TABLE Semester (
    SemesterID INT PRIMARY KEY Identity(1,1),
    SemesterName VARCHAR(100),
    StartDate DATE,
    EndDate DATE
);

CREATE TABLE Course (
    CourseID INT PRIMARY KEY Identity(1,1),
    CourseName VARCHAR(100),
    Credits INT
);
CREATE TABLE StudentCredit (
    STCID INT PRIMARY KEY Identity(1,1), -- Primary key for this table
    StudentID INT, -- Foreign key to Student
    CourseID INT, -- Foreign key to Course
    TeacherID INT, -- Foreign key to Teacher
    SemesterID INT, -- Foreign key to Semester
    CreditsEarned INT,
    FOREIGN KEY (StudentID) REFERENCES Student(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Course(CourseID),
    FOREIGN KEY (TeacherID) REFERENCES Teacher(TeacherID),
    FOREIGN KEY (SemesterID) REFERENCES Semester(SemesterID)
);

