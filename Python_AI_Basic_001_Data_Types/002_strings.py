print("Empty string", str())
print("String repr",str(["A","h"]))
print("String copy", str("MJ"))

#slicing strings
def practice(stringTest):
    str = stringTest[4:6]
    print(str)

def practice2(stringTest):
    str = stringTest[1:10]
    print(str)

practice("This is the first slicing")
practice2("This is the second slicing")

print(
    "Hi \"Python\""
)

encode = '\N{euro sign} \u20AC \U000020AC'
print(encode)