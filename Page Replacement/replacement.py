# user input.
reference_string = [7, 2, 3, 1, 2, 5, 4, 6, 7, 7, 1, 0, 5, 4, 6, 2]
num_frames = 3


# s: reference string.
# f: no. of frames.
def FIFO(s, f):
    stack = []
    to_print = []
    page_fault_count = 0

    print("FIFO Algorithm:")

    for i in range(len(s)):
        page_fault = False
        if s[i] not in stack:
            page_fault = True
            page_fault_count += 1
            if len(stack) < f:
                stack.append(s[i])
                to_print.append(s[i])
            else:
                to_print[to_print.index(stack.pop(0))] = s[i]
                stack.append(s[i])

        if page_fault:
            print(s[i], to_print, sep="  |  ", end="")
            print((f - len(to_print)) * "   " + "  |  X")
        else:
            print(s[i], to_print, sep="  |  ", end="")
            print((f - len(to_print)) * "   ", end="  |\n")

    print("No. of Page Faults:", page_fault_count, "\n")


def LRU(s, f):
    stack = []
    to_print = []
    page_fault_count = 0

    print("LRU Algorithm:")

    for i in range(len(s)):
        page_fault = False
        if s[i] not in stack:
            page_fault = True
            page_fault_count += 1
            if len(stack) < f:
                stack.append(s[i])
                to_print.append(s[i])
            else:
                to_print[to_print.index(stack.pop(0))] = s[i]
                stack.append(s[i])
        else:
            stack.remove(s[i])
            stack.append(s[i])

        if page_fault:
            print(s[i], to_print, sep="  |  ", end="")
            print((f - len(to_print)) * "   " + "  |  X")
        else:
            print(s[i], to_print, sep="  |  ", end="")
            print((f - len(to_print)) * "   ", end="  |\n")

    print("No. of Page Faults:", page_fault_count, "\n")


def optimal(s, f):
    stack = []
    page_fault_count = 0
    occurrence = [None for i in range(f)]

    print("Optimal Algorithm:")
    for i in range(len(s)):
        page_fault = False
        if s[i] not in stack:
            page_fault = True
            page_fault_count += 1
            if len(stack) < f:
                stack.append(s[i])
            else:
                for j in range(len(stack)):
                    if stack[j] not in s[i + 1:]:
                        stack[j] = s[i]
                        break
                    else:
                        occurrence[j] = s[i + 1:].index(stack[j])
                else:
                    stack[occurrence.index(max(occurrence))] = s[i]

        if page_fault:
            print(s[i], stack, sep="  |  ", end="")
            print((f - len(stack)) * "   " + "  |  X")
        else:
            print(s[i], stack, sep="  |  ", end="")
            print((f - len(stack)) * "   ", end="  |\n")

    print("No. of Page Faults:", page_fault_count, "\n")


FIFO(reference_string, num_frames)
LRU(reference_string, num_frames)
optimal(reference_string, num_frames)
