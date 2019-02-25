try:
    with open('registrant_data.csv', 'r') as registrantFile:
        import csv

        registrants = registrantFile.readlines()

    with open('../nametags8py.html', 'w') as nametag8:
        # writeoutthe"front"
        nametag8.write("<!DOCTYPE html><br>\n")
        nametag8.write("<html lang=""en"">\n<head>\n<meta charset=""UTF-8"">\n<title>nametags8</title>\n</head>")
        nametag8.write("<body>\n")
        nametag8.write('<link href="nametags8.css" rel="stylesheet"/>\n')
        nametag8.write("<main>\n")
        # write out name tags
        count = 0

        for registrant in registrants:
            count = count + 1
            data = registrant.split(",")
            if (count % 2) == 1:
                nametag8.write("<table width=" + '"' + "80%" + '"' + " align=" + '"' + "center" + '"' + ">\n")
                nametag8.write("<tr> \n")
            nametag8.write("<th> \n <p class = " + '"' + "div1" + '"' + '>' )

            nametag8.write("<span class =" + '"' + "one" + '"' + ">" + data[2] + "</span><br>\n")
            nametag8.write("<span class =" + '"' + "two" + '"' + ">" + data[3] + "</span><br>\n")
            nametag8.write("<span class =" + '"' + "three" + '"' + ">" + data[12] + "</span><br>\n")
            nametag8.write("<span class =" + '"' + "two" + '"' + ">" + data[13] + "</span><br>\n")
            nametag8.write("<span class =" + '"' + "two" + '"' + ">" + data[6] + "</span><br>\n")
            nametag8.write("</p>\n </th> \n")


            if (count % 2) == 0:
                nametag8.write("</tr>\n </table>\n")




        # write out "end"
        nametag8.write("</main>\n")
        nametag8.write("</body>\n")
        nametag8.write("</html>\n")

    with open('../nametags10py.html', 'w') as nametag10:
        # writeoutthe"front"
        nametag10.write("<!DOCTYPE html><br>\n")
        nametag10.write("<html lang=""en"">\n<head>\n<meta charset=""UTF-8"">\n<title>nametags10</title>\n</head>")
        nametag10.write("<body>\n")
        nametag10.write('<link href="nametags10.css" rel="stylesheet"/>\n')
        nametag10.write("<main>\n")
        # write out name tags
        count = 0

        for registrant in registrants:
            count = count + 1
            data = registrant.split(",")
            if (count % 2) == 1:
                nametag10.write("<table width=" + '"' + "80%" + '"' + " align=" + '"' + "center" + '"' + ">\n")
                nametag10.write("<tr> \n")
            nametag10.write("<th> \n <p class = " + '"' + "div1" + '"' + '>')

            nametag10.write("<span class =" + '"' + "one" + '"' + ">" + data[2] + "</span><br>\n")
            nametag10.write("<span class =" + '"' + "two" + '"' + ">" + data[3] + "</span><br>\n")
            nametag10.write("<span class =" + '"' + "three" + '"' + ">" + data[12] + "</span><br>\n")
            nametag10.write("<span class =" + '"' + "three" + '"' + ">" + data[13] + "</span><br>\n")
            nametag10.write("<span class =" + '"' + "three" + '"' + ">" + data[6] + "</span><br>\n")
            nametag10.write("</p>\n </th> \n")

            if (count % 2) == 0:
                nametag10.write("</tr>\n </table>\n")

        # write out "end"
        nametag10.write("</main>\n")
        nametag10.write("</body>\n")
        nametag10.write("</html>\n")

except IOError as e:
    print('unable to open file')

print("done")


