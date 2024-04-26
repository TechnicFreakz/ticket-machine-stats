import pathlib

raw_log_dir = pathlib.Path("logs_raw")
filter_log_dir = pathlib.Path("logs_rewards_only")


common = [
    "sky island",
    "grass block",
    "nether portal",
    "fireballs",
    "sniper",
    "diamonds",
    "diamond hoe",
    "groopo",
    "missing bed",
    "alchemy",
    "shears",
    "alex",
    "crossed swords",
    "zombie",
    "creeper",
    "guardian",
    "fishing rod",
    "housing",
    "ender pearl",
    "the pit",
    "golden apple",
    "bridge egg",
    "dante",
    "hypixel server",
    "the delivery man",
    "hot air balloon",
    "steve",
    "sheep",
    "don espresso",
    "sandman",
]
rare = [
    "tic tac toe",
    "bed defense",
    "top killer",
    "iron punch",
    "iron rose",
    "emeralds",
    "tnt",
    "hypixel",
    "enderman",
    "rezzus",
    "blitz star",
    "hammer vs heatwave",
    "ratman in the city",
]
legendary = [
    "magma boss",
    "cerberus",
    "legacy statues",
    "bed destroyer",
    "knockback",
    "dragon slayer",
    "build battle",
    "kart racing",
    "executives meeting",
]


def filter_logs():
    for log in raw_log_dir.iterdir():
        filename = log.name
        target_file = filter_log_dir / filename
        with open(log, "r") as reader:
            with open(target_file, "w") as writer:
                for line in reader.readlines():
                    if line[0] != "[":
                        continue
                    line = line[22:]
                    if line[:8] == "Obtained":
                        line = line[9:]
                    line = line.replace(",", "")
                    line = line.replace("!", "")
                    line = line.replace(" Bed Wars", "")
                    line = line.replace(" Slumber", "")
                    writer.write(line)
                writer.write("\n")


def parse(tokens, tickets, experience, figurines, other):
    for log in filter_log_dir.iterdir():
        with open(log, "r") as reader:
            for line in reader.readlines():
                if line[-7:] == "Tokens\n":
                    tokens.append(int(line.replace(" Tokens", "")))
                elif line[-8:] == "Tickets\n":
                    tickets.append(int(line.replace(" Tickets", "")))
                elif line[-11:] == "Experience\n":
                    experience.append(int(line.replace(" Experience", "")))
                elif line[-9:] == "Figurine\n":
                    figurines.append(line.replace(" Figurine\n", ""))
                else:
                    other.append(line[:-1])
