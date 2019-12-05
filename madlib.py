print('*'*41)
print('** Hello!! Welcome to my Madlib Game!! **')
print('**                                     **')
print('** To play, just follow the prompts!   **')
print('** Submit anwsers for each question    **')
print('*'*41)

def template():
    with open('madlib_template.txt') as f:
        template = f.read()
        print(template)
        return template

user_inputs = []

user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter a first name - ')))
user_inputs.append(str(input('enter a past tense verb - ')))
user_inputs.append(str(input('enter a first name - ')))
user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter plural noun - ')))
user_inputs.append(str(input('enter name of a small animal - ')))
user_inputs.append(str(input('enter name of alarge animal - ')))
user_inputs.append(str(input('enter a womans name - ')))
user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter plural noun - ')))
user_inputs.append(str(input('enter adjective - ')))
user_inputs.append(str(input('enter plural noun - ')))
user_inputs.append(str(input('enter a number 1 - 50 - ')))
user_inputs.append(str(input('enter a first name - ')))
user_inputs.append(str(input('enter a number - ')))
user_inputs.append(str(input('enter a plural noun - ')))
user_inputs.append(str(input('enter a number - ')))
user_inputs.append(str(input('enter a plural noun - ')))


def append_to_tempate():
    with open('madlib.txt', 'w') as f:
        temp = template()
        filled_template = temp.format(*user_inputs)
        f.write(filled_template)
        print(filled_template)

append_to_tempate()