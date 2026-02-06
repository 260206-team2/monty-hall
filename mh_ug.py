if switch:
    return alternative
  else:
    return chosen

print "\nMonty Hall problem simulation:"
print doors, "doors,", iterations, "iterations.\n"

print "Not switching allows you to win",
print sum(monty_hall(randrange(3), switch=False)
          for x in range(iterations)),
print "out of", iterations, "times."
print "Switching allows you to win",
print sum(monty_hall(randrange(3), switch=True)
          for x in range(iterations)),
print "out of", iterations, "times.\n"
