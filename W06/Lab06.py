# 1. Name:
#      Nathan Yochim
# 2. Assignment Name:
#      Lab 06: Image Compression
# 3. Assignment Description:
#      This program reads a compressed image description from a JSON file and prints the decompressed image to the screen.
# 4. Algorithmic Efficiency
#      The image decompression is O(num_rows * num_columns) because each output pixel is produced once. The row and run-length loops visit every character in the final image one time, so the work grows linearly with the size of the image. File reading and input/output are not included in that efficiency claim.
# 5. What was the hardest part? Be as specific as possible.
#      The hardest part was making sure the compressed row data expanded in the correct order. It took some care to match the alternating space and hash pattern so the output image would line up exactly with the example.
# 6. How long did it take for you to complete the assignment?
#      About 1.5 hours including reading the assignment and writing the code. I helped to have my pseudocode prepared for this assignment.

import json
import os


def load_image(filename):
    candidates = [filename]
    if not os.path.isabs(filename):
        candidates.append(os.path.join(os.path.dirname(__file__), filename))

    for path in candidates:
        try:
            with open(path, "r") as file:
                image = json.load(file)
            return image.get("num_rows"), image.get("num_columns"), image.get("data")
        except FileNotFoundError:
            continue
        except json.JSONDecodeError:
            print(f"Error: {path} does not contain valid JSON data.")
            return None, None, None

    print(f"Unable to open file {filename}.")
    return None, None, None


def decompress_image(data, num_rows, num_columns):
    grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

    for col in range(num_columns):
        if col >= len(data):
            break

        runs = data[col]
        row = 0
        is_filled = True

        for length in runs:
            for _ in range(length):
                if row >= num_rows:
                    break

                grid[row][col] = 1 if is_filled else 0
                row += 1

            is_filled = not is_filled

    return grid


def print_image(grid):
    for row in grid:
        line = ""
        for cell in row:
            if cell == 1:
                line += "#"
            else:
                line += " "
        print(line)


def main():
    filename = input("Please select a filename: ")
    num_rows, num_columns, data = load_image(filename)

    if num_rows is None or num_columns is None or data is None:
        return

    grid = decompress_image(data, num_rows, num_columns)
    print_image(grid)


if __name__ == "__main__":
    main()