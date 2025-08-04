# Import necessary modules
import tkinter as tk  # GUI toolkit for creating graphical interfaces
from tkinter import scrolledtext  # Provides a text widget with a scrollbar
import requests  # For making HTTP requests to the Ollama server
import json  # For parsing JSON responses
import time  # For measuring response time

# Define the Ollama server URL and the model to be used
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# Function to send a prompt to the Ollama server and display the response
def query_ollama():
    # Get the user input from the text widget
    prompt = input_text.get("1.0", tk.END).strip()
    
    # If the input is empty, show a message and return
    if not prompt:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a prompt.")
        response_time_label.config(text="")
        return

    # Prepare the payload for the POST request
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt
    }

    try:
        # Record the start time
        start_time = time.time()
        
        # Send the request to the Ollama server with streaming enabled
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        response_text = ""
        
        # Read the response line by line
        for line in response.iter_lines():
            if line:
                try:
                    # Decode and parse each line as JSON
                    json_line = json.loads(line.decode('utf-8'))
                    # Append the response text
                    response_text += json_line.get("response", "")
                except json.JSONDecodeError:
                    continue  # Skip lines that can't be decoded

        # Record the end time and calculate elapsed time
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Display the response in the output text widget
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, response_text or "No response received.")
        response_time_label.config(text=f"Response time: {elapsed_time:.2f} seconds")
    
    # Handle any request errors
    except requests.exceptions.RequestException as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        response_time_label.config(text="")

# Function to clear the input text field
def clear_input():
    input_text.delete("1.0", tk.END)

# Function to exit the application
def exit_app():
    window.destroy()

# Create the main GUI window
window = tk.Tk()
window.title("Ollama Query Interface")

# Add a label and text box for user input
tk.Label(window, text="Enter your prompt:").pack()
input_text = tk.Text(window, height=5, width=60)
input_text.pack()

# Create a frame to hold the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=5)

# Add a button to submit the prompt
submit_button = tk.Button(button_frame, text="Query Ollama", command=query_ollama)
submit_button.grid(row=0, column=0, padx=5)

# Add a button to clear the input
clear_button = tk.Button(button_frame, text="Clear Input", command=clear_input)
clear_button.grid(row=0, column=1, padx=5)

# Add a button to exit the application
exit_button = tk.Button(button_frame, text="Exit", command=exit_app)
exit_button.grid(row=0, column=2, padx=5)

# Add a label and text box to display the response
tk.Label(window, text="Ollama Response:").pack()
output_text = scrolledtext.ScrolledText(window, height=10, width=60)
output_text.pack()

# Add a label to show the response time
response_time_label = tk.Label(window, text="", fg="blue")
response_time_label.pack()

# Start the GUI event loop
window.mainloop()
