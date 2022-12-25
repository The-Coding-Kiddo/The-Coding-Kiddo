import time

def measure_writing_speed():
    # Prompt the user to start typing
    print("Start typing the following text:")
    text = "The quick brown fox jumps over the lazy dog."
    print(text)

    # Start the timer
    start_time = time.time()

    # Get the user's input and stop the timer
    typed_text = input()
    end_time = time.time()

    # Calculate the time taken to type the text
    time_taken = end_time - start_time

    # Calculate the typing speed in words per minute
    words = len(text.split())
    typing_speed = words / time_taken * 60

    # Print the results
    print(f"You typed the text in {time_taken:.2f} seconds.")
    print(f"Your typing speed is {typing_speed:.2f} words per minute.")

measure_writing_speed()
