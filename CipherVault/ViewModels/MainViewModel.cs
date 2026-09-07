using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.ObjectModel;
using System.Linq;
using CipherVault.Models;
using System;
using System.Diagnostics;
using System.Windows;
using System.Threading.Tasks;
using System.Threading;

namespace CipherVault.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
        private ObservableCollection<VaultItem> _masterVaultItems;
        private int _toastCounter;

        [ObservableProperty]
        private VaultItem? _selectedVaultItem;

        [ObservableProperty]
        private bool _isPasswordVisible;

        [ObservableProperty]
        private string _searchText = string.Empty;

        [ObservableProperty]
        private bool _isToastVisible;

        [ObservableProperty]
        private string _toastMessage = string.Empty;

        public ObservableCollection<VaultItem> FilteredVaultItems { get; } = new();

        public MainViewModel()
        {
            // Initialize with mock data for GitHub Dev Account
            var initialItem = new VaultItem
            {
                Title = "GitHub",
                Subtitle = "Personal Development Account",
                Category = "Dev Account",
                Username = "alex.chen.dev",
                EncryptedPassword = "super_secure_password_123", // In real app, this is actual encrypted payload
                Url = "https://github.com/login",
                Notes = "Use this account for personal open source contributions.\n\nAssociated email: alex.c@example.com\nRecovery codes are stored in offline physical safe.",
                Badges = new System.Collections.Generic.List<string> { "WORK", "DEVELOPMENT" },
                SecurityScore = 98,
                MfaEnabled = true,
                MfaStatus = "Confirmed via system check",
                LastRotated = DateTime.Now.AddDays(-12),
                BreachStatus = "No leaks detected",
                AuditLogs = new System.Collections.Generic.List<AuditLogEntry>
                {
                    new AuditLogEntry { Timestamp = DateTime.Now.AddMinutes(-5), ActionType = "Password Updated", ActionDescription = "Password changed via settings", IconType = "Pencil" },
                    new AuditLogEntry { Timestamp = DateTime.Now.AddDays(-2), ActionType = "Password Viewed", ActionDescription = "Password revealed in UI", IconType = "Eye" },
                    new AuditLogEntry { Timestamp = DateTime.Now.AddDays(-5), ActionType = "Username Copied", ActionDescription = "Username copied to clipboard", IconType = "Copy" },
                    new AuditLogEntry { Timestamp = DateTime.Now.AddMonths(-6), ActionType = "Entry Created", ActionDescription = "Vault item initially created", IconType = "Plus" }
                }
            };

            _masterVaultItems = new ObservableCollection<VaultItem> { initialItem };
            FilteredVaultItems.Add(initialItem);
            SelectedVaultItem = initialItem;
        }

        partial void OnSearchTextChanged(string value)
        {
            FilteredVaultItems.Clear();
            var lowerValue = value?.ToLowerInvariant() ?? string.Empty;

            foreach (var item in _masterVaultItems)
            {
                if (string.IsNullOrWhiteSpace(lowerValue) ||
                    (item.Title?.ToLowerInvariant().Contains(lowerValue) == true) ||
                    (item.Category?.ToLowerInvariant().Contains(lowerValue) == true))
                {
                    FilteredVaultItems.Add(item);
                }
            }

            if (SelectedVaultItem == null || !FilteredVaultItems.Contains(SelectedVaultItem))
            {
                SelectedVaultItem = FilteredVaultItems.FirstOrDefault();
            }
        }

        [RelayCommand]
        private async Task CopyToClipboardAsync(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ToastMessage = "Copied to clipboard!";
                IsToastVisible = true;

                Interlocked.Increment(ref _toastCounter);
                await Task.Delay(3000);
                if (Interlocked.Decrement(ref _toastCounter) == 0)
                {
                    IsToastVisible = false;
                }
            }
        }

        [RelayCommand]
        private void TogglePasswordVisibility()
        {
            IsPasswordVisible = !IsPasswordVisible;
        }

        [RelayCommand]
        private void LaunchExternalUrl(string url)
        {
            if (!string.IsNullOrEmpty(url))
            {
                try
                {
                    Process.Start(new ProcessStartInfo(url) { UseShellExecute = true });
                }
                catch (Exception ex)
                {
                    Debug.WriteLine($"Failed to launch URL: {ex.Message}");
                }
            }
        }

        [RelayCommand]
        private void EditItem()
        {
            // Edit item logic
        }

        [RelayCommand]
        private void DeleteItem()
        {
            // Delete item logic
        }

        [RelayCommand]
        private void AddNewItem()
        {
            // Add new item logic
        }
    }
}
