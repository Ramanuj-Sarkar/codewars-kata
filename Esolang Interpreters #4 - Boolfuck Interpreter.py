def boolfuck(code, input_string=""):
    pointer = 0     # for instructions
    location = 0    # for tape
    tape = [0]
    bit_input = ''
    bit_output = ''
    output = ''
    
    corresponding_bracket = {}       # dictionary where the values are the corresponding bracket positions of the keys
    bracket_stack = []     # acts as a stack for the last bracket
    
    for num, char in enumerate(code):
        if char == '[':
            bracket_stack.append(num)
        elif char == ']':
            assert len(bracket_stack) > 0, 'unmatched ]'
            corresponding_bracket[num] = bracket_stack[-1]
            corresponding_bracket[bracket_stack[-1]] = num
            bracket_stack.pop()
    assert len(bracket_stack) == 0, 'unmatched ['
    
    while pointer < len(code):
        if code[pointer] == '>':
            location += 1
            if location == len(tape):
                tape.append(0)
        elif code[pointer] == '<':
            if location == 0:
                tape = [0] + tape
            else:
                location -= 1
        elif code[pointer] == '+':
            tape[location] = (tape[location] + 1) % 2
        elif code[pointer] == ';':
            bit_output += str(tape[location])
            if len(bit_output) == 8:
                decimal = 0
                for digit in range(8):
                    decimal += int(bit_output[digit]) * (2**digit)
                output += chr(decimal)
                bit_output = ''
        elif code[pointer] == ',':
            if bit_input == '' and input_string == '':
                bit_input = '00000000'
            if bit_input == '':
                decimal = ord(input_string[0])
                for digit in range(8):
                    bit_input += str(decimal // 2**digit % 2)
                input_string = input_string[1:]
            tape[location] = int(bit_input[0])
            bit_input = bit_input[1:]
        elif code[pointer] == '[':
            if tape[location] == 0:
                pointer = corresponding_bracket[pointer]
        elif code[pointer] == ']':
            if tape[location] == 1:
                pointer = corresponding_bracket[pointer]
        pointer += 1
    if bit_output != '':
        decimal = 0
        for digit in range(len(bit_output)):
            decimal += int(bit_output[digit]) * (2**digit)
        output += chr(decimal)
        bit_output = ''
    return output
