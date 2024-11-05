# Space exploration crew members' data, containing their names, missions, and roles
crew_data = "Neil,Armstrong,Apollo 11,C;Buzz,Aldrin,Apollo 11,P;Michael,Collins,Apollo 11,CM"

# TODO: Split the crew_data string into a list of individual crew member information using the appropriate delimiter
crew_list = crew_data.split(";")
for crew_member in crew_list:
    crew_member_info = crew_member.split(",")
    print(crew_member_info[0], crew_member_info[1], crew_member_info[2], crew_member_info[3])
# TODO: Iterate over the list of crew member data

    # TODO: For each member, split their data string using commas as delimiters

    # TODO: Print the crew member's details in a formatted string

# Expected output:
# Neil Armstrong Apollo 11 C
# Buzz Aldrin Apollo 11 P
# Michael Collins Apollo 11 CM