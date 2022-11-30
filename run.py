import solutions.day1

def print_usage():
    '''Output usage format'''
    print("Usage:")
    print("run.py [-h] day_number")

if __name__ == "__main__" :
    import sys
    if len(sys.argv) < 2:
        print("Error: wrong number of arguments")
        print_usage()
        sys.exit(1)
    if sys.argv[1] == '-h':
        print_usage()
        sys.exit(0)
    day = sys.argv[1]
    if not day.isdigit():
        print("Invalid day number")
        print_usage()
        sys.exit(1)
    try:
        
        exec(f"import solutions.day{day}; solutions.day{day}.day{day}()")
    except:
        print("Error")
        sys.exit(1)