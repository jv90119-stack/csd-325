# Jose Velazquez Saenz
# Module 1.3 Assignment


def beer_countdown(bottles):
    """
    Manages the countdown of bottles of beer on the wall.
    Counts backwards to 1 and displays the correct lyrics.
    """
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1

    # Special case for 1 bottle
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down and pass it around, 0 bottles of beer on the wall.\n")


def main():
    try:
        bottles = int(input("How many bottles of beer are on the wall? "))

        if bottles < 1:
            print("You need at least 1 bottle to sing the song!")
            return

        beer_countdown(bottles)
        print("Time to buy more beer.")

    except ValueError:
        print("Please enter a valid number.")

main()
