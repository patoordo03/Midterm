s = "https://www.google.com"
start = 0
while True:
    start = s.find("http://", start)
    if start == -1:
        break
    end = s.find(" ", start)
    if end == -1:
        print(s[start:])
        break
    print(s[start:end])
    start = end

# Example:
if (s):
    print(f"{s} is a valid URL.")
else:
    print(f"{s} is not a valid URL.")
