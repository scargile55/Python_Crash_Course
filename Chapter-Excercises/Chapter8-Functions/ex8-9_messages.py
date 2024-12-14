def show_messages(*texts):
    for text in texts:
        print(f"{text.title()}")

show_messages('hello', 'see you later', 'how are you')