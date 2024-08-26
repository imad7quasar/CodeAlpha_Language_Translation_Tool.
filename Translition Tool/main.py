import tkinter as tk
from tkinter import ttk, Canvas, Entry, Text
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Function to handle translation
def translate_text():
    input_text = text_input.get("1.0", tk.END).strip()  # Get user input
    detected_lang = translator.detect(input_text).lang  # Detect the language
    dest_language = language_combobox.get()  # Get selected language
    if dest_language:
        dest_language_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(dest_language)]
        translation = translator.translate(input_text, dest=dest_language_code)
        text_output.delete("1.0", tk.END)  # Clear previous output
        text_output.insert(tk.END, translation.text)  # Display the translation
        detected_language_label.config(text=f"Detected Language: {LANGUAGES[detected_lang].title()}")  # Display detected language
    else:
        detected_language_label.config(text="Please select a language.")

# Function to create rounded rectangles
def create_rounded_rect(canvas, x1, y1, x2, y2, radius=25, **kwargs):
    points = [
        x1 + radius, y1,
        x1 + radius, y1,
        x2 - radius, y1,
        x2 - radius, y1,
        x2, y1,
        x2, y1 + radius,
        x2, y1 + radius,
        x2, y2 - radius,
        x2, y2 - radius,
        x2, y2,
        x2 - radius, y2,
        x2 - radius, y2,
        x1 + radius, y2,
        x1 + radius, y2,
        x1, y2,
        x1, y2 - radius,
        x1, y2 - radius,
        x1, y1 + radius,
        x1, y1 + radius,
        x1, y1
    ]
    return canvas.create_polygon(points, **kwargs, smooth=True)

# Create the main application window
root = tk.Tk()
root.title("Language Translator")
root.geometry("650x500")
root.configure(bg="#FFFBE6")  # Set the background color (light cream)

# Set the Poppins font (ensure Poppins is installed or change to a default modern font)
font_family = ("Poppins", 12)
heading_font = ("Poppins", 16, "bold")

# Create a canvas to draw rounded corners
canvas = Canvas(root, bg="#FFFBE6", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Input text label
tk.Label(canvas, text="Enter Text:", font=heading_font, fg="#00712D", bg="#FFFBE6").place(x=50, y=30)

# Rounded rectangle for input text
input_box = create_rounded_rect(canvas, 40, 60, 610, 160, radius=20, fill="#D5ED9F")
text_input = Text(canvas, height=5, width=50, font=font_family, bg="#D5ED9F", fg="#00712D", insertbackground="#00712D", bd=0, highlightthickness=0)
canvas.create_window(325, 110, window=text_input)  # Centered within the rounded box

# Language selection
tk.Label(canvas, text="Select Language:", font=heading_font, fg="#00712D", bg="#FFFBE6").place(x=50, y=180)
language_combobox = ttk.Combobox(canvas, values=list(LANGUAGES.values()), state="readonly", width=30, font=font_family)
language_combobox.place(x=250, y=180)
language_combobox.set("Select Language")  # Default text

# Function to change button color on hover
def on_enter(e):
    e.widget.config(bg="#FF9100")

def on_leave(e):
    e.widget.config(bg="#D5ED9F")

# Button with rounded corners
button_bg = create_rounded_rect(canvas, 200, 230, 450, 280, radius=20, fill="#D5ED9F")
translate_button = tk.Button(canvas, text="Translate", font=("Poppins", 14), bg="#D5ED9F", fg="#00712D", bd=0, cursor="hand2", activebackground="#FF9100", command=translate_text)
translate_button_window = canvas.create_window(325, 255, window=translate_button)
translate_button.bind("<Enter>", on_enter)
translate_button.bind("<Leave>", on_leave)

# Detected language label
detected_language_label = tk.Label(canvas, text="", font=font_family, fg="#00712D", bg="#FFFBE6")
canvas.create_window(325, 310, window=detected_language_label)

# Output label and text box
tk.Label(canvas, text="Translation:", font=heading_font, fg="#00712D", bg="#FFFBE6").place(x=50, y=340)
output_box = create_rounded_rect(canvas, 40, 370, 610, 470, radius=20, fill="#D5ED9F")
text_output = Text(canvas, height=5, width=50, font=font_family, bg="#D5ED9F", fg="#00712D", insertbackground="#00712D", bd=0, highlightthickness=0)
canvas.create_window(325, 420, window=text_output)

# Run the application
root.mainloop()
