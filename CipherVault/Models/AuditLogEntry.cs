using System;

namespace CipherVault.Models
{
    public class AuditLogEntry
    {
        public DateTime Timestamp { get; set; }
        public string ActionType { get; set; } = string.Empty;
        public string ActionDescription { get; set; } = string.Empty;
        public string IconType { get; set; } = string.Empty; // Store Segoe MDL2 character code
    }
}
