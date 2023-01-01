while True:
  # Get the user's input
  expression = input("Enter an expression: ")

  # Use the try-except block to handle any errors that might occur when evaluating the expression
  try:
    # Evaluate the expression and print the result
    result = eval(expression)
    print(result)
  except Exception as e:
    # Print an error message if an exception occurs
    print("Error:", e)
