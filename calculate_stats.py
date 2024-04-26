import pathlib
import util


tokens = []
tickets = []
experience = []
figurines = []
other = []

util.filter_logs(tokens, tickets, experience, figurines, other)
util.parse()
print("Total Stats:")
print(
    "You gambled "
    + (str(len(tokens) + len(tickets) + len(experience) + len(figurines) + len(other)))
    + " times."
)
print(
    "You got Tokens "
    + str(len(tokens))
    + " times for a total of "
    + str(sum(tokens))
    + " Tokens."
)
print(
    "You got Tickets "
    + str(len(tickets))
    + " times for a total of "
    + str(sum(tickets))
    + " Tickets. Subtracting the used tickets results in "
    + str((sum(tickets) - 75 * len(tickets)))
    + " Tickets gained."
)
print(
    "You got Experience "
    + str(len(experience))
    + " times for a total of "
    + str(sum(experience))
    + " Experience."
)
print(
    "You got Figurines "
    + str(len(figurines))
    + " times with "
    + str(len(list(filter(lambda name: name.lower() in util.common, figurines))))
    + " commons, "
    + str(len(list(filter(lambda name: name.lower() in util.rare, figurines))))
    + " rares and "
    + str(len(list(filter(lambda name: name.lower() in util.legendary, figurines))))
    + " legendaries."
)
