astronauts_data = "Buzz Aldrin, 1930;Yuri Gagarin, 1934;Valentina Tereshkova, 1937"

# Splitting the string into a list of astronaut info and stripping any whitespace
astronauts_list = astronauts_data.split(";")
cleaned_astronauts = []

for astronaut in astronauts_list:
    name, year = astronaut.split(",")
    # cleaned_astronauts.append(name.strip() + " " + year.strip())  # Modify this line to use the join() method
    cleaned_astronauts.append(" ".join([name.strip(), year.strip()]))

print(cleaned_astronauts)  # ['Buzz Aldrin 1930', 'Yuri Gagarin 1934', 'Valentina Tereshkova 1937']