from functools import wraps

def lazy(func):
  """
  This function creates a lazy decorator.

  Args:
      func: The function to be decorated.

  Returns:
      A wrapper function that only evaluates the decorated function
      when its result is needed.
  """
  @wraps(func)
  def wrapper(*args, **kwargs):
    """
    This wrapper function stores the arguments and defers the execution 
    of the decorated function until the result is needed.

    Args:
        *args: Arguments to be passed to the decorated function.
        **kwargs: Keyword arguments to be passed to the decorated function.

    Returns:
        The result of the decorated function.
    """
    def evaluation():
      return func(*args, **kwargs)
    return evaluation
  return wrapper

@lazy
def calculate_factorial(n):
  """
  This function calculates the factorial of a number.

  Args:
      n: The number for which to calculate the factorial.

  Returns:
      The factorial of n.
  """
  if n == 0:
    return 1
  else:
    return n * calculate_factorial(n-1)

if __name__ == "__main__":
    inputNumber = int(input("Enter a number: "))
    result = calculate_factorial(inputNumber)
    print(result)
