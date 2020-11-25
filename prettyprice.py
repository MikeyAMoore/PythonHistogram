def pretty_price(total_price, taxes):
  if isinstance(taxes, int):
    taxes = taxes * .01

  return int(total_price) + taxes


print(pretty_price(3.20, 99))
print(pretty_price(3.20, .99))