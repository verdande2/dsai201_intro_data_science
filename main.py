import pandas as pd

def main():
    print("Testing pandas import...")
    # A is first column, B is second column
    test_df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    print(test_df)

if __name__ == "__main__":
    main()
