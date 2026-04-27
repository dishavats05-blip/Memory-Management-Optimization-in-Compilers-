import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class CompilerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Optimizing Compiler")
        self.root.geometry("1200x700")
        self.root.configure(bg="#e6f2ff")


        self.examples = {

            "Basic":
"""int a;
int b;
int c;
a = b + c;
""",

            "Arithmetic":
"""int a;
int b;
int c;
int d;
a = b + c * d;
""",

            "Medium":
"""int x;
int y;
int z;
x = y * z + 10;
""",

            "Complex":
"""int p;
int q;
int r;
p = (q + r) * 5;
""",

            "Chain":
"""int a;
int b;
int c;
int d;
a = b + c;
b = a * d;
""",

            "Heavy Expression":
"""int a;
int b;
int c;
int d;
int e;
int f;
a = b + c * d + e * f;
""",

            "Very Heavy":
"""int a;
int b;
int c;
int d;
int e;
int f;
int g;
int h;
a = b + c * d + e * f + g * h;
""",

            "Nested":
"""int z;
int a;
int b;
int c;
int d;
int e;
int f;
z = ((a + b) * c) + (d * (e + f));
""",

            "Final Demo":
"""int a;
int b;
int c;
int d;
int e;
int f;
a = b + c * d + e * f;
"""
        }

        self.create_widgets()

    def create_widgets(self):

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        main_frame = tk.Frame(self.root, bg="#e6f2ff")
        main_frame.grid(row=0, column=0, sticky="nsew")

        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

        title = tk.Label(main_frame,
                         text="Memory Optimizing Compiler",
                         font=("Segoe UI", 22, "bold"),
                         bg="#e6f2ff",
                         fg="#003366")
        title.grid(row=0, column=0, columnspan=2, pady=10)

        left_frame = tk.Frame(main_frame, bg="#cce6ff")
        left_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        tk.Label(left_frame,
                 text="Source Code",
                 font=("Segoe UI", 14, "bold"),
                 bg="#cce6ff").pack(pady=5)

        self.input_text = tk.Text(left_frame,
                                 font=("Consolas", 11),
                                 bg="white")
        self.input_text.pack(expand=True, fill="both", padx=10, pady=5)

        right_frame = tk.Frame(main_frame, bg="#cce6ff")
        right_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

        tk.Label(right_frame,
                 text="Compiler Output (All Phases)",
                 font=("Segoe UI", 14, "bold"),
                 bg="#cce6ff").pack(pady=5)

        self.output_text = tk.Text(right_frame,
                                  font=("Consolas", 10),
                                  bg="white",
                                  fg="#003366")
        self.output_text.pack(expand=True, fill="both", padx=10, pady=5)

        self.figure = plt.figure(figsize=(4, 2), dpi=100)
        self.ax = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, right_frame)
        self.canvas.get_tk_widget().pack(fill="x", padx=10, pady=5)

        bottom_frame = tk.Frame(main_frame, bg="#e6f2ff")
        bottom_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.example_combo = ttk.Combobox(bottom_frame,
                                          values=list(self.examples.keys()),
                                          state="readonly",
                                          width=30)
        self.example_combo.set("Select Example")
        self.example_combo.pack(side="left", padx=10)

        tk.Button(bottom_frame,
                  text="Load Example",
                  command=self.load_example,
                  bg="#3399ff",
                  fg="white").pack(side="left", padx=5)

        tk.Button(bottom_frame,
                  text="Run Compiler",
                  command=self.run_compiler,
                  bg="#0066cc",
                  fg="white").pack(side="left", padx=5)

        tk.Button(bottom_frame,
                  text="Clear",
                  command=self.clear_text,
                  bg="#cc3300",
                  fg="white").pack(side="left", padx=5)

    def load_example(self):
        selected = self.example_combo.get()
        if selected in self.examples:
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, self.examples[selected])

    def run_compiler(self):

        code = self.input_text.get("1.0", tk.END)
        backend_path = os.path.abspath("../backend/compiler.exe")

        try:
            process = subprocess.Popen(
                backend_path,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            output, error = process.communicate(code)

            self.output_text.delete("1.0", tk.END)

            if error:
                self.output_text.insert(tk.END, "SYSTEM ERROR:\n" + error)
                return

            if "Parse Error" in output:
                messagebox.showerror("Syntax Error", "Invalid syntax in input")
                self.output_text.insert(tk.END, output)
                return

            if "Semantic Error" in output:
                self.output_text.insert(tk.END, "SEMANTIC ERRORS:\n\n" + output)
                return

            formatted = "===== COMPILER RESULT =====\n\n" + output
            self.output_text.insert(tk.END, formatted)

            self.update_graph(output)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_graph(self, output):

        before = re.search(r"Total Memory Before:\s*(\d+)", output, re.IGNORECASE)
        after = re.search(r"Optimized Memory Usage:\s*(\d+)", output, re.IGNORECASE)

        if before and after and "Error" not in output:
            before_val = int(before.group(1))
            after_val = int(after.group(1))

            self.ax.clear()
            self.ax.bar(["Before", "After"], [before_val, after_val])
            self.ax.set_title("Memory Optimization Comparison")
            self.ax.set_ylabel("Bytes")
            self.canvas.draw()

    def clear_text(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.ax.clear()
        self.canvas.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = CompilerGUI(root)
    root.mainloop()