from functools import wraps


def log(filename: str = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} {result}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{message}\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} {args} {kwargs} {e}"
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(f"{message}\n")
                else:
                    print(message)
            return None

        return wrapper

    return decorator
