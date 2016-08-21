with open("A-large.in", "r") as data:
    cases = int(data.readline())
    with open("A-large.out", "w") as result:
        for i in range(cases):
            number = ""
            case = data.readline().rstrip()
            const = case.count("Z")
            if const > 0:
                number += ("0"*const)
                case = case.replace("Z", "", const)
                case = case.replace("E", "", const)
                case = case.replace("R", "", const)
                case = case.replace("O", "", const)
            const = case.count("W")
            if const > 0:
                number += ("2"*const)
                case = case.replace("T", "", const)
                case = case.replace("W", "", const)
                case = case.replace("O", "", const)
            const = case.count("U")
            if const > 0:
                number += ("4"*const)
                case = case.replace("F", "", const)
                case = case.replace("O", "", const)
                case = case.replace("U", "", const)
                case = case.replace("R", "", const)
            const = case.count("X")
            if const > 0:
                number += ("6"*const)
                case = case.replace("S", "", const)
                case = case.replace("I", "", const)
                case = case.replace("X", "", const)
            const = case.count("G")
            if const > 0:
                number += ("8"*const)
                case = case.replace("E", "", const)
                case = case.replace("I", "", const)
                case = case.replace("G", "", const)
                case = case.replace("H", "", const)
                case = case.replace("T", "", const)
            const = case.count("F")
            if const > 0:
                number += ("5"*const)
                case = case.replace("F", "", const)
                case = case.replace("I", "", const)
                case = case.replace("V", "", const)
                case = case.replace("E", "", const)
            const = case.count("O")
            if const > 0:
                number += ("1"*const)
                case = case.replace("O", "", const)
                case = case.replace("N", "", const)
                case = case.replace("E", "", const)
            const = case.count("V")
            if const > 0:
                number += ("7"*const)
                case = case.replace("S", "", const)
                case = case.replace("E", "", const)
                case = case.replace("V", "", const)
                case = case.replace("E", "", const)
                case = case.replace("N", "", const)
            const = case.count("H")
            if const > 0:
                number += ("3"*const)
                case = case.replace("T", "", const)
                case = case.replace("H", "", const)
                case = case.replace("R", "", const)
                case = case.replace("E", "", const)
                case = case.replace("E", "", const)
            if case.count("I") > 0:
                number += ("9"*case.count("I"))
            result.write("Case #" + str(i+1) + ": " + str("".join(sorted(number))) + "\n")
        
