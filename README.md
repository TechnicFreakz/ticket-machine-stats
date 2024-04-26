# How to use

## Collect minecraft logs

- In Minecraft Launcher go to settings and under **Minecraft: Java Edition Settings** tick the box next to *Open output log when Minecraft: Java Edition starts*.
- Go to a calm lobby in Hypixel Bedwars.
- In the **Filter** field of the log window, insert "ticket reward". You should now only see the lines telling you which rewards you got.
- Use the ticket machine.
- Copy the logs into a text-file.

## Clone this repository

If you do not know how to do this, take a look [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Execute

- in the folder *ticket machine stats* create 2 new folders called *logs\_raw* and *logs\_rewards\_only*.
- Move your text file from earlier into *logs\_raw*. You can put multiple files in here to get the combined stats.
- run ```python calculate_stats.py``` inside the folder *ticket machine stats*.
- If you run it multiple times, make sure to delete the contents of *logs\_rewards\_only* first.
- Enjoy the stats!
