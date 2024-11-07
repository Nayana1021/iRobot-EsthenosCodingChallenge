# iRobot-EsthenosCodingChallenge
<<<<<<< HEAD
=======

1. Open a terminal in the directory where the file is saved.
2. Run the program with: "python robot_movement.py"
3. Enter the command sequence for the robot as prompted (e.g., MSMMEMM).
4. The final position of the robot will be displayed on the terminal.
Assumptions:
Robot begins at position (0,0) facing South.
The grid dimensions are 5x4.
The robot ignores instructions that would take it out of bounds.
NOTE:
•	The code simulates the movement of a robot on a 5x4 grid, where the robot starts at position (0, 0) facing South. 
•	For each command, the robot updates its direction if it's a direction change. If it's a move command, it checks the current direction and moves one step in that direction, provided it doesn’t move out of bounds. If the move pushes the robot outside the grid, it stays in the same position. 
•	The command "MSMMEMM" results in the robot moving to (3, 2) facing East, as it can't move beyond the last row. When the same commands are extended to "MSMMEMMM", the robot successfully moves to (3, 3) because the additional 'M' command is valid within the grid bounds.
•	Hence the output Robot Location: (3, 2, 'E') for MSMMEMM and Robot Location: (3, 3, 'E') for MSMMEMMM
>>>>>>> master
