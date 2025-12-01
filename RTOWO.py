import keyboard, random

period_emoticon = ['uwu',  '>w<', '^w^',  ':3', '>:3', 'nwn']
exclamation_emoticon = ['UwU', 'UWU', 'x3', ':3']
question_emoticon = ['owo', 'OWO', 'OwO', ':3c', '>:3c']

def intercept_keys(event):
    if event.event_type == 'down' and event.name in ['l', 'r']:
        keyboard.write('w')
        return False
    elif event.event_type == 'down' and event.name in ['L', 'R']:
        keyboard.write('W')
        return False
    elif event.event_type == 'down' and event.name in ['.', ',']:
        keyboard.write(f' {random.choice(period_emoticon)}{event.name}')
        return False
    elif event.event_type == 'down' and event.name == '!':
        keyboard.write(f' {random.choice(exclamation_emoticon)}{event.name}')
        return False
    elif event.event_type == 'down' and event.name == '?':
        keyboard.write(f' {random.choice(question_emoticon)}{event.name}')
        return False
    else:
        return True

keyboard.hook(intercept_keys, suppress=True)
print('Running, close the window to exit.')
keyboard.wait()
