use project;

DROP TABLE IF EXISTS student;

CREATE TABLE admin (
    Admin_id INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    Email VARCHAR(100)
);

create table Student(
Std_Id int auto_increment primary key,
Name varchar(70),
Department varchar(50),
Intake varchar(40),
Address varchar(90),
Email varchar(40),
Roll_No int,
Phone_No int,
Admin_id int,
FOREIGN KEY (admin_id) REFERENCES admin(admin_id)
);

ALTER TABLE Student
DROP COLUMN Admin_id;

ALTER TABLE Student DROP FOREIGN KEY Admin_id;

ALTER TABLE Student
DROP FOREIGN KEY Admin_id;


ALTER TABLE Student 
ADD COLUMN `Date` VARCHAR(50), 
ADD COLUMN `Time` VARCHAR(50);

alter table Student drop column Admin_id;

ALTER TABLE Student DROP FOREIGN KEY student_ibfk_1;
ALTER TABLE Student DROP COLUMN Admin_id;


ALTER TABLE Student
DROP COLUMN `Date`,
DROP COLUMN `Time`;

SELECT * FROM Student;

SELECT * FROM admin;

SELECT * FROM admin WHERE Admin_id = 1;

insert into admin values(1,"Akib","akib@gmail.com");

insert into admin values(4,"Hasn","haan@gmail.com");

INSERT INTO admin (Admin_id, Name, Email) VALUES (1, "Akib", "akib@gmail.com");

DELETE FROM Student WHERE std_Id = '2';