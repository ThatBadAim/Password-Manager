using System;
using System.Collections.Generic;

namespace CipherVault.Models
{
    public class VaultItem
    {
        public string Id { get; set; } = Guid.NewGuid().ToString();
        public string Title { get; set; } = string.Empty;
        public string Subtitle { get; set; } = string.Empty;
        public string Category { get; set; } = string.Empty;
        public string Username { get; set; } = string.Empty;
        public string EncryptedPassword { get; set; } = string.Empty;
        public string Url { get; set; } = string.Empty;
        public string Notes { get; set; } = string.Empty;
        public List<string> Badges { get; set; } = new();
        public int SecurityScore { get; set; }

        // Security Insights
        public bool MfaEnabled { get; set; }
        public string MfaStatus { get; set; } = string.Empty;
        public DateTime LastRotated { get; set; }
        public string BreachStatus { get; set; } = string.Empty;

        public List<AuditLogEntry> AuditLogs { get; set; } = new();
    }
}
