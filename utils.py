from commands import Command


def check_something_not_none(something):
    return something is None


def execute(line) -> bool:
    raw_command = line.split()
    command = raw_command[0]
    args = raw_command[1:]

    if command == Command.EXIT.value:
        return 1
    print(command, args)
    return 0
