import tkinter as tk
from tkinter import messagebox

# Function to move to the next field when Enter is pressed
def on_enter(event, next_widget):
    next_widget.focus()

# Function to predict personality and display result
def predict_personality():
    try:
        # Get input values
        age = int(age_entry.get())
        openness = float(openness_entry.get())
        neuroticism = float(neuroticism_entry.get())
        conscientiousness = float(conscientiousness_entry.get())
        agreeableness = float(agreeableness_entry.get())
        extraversion = float(extraversion_entry.get())
        gender = gender_entry.get().strip().lower()
        
        # Simple personality prediction based on extraversion
        if extraversion >= 7:
            personality = "Extraverted"
            symbol = "🙂"
        else:
            personality = "Introverted"
            symbol = "🙁"
        
        # Display output in a label
        result_label.config(text=f"Predicted Personality: {personality} {symbol}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid inputs in all fields.")

# Create main window
window = tk.Tk()
window.title("Personality Prediction")

# Set background color
window.config(bg="#D3F1DF")

# Center the window on the screen
window_width = 600
window_height = 500

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a frame for the input fields and button to center everything
frame = tk.Frame(window, bg="#D3F1DF")
frame.pack(padx=20, pady=20, expand=True)

# Create labels and input fields
age_label = tk.Label(frame, text="Age:", bg="#D3F1DF", font=("Arial", 12))
age_label.grid(row=0, column=0, padx=10, pady=10)

age_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
age_entry.grid(row=0, column=1, padx=10, pady=10)
age_entry.bind("<Return>", lambda event: on_enter(event, openness_entry))  # Focus shift to next field

openness_label = tk.Label(frame, text="Openness (1-10):", bg="#D3F1DF", font=("Arial", 12))
openness_label.grid(row=1, column=0, padx=10, pady=10)

openness_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
openness_entry.grid(row=1, column=1, padx=10, pady=10)
openness_entry.bind("<Return>", lambda event: on_enter(event, neuroticism_entry))

neuroticism_label = tk.Label(frame, text="Neuroticism (1-10):", bg="#D3F1DF", font=("Arial", 12))
neuroticism_label.grid(row=2, column=0, padx=10, pady=10)

neuroticism_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
neuroticism_entry.grid(row=2, column=1, padx=10, pady=10)
neuroticism_entry.bind("<Return>", lambda event: on_enter(event, conscientiousness_entry))

conscientiousness_label = tk.Label(frame, text="Conscientiousness (1-10):", bg="#D3F1DF", font=("Arial", 12))
conscientiousness_label.grid(row=3, column=0, padx=10, pady=10)

conscientiousness_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
conscientiousness_entry.grid(row=3, column=1, padx=10, pady=10)
conscientiousness_entry.bind("<Return>", lambda event: on_enter(event, agreeableness_entry))

agreeableness_label = tk.Label(frame, text="Agreeableness (1-10):", bg="#D3F1DF", font=("Arial", 12))
agreeableness_label.grid(row=4, column=0, padx=10, pady=10)

agreeableness_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
agreeableness_entry.grid(row=4, column=1, padx=10, pady=10)
agreeableness_entry.bind("<Return>", lambda event: on_enter(event, extraversion_entry))

extraversion_label = tk.Label(frame, text="Extraversion (1-10):", bg="#D3F1DF", font=("Arial", 12))
extraversion_label.grid(row=5, column=0, padx=10, pady=10)

extraversion_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
extraversion_entry.grid(row=5, column=1, padx=10, pady=10)
extraversion_entry.bind("<Return>", lambda event: on_enter(event, gender_entry))

gender_label = tk.Label(frame, text="Gender (Male/Female):", bg="#D3F1DF", font=("Arial", 12))
gender_label.grid(row=6, column=0, padx=10, pady=10)

gender_entry = tk.Entry(frame, font=("Arial", 12), bg="#85A98F")
gender_entry.grid(row=6, column=1, padx=10, pady=10)
gender_entry.bind("<Return>", lambda event: on_enter(event, predict_button))

# Button to predict personality
predict_button = tk.Button(frame, text="Predict Personality", font=("Arial", 14), bg="#5A6C57", fg="white", command=predict_personality, cursor="hand2")
predict_button.grid(row=7, column=0, columnspan=2, padx=10, pady=20)

# Label to display the result
result_label = tk.Label(frame, text="", bg="#D3F1DF", font=("Arial", 14), fg="#525B44")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=20)

# Start the Tkinter event loop
window.mainloop()
