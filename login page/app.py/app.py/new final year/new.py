import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import re
from datetime import date


# =========================================================
# FILE SETTINGS
# =========================================================

USER_FILE = "users.json"


# =========================================================
# COLORS
# =========================================================

BG = "#EEF4FF"
PRIMARY = "#4F46E5"
PRIMARY_DARK = "#3730A3"
SECONDARY = "#7C3AED"
ACCENT = "#06B6D4"

WHITE = "#FFFFFF"
TEXT = "#172554"
TEXT_LIGHT = "#64748B"
BORDER = "#D9E2F2"

SUCCESS = "#16A34A"
ERROR = "#DC2626"

DARKBAR = "#1F2937"


# =========================================================
# STATIC DATA
# =========================================================

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

CURRENT_YEAR = date.today().year

SUBJECTS = [
    ("DB", "DBMS"),
    ("DS", "DSA"),
    ("OO", "OOPs (Java)"),
    ("PY", "Python Programming"),
    ("WD", "Web Development"),
    ("ML", "Machine Learning")
]


# =========================================================
# LOAD / SAVE USERS
# =========================================================

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    try:
        with open(USER_FILE, "r") as file:
            return json.load(file)
    except Exception:
        return {}


def save_users(users):
    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


def calculate_age(day, month_name, year):
    """Calculates age from a Day / Month name / Year combination."""
    month_index = MONTHS.index(month_name) + 1
    born = date(year, month_index, day)
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


users = load_users()


# =========================================================
# MAIN APPLICATION
# =========================================================

class EduBridgeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("EduBridge - Student Portal")
        self.root.geometry("1200x750")
        self.root.resizable(False, False)
        self.root.configure(bg=BG)

        self.current_email = None
        self.current_role = None

        # register-page state
        self.selected_role = tk.StringVar(value="student")

        # study-material state
        self.active_tab = tk.StringVar(value="Subjects")

        self.show_login_page()

    # =====================================================
    # CLEAR SCREEN
    # =====================================================

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # =====================================================
    # BACKGROUND
    # =====================================================

    def create_background(self):
        canvas = tk.Canvas(self.root, width=1200, height=750, bg=BG, highlightthickness=0)
        canvas.place(x=0, y=0)

        canvas.create_oval(-180, -150, 250, 280, fill="#DDE7FF", outline="")
        canvas.create_oval(970, -120, 1320, 230, fill="#E5D9FF", outline="")
        canvas.create_oval(-150, 620, 220, 1000, fill="#DDF8FF", outline="")
        canvas.create_oval(1020, 570, 1350, 900, fill="#E8DEFF", outline="")
        canvas.create_oval(1050, 300, 1100, 350, fill="#C7D2FE", outline="")
        canvas.create_oval(120, 450, 165, 495, fill="#BAE6FD", outline="")

        return canvas

    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):
        header = tk.Frame(self.root, bg=PRIMARY, height=105)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        logo = tk.Canvas(header, width=55, height=55, bg=PRIMARY, highlightthickness=0)
        logo.place(x=35, y=25)
        logo.create_oval(3, 3, 52, 52, fill=WHITE, outline="")
        logo.create_text(27, 27, text="E", font=("Arial", 25, "bold"), fill=PRIMARY)

        tk.Label(header, text="EduBridge", font=("Arial", 28, "bold"),
                 fg=WHITE, bg=PRIMARY).place(x=105, y=20)

        tk.Label(header, text="Bridging Students to Better Learning", font=("Arial", 11),
                 fg="#E0E7FF", bg=PRIMARY).place(x=108, y=62)

        if self.current_role:
            role_text = "🧑‍🏫 Mentor" if self.current_role == "mentor" else "🎓 Student"
            tk.Label(header, text=role_text, font=("Arial", 11, "bold"),
                     fg=WHITE, bg=PRIMARY).place(x=1080, y=40)

    # =====================================================
    # LOGIN PAGE
    # =====================================================

    def show_login_page(self):
        self.clear_screen()
        self.current_email = None
        self.current_role = None

        self.create_background()
        self.create_header()

        card = tk.Frame(self.root, bg=WHITE, width=450, height=490,
                         highlightbackground=BORDER, highlightthickness=1)
        card.place(x=375, y=155)
        card.pack_propagate(False)

        tk.Label(card, text="Welcome Back! 👋", font=("Arial", 25, "bold"),
                 fg=TEXT, bg=WHITE).pack(pady=(35, 5))

        tk.Label(card, text="Login to continue to EduBridge", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=WHITE).pack(pady=(0, 30))

        tk.Label(card, text="Email Address", font=("Arial", 11, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=50)

        self.login_email = tk.Entry(card, font=("Arial", 12), width=34, relief="solid", bd=1)
        self.login_email.pack(padx=50, pady=(7, 18), ipady=8)

        tk.Label(card, text="Password", font=("Arial", 11, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=50)

        self.login_password = tk.Entry(card, font=("Arial", 12), width=34,
                                        show="*", relief="solid", bd=1)
        self.login_password.pack(padx=50, pady=(7, 10), ipady=8)

        tk.Button(card, text="LOGIN  →", font=("Arial", 12, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, activeforeground=WHITE, relief="flat",
                  cursor="hand2", width=30, command=self.login).pack(pady=20, ipady=9)

        register_frame = tk.Frame(card, bg=WHITE)
        register_frame.pack(pady=10)

        tk.Label(register_frame, text="Don't have an account?", font=("Arial", 10),
                 fg=TEXT_LIGHT, bg=WHITE).pack(side="left")

        tk.Button(register_frame, text="Create Account", font=("Arial", 10, "bold"),
                  fg=PRIMARY, bg=WHITE, bd=0, cursor="hand2",
                  command=self.show_register_page).pack(side="left", padx=5)

    # =====================================================
    # REGISTER PAGE  (Student / Mentor choice included)
    # =====================================================

    def show_register_page(self):
        self.clear_screen()
        self.selected_role.set("student")

        self.create_background()
        self.create_header()

        card = tk.Frame(self.root, bg=WHITE, width=470, height=610,
                         highlightbackground=BORDER, highlightthickness=1)
        card.place(x=365, y=100)
        card.pack_propagate(False)

        tk.Label(card, text="Create Your Account", font=("Arial", 24, "bold"),
                 fg=TEXT, bg=WHITE).pack(pady=(25, 5))

        tk.Label(card, text="Join EduBridge and start your learning journey",
                 font=("Arial", 10), fg=TEXT_LIGHT, bg=WHITE).pack(pady=(0, 15))

        # ---------------- ROLE SELECTION ----------------
        role_frame = tk.Frame(card, bg=WHITE)
        role_frame.pack(pady=(0, 15))

        self.student_role_btn = tk.Button(
            role_frame, text="🎓  Student", font=("Arial", 11, "bold"),
            width=17, relief="flat", cursor="hand2",
            command=lambda: self.select_role("student")
        )
        self.student_role_btn.grid(row=0, column=0, padx=5, ipady=8)

        self.mentor_role_btn = tk.Button(
            role_frame, text="🧑‍🏫  Mentor", font=("Arial", 11, "bold"),
            width=17, relief="flat", cursor="hand2",
            command=lambda: self.select_role("mentor")
        )
        self.mentor_role_btn.grid(row=0, column=1, padx=5, ipady=8)

        self.select_role("student")

        # ---------------- FORM FIELDS ----------------
        tk.Label(card, text="Full Name", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=45)
        self.name_entry = tk.Entry(card, width=38, font=("Arial", 11), relief="solid", bd=1)
        self.name_entry.pack(padx=45, pady=(5, 10), ipady=6)

        tk.Label(card, text="Email", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=45)
        self.email_entry = tk.Entry(card, width=38, font=("Arial", 11), relief="solid", bd=1)
        self.email_entry.pack(padx=45, pady=(5, 10), ipady=6)

        tk.Label(card, text="Password", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=45)
        self.password_entry = tk.Entry(card, width=38, font=("Arial", 11),
                                        show="*", relief="solid", bd=1)
        self.password_entry.pack(padx=45, pady=(5, 10), ipady=6)

        tk.Label(card, text="Confirm Password", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w", padx=45)
        self.confirm_password_entry = tk.Entry(card, width=38, font=("Arial", 11),
                                                 show="*", relief="solid", bd=1)
        self.confirm_password_entry.pack(padx=45, pady=(5, 10), ipady=6)

        tk.Button(card, text="CREATE ACCOUNT", font=("Arial", 11, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=30,
                  command=self.register).pack(pady=15, ipady=8)

        tk.Button(card, text="← Back to Login", font=("Arial", 10), fg=PRIMARY, bg=WHITE,
                  bd=0, cursor="hand2", command=self.show_login_page).pack()

    def select_role(self, role):
        self.selected_role.set(role)

        if role == "student":
            self.student_role_btn.config(bg=PRIMARY, fg=WHITE, activebackground=PRIMARY_DARK)
            self.mentor_role_btn.config(bg="#E5E9F5", fg=TEXT, activebackground="#DCE1F2")
        else:
            self.mentor_role_btn.config(bg=PRIMARY, fg=WHITE, activebackground=PRIMARY_DARK)
            self.student_role_btn.config(bg="#E5E9F5", fg=TEXT, activebackground="#DCE1F2")

    # =====================================================
    # REGISTER
    # =====================================================

    def register(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip().lower()
        password = self.password_entry.get()
        confirm = self.confirm_password_entry.get()
        role = self.selected_role.get()

        if not name or not email or not password or not confirm:
            messagebox.showwarning("Missing Information", "Please fill in all fields.")
            return

        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            messagebox.showerror("Invalid Email", "Please enter a valid email address.")
            return

        if len(password) < 6:
            messagebox.showerror("Weak Password", "Password must contain at least 6 characters.")
            return

        if password != confirm:
            messagebox.showerror("Password Error", "Passwords do not match.")
            return

        if email in users:
            messagebox.showerror("Account Exists", "This email is already registered.")
            return

        if role == "mentor":
            users[email] = {
                "name": name,
                "password": password,
                "role": "mentor",
                "department": "",
                "subject_expertise": ""
            }
        else:
            users[email] = {
                "name": name,
                "password": password,
                "role": "student",
                "dob": "",
                "age": "",
                "class": "",
                "university": "",
                "college": "",
                "department": "",
                "course": "",
                "semester": "",
                "progress": {
                    "study_hours": 0,
                    "videos_watched": 0,
                    "assignments_done": 0,
                    "courses_completed": 0
                }
            }

        save_users(users)

        messagebox.showinfo("Success", "Your EduBridge account has been created!")
        self.show_login_page()

    # =====================================================
    # LOGIN
    # =====================================================

    def login(self):
        email = self.login_email.get().strip().lower()
        password = self.login_password.get()

        if not email or not password:
            messagebox.showwarning("Missing Information", "Please enter email and password.")
            return

        if email not in users:
            messagebox.showerror("Login Failed", "No account found with this email.")
            return

        if users[email]["password"] != password:
            messagebox.showerror("Login Failed", "Incorrect password.")
            return

        self.current_email = email
        role = users[email].get("role", "student")
        self.current_role = role
        name = users[email]["name"]

        if role == "mentor":
            self.show_mentor_dashboard(name, email)
            return

        # student flow
        if users[email].get("university"):
            self.show_dashboard(
                name, email,
                users[email].get("university", ""),
                users[email].get("college", ""),
                users[email].get("department", ""),
                users[email].get("semester", "")
            )
        else:
            self.show_student_details(name, email)

    # =====================================================
    # ACADEMIC PROFILE (with Date of Birth -> Auto Age)
    # =====================================================

    def show_student_details(self, name, email):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text=f"Welcome, {name}! 🎓", font=("Arial", 24, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(15, 5))

        tk.Label(self.root, text="Let's create your academic profile", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 8))

        form = tk.Frame(self.root, bg=WHITE, width=900, height=560,
                         highlightbackground=BORDER, highlightthickness=1)
        form.pack()
        form.pack_propagate(False)

        # ---------------- ROW 1 : Name / Email ----------------
        row1 = tk.Frame(form, bg=WHITE)
        row1.pack(pady=(20, 5))

        self.student_name_entry = self.create_input(row1, "Name", 0)
        self.student_name_entry.insert(0, name)

        self.create_input(row1, "Email", 1, value=email, readonly=True)

        # ---------------- ROW 2 : Date of Birth / Age ----------------
        row2 = tk.Frame(form, bg=WHITE)
        row2.pack(pady=5)

        dob_frame = tk.Frame(row2, bg=WHITE, width=500, height=90)
        dob_frame.grid(row=0, column=0, padx=10, columnspan=2)
        dob_frame.pack_propagate(False)

        tk.Label(dob_frame, text="Date of Birth", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        dob_inputs = tk.Frame(dob_frame, bg=WHITE)
        dob_inputs.pack(pady=5)

        self.dob_day = ttk.Combobox(dob_inputs, values=[str(d) for d in range(1, 32)],
                                     state="readonly", width=5, font=("Arial", 10))
        self.dob_day.set("Day")
        self.dob_day.grid(row=0, column=0, padx=3, ipady=4)

        self.dob_month = ttk.Combobox(dob_inputs, values=MONTHS,
                                       state="readonly", width=11, font=("Arial", 10))
        self.dob_month.set("Month")
        self.dob_month.grid(row=0, column=1, padx=3, ipady=4)

        self.dob_year = ttk.Combobox(
            dob_inputs,
            values=[str(y) for y in range(CURRENT_YEAR - 10, CURRENT_YEAR - 60, -1)],
            state="readonly", width=7, font=("Arial", 10)
        )
        self.dob_year.set("Year")
        self.dob_year.grid(row=0, column=2, padx=3, ipady=4)

        self.dob_day.bind("<<ComboboxSelected>>", self.update_age_preview)
        self.dob_month.bind("<<ComboboxSelected>>", self.update_age_preview)
        self.dob_year.bind("<<ComboboxSelected>>", self.update_age_preview)

        age_frame = tk.Frame(row2, bg=WHITE, width=200, height=90)
        age_frame.grid(row=0, column=2, padx=10)
        age_frame.pack_propagate(False)

        tk.Label(age_frame, text="Age (auto)", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        self.age_value_label = tk.Label(age_frame, text="--", font=("Arial", 16, "bold"),
                                         fg=PRIMARY, bg=WHITE)
        self.age_value_label.pack(pady=8)

        # ---------------- ROW 3 : Class / University / College ----------------
        row3 = tk.Frame(form, bg=WHITE)
        row3.pack(pady=5)

        self.class_entry = self.create_input(row3, "Class", 0)
        self.university_entry = self.create_input(row3, "University", 1)

        college_frame = tk.Frame(row3, bg=WHITE, width=240, height=90)
        college_frame.grid(row=0, column=2, padx=10)
        college_frame.pack_propagate(False)

        tk.Label(college_frame, text="College", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        self.college_combo = ttk.Combobox(college_frame, values=["JNEC", "IICT", "Other"],
                                           state="readonly", width=22, font=("Arial", 10))
        self.college_combo.pack(pady=5, ipady=5)
        self.college_combo.set("Select College")

        # ---------------- ROW 4 : Department / Course / Semester ----------------
        row4 = tk.Frame(form, bg=WHITE)
        row4.pack(pady=5)

        department_frame = tk.Frame(row4, bg=WHITE, width=240, height=90)
        department_frame.grid(row=0, column=0, padx=10)
        department_frame.pack_propagate(False)

        tk.Label(department_frame, text="Department", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        self.department_combo = ttk.Combobox(
            department_frame,
            values=[
                "Data Science (DS)",
                "Artificial Intelligence & Machine Learning",
                "Information Technology (IT)",
                "Computer Science (CS)",
                "Computer Science & Engineering (CSE)",
                "Electronics & Telecommunication (ENTC)"
            ],
            state="readonly", width=22, font=("Arial", 9)
        )
        self.department_combo.pack(pady=5, ipady=5)
        self.department_combo.set("Select Department")

        course_frame = tk.Frame(row4, bg=WHITE, width=240, height=90)
        course_frame.grid(row=0, column=1, padx=10)
        course_frame.pack_propagate(False)

        tk.Label(course_frame, text="Course", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        self.course_combo = ttk.Combobox(
            course_frame,
            values=["B.Tech", "B.E.", "B.Sc.", "M.Tech", "MCA", "Other"],
            state="readonly", width=22, font=("Arial", 10)
        )
        self.course_combo.pack(pady=5, ipady=5)
        self.course_combo.set("Select Course")

        semester_frame = tk.Frame(row4, bg=WHITE, width=240, height=90)
        semester_frame.grid(row=0, column=2, padx=10)
        semester_frame.pack_propagate(False)

        tk.Label(semester_frame, text="Semester", font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        self.semester_combo = ttk.Combobox(
            semester_frame,
            values=[f"Semester {i}" for i in range(1, 9)],
            state="readonly", width=22, font=("Arial", 10)
        )
        self.semester_combo.pack(pady=5, ipady=5)
        self.semester_combo.set("Select Semester")

        # ---------------- BUTTONS ----------------
        tk.Button(form, text="SAVE PROFILE  →", font=("Arial", 11, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=30,
                  command=lambda: self.save_student_details(email)).pack(pady=15, ipady=8)

        tk.Button(form, text="Logout", font=("Arial", 10), fg=TEXT_LIGHT, bg=WHITE,
                  bd=0, cursor="hand2", command=self.show_login_page).pack()

    def update_age_preview(self, event=None):
        day = self.dob_day.get()
        month = self.dob_month.get()
        year = self.dob_year.get()

        if day == "Day" or month == "Month" or year == "Year":
            return

        try:
            age = calculate_age(int(day), month, int(year))
            self.age_value_label.config(text=str(age))
        except ValueError:
            self.age_value_label.config(text="--")

    # =====================================================
    # CREATE INPUT (generic helper)
    # =====================================================

    def create_input(self, parent, label, column, value="", readonly=False):
        frame = tk.Frame(parent, bg=WHITE, width=240, height=90)
        frame.grid(row=0, column=column, padx=10)
        frame.pack_propagate(False)

        tk.Label(frame, text=label, font=("Arial", 10, "bold"),
                 fg=TEXT, bg=WHITE).pack(anchor="w")

        entry = tk.Entry(frame, width=22, font=("Arial", 10), relief="solid", bd=1)
        entry.pack(pady=5, ipady=5)

        if value:
            entry.insert(0, value)

        if readonly:
            entry.config(state="readonly")

        return entry

    # =====================================================
    # SAVE PROFILE
    # =====================================================

    def save_student_details(self, email):
        name = self.student_name_entry.get().strip()
        day = self.dob_day.get()
        month = self.dob_month.get()
        year = self.dob_year.get()
        student_class = self.class_entry.get().strip()
        university = self.university_entry.get().strip()
        college = self.college_combo.get()
        department = self.department_combo.get()
        course = self.course_combo.get()
        semester = self.semester_combo.get()

        if not name:
            messagebox.showwarning("Required", "Please enter your name.")
            return

        if day == "Day" or month == "Month" or year == "Year":
            messagebox.showwarning("Required", "Please select your complete date of birth.")
            return

        try:
            age = calculate_age(int(day), month, int(year))
        except ValueError:
            messagebox.showerror("Invalid Date", "Please select a valid date of birth.")
            return

        if age < 0:
            messagebox.showerror("Invalid Date", "Please select a valid date of birth.")
            return

        if not student_class:
            messagebox.showwarning("Required", "Please enter your class.")
            return

        if not university:
            messagebox.showwarning("Required", "Please enter your university.")
            return

        if college == "Select College":
            messagebox.showwarning("Required", "Please select your college.")
            return

        if department == "Select Department":
            messagebox.showwarning("Required", "Please select your department.")
            return

        if course == "Select Course":
            messagebox.showwarning("Required", "Please select your course.")
            return

        if semester == "Select Semester":
            messagebox.showwarning("Required", "Please select your semester.")
            return

        dob_str = f"{int(day):02d}-{month}-{year}"

        users[email]["name"] = name
        users[email]["dob"] = dob_str
        users[email]["age"] = age
        users[email]["class"] = student_class
        users[email]["university"] = university
        users[email]["college"] = college
        users[email]["department"] = department
        users[email]["course"] = course
        users[email]["semester"] = semester

        save_users(users)

        messagebox.showinfo("Profile Saved", "Academic profile saved successfully!")

        self.show_dashboard(name, email, university, college, department, semester)

    # =====================================================
    # MAIN DASHBOARD (Student)
    # =====================================================

    def show_dashboard(self, name, email, university, college, department, semester):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text=f"Welcome to EduBridge, {name}! 🎓", font=("Arial", 26, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(35, 5))

        tk.Label(self.root, text="Your personalized student dashboard", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 20))

        cards_frame = tk.Frame(self.root, bg=BG)
        cards_frame.pack()

        dashboard_items = [
            ("📚", "Courses", "View your courses", lambda: self.show_courses()),
            ("📖", "Study Material", "PDF • Videos • Notes", lambda: self.show_study_material()),
            ("📝", "Assignments", "Manage assignments", lambda: self.show_assignments()),
            ("🤖", "AI Assistant", "Ask your questions", lambda: self.show_ai_assistant()),
            ("📊", "Progress", "Track your progress", lambda: self.show_progress()),
            ("👤", "Profile", "View your profile", lambda: self.show_profile())
        ]

        for i, item in enumerate(dashboard_items):
            icon, title, subtitle, command = item

            card = tk.Frame(cards_frame, bg=WHITE, width=260, height=130,
                             highlightbackground=BORDER, highlightthickness=1, cursor="hand2")
            card.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            card.pack_propagate(False)

            icon_label = tk.Label(card, text=icon, font=("Arial", 25), bg=WHITE, cursor="hand2")
            icon_label.pack(pady=(15, 3))

            title_label = tk.Label(card, text=title, font=("Arial", 13, "bold"),
                                    fg=TEXT, bg=WHITE, cursor="hand2")
            title_label.pack()

            subtitle_label = tk.Label(card, text=subtitle, font=("Arial", 9),
                                       fg=TEXT_LIGHT, bg=WHITE, cursor="hand2")
            subtitle_label.pack(pady=3)

            for widget in (card, icon_label, title_label, subtitle_label):
                widget.bind("<Button-1>", lambda event, c=command: c())

        tk.Button(self.root, text="LOGOUT", font=("Arial", 11, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=25,
                  command=self.show_login_page).pack(pady=25, ipady=8)

    # =====================================================
    # MENTOR DASHBOARD
    # =====================================================

    def show_mentor_dashboard(self, name, email):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text=f"Welcome, Mentor {name}! 🧑‍🏫", font=("Arial", 26, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(35, 5))

        tk.Label(self.root, text="Manage your students and study material", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 20))

        cards_frame = tk.Frame(self.root, bg=BG)
        cards_frame.pack()

        mentor_items = [
            ("👥", "My Students", "View registered students", self.mentor_view_students),
            ("📖", "Study Material", "Manage subject material", self.show_study_material),
            ("📢", "Announcements", "Post an announcement", self.mentor_post_announcement),
            ("📝", "Test Series", "Manage tests", self.mentor_manage_tests)
        ]

        for i, item in enumerate(mentor_items):
            icon, title, subtitle, command = item

            card = tk.Frame(cards_frame, bg=WHITE, width=260, height=130,
                             highlightbackground=BORDER, highlightthickness=1, cursor="hand2")
            card.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            card.pack_propagate(False)

            icon_label = tk.Label(card, text=icon, font=("Arial", 25), bg=WHITE, cursor="hand2")
            icon_label.pack(pady=(15, 3))

            title_label = tk.Label(card, text=title, font=("Arial", 13, "bold"),
                                    fg=TEXT, bg=WHITE, cursor="hand2")
            title_label.pack()

            subtitle_label = tk.Label(card, text=subtitle, font=("Arial", 9),
                                       fg=TEXT_LIGHT, bg=WHITE, cursor="hand2")
            subtitle_label.pack(pady=3)

            for widget in (card, icon_label, title_label, subtitle_label):
                widget.bind("<Button-1>", lambda event, c=command: c())

        tk.Button(self.root, text="LOGOUT", font=("Arial", 11, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=25,
                  command=self.show_login_page).pack(pady=25, ipady=8)

    def mentor_view_students(self):
        students = [u for u in users.values() if u.get("role") == "student"]

        if not students:
            messagebox.showinfo("My Students", "No students have registered yet.")
            return

        listing = "\n".join(
            f"• {s.get('name', 'Unknown')} - {s.get('course', 'N/A')} "
            f"({s.get('semester', 'N/A')})"
            for s in students
        )
        messagebox.showinfo("My Students", listing)

    def mentor_post_announcement(self):
        messagebox.showinfo(
            "Post Announcement",
            "Announcement posting can be connected here.\n\n"
            "(Add a text box + save-to-file logic for a full implementation.)"
        )

    def mentor_manage_tests(self):
        messagebox.showinfo(
            "Test Series",
            "Test creation and management can be connected here."
        )

    # =====================================================
    # COURSES
    # =====================================================

    def show_courses(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text="📚 Courses", font=("Arial", 27, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(25, 5))

        tk.Label(self.root, text="Select a course to start learning", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 20))

        courses = [
            ("📊", "Data Analysis"), ("🗄️", "DBMS"), ("🐍", "Python Programming"),
            ("🤖", "Machine Learning"), ("🧠", "Artificial Intelligence"), ("📈", "Statistics")
        ]

        frame = tk.Frame(self.root, bg=BG)
        frame.pack()

        for i, (icon, course) in enumerate(courses):
            card = tk.Frame(frame, bg=WHITE, width=300, height=110,
                             highlightbackground=BORDER, highlightthickness=1)
            card.grid(row=i // 2, column=i % 2, padx=10, pady=8)
            card.pack_propagate(False)

            tk.Label(card, text=icon, font=("Arial", 24), bg=WHITE).pack(pady=(10, 2))

            tk.Button(card, text=course, font=("Arial", 12, "bold"), fg=TEXT, bg=WHITE,
                      bd=0, cursor="hand2", command=lambda c=course: self.open_course(c)).pack()

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack(pady=15)

    def open_course(self, course):
        messagebox.showinfo(
            course,
            f"You selected:\n\n{course}\n\n"
            "Course learning section can be connected here "
            "with lectures, videos, PDFs and quizzes."
        )

    # =====================================================
    # STUDY MATERIAL  (PW-style Subjects / Resources / Tests / Announcements)
    # =====================================================

    def show_study_material(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        # ---------------- TOP BANNER ----------------
        banner = tk.Frame(self.root, bg=PRIMARY, width=1200, height=110)
        banner.pack(fill="x")
        banner.pack_propagate(False)

        tk.Label(banner, text="DBMS, DSA & Full Stack — Free Batch 2027",
                 font=("Arial", 22, "bold"), fg=WHITE, bg=PRIMARY).place(x=40, y=35)

        # ---------------- TAB BAR ----------------
        tab_bar = tk.Frame(self.root, bg=WHITE, width=1200, height=45)
        tab_bar.pack(fill="x")
        tab_bar.pack_propagate(False)

        self.tab_buttons = {}
        tab_names = ["Description", "Subjects", "Resources", "Tests", "Announcements"]

        tabs_holder = tk.Frame(tab_bar, bg=WHITE)
        tabs_holder.pack(side="left", padx=25, pady=8)

        for tab in tab_names:
            btn = tk.Button(
                tabs_holder, text=tab, font=("Arial", 11, "bold"), bd=0, bg=WHITE,
                fg=(PRIMARY if tab == self.active_tab.get() else TEXT_LIGHT),
                activebackground=WHITE, cursor="hand2",
                command=lambda t=tab: self.select_material_tab(t)
            )
            btn.pack(side="left", padx=15)
            self.tab_buttons[tab] = btn

        # underline for active tab
        tk.Frame(tab_bar, bg=BORDER, height=1).pack(fill="x", side="bottom")

        # ---------------- INFO STRIP ----------------
        self.info_strip = tk.Frame(self.root, bg=DARKBAR, width=1200, height=38)
        self.info_strip.pack(fill="x")
        self.info_strip.pack_propagate(False)

        tk.Label(self.info_strip, text="Completion % depends on lecture and DPP progress!",
                 font=("Arial", 10), fg=WHITE, bg=DARKBAR).place(x=25, y=9)

        tk.Button(self.info_strip, text="✕", font=("Arial", 10, "bold"), fg=WHITE, bg=DARKBAR,
                  bd=0, cursor="hand2",
                  command=self.info_strip.pack_forget).place(x=1150, y=7)

        # ---------------- CONTENT AREA ----------------
        self.material_content = tk.Frame(self.root, bg=BG, width=1200, height=430)
        self.material_content.pack(fill="both", expand=True)

        self.render_material_tab()

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack(pady=8)

    def select_material_tab(self, tab):
        self.active_tab.set(tab)
        for name, btn in self.tab_buttons.items():
            btn.config(fg=(PRIMARY if name == tab else TEXT_LIGHT))
        self.render_material_tab()

    def render_material_tab(self):
        for widget in self.material_content.winfo_children():
            widget.destroy()

        tab = self.active_tab.get()

        if tab == "Description":
            self.render_description_tab()
        elif tab == "Subjects":
            self.render_subjects_tab()
        elif tab == "Resources":
            self.render_resources_tab()
        elif tab == "Tests":
            self.render_tests_tab()
        elif tab == "Announcements":
            self.render_announcements_tab()

    def render_description_tab(self):
        tk.Label(
            self.material_content,
            text="This batch covers core Computer Science subjects — Database\n"
                 "Management Systems, Data Structures & Algorithms, Object-Oriented\n"
                 "Programming, Python, Web Development and Machine Learning — with\n"
                 "structured lectures, notes, DPPs and tests for every subject.",
            font=("Arial", 12), fg=TEXT, bg=BG, justify="left"
        ).pack(padx=40, pady=30, anchor="w")

    def render_subjects_tab(self):
        grid = tk.Frame(self.material_content, bg=BG)
        grid.pack(pady=25)

        for i, (abbr, subject) in enumerate(SUBJECTS):
            card = tk.Frame(grid, bg=WHITE, width=360, height=90,
                             highlightbackground=BORDER, highlightthickness=1, cursor="hand2")
            card.grid(row=i // 3, column=i % 3, padx=10, pady=10)
            card.pack_propagate(False)

            badge = tk.Label(card, text=abbr, font=("Arial", 11, "bold"), fg=PRIMARY,
                              bg="#E7E9FD", width=3, height=1)
            badge.place(x=18, y=28)

            name_label = tk.Label(card, text=subject, font=("Arial", 13, "bold"),
                                   fg=TEXT, bg=WHITE)
            name_label.place(x=75, y=15)

            pct_label = tk.Label(card, text="0 %", font=("Arial", 10), fg=TEXT_LIGHT, bg=WHITE)
            pct_label.place(x=290, y=15)

            bar = ttk.Progressbar(card, length=230, maximum=100, value=0)
            bar.place(x=75, y=48)

            arrow_label = tk.Label(card, text="›", font=("Arial", 16, "bold"),
                                    fg=TEXT_LIGHT, bg=WHITE)
            arrow_label.place(x=330, y=32)

            for widget in (card, badge, name_label, pct_label, arrow_label):
                widget.bind("<Button-1>", lambda e, s=subject: self.open_subject(s))

    def render_resources_tab(self):
        resources = ["📄 Lecture Notes (PDF)", "📊 Formula Sheets", "🗂️ Reference Books", "🔗 Useful Links"]

        for r in resources:
            row = tk.Frame(self.material_content, bg=WHITE, width=500, height=50,
                            highlightbackground=BORDER, highlightthickness=1)
            row.pack(pady=6)
            row.pack_propagate(False)

            tk.Label(row, text=r, font=("Arial", 11), fg=TEXT, bg=WHITE).pack(
                side="left", padx=15, pady=12)

    def render_tests_tab(self):
        tests = ["DBMS Unit Test 1", "DSA Practice Test", "Python Basics Quiz", "Full Syllabus Mock Test"]

        for t in tests:
            row = tk.Frame(self.material_content, bg=WHITE, width=500, height=50,
                            highlightbackground=BORDER, highlightthickness=1)
            row.pack(pady=6)
            row.pack_propagate(False)

            tk.Label(row, text=t, font=("Arial", 11), fg=TEXT, bg=WHITE).pack(
                side="left", padx=15, pady=12)

            tk.Button(row, text="Start", font=("Arial", 9, "bold"), fg=WHITE, bg=PRIMARY,
                      relief="flat", cursor="hand2",
                      command=lambda name=t: messagebox.showinfo(
                          name, f"{name} can be connected here.")).pack(side="right", padx=15)

    def render_announcements_tab(self):
        announcements = [
            "📢 New DBMS lecture added this week.",
            "📢 DSA test scheduled for next Monday.",
            "📢 Machine Learning module launching soon."
        ]

        for a in announcements:
            tk.Label(self.material_content, text=a, font=("Arial", 11), fg=TEXT, bg=BG,
                     anchor="w").pack(fill="x", padx=60, pady=8)

    def open_subject(self, subject):
        material_var = tk.StringVar()

        popup = tk.Toplevel(self.root)
        popup.title(subject)
        popup.geometry("380x220")
        popup.configure(bg=WHITE)
        popup.resizable(False, False)

        tk.Label(popup, text=subject, font=("Arial", 15, "bold"),
                 fg=TEXT, bg=WHITE).pack(pady=(20, 10))

        material_combo = ttk.Combobox(popup, textvariable=material_var,
                                       values=["📄 PDF", "🎥 Videos", "📝 Notes"],
                                       state="readonly", width=25, font=("Arial", 11))
        material_combo.pack(ipady=6)
        material_combo.set("Select Study Material")

        def open_selected():
            material = material_var.get()

            if material == "Select Study Material":
                messagebox.showwarning("Select Material", "Please select PDF, Videos or Notes.")
                return

            messagebox.showinfo(
                f"{subject} - {material}",
                f"{material} section for {subject} opened.\n\n"
                "You can connect real files/links here."
            )
            popup.destroy()

        tk.Button(popup, text="OPEN MATERIAL  →", font=("Arial", 11, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=22,
                  command=open_selected).pack(pady=20, ipady=6)

    # =====================================================
    # ASSIGNMENTS
    # =====================================================

    def show_assignments(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text="📝 Assignments", font=("Arial", 27, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(30, 5))

        tk.Label(self.root, text="Manage your assignments", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 20))

        assignments = [
            "Data Analysis Assignment", "DBMS SQL Assignment",
            "Python Programming Assignment", "Machine Learning Assignment"
        ]

        frame = tk.Frame(self.root, bg=WHITE, width=650, height=300,
                          highlightbackground=BORDER, highlightthickness=1)
        frame.pack()
        frame.pack_propagate(False)

        for assignment in assignments:
            var = tk.BooleanVar()
            tk.Checkbutton(frame, text=assignment, variable=var, font=("Arial", 11), fg=TEXT,
                           bg=WHITE, activebackground=WHITE, selectcolor=WHITE,
                           anchor="w", width=45).pack(pady=12)

        tk.Button(frame, text="SAVE ASSIGNMENT PROGRESS", font=("Arial", 10, "bold"), fg=WHITE,
                  bg=PRIMARY, relief="flat", cursor="hand2",
                  command=self.assignment_completed).pack(pady=10, ipady=7)

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack(pady=15)

    def assignment_completed(self):
        progress = users[self.current_email].setdefault("progress", {})
        progress["assignments_done"] = progress.get("assignments_done", 0) + 1
        save_users(users)
        messagebox.showinfo("Progress Updated", "Assignment progress updated successfully!")

    # =====================================================
    # AI ASSISTANT
    # =====================================================

    def show_ai_assistant(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        tk.Label(self.root, text="🤖 EduBridge AI Assistant", font=("Arial", 27, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(20, 5))

        tk.Label(self.root, text="Ask questions related to your studies", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 15))

        chat_frame = tk.Frame(self.root, bg=WHITE, width=800, height=430,
                               highlightbackground=BORDER, highlightthickness=1)
        chat_frame.pack()
        chat_frame.pack_propagate(False)

        self.chat_box = tk.Text(chat_frame, font=("Arial", 11), bg=WHITE, fg=TEXT,
                                 wrap="word", state="disabled")
        self.chat_box.pack(fill="both", expand=True, padx=10, pady=10)

        self.add_chat_message(
            "EduBridge AI",
            "Hello! 👋 I am your EduBridge AI Assistant.\n\n"
            "You can ask me questions about DBMS, Python, "
            "Data Analysis, Machine Learning, Statistics and more."
        )

        input_frame = tk.Frame(self.root, bg=BG)
        input_frame.pack(pady=10)

        self.question_entry = tk.Entry(input_frame, font=("Arial", 11), width=65,
                                        relief="solid", bd=1)
        self.question_entry.grid(row=0, column=0, ipady=8, padx=5)

        tk.Button(input_frame, text="ASK", font=("Arial", 10, "bold"), fg=WHITE, bg=PRIMARY,
                  activebackground=PRIMARY_DARK, relief="flat", cursor="hand2", width=10,
                  command=self.ask_ai).grid(row=0, column=1, ipady=7)

        self.question_entry.bind("<Return>", lambda event: self.ask_ai())

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack()

    def add_chat_message(self, sender, message):
        self.chat_box.config(state="normal")
        self.chat_box.insert("end", f"{sender}:\n{message}\n\n")
        self.chat_box.config(state="disabled")
        self.chat_box.see("end")

    def ask_ai(self):
        question = self.question_entry.get().strip()
        if not question:
            return

        self.add_chat_message("You", question)
        self.question_entry.delete(0, "end")

        answer = self.generate_ai_answer(question)
        self.add_chat_message("EduBridge AI", answer)

    def generate_ai_answer(self, question):
        q = question.lower()

        if "dbms" in q:
            return ("DBMS stands for Database Management System. "
                    "It is software used to create, store, manage "
                    "and retrieve data from databases.\n\n"
                    "Examples include MySQL, Oracle and PostgreSQL.")

        if "dsa" in q or "data structure" in q:
            return ("DSA (Data Structures & Algorithms) deals with organizing data "
                    "efficiently (arrays, linked lists, trees, graphs) and writing "
                    "efficient step-by-step procedures to solve problems.")

        if "data analysis" in q:
            return ("Data Analysis is the process of inspecting, cleaning, "
                    "transforming and interpreting data to find useful information.\n\n"
                    "Common tools include Python, Pandas, NumPy, Matplotlib and Excel.")

        if "python" in q:
            return ("Python is a high-level programming language widely used in "
                    "Data Science, AI and Machine Learning.\n\n"
                    "Important concepts include variables, loops, functions, "
                    "lists, dictionaries and classes.")

        if "machine learning" in q or "ml" in q:
            return ("Machine Learning is a branch of Artificial Intelligence "
                    "where computers learn patterns from data and use those "
                    "patterns to make predictions.")

        if "artificial intelligence" in q or q == "ai":
            return ("Artificial Intelligence is the field of computer science "
                    "concerned with creating systems capable of performing tasks "
                    "that normally require human intelligence.")

        if "statistics" in q:
            return ("Statistics is the science of collecting, organizing, "
                    "analyzing and interpreting data.\n\n"
                    "Important concepts include mean, median, mode, variance, "
                    "standard deviation and probability.")

        if "mean" in q:
            return ("Mean is the arithmetic average of a set of values.\n\n"
                    "Formula:\nMean = Sum of all observations / Number of observations.")

        if "sql" in q:
            return ("SQL stands for Structured Query Language. It is used to "
                    "communicate with relational databases.\n\n"
                    "Common commands include SELECT, INSERT, UPDATE, DELETE, "
                    "CREATE and ALTER.")

        if "hello" in q or "hi" in q:
            return "Hello! 👋 How can I help you with your studies today?"

        if "thank" in q:
            return "You're welcome! 😊 Keep learning and keep improving!"

        return ("That's an interesting question! 📚\n\n"
                "I can currently help with topics such as DBMS, DSA, SQL, "
                "Data Analysis, Python, Machine Learning, Artificial Intelligence "
                "and Statistics.\n\nTry asking a question related to one of these topics.")

    # =====================================================
    # PROGRESS
    # =====================================================

    def show_progress(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        email = self.current_email
        progress = users[email].get("progress", {})

        study_hours = progress.get("study_hours", 0)
        videos = progress.get("videos_watched", 0)
        assignments = progress.get("assignments_done", 0)
        courses = progress.get("courses_completed", 0)

        total_score = min(study_hours, 10) + min(videos, 10) + min(assignments, 10) + min(courses, 5)
        percentage = int((total_score / 35) * 100)
        percentage = min(percentage, 100)

        tk.Label(self.root, text="📊 My Progress", font=("Arial", 27, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(25, 5))

        tk.Label(self.root, text="Track your learning performance", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 15))

        tk.Label(self.root, text=f"{percentage}% Overall Progress", font=("Arial", 22, "bold"),
                 fg=PRIMARY, bg=BG).pack(pady=5)

        progress_bar = ttk.Progressbar(self.root, length=650, maximum=100, value=percentage)
        progress_bar.pack(pady=10)

        stats_frame = tk.Frame(self.root, bg=BG)
        stats_frame.pack(pady=15)

        statistics = [
            ("⏱️", "Study Hours", study_hours),
            ("🎥", "Videos Watched", videos),
            ("📝", "Assignments Done", assignments),
            ("🎓", "Courses Completed", courses)
        ]

        for i, (icon, title, value) in enumerate(statistics):
            card = tk.Frame(stats_frame, bg=WHITE, width=200, height=130,
                             highlightbackground=BORDER, highlightthickness=1)
            card.grid(row=0, column=i, padx=6)
            card.pack_propagate(False)

            tk.Label(card, text=icon, font=("Arial", 23), bg=WHITE).pack(pady=(15, 3))
            tk.Label(card, text=str(value), font=("Arial", 20, "bold"),
                     fg=PRIMARY, bg=WHITE).pack()
            tk.Label(card, text=title, font=("Arial", 9), fg=TEXT_LIGHT, bg=WHITE).pack()

        tk.Button(self.root, text="➕ Add Study Hour", font=("Arial", 10, "bold"), fg=WHITE,
                  bg=PRIMARY, relief="flat", cursor="hand2",
                  command=self.add_study_hour).pack(pady=5, ipady=6)

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack(pady=10)

    def add_study_hour(self):
        progress = users[self.current_email].setdefault("progress", {})
        progress["study_hours"] = progress.get("study_hours", 0) + 1
        save_users(users)
        messagebox.showinfo("Progress Updated", "1 study hour added successfully!")
        self.show_progress()

    # =====================================================
    # PROFILE
    # =====================================================

    def show_profile(self):
        self.clear_screen()
        self.create_background()
        self.create_header()

        user = users[self.current_email]

        tk.Label(self.root, text="👤 Student Profile", font=("Arial", 27, "bold"),
                 fg=TEXT, bg=BG).pack(pady=(20, 5))

        tk.Label(self.root, text="Complete EduBridge student information", font=("Arial", 11),
                 fg=TEXT_LIGHT, bg=BG).pack(pady=(0, 15))

        profile = tk.Frame(self.root, bg=WHITE, width=800, height=480,
                            highlightbackground=BORDER, highlightthickness=1)
        profile.pack()
        profile.pack_propagate(False)

        details = [
            ("👤 Name", user.get("name", "")),
            ("📧 Email", self.current_email),
            ("🎂 Date of Birth", user.get("dob", "")),
            ("🔢 Age", str(user.get("age", ""))),
            ("🏫 Class", user.get("class", "")),
            ("🏛️ University", user.get("university", "")),
            ("🏢 College", user.get("college", "")),
            ("💻 Department", user.get("department", "")),
            ("🎓 Course", user.get("course", "")),
            ("📚 Semester", user.get("semester", ""))
        ]

        for label, value in details:
            row = tk.Frame(profile, bg=WHITE)
            row.pack(pady=5)

            tk.Label(row, text=label, font=("Arial", 10, "bold"), fg=PRIMARY, bg=WHITE,
                     width=22, anchor="e").pack(side="left")

            tk.Label(row, text=value if value else "Not provided", font=("Arial", 10),
                     fg=TEXT, bg=WHITE, width=45, anchor="w").pack(side="left", padx=15)

        tk.Button(self.root, text="← Back to Dashboard", font=("Arial", 10, "bold"), fg=PRIMARY,
                  bg=BG, bd=0, cursor="hand2", command=self.back_to_dashboard).pack(pady=15)

    # =====================================================
    # BACK TO DASHBOARD
    # =====================================================

    def back_to_dashboard(self):
        user = users[self.current_email]

        if self.current_role == "mentor":
            self.show_mentor_dashboard(user.get("name", ""), self.current_email)
            return

        self.show_dashboard(
            user.get("name", ""), self.current_email,
            user.get("university", ""), user.get("college", ""),
            user.get("department", ""), user.get("semester", "")
        )


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = EduBridgeApp(root)
    root.mainloop()