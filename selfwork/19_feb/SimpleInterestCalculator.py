p_input = input("Enter principal: ")
v = 1
for ch in p_input:
    v = v * ((ch >= '0') * (ch <= '9'))
p = int(p_input) * v

r_input = input("Enter rate (%): ")
v = 1
for ch in r_input:
    v = v * ((ch >= '0') * (ch <= '9'))
r = int(r_input) * v

t_input = input("Enter time (years): ")
v = 1
for ch in t_input:
    v = v * ((ch >= '0') * (ch <= '9'))
t = int(t_input) * v

interest = p * r * t / 100
print("Simple Interest =", interest)
