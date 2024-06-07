import tkinter as tk
import requests

# Workflow while creating a GUI using Tkinter
# 1 Imports
# 2 Create GUI apppn main window(Designing app)
# 3 Add 1/more widgets(ctrls used in GUI appn such as labels, bttns and text boxes) to GUI
# 4 Enter main event loop to take action against each action triggered by user

# Application layout is controlled with geometry managers.


def convert_currency():
    # Get the currency to convert from
    usr_currency = usr_currency_from_entry.get().upper()
    try:
        # Get and validate the amount
        amount = float(amount_entry.get())
    except ValueError:
        result_label.config(text="Invalid amount. Enter numeric values.")
        return

    # Get the currency to convert to
    usr_cnvtd_currency = usr_cnvtd_currency_entry.get().upper()

    try:
        # Fetch conversion rates from the API
        response = requests.get(
            f"https://v6.exchangerate-api.com/v6/e06dd8e5b23d9bff2d22e45d/latest/{usr_currency}"
        )
        data = response.json()

        if data["result"] == "success" and "conversion_rates" in data:
            if usr_cnvtd_currency in data["conversion_rates"]:
                # Get the conversion rate
                exchng_rate = data["conversion_rates"][usr_cnvtd_currency]
                # Calculate the converted amount
                cnvtd_amount = amount * exchng_rate
                # Get the last update time
                last_update = data["time_last_update_utc"]
                result_label.config(
                    text=f"{amount} {usr_currency} is equal to {cnvtd_amount:.2f} {usr_cnvtd_currency}\nLast update: {last_update}"
                )
            else:
                result_label.config(
                    text=f"Conversion rate for {usr_cnvtd_currency} not found."
                )
        else:
            result_label.config(text="Failed to retrieve conversion rates.")
    except requests.RequestException as e:
        result_label.config(
            text=f"Error during requests to the currency conversion API: {e}"
        )


# Widgets are contained inside of main window.
# Main window
window = tk.Tk()
window.title("Currency Converter")

# Frame widgets are used to organize the layout of your widgets
# Frames are best thought of as containers for other widgets
frame_1 = tk.Frame(master=window)
frame_1.grid(row=0, column=0, sticky="W", padx=10, pady=5)
# Use Label class to add/display some text to a window
usr_currency_from = tk.Label(master=frame_1, text="Currency to convert from: ")
# Addition of widget to the window
usr_currency_from.pack(side=tk.LEFT)
# Entry widget to get user input
# Displays a small text box to type something into
usr_currency_from_entry = tk.Entry(master=frame_1, width=5)
usr_currency_from_entry.pack(side=tk.LEFT)

frame_2 = tk.Frame(master=window)
frame_2.grid(row=1, column=0, sticky="W", padx=10, pady=5)
amount = tk.Label(master=frame_2, text="Amount: ")
amount.pack(side=tk.LEFT)
amount_entry = tk.Entry(master=frame_2, width=10)
amount_entry.pack(side=tk.LEFT)

frame_3 = tk.Frame(master=window)
frame_3.grid(row=2, column=0, sticky="W", padx=10, pady=5)
usr_cnvtd_currency = tk.Label(master=frame_3, text="Currency to convert to: ")
usr_cnvtd_currency.pack(side=tk.LEFT)
usr_cnvtd_currency_entry = tk.Entry(master=frame_3, width=5)
usr_cnvtd_currency_entry.pack(side=tk.LEFT)

# Frame for buttons
button_frame = tk.Frame(master=window)
button_frame.grid(row=3, column=0, sticky="W", padx=10, pady=10)

# Button Widget(to display clickable buttons)
cnvsn_btn = tk.Button(master=button_frame, text="Convert", command=convert_currency)
cnvsn_btn.pack(side=tk.LEFT, padx=5)

# Quit button widget
quit_btn = tk.Button(master=button_frame, text="Quit", command=window.destroy)
quit_btn.pack(side=tk.LEFT, padx=5)

# Result Label
result_label = tk.Label(master=window, text="")
result_label.grid(row=4, column=0, sticky="W", padx=10, pady=10)

# Tells python to run tkinter event loop
window.mainloop()
