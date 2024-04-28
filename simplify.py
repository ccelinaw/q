def simplify(row_number):
  '''
  Simplifies larger numbers by turning them into billions, millions or thousands for readability in comparisons

  Parameters
  ----------
  row_number: integer
      The row number (and/or index) of the value in the dataset

  Returns
  -------
  string
      The simplified number alongside the abbreviated denomination (B, M, or K)
  '''
  # converts to billions
  if row_number >= 1e9:
    quotient = (row_number // 1e9)
    remainder = float((row_number % 1e9) / 1e9)
    simplified_num = f'{round(quotient + remainder, 3)}B'
  # converts to millions
  elif (row_number >= 1e6):
    quotient = (row_number // 1e6)
    remainder = float((row_number % 1e6) / 1e6)
    simplified_num = f'{round(quotient + remainder, 3)}M'
  # converts to thousands
  elif (int(row_number >= 1e3)):
    quotient = (row_number // 1e3)
    remainder = float((row_number % 1e3) / 1e3)
    simplified_num = f'{round(quotient + remainder, 3)}K'
  else:
    simplified_num = str(row_number)
  return simplified_num
