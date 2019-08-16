import re

filePath = r"/Users/michaelspencer/Library/Mobile Documents/com~apple~CloudDocs/GitHub/AnastasiaPortfolio/AnastasiaSite/WebTemplate/CurrentVersion/pythonScript/cssDoc.txt"

htmlString = """<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <link rel="icon" href="img/favicon.png" type="image/png">
        <title>MeetMe Personal</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="css/bootstrap.css">
        <link rel="stylesheet" href="vendors/linericon/style.css">
        <link rel="stylesheet" href="css/font-awesome.min.css">
        <link rel="stylesheet" href="vendors/owl-carousel/owl.carousel.min.css">
        <link rel="stylesheet" href="vendors/lightbox/simpleLightbox.css">
        <link rel="stylesheet" href="vendors/nice-select/css/nice-select.css">
        <link rel="stylesheet" href="vendors/animate-css/animate.css">
        <link rel="stylesheet" href="vendors/popup/magnific-popup.css">
        <!-- main css -->
        <link rel="stylesheet" href="css/style.css">
        <link rel="stylesheet" href="css/responsive.css">
    </head>
    <body>
        <div>
            <ul id="ImgList" class="list basic_info">								
                    <li><a href="#"><i class="lnr lnr-phone-handset"></i></a></li>


"""


def CreateHtmlDoc(filePath, htmlString):

    # Open text document
    with open(filePath, "r") as txt:
        for line in txt:
            rl = re.findall('lnr-.+(?=:)', line)
            if len(rl) > 0:
                lnrString = rl[0]                
                # add the string the htmlString
                lineItemString = "<li><a href=#><i class=\"iconImgs lnr " + lnrString + " \"></i></a></li> "
                print(lineItemString)
                htmlString = htmlString + lineItemString + "\n"
    txt.close()   
    htmlString = htmlString + "</ul></div></body></html>"

    htmlFile = open("/Users/michaelspencer/lnr_HTML_Output.html", "w")   
    htmlFile.write(htmlString)
    htmlFile.close()       

    #save string to file


    print("all done.")
CreateHtmlDoc(filePath, htmlString)
