import os


def main():
    x = 0.25


    for i in range(100):
        #print(f"Iteration: {i}, x: {round(x, 4)}, next x: {round(16 * (x - 3/16), 4)} (actual x: {x})")

        print("Iteration: %d: x: %.4f, next x: %.4f" % (i, x, 16 * (x - 3/16)))
        x = 16 * (x - 3.75/16)

if __name__ == "__main__":
    main()