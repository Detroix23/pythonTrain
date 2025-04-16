# utf-8 #
"""
auth: Detroix23
date: 05/12/2024
use: Generate info card of an RPG character

"""

# Variables
ok = False
table = {}
status = "running"

# Start of UI
## Ask for title
title = input("* Enter a header: ")

## td
print("* Enter info")
while not ok:
    ### User input + dic incrementation
    print("New line")
    para = input("Enter parameter: ")
    val = input("Enter value for that parameter: ")
    if para != "":
        table[para] = val
    else:
        print("Warning - Parameter must not be blank. Skipping")
    ### Ask user if exit
    c = input("Continue? Yes (y) or no (n): ")
    if c.lower() == "n":
        ok = True
print()

# Debug
print("* Debug")
print(title)
for para, val in table.items():
    print(para, val)
print()

# Writing results

## Creating new html file
fileName = "html/" + title + ".html"
try:
    page = open(fileName, "x")
except FileExistsError:
    status = "error_fileAlreadyExits"

if status == "running":
    ## Writing static start
    page = open(fileName, "a")
    page.write(
        """
    <!DOCTYPE html >
    <html>
    <head>
    <meta charset = "utf-8" >
    <meta name = "viewport" content = "width=device-width, initial-scale=1">
    <link rel="stylesheet" href="../style1.css">
        """
    )
    page.write(
        f"""
<title>{title}</title>
        """
    )
    page.write(
        f"""
</head>

<body>
    
    <div id="stats">
        <h1>{title}</h1>
        
        <table>
        """
    )

    ## Writing each line
    page.write(
        """
        <tr>
            <th id="para"> Parameter </th>
            <th id="val"> Value </th>
        </tr>
        """
    )

    for para, val in table.items():
        page.write(
            f"""
        <tr>
            <td>{para}</td>
            <td>{val}</td>
        </tr>
            """
        )

    ## Writing last lines
    page.write(
        """
        </table>
    </div>


</body> 
</html>
        """
    )

    page.close()

    ## Returning status
    status = "success"

# End
print("* Results")
if status == "error_fileAlreadyExits":
    print("Error - Fail at creation: file already exited")
elif status == "success":
    print(f"Succes - The program created and formated the file '{fileName}'")
elif status == "running":
    print("Error - Stated running")
else:
    print("Exit - Status undefined")

EXIT = input("Enter to escape...")
