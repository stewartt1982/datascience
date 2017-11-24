#
# Example for parsing and processing XML
#

import xml.dom.minidom


def main():
    doc = xml.dom.minidom.parse("samplexml.xml")

    print doc.nodeName
    print doc.firstChild.tagName

    #get list of XML tags from doc and print them
    skills = doc.getElementsByTagName("skill")
    print "%d skills:" % skills.length
    for skill in skills:
        print skill.getAttribute("name")

    #create a new skill
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","jQuery")
    doc.firstChild.appendChild(newSkill)

    #get list of XML tags from doc and print them
    skills = doc.getElementsByTagName("skill")
    print "%d skills:" % skills.length
    for skill in skills:
        print skill.getAttribute("name")

    
if __name__ == "__main__":
    main()
