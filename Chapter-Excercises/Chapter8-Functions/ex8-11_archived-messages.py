queue = [
    'One',
    'Two',
    'Three',
    'Four',
]

complete = []

def show_messages(queue, complete):
    while queue:
        message = queue.pop()
        print(f"Message: {message}")
        complete.append(message)

# Makes no changes to the queue list
show_messages(queue[:], complete)
print()
print(f"Queue: {queue}")
print(f"Complete: {complete}")