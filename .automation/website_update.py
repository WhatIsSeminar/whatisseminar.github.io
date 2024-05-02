"""
@author: Nicolas Weiss
@date: 2024-04-30

@goal: Update website with the information on the upcoming talk, guiding through the update.

@python-version: 3  

@tested: Only tested on linux. 

@run: python3 website_update.py

Remark on handling cases: 
-- On the user input side, we will make for now assertions, to ensure it works, and abort otherwise.
"""

from os import path
import re




# Maps:
maps = {
    "TU" : "tu_map.jpg",
    "HU" : "hu_map_named.jpg",
    "FU" : "fu_map_numbers.jpg",
}


# Locations:  (map specficied according to above dictionary. or None)

locations = [
    {"uni": "HU Berlin", "building" :"Erwin-Schrödinger-Zentrum",                "map" : maps["HU"]},

    {"uni": "TU Berlin", "building" : "Eugene-Paul-Wigner-Gebäude (EW)",          "map" : maps["TU"]},

    {"uni": "FU Berlin", "building" : "Arnimallee 3",                             "map" : maps["FU"]},
    {"uni": "FU Berlin", "building" : "Takustraße 9 (T9)",                        "map" : maps["FU"]},
    {"uni": "FU Berlin", "building" : "ZIB",                                      "map" : maps["FU"]},
]



##### Format (regex) #######

date_format = r"\d{4}/\d{2}/\d{2}$" # i.e. '2024/05/02'  (2nd of May, 2024)

title_whatis = r"What is\.\.\. .*\?$"   # Start with 'What is... ' and end with '?'
title_whatare = r"What are\.\.\. .*\?$"   # So needs to start with: 'What are... ' and end with '?' 


#######################

def prompt_loop_read_data(prompt, condition_fn=None, request_confirm=True, default=None):
    response = ""
    confirmed = False

    while not confirmed:
        response = input(prompt).strip()

        if default != None and response == "":
            return default

        if condition_fn != None:
            if not condition_fn(response):
                print("Format not met.")
                continue

        if request_confirm:
            print("Input: {}".format(response))
            confirm_input = input("Confirm (y/n)? [y] ").strip()
            confirmed = confirm_input == "y" or confirm_input == ""
        else:
            confirmed = True 
    
    return response


def collect_information():
    """
    Collects: Title, Abstract, Speaker, Location, Livestream info, date. 
    """

    print("--- Let us begin by collecting metadata about the talk.")

    date = prompt_loop_read_data("Date (yyyy/mm/dd): ", condition_fn = lambda s : re.match(date_format, s) and len(s) == 10)

    time = prompt_loop_read_data("Time: [13:00 s.t.] ", default="13:00 s.t.")

    location_num = int(prompt_loop_read_data("Please specify the location from the list: \n{} \n--> Location Number: ".format("\n".join([str(i) + " - " + loc["uni"] + ", " + loc["building"] for i, loc in enumerate(locations)])),
                                             condition_fn=lambda s : s.isnumeric() and int(s) in range(len(locations))))
    location = locations[location_num]

    room = prompt_loop_read_data("Please specify the room: ")

    live_streamed = "y" == prompt_loop_read_data("Will it be livestreamed? (y/n) ",
                                             condition_fn=lambda s : s in ["y", "n"])
    

    print("\n--- We will now collect the details about the speaker and talk. ---\n ")


    speaker = prompt_loop_read_data("Speaker's name: ")

    affiliation = prompt_loop_read_data("Affiliation: ")

    title = prompt_loop_read_data("Title (either 'What is... ' + smth + '?' or 'What are... ' + smth + '?', e.g. 'What is... a square?' or 'What are... squares?')\n--> ",
                                  condition_fn=lambda s : re.match(title_whatare, s) or re.match(title_whatis, s))

    abstract = prompt_loop_read_data("Abstract (1 line, no new-line character): ")


    print("\n--- We will now collect the details about the speaker and talk. ---\n ")

    before_mathplus = "y" == prompt_loop_read_data("Is there a MATH+ talk afterwards (y/n) ?  [y]", condition_fn=lambda s : s in ["y", "n"], default="y")
    mathplus_speaker = None
    mathplus_poster_link = None

    if before_mathplus:
        mathplus_speaker = prompt_loop_read_data("Who is the speaker of the MATH+ talk? ")
        mathplus_poster_link = prompt_loop_read_data("Please enter the poster link to the MATH+ talk, \n(i.e 'https://www.math-berlin.de/images/poster/MATHFriday_Sahasrabudhe.pdf'):\n--> ")
    

    print("\n--- This is a summary of the data: ---\n")

    print("Date: {}".format(date))
    print("Time: {}".format(time))
    print("Location: {}".format(location["uni"] + ", " + location["building"]))
    print("Room: {}".format(room))
    print("Live-streamed: {}\n".format(live_streamed))

    print("Speaker: {}".format(speaker))
    print("Affiliation: {}".format(affiliation))
    print("Title: {}".format(title))
    print("Abstract: {}\n".format(abstract))

    print("Before MATH+: {}".format(before_mathplus))
    print("MATH+ Speaker: {}".format(mathplus_speaker))
    print("MATH+ Poster: {}\n".format(mathplus_poster_link))

    confirmed = "y" == prompt_loop_read_data("Confirm? (y/n) [y] ", condition_fn=lambda s : s in ["y", "n"], default="y")

    if confirmed:
        return {"date":date, "time":time, "location":location, "room":room, "live-streamed":live_streamed, 
                "speaker":speaker, "affiliation":affiliation, "title":title, "abstract":abstract,
                "before_mathplus":before_mathplus, "mathplus_speaker":mathplus_speaker, "mathplus_poster_link":mathplus_poster_link}
    else:
        return collect_information()


