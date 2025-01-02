import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from shapes import calculate_area
from lessons import lessons
from database import update_progress, fetch_progress

# Theme colors (ttkbootstrap manages most of these)
BG_COLOR = "#0d47a1"  # Dark blue background color
HEADING_COLOR = "#e3f2fd"  # Light blue heading color


def show_lesson(shape):
    lesson = lessons[shape]
    top = ttk.Toplevel()
    top.configure(bg=BG_COLOR)
    top.title(f"{shape} Lesson")
    top.geometry("800x700")
    top.resizable(False, False)

    ttk.Label(top, text=f"Learn about {shape}!", font=("Arial", 22, "bold"), bootstyle="danger").pack(pady=20)
    ttk.Label(top, text=f"Formula: {lesson['formula']}", font=("Arial", 16), bootstyle="info").pack(pady=10)
    ttk.Label(top, text=f"Example: {lesson['example']}", font=("Arial", 14), bootstyle="info").pack(pady=10)

    image_path = lesson["image"]
    img = ttk.PhotoImage(file=image_path)
    image_label = ttk.Label(top, image=img)
    image_label.image = img
    image_label.pack(pady=10)

    ttk.Button(top, text="Close", command=top.destroy, bootstyle="danger", width=15).pack(pady=20)


def ask_question(shape):
    lesson = lessons[shape]
    question = lesson['questions'][0]

    def check_answer():
        try:
            user_answer = float(answer_entry.get())
            correct_answer = calculate_area(shape, **question)
            if abs(user_answer - correct_answer) < 0.01:
                update_progress("Student", shape, 10)
                ttk.messagebox.showinfo("Result", "\ud83c\udf89 Correct! Well done!")
            else:
                ttk.messagebox.showinfo("Result", f"\u274c Incorrect! The correct answer is {correct_answer:.2f}")
            answer_entry.delete(0, ttk.END)
        except ValueError:
            ttk.messagebox.showwarning("Invalid Input", "Please enter a valid number.")

    top = ttk.Toplevel()
    top.configure(bg=BG_COLOR)
    top.title(f"{shape} Question")
    top.geometry("800x700")
    top.resizable(False, False)

    ttk.Label(top, text=f"Question about {shape}", font=("Arial", 20, "bold"), bootstyle="danger").pack(pady=20)
    ttk.Label(top, text=question["q"], font=("Arial", 16), bootstyle="info").pack(pady=10)

    image_path = lesson["image"]
    img = ttk.PhotoImage(file=image_path)
    image_label = ttk.Label(top, image=img)
    image_label.image = img
    image_label.pack(pady=10)

    answer_entry = ttk.Entry(top, font=("Arial", 14), width=10)
    answer_entry.pack(pady=10)

    ttk.Button(top, text="Submit", command=check_answer, bootstyle="success", width=15).pack(pady=10)
    ttk.Button(top, text="Close", command=top.destroy, bootstyle="danger", width=15).pack(pady=20)


def main_gui():
    root = ttk.Window(themename="darkly")
    root.title("Intelligent Tutoring System")
    root.geometry("800x1000")
    root.resizable(False, False)

    ttk.Label(root, text="\ud83d\udcd8 Intelligent Tutoring System for MATH", font=("Arial", 26, "bold"), bootstyle="danger").pack(pady=20)
    ttk.Label(root, text="Choose a geometry to learn and to practice!", font=("Arial", 18), bootstyle="info").pack(pady=10)

    for shape in lessons.keys():
        frame = ttk.Frame(root)
        frame.pack(pady=10)

        ttk.Button(frame, text=f"\ud83d\udcd8 Learn {shape}",
                   command=lambda s=shape: show_lesson(s),
                   bootstyle="primary", width=20).pack(side="left", padx=10)

        ttk.Button(frame, text=f"\ud83d\udcdd {shape} Quiz",
                   command=lambda s=shape: ask_question(s),
                   bootstyle="success", width=20).pack(side="left", padx=10)

    ttk.Button(root, text="Exit", command=root.destroy, bootstyle="danger", width=20).pack(pady=30)

    root.mainloop()

main_gui()
