using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.ObjectModel;
using CipherVault.Models;
using System;
using System.Diagnostics;
using System.Windows;

namespace CipherVault.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
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

        public ObservableCollection<VaultItem> VaultItems { get; } = new();
        public ObservableCollection<VaultItem> FilteredVaultItems { get; } = new();

        private int _toastCounter;

        public MainViewModel()
        {
            // Initialize with mock data for GitHub Dev Account
            var githubItem = new VaultItem
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

            var extraItem = new VaultItem
            {
                Title = "Extra Item",
                Subtitle = "For Search Testing",
                Category = "Test",
                Username = "test.user",
                EncryptedPassword = "test_password",
                Url = "https://example.com"
            };

            VaultItems.Add(githubItem);
            VaultItems.Add(extraItem);

            foreach (var item in VaultItems)
            {
                FilteredVaultItems.Add(item);
            }

            _selectedVaultItem = githubItem;
        }

        partial void OnSearchTextChanged(string value)
        {
            FilteredVaultItems.Clear();

            if (string.IsNullOrWhiteSpace(value))
            {
                foreach (var item in VaultItems)
                {
                    FilteredVaultItems.Add(item);
                }
            }
            else
            {
                var lowerSearch = value.ToLowerInvariant();
                foreach (var item in VaultItems)
                {
                    if (item.Title?.ToLowerInvariant().Contains(lowerSearch) == true ||
                        item.Subtitle?.ToLowerInvariant().Contains(lowerSearch) == true ||
                        item.Category?.ToLowerInvariant().Contains(lowerSearch) == true)
                    {
                        FilteredVaultItems.Add(item);
                    }
                }
            }

            if (FilteredVaultItems.Count > 0 && (SelectedVaultItem == null || !FilteredVaultItems.Contains(SelectedVaultItem)))
            {
                SelectedVaultItem = FilteredVaultItems[0];
            }
            else if (FilteredVaultItems.Count == 0)
            {
                SelectedVaultItem = null;
            }
        }

        [RelayCommand]
        private async System.Threading.Tasks.Task CopyToClipboardAsync(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ToastMessage = "Copied to clipboard";
                IsToastVisible = true;

                int currentCounter = System.Threading.Interlocked.Increment(ref _toastCounter);

                await System.Threading.Tasks.Task.Delay(3000);

                if (currentCounter == _toastCounter)
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
