alg = "1"
stopState = "H"
if alg != "optional":
    alg = int(alg)
fom = "SS" #SS(StateStateCharCharHead), SC(StateCharStateCharHead)
if fom == "SS":
    gHed = 2 #getProgram2
    nSta = 1 #new state
    mHed = 4 #move head
    nCha = 3 #new char
else:
    gHed = 1
    nSta = 2
    mHed = 4
    nCha = 3


tape = str(input())

headPosition = 0

state = 'A'

programs = []

program = ""

file = open("UniversalTuringMachineStatesList.txt", "r", encoding = "utf-8")
for line in file:
    programs.append(line)

"""
while (program != "RUN"):
    program = str(input())
    if program != "RUN":
        programs.append(program)
"""

getProgram = programs[0]

selectedPrograms = []

while (state != stopState):
    if headPosition >= len(tape):
        for j in range(headPosition + 1 - len(tape)):
            tape = tape[:len(tape)] + '-' + tape[len(tape) + 1:]

    elif headPosition < 0:
        # for k in range(abs(headPosition) + 1 - len(tape)):
        tape = tape[:0] + '-' + tape[0:]
        headPosition = 0

    print("Tape: " + tape)
    print("      " + " " * headPosition + "^")
    print("      " + " " * headPosition + state)

    
    selectedPrograms = []

    for i in range(len(programs)):
        getProgram = programs[i]
            
        if getProgram[0] == state:
            if getProgram[gHed:gHed + alg] == tape[headPosition]:
                selectedPrograms.append(getProgram)
            elif getProgram[gHed:gHed + alg] == '０' and tape[headPosition] == '0':
                selectedPrograms.append(getProgram)
            elif getProgram[gHed:gHed + alg] == '１' and tape[headPosition] == '1':
                selectedPrograms.append(getProgram)
            elif getProgram[gHed:gHed + alg] == 'ー' and tape[headPosition] == '-':
                selectedPrograms.append(getProgram)


    if len(selectedPrograms) == 1:
        error = False
        getProgram = selectedPrograms[0]
        state = getProgram[nSta:nSta + alg]
        if getProgram[nCha:nCha + alg] == '０' or getProgram[nCha:nCha + alg] == '0':
            tape = tape[:headPosition] + '0' + tape[headPosition + 1:]
        elif getProgram[nCha:nCha + alg] == '１' or getProgram[nCha:nCha + alg] == '1':
            tape = tape[:headPosition] + '1' + tape[headPosition + 1:]
        elif getProgram[nCha:nCha + alg] == 'ー' or getProgram[nCha:nCha + alg] == '-':
            tape = tape[:headPosition] + '-' + tape[headPosition + 1:]
        
        if getProgram[mHed:mHed + alg] == 'R' or getProgram[mHed:mHed + alg] == 'r' or getProgram[mHed:mHed + alg] == 'ｒ':
            headPosition += 1
        elif getProgram[mHed:mHed + alg] == 'L' or getProgram[mHed:mHed + alg] == 'l' or getProgram[mHed:mHed + alg] == 'ｌ':
            headPosition -= 1
        elif getProgram[mHed:mHed + alg] == 'S' or getProgram[mHed:mHed + alg] == 's' or getProgram[mHed:mHed + alg] == 'ｓ':
            headPosition = headPosition

    if len(selectedPrograms) == 0:
        print("No applicable line found")
        state = stopState
        error = True

    if len(selectedPrograms) >= 2:
        print("Duplicated line has detected: " + str(len(selectedPrograms)))
        print("State: " + str(state))
        state = stopState
        error = True

if error == False:
    print("Tape: " + tape)
    print("      " + " " * headPosition + "^")
    print("      " + " " * headPosition + state)

#0101001010100101-01001010101010010101
#111-111101101100001--11100000010011-
# TuringMachine
