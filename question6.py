# code showing list is mutable
list_mutable = [1, 2, 3, 4, 5]
list_mutable[2] = 10
list_mutable.append(6)
print(list_mutable)

# code showing string is immutable
string_immutable = "Patricio" # trying to modify gives an error

string_new = string_immutable + " Ordonez" # so you can make a copy instead, and add it to the string

print(string_new)