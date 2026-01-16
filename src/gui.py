import tkinter as tk
from src.password_scanner import scan_password
from src.password_generator import generate_password
from src.password_suggestions import get_suggestions
from src.entropy_calculator import calculate_entropy, entropy_level
from src.breach_checker import is_breached
from src.strength_score import calculate_strength_score

show_password = False
generated_password = ""

# Main GUI function
def GUI():
    # Main window
    root = tk.Tk()
    root.title("Password Vulnerability & Generator (AI)")
    root.geometry("450x600")
    root.resizable(False, False)

    # Title
    title = tk.Label(
        root,
        text="Password Vulnerability & Generator",
        font=("Arial", 16, "bold")
    )
    title.pack(pady=10)

    # Password label
    pwd_label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
    pwd_label.pack()

    # Password entry
    password_entry = tk.Entry(root, width=30, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)
    
    # Toggle password visibility
    def toggle_password():
        global show_password

        if show_password:
            password_entry.config(show="*")
            toggle_btn.config(text="🐵")
            show_password = False
        else:
            password_entry.config(show="")
            toggle_btn.config(text="🙈")
            show_password = True

    # Toggle button
    toggle_btn = tk.Button(
        root,
        text="🐵",
        font=("Arial", 10),
        command=toggle_password
    )
    toggle_btn.pack(pady=5)

    # Result label
    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    # Scan password function
    def scan():
        password = password_entry.get()
        if password == "":
            result_label.config(text="Please enter a password", fg="red")
            suggestion_label.config(text="")
            entropy_label.config(text="")
            breach_label.config(text="")
            return

        strength = scan_password(password)
        suggestions = get_suggestions(password)

        entropy = calculate_entropy(password)
        level = entropy_level(entropy)

        breached = is_breached(password)

        # Strength
        if strength == "Very Weak":
            result_label.config(text="Strength: VERY WEAK ❌", fg="red")
        elif strength == "Medium":
            result_label.config(text="Strength: MEDIUM ⚠️", fg="orange")
        else:
            result_label.config(text="Strength: STRONG ✅", fg="green")

        # Suggestions
        suggestion_text = "Suggestions:\n"
        for s in suggestions:
            suggestion_text += f"- {s}\n"
        suggestion_label.config(text=suggestion_text)

        # Entropy
        entropy_label.config(
            text=f"Entropy Score: {entropy} bits ({level})"
        )

        # Breach warning
        if breached:
            breach_label.config(
                text="⚠️ ALERT: This password was found in a data breach!",
                fg="red"
            )
        else:
            breach_label.config(
                text="✅ This password was NOT found in known breaches",
                fg="green"
            )
        # Strength score calculation
        score = calculate_strength_score(
            strength,
            entropy,
            password,
            breached
        )

        score_label.config(
            text=f"Strength Score: {score} / 100",
            fg="green" if score >= 70 else "orange" if score >= 40 else "red"
        )


    # Generate password function
    def generate():
        global generated_password
        generated_password = generate_password()

        gen_label.config(
            text=f"Generated Password: {generated_password}",
            fg="blue"
        )

        entropy = calculate_entropy(generated_password)
        level = entropy_level(entropy)

        result_label.config(text="Generated Strong Password ✅", fg="green")
        suggestion_label.config(text="No suggestions needed 👍")
        entropy_label.config(
            text=f"Entropy Score: {entropy} bits ({level})"
        )

        if is_breached(generated_password):
            breach_label.config(
                text="⚠️ Generated password exists in breach list",
                fg="red"
            )
        else:
            breach_label.config(
                text="✅ Generated password is safe",
                fg="green"
            )

        # Strength score calculation
        score = calculate_strength_score(
            "Strong",
            entropy,
            generated_password,
            False
        )

        score_label.config(
            text=f"Strength Score: {score} / 100",
            fg="green"
        )


    # Copy to clipboard function
    def copy_password():
        if generated_password == "":
            result_label.config(text="No password to copy ❌", fg="red")
            return

        root.clipboard_clear()
        root.clipboard_append(generated_password)
        root.update()  # keeps clipboard after app closes

        result_label.config(text="Password copied to clipboard 📋", fg="green")

    # Scan button
    scan_btn = tk.Button(
        root,
        text="Scan Password",
        font=("Arial", 12),
        width=22,
        command=scan
    )
    scan_btn.pack(pady=5)

    # Generate button
    gen_btn = tk.Button(
        root,
        text="Generate Secure Password",
        font=("Arial", 12),
        width=22,
        command=generate
    )
    gen_btn.pack(pady=5)

    # Copy button
    copy_btn = tk.Button(
        root,
        text="Copy Password",
        font=("Arial", 12),
        width=18,
        command=copy_password
    )
    copy_btn.pack(pady=5)

    # Generated password label
    gen_label = tk.Label(
        root,
        text="",
        font=("Arial", 9, "italic")
    )
    gen_label.pack(pady=5)

    # Suggestions label
    suggestion_label = tk.Label(
        root,
        text="",
        font=("Arial", 10),
        justify="left",
        wraplength=380
    )
    suggestion_label.pack(pady=5)

    # Breach label
    breach_label = tk.Label(
        root,
        text="",
        font=("Arial", 11, "bold")
    )
    breach_label.pack(pady=5)

    score_label = tk.Label(
        root,
        text="",
        font=("Arial", 12, "bold")
    )
    score_label.pack(pady=5)

    # Entropy label
    entropy_label = tk.Label(
        root,
        text="",
        font=("Arial", 11, "bold")
    )
    entropy_label.pack(pady=5)

    # Footer
    footer = tk.Label(
        root,
        text="©2026 AI Based Cyber Security Project",
        font=("Arial", 9)
    )
    footer.pack(side="bottom", pady=10)

    # Run GUI
    root.mainloop()
