# student-management-system
The Student Management System is a Python-based application developed using Visual Studio Code that helps manage and organize student-related data in a simple, efficient, and user-friendly way. This project is designed to automate basic academic record-keeping tasks that are commonly performed manually in schools and colleges.
# 🎓 Student Management System (Python)

A **menu-driven Student Management System** built using **Python** and developed in **Visual Studio Code**. This project helps manage student records efficiently using file handling and includes **voice feedback** for better user interaction.

---

## 📌 Project Overview

The Student Management System is a console-based Python application designed to perform basic academic record management tasks. It allows users to add, view, search, and delete student records. All data is stored permanently in a text file, ensuring simplicity and ease of use without the need for an external database.

To enhance user experience, the system integrates **text-to-speech functionality** using the `pyttsx3` library, which provides voice responses for major actions such as adding, viewing, or deleting records.

This project is ideal for **beginners and intermediate learners** who want to understand real-world use of Python concepts like file handling, functions, loops, and conditional statements.

---

## ✨ Features

* ➕ Add new student records (Name, Roll No, Course, Marks)
* 📄 View all stored student records
* 🔍 Search student details by name
* ❌ Delete student records
* 💾 Permanent data storage using text files
* 🔊 Voice feedback using text-to-speech
* 🧭 Simple and user-friendly menu-driven interface

---

## 🛠️ Technologies Used

* **Python 3**
* **Visual Studio Code**
* **Libraries:**

  * `pyttsx3` – for text-to-speech
  * `os` – for file existence checks
  * `time` – for voice delay handling

---

## 📂 Project Structure

```
Student-Management-System/
│
├── stu.py              # Main Python file
├── STUDENT.TXT         # Data storage file (auto-created)
├── requirement.txt     # Required libraries
└── README.md           # Project documentation
```

---

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/student-management-system.git
   ```

2. Navigate to the project folder:

   ```bash
   cd student-management-system
   ```

3. Install required library:

   ```bash
   pip install pyttsx3
   ```

4. Run the program:

   ```bash
   python stu.py
   ```

---

## 🚀 Future Enhancements

* Add update/edit student feature
* Implement login authentication
* Use database (SQLite/MySQL) instead of text file
* Create a GUI using Tkinter or PyQt
* Improve search using roll number or course

---

## 📚 Learning Outcomes

* Understanding file handling in Python
* Working with functions and loops
* Implementing menu-driven programs
* Using external libraries for real-world features
* Building confidence in Python project development

---

## 👨‍💻 Author

**Divyansh Mishra**
B.Com (Hons) | Python Learner | Aspiring Data Analyst

---

⭐ If you find this project useful, don’t forget to **star the repository**!
