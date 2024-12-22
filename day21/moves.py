
def getMappings():

    mapping = {}
    mapping["A0"] = "<A"
    mapping["A3"] = "^A"
    mapping["A2"] = "<^A"
    mapping["A5"] = "<^^A"
    mapping["A4"] = "^^<<A"

    mapping["8A"] = "vvv>A"
    mapping["6A"] = "vvA"
    mapping["1A"] = ">>vA"
    mapping["3A"] = "vA"

    mapping["02"] = "^A"
    mapping["29"] = "^^>A"
    mapping["9A"] = "vvvA"
#
    mapping["20"] = "vA"
    mapping["58"] = "^A"
    mapping["34"] = "<<^A"
    mapping["46"] = ">>A"
    mapping["59"] = "^>A"
#
#
    mapping["08"] = "^^^A"
    mapping["86"] = "v>A"
    mapping["41"] = "vA"
    mapping["63"] = "vA"
    mapping["93"] = "vvA"
#
    mapping["AA"] = "A"
    mapping["A^"] = "<A"
    mapping["A>"] = "vA"
    mapping["Av"] = "<vA"
    mapping["A<"] = "v<<A"

    mapping["^A"] = ">A"
    mapping["^^"] = "A"
    mapping["^>"] = "v>A"
    mapping["^v"] = "vA"
    mapping["^<"] = "v<A"

    mapping["<A"] = ">>^A"
    mapping["<^"] = ">^A"
    mapping["<>"] = ">>A"
    mapping["<v"] = ">A"
    mapping["<<"] = "A"

    mapping["vA"] = "^>A"
    mapping["v^"] = "^A"
    mapping["v>"] = ">A"
    mapping["vv"] = "A"
    mapping["v<"] = "<A"

    mapping[">A"] = "^A"
    mapping[">^"] = "<^A"
    mapping[">>"] = "A"
    mapping[">v"] = "<A"
    mapping["><"] = "<<A"

    return mapping