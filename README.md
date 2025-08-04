# ollama_interface
Ollama Interface

# Create the design document content in Markdown format
design_doc_md = """# 📝 Design Document: Ollama Query Interface

## 1. **Overview**

The **Ollama Query Interface** is a desktop GUI application built using Python's `tkinter` library. It allows users to input prompts and receive responses from a locally hosted Ollama server using the `llama3` model. The application is designed for ease of use, with features to submit queries, clear input, and exit the interface.

## 2. **Objectives**

- Provide a user-friendly interface to interact with the Ollama server.
- Display real-time responses from the model.
- Measure and show response time for each query.
- Handle errors gracefully and inform the user.

## 3. **Technology Stack**

- **Frontend**: `tkinter` (Python standard GUI library)
- **Backend**: `requests` for HTTP communication with Ollama server
- **Model**: `llama3` hosted on `localhost:11434`
- **Utilities**: `json` for parsing responses, `time` for measuring latency

## 4. **Architecture**

### Components:

- **GUI Window**: Main application window
- **Input Text Box**: For user to enter prompt
- **Buttons**:
  - **Query Ollama**: Sends prompt to server
  - **Clear Input**: Clears the input field
  - **Exit**: Closes the application
- **Output Text Box**: Displays model response
- **Response Time Label**: Shows time taken for response

### Data Flow:

1. User enters a prompt.
2. On clicking "Query Ollama":
   - Prompt is sent to the Ollama server via POST request.
   - Response is streamed and parsed line-by-line.
   - Output is displayed in the text box.
   - Response time is calculated and shown.
3. User can clear input or exit the application.

## 5. **Functional Specifications**

### `query_ollama()`
- Validates input.
- Sends POST request to Ollama server.
- Streams and parses response.
- Updates output and response time.

### `clear_input()`
- Clears the input text box.

### `exit_app()`
- Destroys the main window and exits the application.

## 6. **Error Handling**

- Empty prompt: Displays a warning message.
- Request failure: Catches exceptions and shows error message.
- JSON decode errors: Skips invalid lines silently.

## 7. **User Interface Design**

- Simple layout with clear labels.
- Scrollable output box for long responses.
- Buttons grouped for intuitive access.

## 8. **Future Enhancements**

- Add support for multiple models.
- Enable saving responses to a file.
- Add history of queries and responses.
- Improve UI with themes and layout options.
"""

# Save the content to a Markdown file
with open("Ollama_Query_Interface_Design_Document.md", "w") as f:
    f.write(design_doc_md)

print("Design document has been saved as 'Ollama_Query_Interface_Design_Document.md'.")

