import tkinter as tk
from time import strftime

def update_time():
    """
    Gets the current time and updates the time_label.
    This function is called every second.
    """
    # Format the time string (e.g., 14:30:55)
    time_string = strftime('%H:%M:%S %p')
    time_label.config(text=time_string)
    
    # Format the date string (e.g., Wednesday, Oct 15, 2025)
    date_string = strftime('%A, %b %d, %Y')
    date_label.config(text=date_string)

    # Schedule the update_time function to be called after 1000ms (1 second)
    time_label.after(1000, update_time)

# --- Create the main window ---
root = tk.Tk()
root.title("Digital Clock")
root.geometry("800x250") # default size
root.configure(bg='black') # black background for a classic clock look
root.resizable(False, False) # Making the window not resizable

# --- Create Labels to display time and date ---
time_label = tk.Label(
    root,
    font=('terminal', 150, 'bold'),
    background='black',
    foreground='cyan'
)
time_label.pack(anchor='center', pady=(10, 0))

date_label = tk.Label(
    root,
    font=('terminal', 30),
    background='black',
    foreground='magenta'
)
date_label.pack(anchor='center')


# --- Initial call to the update function ---
update_time()

# --- Start the GUI event loop ---
root.mainloop()
