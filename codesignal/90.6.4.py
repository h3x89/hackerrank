# This function processes astronaut names and planets from a string 
# then prints out a neat summary of who is exploring which planet.
def process_astronaut_data(data):
    # Remove whitespace from the start and end of the string.
    data = data.strip()
    astronaut_details = data.split(';')
    for detail in astronaut_details:
        # TODO: Extract the astronaut name and explored planet from the detail, strip away the whitespace.
        detail = detail.strip()
        astronaut, planet = detail.split('-')
        astronaut = astronaut.strip()
        planet = planet.strip()
        print(f"Astronaut {astronaut} is exploring {planet}.")
        # TODO: Print the statement in the format "Astronaut [name] is exploring [planet]."
        
# String containing astronaut names and planets, separated by semicolons.
# Each astronaut-planet pair is separated by a dash.
astronaut_data = "    Neil-Mars; Buzz-Jupiter; Sally-Venus    "
process_astronaut_data(astronaut_data)