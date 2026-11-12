# Creating a function

def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!
print(greet("Bob"))    # Output: Hello, Bob!

def add(a, b):
    return a + b

# Calling the function
print(add(5, 3))  # Output: 8
print(add(10, 20))  # Output: 30



def check_agent_status(memory_available, is_connected):
    if memory_available >= 16 and is_connected == True:
        return "Agent is ready to Deploy"
    else :
        return "Agent Needs Maintenance"

print(check_agent_status(16, True))  # Output: "Agent is ready to Deploy"

