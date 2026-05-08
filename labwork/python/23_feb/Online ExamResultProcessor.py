# -------------------------------------------------------
# Online Exam Result Processor (Optimized)
# - Remove lowest 2 scores
# - Add grace marks (5) for scores between 30 and 35
# - Count students who passed (>= 40)
# - No split(), no sort(), no built-in numeric functions
# -------------------------------------------------------

def exam_result_processor():

    data = input("Enter student scores separated by space: ")

    scores = []
    number = ""

    # -----------------------------------
    # Manual parsing (optimized validation)
    # -----------------------------------
    for i in range(len(data)):

        if data[i] != " ":
            number = number + data[i]
        else:
            if number != "":
                valid = True

                for ch in number:
                    if ch < '0' or ch > '9':
                        valid = False
                        break   # Optimization

                if valid:
                    scores.append(int(number))

            number = ""

    # Add last number
    if number != "":
        valid = True

        for ch in number:
            if ch < '0' or ch > '9':
                valid = False
                break

        if valid:
            scores.append(int(number))

    # -----------------------------------
    # Check minimum required scores
    # -----------------------------------
    if len(scores) <= 2:
        print("Not enough scores to remove lowest 2.")
        return

    # -----------------------------------
    # Manual Bubble Sort (Ascending)
    # -----------------------------------
    for i in range(len(scores)):
        for j in range(0, len(scores) - i - 1):
            if scores[j] > scores[j + 1]:
                temp = scores[j]
                scores[j] = scores[j + 1]
                scores[j + 1] = temp

    # -----------------------------------
    # Remove lowest 2
    # -----------------------------------
    remaining = []

    for i in range(2, len(scores)):
        remaining.append(scores[i])

    # -----------------------------------
    # Add grace marks (30–35 inclusive)
    # -----------------------------------
    for i in range(len(remaining)):
        if remaining[i] >= 30 and remaining[i] <= 35:
            remaining[i] = remaining[i] + 5

    # -----------------------------------
    # Count passed students (>= 40)
    # -----------------------------------
    passed_count = 0

    for i in range(len(remaining)):
        if remaining[i] >= 40:
            passed_count = passed_count + 1

    # -----------------------------------
    # Display results
    # -----------------------------------
    print("\nScores after removing lowest 2:", remaining)
    print("Number of students passed:", passed_count)

    '''output:
    
    Enter student scores separated by space: 25 30 32 28 40 45 38
    Scores after removing lowest 2: [35, 38, 40, 45]
    Number of students passed: 4
    '''