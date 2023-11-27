"""Module docstring providing a brief description of the module."""

class Bug:
    """Class representing a bug."""

    def init(self, description, severity, deadline, status, assignee):
        """
        Initialize a Bug object.

        Args:
            description (str): Description of the bug.
            severity (str): Severity level of the bug.
            deadline (str): Deadline for resolving the bug.
            status (str): Current status of the bug.
            assignee (str): Person assigned to the bug.
        """
        self.description = description
        self.severity = severity
        self.deadline = deadline
        self.status = status
        self.assignee = assignee


class Backlog:
    """Class representing a backlog of bugs."""

    def init(self):
        """Initialize a Backlog object."""
        self.bugs = []

    def add_bug(self, bug):
        """
        Add a bug to the backlog.

        Args:
            bug (Bug): Bug object to be added to the backlog.
        """
        if bug not in self.bugs:
            self.bugs.append(bug)

    def get_resolved_bugs_for_assignee(self, assignee):
        """
        Get resolved bugs for a specific assignee.

        Args:
            assignee (str): The assignee to filter resolved bugs.

        Returns:
            list: List of resolved bugs for the assignee.
        """
        resolved_bugs = [bug for bug in self.bugs if
                  bug.status == "RESOLVED" and bug.assignee == assignee]


        print(f"Resolved bugs for {assignee}:")
        for bug in resolved_bugs:
            print(f"Bug description: {bug.description}, Severity: {bug.severity}")

        return resolved_bugs

    def sort_by_severity(self):
        """Sort the backlog by severity."""
        self.bugs.sort(key=lambda bug: bug.severity)

        print("\nBacklog sorted by severity:")
        for bug in self.bugs:
            print(f"Bug description: {bug.description}, Severity: {bug.severity}")

from lab5 import Bug, Backlog

def main():
    bug1 = Bug("UI issue", "Minor", "2023-11-01", "OPEN", "Developer1")
    bug2 = Bug("Critical functionality bug", "Critical", "2023-10-30", "RESOLVED", "Developer2")
    bug3 = Bug("Performance problem", "Major", "2023-11-05", "RESOLVED", "Developer1")
    bug4 = Bug("Database error", "Major", "2023-11-10", "OPEN", "Developer3")

    backlog = Backlog()
    backlog.add_bug(bug1)
    backlog.add_bug(bug2)
    backlog.add_bug(bug3)
    backlog.add_bug(bug4)

    backlog.get_resolved_bugs_for_assignee("Developer1")
    backlog.sort_by_severity()


if __name__ == "__main__":
    main()