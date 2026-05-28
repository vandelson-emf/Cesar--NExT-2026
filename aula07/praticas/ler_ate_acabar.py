while True:
    try:
        _ = input()
        ...
    except (EOFError, KeyboardInterrupt):
        break
