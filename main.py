import pygame

import random

# Initialize Pygame

pygame.init()

# Set the window size and title

WINDOW_WIDTH = 600

WINDOW_HEIGHT = 400

WINDOW_TITLE = "Minesweeper"

# Create the game window

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption(WINDOW_TITLE)

# Create a Minesweeper grid

ROWS = 10

COLUMNS = 10

MINES = 10

# Create a grid with the specified number of rows and columns

grid = [[0 for i in range(COLUMNS)] for j in range(ROWS)]

# Add mines to the grid

for i in range(MINES):

  row = random.randint(0, ROWS - 1)

  column = random.randint(0, COLUMNS - 1)

  grid[row][column] = 1

# Calculate the number of adjacent mines for each cell

for row in range(ROWS):

  for column in range(COLUMNS):

    adjacent_mines = 0

    for i in range(-1, 2):

      for j in range(-1, 2):

        if i == 0 and j == 0:

          continue

        if row + i < 0 or row + i >= ROWS:

          continue

        if column + j < 0 or column + j >= COLUMNS:

          continue

        if grid[row + i][column + j] == 1:

          adjacent_mines += 1

    grid[row][column] = adjacent_mines
# Add graphics to the grid

cell_size = WINDOW_WIDTH // COLUMNS

for row in range(ROWS):

  for column in range(COLUMNS):

    x = column * cell_size

    y = row * cell_size

    pygame.draw.rect(screen, (255, 255, 255), (x, y, cell_size, cell_size))

    text = pygame.font.SysFont("Arial", 20).render(str(grid[row][column]), True, (0, 0, 0))

    screen.blit(text, (x + 5, y + 5))

# Handle user input

running = True

while running:

  # Get user input

  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:

      x, y = pygame.mouse.get_pos()

      row = y // cell_size

      column = x // cell_size

      if grid[row][column] == 1:

        # Detonate the mine

        for i in range(ROWS):

          for j in range(COLUMNS):

            if grid[i][j] == 1:

              screen.fill((255, 0, 0), (i * cell_size, j * cell_size, cell_size, cell_size))

        pygame.display.update()

        time.sleep(1)

        running = False

      elif grid[row][column] == 0:

        # Clear the cell

        screen.fill((255, 255, 255), (row * cell_size, column * cell_size, cell_size, cell_size))

        text = pygame.font.SysFont("Arial", 20).render(str(grid[row][column]), True, (0, 0, 0))

        screen.blit(text, (row * cell_size + 5, column * cell_size + 5))

        for i in range(-1, 2):

          for j in range(-1, 2):

            if i == 0 and j == 0:

              continue

            if row + i < 0 or row + i >= ROWS:

              continue

            if column + j < 0 or column + j >= COLUMNS:

              continue

            if grid[row + i][column + j] == 0:
clear_cell(row + i, column + j)
# Update the display

pygame.display.update()

# Implement game logic

def clear_cell(row, column):

  if grid[row][column] == 1:

    return

  grid[row][column] = 0

  for i in range(-1, 2):

    for j in range(-1, 2):

      if i == 0 and j == 0:

        continue

      if row + i < 0 or row + i >= ROWS:

        continue

      if column + j < 0 or column + j >= COLUMNS:

        continue

      clear_cell(row + i, column + j)

# Add game over screen

def game_over():

  screen.fill((255, 0, 0))

  text = pygame.font.SysFont("Arial", 40).render("Game Over!", True, (0, 0, 0))

  screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

  pygame.display.update()

  time.sleep(1)

# Add sound effects

pygame.mixer.init()

click_sound = pygame.mixer.Sound("click.wav")

mine_sound = pygame.mixer.Sound("mine.wav")

# Run the game

while running:

  # Get user input

  for event in pygame.event.get():

    if event.type == pygame.QUIT:

      running = False

    elif event.type == pygame.MOUSEBUTTONDOWN:

      x, y = pygame.mouse.get_pos()

      row = y // cell_size

      column = x // cell_size

      if grid[row][column] == 1:

        mine_sound.play()

        game_over()
        running = False

      elif grid[row][column] == 0:

        click_sound.play()

        clear_cell(row, column)

  # Update the display

  pygame.display.update()
  # Check if the game is won

def check_win():

  for row in range(ROWS):

    for column in range(COLUMNS):

      if grid[row][column] == -1:

        return False

  return True

# Check if the game is lost

def check_lose():

  for row in range(ROWS):

    for column in range(COLUMNS):

      if grid[row][column] == 1:

        return True

  return False

# Win screen

def win_screen():

  screen.fill((0, 255, 0))

  text = pygame.font.SysFont("Arial", 40).render("You win!", True, (0, 0, 0))

  screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))

  pygame.display.update()

  time.sleep(1)

# Restart the game

def restart():

  global grid, running

  grid = [[0 for i in range(COLUMNS)] for j in range(ROWS)]

  running = True

# Main loop

while True:

  # Run the game

  while running:

    # Get user input

    for event in pygame.event.get():

      if event.type == pygame.QUIT:

        break

      elif event.type == pygame.MOUSEBUTTONDOWN:

        x, y = pygame.mouse.get_pos()

        row = y // cell_size

        column = x // cell_size

        if grid[row][column] == 1:

          mine_sound.play()

          game_over()

          break
          elif grid[row][column] == 0:

          click_sound.play()

          clear_cell(row, column)

    # Update the display

    pygame.display.update()

    # Check if the game is won

    if check_win():

      win_screen()

      restart()

      break

    # Check if the game is lost

    if check_lose():

      game_over()

      break

  # Restart the game

  restart()

# Quit Pygame

pygame.quit()
           
