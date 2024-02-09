
import random

def dice_roll(dice_specification):
    # Split the input string into number of dice and type of dice
    num_dice, dice_type = map(int, dice_specification.split("D"))
    
    # Roll the dice and sum the results
    total = sum(random.randint(1, dice_type) for _ in range(num_dice))
    
    return total

# Example usage:
if __name__ == "__main__":
    result1 = dice_roll("1D6")
    print("Result of rolling 1D6:", result1)

    result2 = dice_roll("2D10")
    print("Result of rolling 2D10:", result2)