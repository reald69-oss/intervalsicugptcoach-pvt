# audit_core/errors.py

class AuditHalt(Exception):
    """
    Raised when audit chain must halt due to integrity or data issues.

    Now includes metadata for graceful handling.
    """

    def __init__(self, message, code="DATA_INTEGRITY", severity="soft"):
        super().__init__(message)
        self.message = message
        self.code = code
        self.severity = severity

    def to_dict(self):
        return {
            "status": "halted",
            "error_type": self.code,
            "severity": self.severity,
            "message": self._friendly_message()
        }

    def _friendly_message(self):
        # Map common raw messages to cleaner UI messages
        if "snapshot source empty" in self.message.lower():
            return "No training data available for the selected period."
        if "missing 'type' column" in self.message.lower():
            return "Training data schema incomplete. Please re-sync activities."
        return self.message
