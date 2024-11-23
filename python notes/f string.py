letter = "Hey my name is {1} and and I am from {0}"
country = "India"
name="nikhil"

print(letter.format(country, name))
print(f"Hey my name is {name} and and I am from {country}")

txt = "for only {price:.2f} dollors!"
print(txt.format(price = 49.099))
print(f"{2*40}")
print(f"Hey my name is {{name}} and and I am from {{country}}")
