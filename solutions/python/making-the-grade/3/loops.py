"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    curved = []
    for score in student_scores:
        curved.append(round(score))
    return curved
       


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    utter_failures = 0
    for score in student_scores:
        if score <= 40:
            utter_failures += 1
    return utter_failures


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_of_the_best_sir = []
    for score in student_scores:
        if score >= threshold:
            best_of_the_best_sir.append(score)
    return best_of_the_best_sir
           


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    failing = 40
    interval_range = highest - failing
    grade_intervals = interval_range // 4
    d_threshold = failing + 1
    c_threshold = d_threshold + grade_intervals
    b_threshold = c_threshold + grade_intervals
    a_threshold = b_threshold + grade_intervals
    return [d_threshold, c_threshold, b_threshold, a_threshold]
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    compiled_nonsense = []
    ranks = 1
    index_number = 0
    for score in student_scores:
        compiled_nonsense.append(str(ranks) + '. ' + student_names[index_number] + ': ' + str(score))
        ranks += 1
        index_number += 1
    return compiled_nonsense


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for perfect_little_angel in student_info:
        if perfect_little_angel[1] == 100:
            return perfect_little_angel
    return []