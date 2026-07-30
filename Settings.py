from tkinter import *
import config 
from tkinter import messagebox


def settings(window):
    
    # Initialize the settings Toplevel window
    settings_window = Toplevel(window)
    settings_window.geometry("700x400")
    settings_window.title("Settings")
    settings_window.option_add("*font", "Arial 20")
    settings_window.attributes("-fullscreen", config.FULLSCREEN)

    # FIX 1: Instant screen and text toggle handling when clicked
    def toggle_fullscreen():
        is_fs = fullscreen_value.get()
        
        if is_fs:
            fullscreen_btn.config(text="Fullscreen on")
            window.attributes("-fullscreen", True)
            settings_window.attributes("-fullscreen", True)
        else:
            fullscreen_btn.config(text="Fullscreen off")
            window.attributes("-fullscreen", False)
            settings_window.attributes("-fullscreen", False)
            
            # Forces operating systems to snap layouts back to desktop sizes 
            # instead of keeping them artificially maximized
            window.geometry("600x400")
            settings_window.geometry("700x400")

    # FIX 2: Overwrite the specific line inside your config.py script
    def save():
        current_fs = fullscreen_value.get()
        
        # 1. Sync the running app variable instantly
        config.FULLSCREEN = current_fs
        
        try:
            # 2. Extract current lines out of the file
            with open("config.py", "r") as file:
                lines = file.readlines()
            
            # 3. Target and rewrite only the FULLSCREEN declaration line
            for i, line in enumerate(lines):
                if line.strip().startswith("FULLSCREEN"):
                    lines[i] = f"FULLSCREEN = {current_fs}\n"
                    break
            else:
                # Appends line if missing from the script entirely
                lines.append(f"FULLSCREEN = {current_fs}\n")
            
            # 4. Write back the updated line array
            with open("config.py", "w") as file:
                file.writelines(lines)
                
        except Exception as error:
            print(f"Failed to overwrite config script: {error}")

        # Synchronize structural frames
        window.attributes("-fullscreen", config.FULLSCREEN)
        settings_window.attributes("-fullscreen", config.FULLSCREEN)
        messagebox.showinfo("Settings", "Settings Saved Successfully!")

    def back():
        settings_window.destroy()
        window.deiconify()
        window.attributes("-fullscreen", config.FULLSCREEN)

    # Configuration Variables
    difficulty = StringVar()
    difficulty.set("Medium")

    mute_sound_value = BooleanVar(value=True)
    fullscreen_value = BooleanVar(value=config.FULLSCREEN)

    # UI Element Layout - Difficulty
    label = Label(settings_window, text="Difficulty settings")
    label.pack(pady=13)

    easy = Radiobutton(settings_window, text="Easy", variable=difficulty, value="easy")
    easy.pack()

    medium = Radiobutton(settings_window, text="Medium", variable=difficulty, value="medium")
    medium.pack()

    hard = Radiobutton(settings_window, text="Hard", variable=difficulty, value="hard")
    hard.pack()

    # UI Element Layout - Extras
    label = Label(settings_window, text="Extra")
    label.pack(pady=13)

    # Dynamic label generation matching real initialization parameters
    initial_fs_text = "Fullscreen on" if config.FULLSCREEN else "Fullscreen off"
    fullscreen_btn = Checkbutton(
        settings_window, 
        text=initial_fs_text, 
        variable=fullscreen_value, 
        command=toggle_fullscreen
    )
    fullscreen_btn.pack()

    def sound():
        if mute_sound_value.get():
            mute_sound.config(text="Mute on")
        else:
            mute_sound.config(text="Mute off")

    mute_sound = Checkbutton(settings_window, command=sound, text="Mute on", variable=mute_sound_value)
    mute_sound.pack()

    # Form Submission and Navigation
    back_btn = Button(settings_window, text="Back", command=back)
    back_btn.place(x=0, y=0)

    save_btn = Button(settings_window, text="Save settings", command=save)
    save_btn.pack()