import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import re


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


# =========================================================
# LOAD USERS
# =========================================================

def load_users():

    if not os.path.exists(USER_FILE):
        return {}

    try:

        with open(USER_FILE, "r") as file:
            return json.load(file)

    except:

        return {}


# =========================================================
# SAVE USERS
# =========================================================

def save_users(users):

    with open(USER_FILE, "w") as file:
        json.dump(users, file, indent=4)


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

        self.show_login_page()


    # =====================================================
    # CLEAR SCREEN
    # =====================================================

    def clear_screen(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # =====================================================
    # BACKGROUND DESIGN
    # =====================================================

    def create_background(self):

        canvas = tk.Canvas(
            self.root,
            width=1200,
            height=750,
            bg=BG,
            highlightthickness=0
        )

        canvas.place(
            x=0,
            y=0
        )

        # Large circles

        canvas.create_oval(
            -180,
            -150,
            250,
            280,
            fill="#DDE7FF",
            outline=""
        )

        canvas.create_oval(
            970,
            -120,
            1320,
            230,
            fill="#E5D9FF",
            outline=""
        )

        canvas.create_oval(
            -150,
            620,
            220,
            1000,
            fill="#DDF8FF",
            outline=""
        )

        canvas.create_oval(
            1020,
            570,
            1350,
            900,
            fill="#E8DEFF",
            outline=""
        )

        # Small circles

        canvas.create_oval(
            1050,
            300,
            1100,
            350,
            fill="#C7D2FE",
            outline=""
        )

        canvas.create_oval(
            120,
            450,
            165,
            495,
            fill="#BAE6FD",
            outline=""
        )

        return canvas


    # =====================================================
    # HEADER
    # =====================================================

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg=PRIMARY,
            height=105
        )

        header.pack(
            fill="x",
            side="top"
        )

        header.pack_propagate(False)


        # Logo

        logo = tk.Canvas(
            header,
            width=55,
            height=55,
            bg=PRIMARY,
            highlightthickness=0
        )

        logo.place(
            x=35,
            y=25
        )

        logo.create_oval(
            3,
            3,
            52,
            52,
            fill=WHITE,
            outline=""
        )

        logo.create_text(
            27,
            27,
            text="E",
            font=("Arial", 25, "bold"),
            fill=PRIMARY
        )


        # EduBridge

        tk.Label(
            header,
            text="EduBridge",
            font=("Arial", 28, "bold"),
            fg=WHITE,
            bg=PRIMARY
        ).place(
            x=105,
            y=20
        )


        tk.Label(
            header,
            text="Bridging Students to Better Learning",
            font=("Arial", 11),
            fg="#E0E7FF",
            bg=PRIMARY
        ).place(
            x=108,
            y=62
        )


    # =====================================================
    # LOGIN PAGE
    # =====================================================

    def show_login_page(self):

        self.clear_screen()

        self.create_background()

        self.create_header()


        # Login Card

        card = tk.Frame(
            self.root,
            bg=WHITE,
            width=450,
            height=490,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.place(
            x=375,
            y=155
        )

        card.pack_propagate(False)


        # Heading

        tk.Label(
            card,
            text="Welcome Back! 👋",
            font=("Arial", 25, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            pady=(35, 5)
        )


        tk.Label(
            card,
            text="Login to continue to EduBridge",
            font=("Arial", 11),
            fg=TEXT_LIGHT,
            bg=WHITE
        ).pack(
            pady=(0, 30)
        )


        # Email

        tk.Label(
            card,
            text="Email Address",
            font=("Arial", 11, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=50
        )


        self.login_email = tk.Entry(
            card,
            font=("Arial", 12),
            width=34,
            relief="solid",
            bd=1
        )

        self.login_email.pack(
            padx=50,
            pady=(7, 18),
            ipady=8
        )


        # Password

        tk.Label(
            card,
            text="Password",
            font=("Arial", 11, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=50
        )


        self.login_password = tk.Entry(
            card,
            font=("Arial", 12),
            width=34,
            show="*",
            relief="solid",
            bd=1
        )

        self.login_password.pack(
            padx=50,
            pady=(7, 10),
            ipady=8
        )


        # Login Button

        tk.Button(
            card,
            text="LOGIN  →",
            font=("Arial", 12, "bold"),
            fg=WHITE,
            bg=PRIMARY,
            activebackground=PRIMARY_DARK,
            activeforeground=WHITE,
            relief="flat",
            cursor="hand2",
            width=30,
            command=self.login
        ).pack(
            pady=20,
            ipady=9
        )


        # Register

        register_frame = tk.Frame(
            card,
            bg=WHITE
        )

        register_frame.pack(
            pady=10
        )


        tk.Label(
            register_frame,
            text="Don't have an account?",
            font=("Arial", 10),
            fg=TEXT_LIGHT,
            bg=WHITE
        ).pack(
            side="left"
        )


        tk.Button(
            register_frame,
            text="Create Account",
            font=("Arial", 10, "bold"),
            fg=PRIMARY,
            bg=WHITE,
            bd=0,
            cursor="hand2",
            command=self.show_register_page
        ).pack(
            side="left",
            padx=5
        )


    # =====================================================
    # REGISTRATION PAGE
    # =====================================================

    def show_register_page(self):

        self.clear_screen()

        self.create_background()

        self.create_header()


        card = tk.Frame(
            self.root,
            bg=WHITE,
            width=470,
            height=550,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        card.place(
            x=365,
            y=130
        )

        card.pack_propagate(False)


        # Heading

        tk.Label(
            card,
            text="Create Your Account",
            font=("Arial", 24, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            pady=(25, 5)
        )


        tk.Label(
            card,
            text="Join EduBridge and start your learning journey",
            font=("Arial", 10),
            fg=TEXT_LIGHT,
            bg=WHITE
        ).pack(
            pady=(0, 20)
        )


        # Name

        tk.Label(
            card,
            text="Full Name",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=45
        )


        self.name_entry = tk.Entry(
            card,
            width=38,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.name_entry.pack(
            padx=45,
            pady=(5, 10),
            ipady=6
        )


        # Email

        tk.Label(
            card,
            text="Email",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=45
        )


        self.email_entry = tk.Entry(
            card,
            width=38,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        self.email_entry.pack(
            padx=45,
            pady=(5, 10),
            ipady=6
        )


        # Password

        tk.Label(
            card,
            text="Password",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=45
        )


        self.password_entry = tk.Entry(
            card,
            width=38,
            font=("Arial", 11),
            show="*",
            relief="solid",
            bd=1
        )

        self.password_entry.pack(
            padx=45,
            pady=(5, 10),
            ipady=6
        )


        # Confirm Password

        tk.Label(
            card,
            text="Confirm Password",
            font=("Arial", 10, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            anchor="w",
            padx=45
        )


        self.confirm_password_entry = tk.Entry(
            card,
            width=38,
            font=("Arial", 11),
            show="*",
            relief="solid",
            bd=1
        )

        self.confirm_password_entry.pack(
            padx=45,
            pady=(5, 10),
            ipady=6
        )


        # Register Button

        tk.Button(
            card,
            text="CREATE ACCOUNT",
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PRIMARY,
            activebackground=PRIMARY_DARK,
            relief="flat",
            cursor="hand2",
            width=30,
            command=self.register
        ).pack(
            pady=15,
            ipady=8
        )


        # Back

        tk.Button(
            card,
            text="← Back to Login",
            font=("Arial", 10),
            fg=PRIMARY,
            bg=WHITE,
            bd=0,
            cursor="hand2",
            command=self.show_login_page
        ).pack()


    # =====================================================
    # REGISTER
    # =====================================================

    def register(self):

        name = self.name_entry.get().strip()

        email = self.email_entry.get().strip().lower()

        password = self.password_entry.get()

        confirm = self.confirm_password_entry.get()


        if not name or not email or not password or not confirm:

            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )

            return


        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"


        if not re.match(email_pattern, email):

            messagebox.showerror(
                "Invalid Email",
                "Please enter a valid email address."
            )

            return


        if len(password) < 6:

            messagebox.showerror(
                "Weak Password",
                "Password must contain at least 6 characters."
            )

            return


        if password != confirm:

            messagebox.showerror(
                "Password Error",
                "Passwords do not match."
            )

            return


        if email in users:

            messagebox.showerror(
                "Account Exists",
                "This email is already registered."
            )

            return


        users[email] = {

            "name": name,

            "password": password

        }


        save_users(users)


        messagebox.showinfo(
            "Success",
            "Your EduBridge account has been created!"
        )


        self.show_login_page()


    # =====================================================
    # LOGIN
    # =====================================================

    def login(self):

        email = self.login_email.get().strip().lower()

        password = self.login_password.get()


        if not email or not password:

            messagebox.showwarning(
                "Missing Information",
                "Please enter email and password."
            )

            return


        if email not in users:

            messagebox.showerror(
                "Login Failed",
                "No account found with this email."
            )

            return


        if users[email]["password"] != password:

            messagebox.showerror(
                "Login Failed",
                "Incorrect password."
            )

            return


        # Get registered name

        name = users[email]["name"]


        # IMPORTANT:
        # Send BOTH name and email
        # to academic profile

        self.show_student_details(
            name,
            email
        )


    # =====================================================
    # ACADEMIC PROFILE INPUT PAGE
    # =====================================================

    def show_student_details(
        self,
        name,
        email
    ):

        self.clear_screen()

        self.create_background()

        self.create_header()


        # Welcome

        tk.Label(
            self.root,
            text=f"Welcome, {name}! 🎓",
            font=("Arial", 25, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=(25, 5)
        )


        tk.Label(
            self.root,
            text="Let's create your academic profile",
            font=("Arial", 11),
            fg=TEXT_LIGHT,
            bg=BG
        ).pack(
            pady=(0, 15)
        )


        # =================================================
        # FOUR COLUMNS
        # =================================================

        container = tk.Frame(
            self.root,
            bg=BG
        )

        container.pack(
            pady=5
        )


        # =================================================
        # COLUMN 1 - NAME
        # =================================================

        name_card = self.create_profile_card(
            container,
            0,
            "1",
            "Name",
            "Your full name"
        )


        self.student_name_entry = tk.Entry(
            name_card,
            width=22,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )


        self.student_name_entry.pack(
            pady=10,
            ipady=7
        )


        # Automatically insert name

        self.student_name_entry.insert(
            0,
            name
        )


        # =================================================
        # COLUMN 2 - UNIVERSITY
        # =================================================

        university_card = self.create_profile_card(
            container,
            1,
            "2",
            "University",
            "Enter university"
        )


        self.university_entry = tk.Entry(
            university_card,
            width=22,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )


        self.university_entry.pack(
            pady=10,
            ipady=7
        )


        # =================================================
        # COLUMN 3 - COLLEGE
        # =================================================

        college_card = self.create_profile_card(
            container,
            2,
            "3",
            "College",
            "Select college"
        )


        self.college_combo = ttk.Combobox(
            college_card,
            values=[
                "JNEC",
                "IICT"
            ],
            state="readonly",
            width=20,
            font=("Arial", 11)
        )


        self.college_combo.pack(
            pady=10,
            ipady=6
        )


        self.college_combo.set(
            "Select College"
        )


        # =================================================
        # COLUMN 4 - DEPARTMENT
        # =================================================

        department_card = self.create_profile_card(
            container,
            3,
            "4",
            "Department",
            "Select department"
        )


        self.department_combo = ttk.Combobox(
            department_card,
            values=[
                "Data Science (DS)",
                "Artificial Intelligence & Machine Learning",
                "Information Technology (IT)",
                "Computer Science (CS)",
                "Computer Science & Engineering (CSE)",
                "Electronics & Telecommunication (ENTC)"
            ],
            state="readonly",
            width=20,
            font=("Arial", 9)
        )


        self.department_combo.pack(
            pady=10,
            ipady=6
        )


        self.department_combo.set(
            "Select Department"
        )


        # =================================================
        # SEMESTER
        # =================================================

        tk.Label(
            self.root,
            text="Select Semester",
            font=("Arial", 11, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=(10, 5)
        )


        self.semester_combo = ttk.Combobox(
            self.root,
            values=[
                "Semester 1",
                "Semester 2",
                "Semester 3",
                "Semester 4",
                "Semester 5",
                "Semester 6",
                "Semester 7",
                "Semester 8"
            ],
            state="readonly",
            width=25,
            font=("Arial", 11)
        )


        self.semester_combo.pack(
            ipady=6
        )


        self.semester_combo.set(
            "Select Semester"
        )


        # =================================================
        # SUBMIT BUTTON
        # =================================================

        tk.Button(
            self.root,
            text="SUBMIT ACADEMIC PROFILE  →",
            font=("Arial", 12, "bold"),
            fg=WHITE,
            bg=PRIMARY,
            activebackground=PRIMARY_DARK,
            relief="flat",
            cursor="hand2",
            width=32,
            command=lambda: self.save_student_details(
                email
            )
        ).pack(
            pady=18,
            ipady=9
        )


        # Logout

        tk.Button(
            self.root,
            text="Logout",
            font=("Arial", 10),
            fg=TEXT_LIGHT,
            bg=BG,
            bd=0,
            cursor="hand2",
            command=self.show_login_page
        ).pack()


    # =====================================================
    # PROFILE CARD
    # =====================================================

    def create_profile_card(
        self,
        parent,
        column,
        number,
        title,
        subtitle
    ):

        card = tk.Frame(
            parent,
            bg=WHITE,
            width=255,
            height=200,
            highlightbackground=BORDER,
            highlightthickness=1
        )


        card.grid(
            row=0,
            column=column,
            padx=6
        )


        card.pack_propagate(False)


        # Number circle

        circle = tk.Canvas(
            card,
            width=45,
            height=45,
            bg=WHITE,
            highlightthickness=0
        )


        circle.pack(
            pady=(15, 3)
        )


        circle.create_oval(
            3,
            3,
            42,
            42,
            fill=PRIMARY,
            outline=""
        )


        circle.create_text(
            22,
            22,
            text=number,
            fill=WHITE,
            font=("Arial", 15, "bold")
        )


        # Title

        tk.Label(
            card,
            text=title,
            font=("Arial", 14, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack()


        # Subtitle

        tk.Label(
            card,
            text=subtitle,
            font=("Arial", 9),
            fg=TEXT_LIGHT,
            bg=WHITE
        ).pack(
            pady=4
        )


        return card


    # =====================================================
    # SAVE ACADEMIC PROFILE
    # =====================================================

    def save_student_details(
        self,
        email
    ):

        name = self.student_name_entry.get().strip()

        university = self.university_entry.get().strip()

        college = self.college_combo.get()

        department = self.department_combo.get()

        semester = self.semester_combo.get()


        # =================================================
        # VALIDATION
        # =================================================

        if not name:

            messagebox.showwarning(
                "Name Required",
                "Please enter your name."
            )

            return


        if not university:

            messagebox.showwarning(
                "University Required",
                "Please enter your university name."
            )

            return


        if college == "Select College":

            messagebox.showwarning(
                "College Required",
                "Please select your college."
            )

            return


        if department == "Select Department":

            messagebox.showwarning(
                "Department Required",
                "Please select your department."
            )

            return


        if semester == "Select Semester":

            messagebox.showwarning(
                "Semester Required",
                "Please select your semester."
            )

            return


        # =================================================
        # SHOW ACADEMIC PROFILE
        # =================================================

        self.show_main_dashboard(

            name,

            email,

            university,

            college,

            department,

            semester
        )


    # =====================================================
    # ACADEMIC PROFILE
    # =====================================================

    def show_main_dashboard(

        self,

        name,

        email,

        university,

        college,

        department,

        semester

    ):

        self.clear_screen()

        self.create_background()

        self.create_header()


        # Title

        tk.Label(
            self.root,
            text="Academic Profile 🎓",
            font=("Arial", 28, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=(25, 5)
        )


        tk.Label(
            self.root,
            text="Your EduBridge academic information",
            font=("Arial", 11),
            fg=TEXT_LIGHT,
            bg=BG
        ).pack(
            pady=(0, 15)
        )


        # =================================================
        # PROFILE CARD
        # =================================================

        profile = tk.Frame(
            self.root,
            bg=WHITE,
            width=750,
            height=390,
            highlightbackground=BORDER,
            highlightthickness=1
        )


        profile.pack(
            pady=5
        )


        profile.pack_propagate(False)


        # Profile heading

        tk.Label(
            profile,
            text="🎓  Student Academic Profile",
            font=("Arial", 20, "bold"),
            fg=TEXT,
            bg=WHITE
        ).pack(
            pady=(18, 12)
        )


        # =================================================
        # PROFILE INFORMATION
        # =================================================

        details = [

            ("Name", name),

            ("Email", email),

            ("University", university),

            ("College", college),

            ("Department", department),

            ("Semester", semester)

        ]


        for label, value in details:

            row = tk.Frame(
                profile,
                bg=WHITE
            )

            row.pack(
                pady=4
            )


            tk.Label(
                row,
                text=f"{label}:",
                font=("Arial", 11, "bold"),
                fg=PRIMARY,
                bg=WHITE,
                width=16,
                anchor="e"
            ).pack(
                side="left"
            )


            tk.Label(
                row,
                text=value,
                font=("Arial", 11),
                fg=TEXT,
                bg=WHITE,
                width=48,
                anchor="w"
            ).pack(
                side="left",
                padx=12
            )


        # =================================================
        # DASHBOARD BUTTON
        # =================================================

        tk.Button(
            self.root,
            text="GO TO EDUBRIDGE DASHBOARD  →",
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PRIMARY,
            activebackground=PRIMARY_DARK,
            relief="flat",
            cursor="hand2",
            width=32,
            command=lambda: self.show_dashboard(
                name,
                email,
                university,
                college,
                department,
                semester
            )
        ).pack(
            pady=15,
            ipady=8
        )


        # Logout

        tk.Button(
            self.root,
            text="Logout",
            font=("Arial", 10),
            fg=TEXT_LIGHT,
            bg=BG,
            bd=0,
            cursor="hand2",
            command=self.show_login_page
        ).pack()


    # =====================================================
    # FINAL DASHBOARD
    # =====================================================

    def show_dashboard(

        self,

        name,

        email,

        university,

        college,

        department,

        semester

    ):

        self.clear_screen()

        self.create_background()

        self.create_header()


        # Dashboard title

        tk.Label(
            self.root,
            text=f"Welcome to EduBridge, {name}! 🎓",
            font=("Arial", 26, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(
            pady=(35, 5)
        )


        tk.Label(
            self.root,
            text="Your personalized student dashboard",
            font=("Arial", 11),
            fg=TEXT_LIGHT,
            bg=BG
        ).pack(
            pady=(0, 25)
        )


        # =================================================
        # DASHBOARD CARDS
        # =================================================

        cards_frame = tk.Frame(
            self.root,
            bg=BG
        )

        cards_frame.pack()


        dashboard_items = [

            ("📚", "Courses", "View your courses"),

            ("📖", "Study Material", "Access study resources"),

            ("📝", "Assignments", "Manage assignments"),

            ("🤖", "AI Assistant", "Get AI learning help"),

            ("📊", "Progress", "Track your progress"),

            ("👤", "Profile", "View your profile")

        ]


        for i, item in enumerate(dashboard_items):

            icon, title, subtitle = item


            card = tk.Frame(
                cards_frame,
                bg=WHITE,
                width=260,
                height=130,
                highlightbackground=BORDER,
                highlightthickness=1,
                cursor="hand2"
            )


            card.grid(
                row=i // 3,
                column=i % 3,
                padx=10,
                pady=10
            )


            card.pack_propagate(False)


            tk.Label(
                card,
                text=icon,
                font=("Arial", 25),
                bg=WHITE
            ).pack(
                pady=(15, 3)
            )


            tk.Label(
                card,
                text=title,
                font=("Arial", 13, "bold"),
                fg=TEXT,
                bg=WHITE
            ).pack()


            tk.Label(
                card,
                text=subtitle,
                font=("Arial", 9),
                fg=TEXT_LIGHT,
                bg=WHITE
            ).pack(
                pady=3
            )


        # =================================================
        # LOGOUT
        # =================================================

        tk.Button(
            self.root,
            text="LOGOUT",
            font=("Arial", 11, "bold"),
            fg=WHITE,
            bg=PRIMARY,
            activebackground=PRIMARY_DARK,
            relief="flat",
            cursor="hand2",
            width=25,
            command=self.show_login_page
        ).pack(
            pady=25,
            ipady=8
        )


# =========================================================
# START APPLICATION
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = EduBridgeApp(root)

    root.mainloop()