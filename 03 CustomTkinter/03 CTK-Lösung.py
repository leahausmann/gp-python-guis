import customtkinter as ctk




# Dark mode aktivieren
ctk.set_appearance_mode("Dark")

# Fenster erstellen
app = ctk.CTk()
app.title("CustomTkinter_Demo")
app.geometry("400x800")

button = ctk.CTkButton(app, text="Klick mich") 
button.pack (pady=10) 


entry = ctk.CTkEntry(app, placeholder_text="Dein Name")
entry.pack(pady=10)



app.mainloop()