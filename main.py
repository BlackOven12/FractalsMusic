import tkinter as tk
from tkinter import messagebox
import music

# Window
root = tk.Tk()
root.title("Music By Fractals")
root.geometry("500x400")
root.configure(bg="#1a1a2e")

# Settings
sample_rate_var = tk.IntVar(value=44100)
amplitude_var = tk.DoubleVar(value=0.5)
length_var = tk.IntVar(value=300)


def generate_with_settings():
    sample_rate = sample_rate_var.get()
    amplitude = amplitude_var.get()
    length = length_var.get()

    if sample_rate < 8000 or sample_rate > 96000:
        messagebox.showerror("Error", "Sample rate: 8000-96000")
        return
    if amplitude <= 0 or amplitude > 1.0:
        messagebox.showerror("Error", "Amplitude: 0.01-1.0")
        return
    if length < 10 or length > 1000:
        messagebox.showerror("Error", "Length: 10-1000")
        return

    btn.config(text="Generating...", state="disabled")
    root.update()

    print(
        f"→ Starting with: sample_rate={sample_rate}, amp={amplitude}, length={length}"
    )
    music.generate_random_wav(sample_rate, amplitude, length)

    btn.config(text="READY", state="normal")
    messagebox.showinfo(
        "WAV IS READY",
        f"Created with these settings:\n"
        f"Sample rate: {sample_rate}\n"
        f"Amplitude: {amplitude}\n"
        f"Length: {length} sinusoids",
    )


tk.Label(
    root,
    text="GENERATION'S SETTINGS",
    font=("Arial", 16, "bold"),
    fg="#00ff99",
    bg="#1a1a2e",
).pack(pady=20)

# Sample rate
tk.Label(root, text="Sample rate (8000-96000):", fg="white", bg="#1a1a2e").pack()
tk.Entry(root, textvariable=sample_rate_var, width=15, font=("Arial", 12)).pack(pady=5)

# Amplitude
tk.Label(root, text="Amplitude (0.01-1.0):", fg="white", bg="#1a1a2e").pack()
tk.Entry(root, textvariable=amplitude_var, width=15, font=("Arial", 12)).pack(pady=5)

# Length (sinusoids' amount)
tk.Label(root, text="Sinusoids' amount (10-1000):", fg="white", bg="#1a1a2e").pack()
tk.Entry(root, textvariable=length_var, width=15, font=("Arial", 12)).pack(pady=5)

# Button
btn = tk.Button(
    root,
    text="CREATE WAV",
    font=("Arial", 18, "bold"),
    bg="#ff0044",
    fg="white",
    command=generate_with_settings,
)
btn.pack(pady=30)

root.mainloop()