def update_line(line, talk_data):
    """Takes a line from the template file and replace all placeholders of the form $$xyz$$ 
        according to the talk_data dictionary."""

    updated_line = line

    for key in talk_data.keys():
        if updated_line.find("$$" + key + "$$") != -1:
            updated_line = updated_line.replace("$$" + key + "$$", talk_data[key])

    return updated_line


def create_talk_website(talk_data):
    """Take the talk data collected above and create the website of the talk, i.e. the 'yyyymmdd.html' file
    
    TODO: Instead of modifying the talk data dict, we should better copy each entry that we want to use."""

    talk_path = path.join("..", "talks", talk_data["date"].replace("/","") + ".html")

    # Check if file already exists.
    if path.exists(talk_path):
        overwrite = "y" == prompt_loop_read_data("The path '{}' already exists. Overwrite? (y/n) [n] ", condition_fn=lambda s : s in ["y", "n"], default="n")
        if not overwrite:
            print("Quitting here. Nothing written.")
            return

    # Add the info on the fancy latex presentation
    if re.match(title_whatis, talk_data["title"]):
        talk_data["title_minus_whatisare"] = talk_data["title"].replace("What is... ", "")
        talk_data["fancy_whatisare"] =  r"$\vec{w}h\alpha\mathfrak{t}\;\; i\mathbb{S}\ldots$" 
    elif re.match(title_whatare, talk_data["title"]):
        talk_data["title_minus_whatisare"] = talk_data["title"].replace("What are... ", "")
        talk_data["fancy_whatisare"] =  r"$\vec{w}h\alpha\mathfrak{t}\;\; \forall\mathbb{R}\varepsilon\ldots$" 

    # creating other useful tags:
    if talk_data["before_mathplus"]:
        talk_data["mathplus_talk_info"] = r'<br>Before the MATH+ Friday colloquium talk by <a href="' + talk_data["mathplus_poster_link"] + r'">' + talk_data["mathplus_speaker"] + r'</a>'

    talk_data["location_descriptor"] = talk_data["location"]["uni"] + ", " + r'<a href="' + r'../map/' + talk_data["location"]["map"] +  r'">' + talk_data["location"]["building"] + r'</a>'

    # Printing the file:
    print("\n--- Now creating the website file. ---\n")

    with open(talk_path, "w") as html_file:
        with open("template", "r") as template_file:
            for line in template_file:
                updated_line = update_line(line, talk_data)
                html_file.write(updated_line)


    print("Done.")


if __name__ == "__main__":
    # talk_data = collect_information()

    # Test data:
    talk_data = {'date': '2024/05/03', 'time': '13:00 s.t.', 'location': {'uni': 'FU Berlin', 'building': 'Arnimallee 3', 'map': 'fu_map_numbers.jpg'}, 'room': 'SR 119', 'live-streamed': False, 'speaker': 'Ji Hoon Chun', 'affiliation': 'TU Berlin', 'title': 'What are... sphere packing lower and upper bounds?', 'abstract': 'In Euclidean space, the densest sphere packings and their densities are only known in dimensions 1, 2 (Thue, Fejes Tóth), 3 (Hales), 8 (Viazovska), and 24 (Cohn et al.). However, several nontrivial lower and upper bounds for the density δ(d) of the densest packing in dimension d have been established. A simple "folklore" result states that δ(d) ≥ 1/2^d. In this talk we present the intuition and details of three other lower and upper bounds for δ(d): the Minkowski–Hlawka theorem for a lower bound, Blichfeldt\'s upper bound, and Rogers\'s upper bound. These results, among others, place δ(d) within a narrow strip of possible densities.', 'before_mathplus': True, 'mathplus_speaker': 'Julian Sahasrabudhe (U Cambridge)', 'mathplus_poster_link': 'https://www.math-berlin.de/images/poster/MATHFriday_Sahasrabudhe.pdf'}

    print("Talk Data: \n{}".format(talk_data))

    create_talk_website(talk_data)

    print("\n--- Left to be done --- \n")
    print("-> Update the currenttalk.html and talks.html file")