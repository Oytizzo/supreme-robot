with open("math.txt", "r") as math_fp:
    text_lines = math_fp.read().splitlines()

right_count = 0
wrong_count = 0

result = []
for item in text_lines:
    x = item.partition("=")
    if eval(x[0]) == eval(x[2]):
        result.append(f"v {x[0]}{x[1]}{x[2]}")
        right_count += 1
    elif eval(x[0]) != eval(x[2]):
        result.append(f"x {x[0]}{x[1]}{x[2]}\t=>\t{eval(x[0])}")
        wrong_count += 1

result.append("="*20)
result.append(f"Right Count: {right_count}\nWrong Count: {wrong_count}")
result.append("="*20)
with open("result_math.txt", "w") as result_math_fp:
    result_math_fp.write('\n'.join(result))

print(text_lines)
print(result)
print(f"Right Count: {right_count}\nWrong Count: {wrong_count}")
