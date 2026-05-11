from enum import Enum

class TaskStatus(str, Enum): 
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    TO_REVIEW = "to_review"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


TRANSITIONS = {
    TaskStatus.TODO: {TaskStatus.IN_PROGRESS, TaskStatus.CANCELLED},
    TaskStatus.IN_PROGRESS: {TaskStatus.TO_REVIEW, TaskStatus.CANCELLED},
    TaskStatus.TO_REVIEW: {TaskStatus.COMPLETED, TaskStatus.IN_PROGRESS},
    TaskStatus.COMPLETED: set(),
    TaskStatus.CANCELLED: set(),
}

def can_transition(current: TaskStatus, new: TaskStatus) -> bool: 
    return new in TRANSITIONS[current]







