import random

def interpret(code):
    stack = []
    push_here = ''
    y = 0
    x = 0
    
    direction = '>'
    direction_string = 'v<^>'
    string_mode = False
    
    running = code.split('\n')
    
    char = running[y][x]
    while char != '@':
        if char == '"':
            string_mode = not string_mode
        
        elif string_mode:
            stack.append(ord(char))
        
        elif ord('0') <= ord(char) <= ord('9'):
            stack.append(int(char))
        
        elif char in 'v<^>?:': # don't pop any values
            if char in direction_string:
                direction = char
            elif char == '?':
                direction = direction_string[random.randint(0,3)]
            elif char == ':':
                if len(stack) == 0:
                    stack.append(0)
                stack.append(stack[-1])
        
        elif char == '#':
            if direction == 'v':
                y = (y + 1) % len(running)
            elif direction == '<':
                x = (x - 1) % len(running[y])
            elif direction == '^':
                y = (y - 1) % len(running)
            else:
                x = (x + 1) % len(running[y])
        
        
        
        elif char in '!_|$.,': # pop one value
            result = stack.pop()
            if char == '!':
                stack.append(1 if result == 0 else 0)
            elif char == '_':
                direction = ('>' if result == 0 else '<')
            elif char == '|':
                direction = ('v' if result == 0 else '^')
            if char == '.':
                push_here += str(result)
            elif char == ',':
                push_here += ('' if result == 0 else chr(result))
        
        elif char in '+-*/%`g': # pop two values, push one value
            a = stack.pop()
            b = stack.pop()
            
            if char == '+':
                result = b+a
            elif char == '-':
                result = b-a
            elif char == '*':
                result = b*a
            elif char == '/':
                if a == 0:
                    result = 0
                else:
                    result = b//a
            elif char == '%':
                if a == 0:
                    result = 0
                else:
                    result = b%a
            elif char == '`':
                result = int(b>a)
            elif char == 'g':
                if a >= len(running) or b >= len(running[a]):
                    result = 0
                else:
                    result = ord(running[a][b])
            
            stack.append(result)
        
        elif char == '\\':
            a = stack.pop()
            if len(stack) == 0:
                b = 0
            else:
                b = stack.pop()
            stack.append(a)
            stack.append(b)
        
        elif char == 'p':
            py = stack.pop()
            assign_row = running[py]
            px = stack.pop()
            pv = chr(stack.pop())
            assign_row = assign_row[:px] + pv + assign_row[px+1:]
            running[py] = assign_row
            
        
        if direction == 'v':
            y = (y + 1) % len(running)
        elif direction == '<':
            x = (x - 1) % len(running[y])
        elif direction == '^':
            y = (y - 1) % len(running)
        else:
            x = (x + 1) % len(running[y])
        
        char = running[y][x]
    return push_here
