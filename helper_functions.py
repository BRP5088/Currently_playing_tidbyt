import Person


def get_person( peopleLst, name ):
    for person in peopleLst:
        if person.name == name:
            return person