import logging

# Configure logging to write messages to a log file.
logging.basicConfig(
    level=logging.INFO,                # Record INFO level and above.
    filename="app_errors.log",         # Log file where messages are stored.
    filemode="a",                      # Append mode to keep existing logs.
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_greeting(file_path):
    """
    Attempts to load a greeting message from a text file.
    
    If the file does not exist or an error occurs:
      - Logs the error to 'app_errors.log'.
      - Uses a default greeting.
    
    Regardless of success or failure, writes the greeting to 'greeting_output.txt'.
    
    Returns the greeting message for use in the application.
    """
    try:
        # Attempt to open and read the greeting file.
        with open(file_path, "r") as file:
            greeting = file.read().strip()
    except FileNotFoundError as e:
        logging.error(f"Greeting file not found: {file_path}. Error: {e}")
        greeting = "Hello, welcome!"  # Use default greeting.
    except Exception as e:
        logging.error(f"Unexpected error when loading greeting: {e}")
        greeting = "Hello, welcome!"
    else:
        logging.info(f"Greeting loaded successfully from {file_path}.")
    finally:
        logging.info("Finished attempting to load greeting.")
    
    # Write the greeting message to 'greeting_output.txt' regardless of errors.
    try:
        with open("greeting_output.txt", "w") as output_file:
            output_file.write(greeting)
        logging.info("Greeting written to 'greeting_output.txt'.")
    except Exception as e:
        logging.error(f"Error writing greeting to output file: {e}")
    
    return greeting

# Example usage in the application:
greeting_message = load_greeting("greeting.txt")
# The variable 'greeting_message' now holds the greeting (from the file or the default)
# and the greeting is written to 'greeting_output.txt'.

