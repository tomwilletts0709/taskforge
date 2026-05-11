from enum import Enum

class UserProgress(str, Enum): 
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    TO_REVIEW = "to_review"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


TRANSITIONS = {
    UserProgress.TODO: {UserProgress.IN_PROGRESS, UserProgress.CANCELLED},
    UserProgress.IN_PROGRESS: {UserProgress.TO_REVIEW, UserProgress.CANCELLED},
    UserProgress.TO_REVIEW: {UserProgress.COMPLETED, UserProgress.IN_PROGRESS},
    UserProgress.COMPLETED: set(),
    UserProgress.CANCELLED: set(),
}

def can_transition(current: UserProgress, new: UserProgress) -> bool: 
    return new in TRANSITIONS[current]







