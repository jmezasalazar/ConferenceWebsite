sites = ["Workshop A", "Workshop B", "Workshop C", "Workshop D", "Workshop E", "Workshop F", "Workshop G", "Workshop H",
         "Workshop I", "mealpack", "dinnerday2", "All Conference", '']
actual = ["Home Button?", "GalaxyForever", "Green Bubble", "IphoneInfinity", "TroubleShooting", "AndroidHelp", "Tips", "Gadgets",
          "Pixels+", "mealpack", "dinnerday2", "All Conference", "blank"]
keys = {sites[x]: actual[x] for x in range(len(sites))}

lists = {x: [] for x in sites}


def getJSONdata():
    import json
    registrant_list = []
    with open('registrant_data.json', 'r') as registrantFile:
        jsonData = json.load(registrantFile)
        for registrant in jsonData['registrants']:
            registrant_list.append(registrant)
    return registrant_list


for x in getJSONdata():
    lists["All Conference"].append(x)
    lists[x["session1"]].append(x)
    lists[x["session2"]].append(x)
    lists[x["session3"]].append(x)
    lists[x["meals"]].append(x)


def generateHTML(lists, keys):
    for x in lists:
        counter = 0
        file = x + ".html"
        print('generating page for, ' + file)
        with open('../'+file, 'w') as outputFile:
            outputFile.write("<!DOCTYPE html><br>\n")
            outputFile.write("<html lang=""en"">\n<head>\n<meta charset=""UTF-8"">\n<title>nametags8</title>\n</head>")
            outputFile.write("<body>\n")
            outputFile.write('<link href="list.css" rel="stylesheet"/>\n')
            outputFile.write("<main>\n")
            outputFile.write(('<h1> ' + keys[x] + '</h1>\n'))

            # output/write the list
            for registrant in lists[x]:
                counter = counter + 1
                outputFile.write('\t\t<p>' + str(counter) + ". " + registrant['lastname'] + ", " + registrant['firstname'] +
                                           '</p> \n')

                # output/write the end stuff
            outputFile.write("</main>\n")
            outputFile.write("</body>\n")
            outputFile.write("</html>\n")


generateHTML(lists, keys)
