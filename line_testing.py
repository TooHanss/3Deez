import curses


def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1

    if dx > dy:
        err = dx / 2.0
        while x0 != x1:
            points.append((x0, y0))
            err -= dy
            if err < 0:
                y0 += sy
                err += dx
            x0 += sx
    else:
        err = dy / 2.0
        while y0 != y1:
            points.append((x0, y0))
            err -= dx
            if err < 0:
                x0 += sx
                err += dy
            y0 += sy

    points.append((x1, y1))  # Ensure the endpoint is included
    return points


def draw_line(stdscr, x0, y0, x1, y1):
    stdscr.clear()
    curses.curs_set(0)  # Hide cursor

    points = bresenham_line(x0, y0, x1, y1)
    for x, y in points:
        stdscr.addstr(y, x * 2, "██")  # Double up characters to make it more square

    stdscr.refresh()
    stdscr.getch()  # Wait for user input before exiting


if __name__ == "__main__":
    curses.wrapper(draw_line, 1, 30, 30, 30)
