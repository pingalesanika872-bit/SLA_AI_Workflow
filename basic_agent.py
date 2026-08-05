# basic_agent.py
# A simple Python agent that interacts with the user via the console.

# Print a greeting to the user when the program starts.
print('Hello! I am your basic Python agent.')

# Ask the user for their name and store it in a variable.
user_name = input('What is your name? ')

# Use the user's name in a personalized follow-up message.
print(f'Nice to meet you, {user_name}!')

# Ask the user how the agent can help and save their response.
user_request = input('How can I help you today? ')

# Convert the user's input to lowercase so the comparison is case-insensitive.
user_request_lower = user_request.lower()

# Use if-elif statements to respond to recognized commands.
if 'hello' in user_request_lower:
    print('Hello! I hope you are having a great day.')
elif 'time' in user_request_lower:
    # Import datetime only when we need it for the time response.
    from datetime import datetime
    current_time = datetime.now().strftime('%H:%M:%S')
    print(f'The current time is {current_time}.')
elif 'bye' in user_request_lower:
    print('Goodbye! Have a wonderful day.')
else:
    # Respond with a default message for any other input.
    print('I am sorry, I can only respond to hello, time, or bye.')
