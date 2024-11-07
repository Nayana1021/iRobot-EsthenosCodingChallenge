class Robot:
    def __init__(self):
        self.position = (0, 0)        # Starting at (0,0)
        self.direction = 'S'          # Starting direction
        self.max_row, self.max_col = 4, 3  # Grid boundaries
        # Direction mapping with (row_change, col_change)
        self.directions = {'N': (-1, 0), 'S': (1, 0), 'E': (0, 1), 'W': (0, -1)}

    def execute_commands(self, commands):
        for command in commands:
            if command in self.directions and command != self.direction:
                self.direction = command   # Changing direction if different
            elif command == 'M':  # Move command
                # Calculating next position
                new_row = self.position[0] + self.directions[self.direction][0]
                new_col = self.position[1] + self.directions[self.direction][1]
                # Updating position only if within grid boundaries
                if 0 <= new_row <= self.max_row and 0 <= new_col <= self.max_col:
                    self.position = (new_row, new_col)
        return (*self.position, self.direction)  # Unpacking tuple for cleaner return

# Main function
def main():
    commands = input("please enter the command sequence: ").strip()
    final_position = Robot().execute_commands(commands)
    print(f"Robot Location: {final_position}")

if __name__ == "__main__":
    main()

'''After implementing the code, I noticed that for the command "MSMMEMM", the robot's final position
was (3, 2, 'E') instead of (3, 3, 'E'). The robot was not moving beyond the grid boundaries as 
expected, so I searched on ChatGPT for an explanation and found that the robot should remain stationary
if a move command causes it to go out of bounds. The solution was to check for the grid boundaries before
updating the robot's position, ensuring it doesn't exceed the grid's limits.'''