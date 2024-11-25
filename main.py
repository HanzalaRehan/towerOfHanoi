"""
Author(s): 1. Hanzala B. Rehan
Description: A Tower of Hanoi solver using recursion, visualized using Pygame.
Date created: November 22nd, 2024
Date last modified: November 23rd, 2024
"""

import pygame
import time

# Pygame window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
DISK_HEIGHT = 20
FPS = 30

# Colors
BACKGROUND_COLOR = (20, 20, 20)
ROD_COLOR = (200, 200, 200)
DISK_COLORS = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 0, 255), (0, 255, 255), (200, 100, 50)
]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
clock = pygame.time.Clock()


# Draw function
def draw_rods(disks):
    """
    Desc: Draws rods and disks based on the current state.
    Parameters:
        disks (list[list[int]]): Current state of rods and disks.
    """
    screen.fill(BACKGROUND_COLOR)

    # Rod positions
    rod_positions = [SCREEN_WIDTH // 4, SCREEN_WIDTH // 2, 3 * SCREEN_WIDTH // 4]
    rod_width = 10
    rod_height = SCREEN_HEIGHT // 2

    # Draw rods
    for rod_x in rod_positions:
        pygame.draw.rect(screen, ROD_COLOR,
                         (rod_x - rod_width // 2, SCREEN_HEIGHT - rod_height, rod_width, rod_height))

    # Draw disks
    for rod_idx, rod in enumerate(disks):
        rod_x = rod_positions[rod_idx]
        for disk_idx, disk in enumerate(rod):
            disk_width = disk * 20
            disk_x = rod_x - disk_width // 2
            disk_y = SCREEN_HEIGHT - rod_height - (disk_idx + 1) * DISK_HEIGHT
            pygame.draw.rect(screen, DISK_COLORS[disk % len(DISK_COLORS)],
                             (disk_x, disk_y, disk_width, DISK_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)


# Recursive Tower of Hanoi solver
def tower_of_hanoi(n, source, target, auxiliary, disks):
    """
    Desc: Recursive Tower of Hanoi solver.
    Parameters:
        n (int): Number of disks to move.
        source (int): Index of source rod.
        target (int): Index of target rod.
        auxiliary (int): Index of auxiliary rod.
        disks (list[list[int]]): Current state of rods and disks.
    """
    if n == 1:
        # Move a single disk
        disk = disks[source].pop()
        disks[target].append(disk)
        draw_rods(disks)
        time.sleep(0.5)
    else:
        # Move n-1 disks to auxiliary rod
        tower_of_hanoi(n - 1, source, auxiliary, target, disks)
        # Move the nth disk to target rod
        tower_of_hanoi(1, source, target, auxiliary, disks)
        # Move the n-1 disks from auxiliary rod to target rod
        tower_of_hanoi(n - 1, auxiliary, target, source, disks)


# Main function
def main():
    """
    Desc: Initializes the Tower of Hanoi puzzle and starts the visualization.
    """
    num_disks = 3  # Change this to increase/decrease the number of disks
    disks = [list(range(num_disks, 0, -1)), [], []]
    draw_rods(disks)
    time.sleep(1)

    running = True
    hanoi_done = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not hanoi_done:
            tower_of_hanoi(num_disks, 0, 2, 1, disks)
            hanoi_done = True
            time.sleep(2)

    pygame.quit()


# Run the program
if __name__ == "__main__":
    main()
