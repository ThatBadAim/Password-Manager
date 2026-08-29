using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.ObjectModel;
using CipherVault.Models;
using System;
using System.Diagnostics;
using System.Windows;
using System.Threading;
using System.Threading.Tasks;
using System.Linq;

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
        private string? _toastMessage;

        private readonly ObservableCollection<VaultItem> _allVaultItems;

        public ObservableCollection<VaultItem> FilteredVaultItems { get; }

        private int _toastCounter = 0;

        public MainViewModel()
        {
            // Initialize with mock data for GitHub Dev Account
            _selectedVaultItem = new VaultItem
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

            _allVaultItems = new ObservableCollection<VaultItem>
            {
                _selectedVaultItem
            };
            FilteredVaultItems = new ObservableCollection<VaultItem>(_allVaultItems);
        }

        partial void OnSearchTextChanged(string value)
        {
            FilteredVaultItems.Clear();
            if (string.IsNullOrWhiteSpace(value))
            {
                foreach (var item in _allVaultItems)
                {
                    FilteredVaultItems.Add(item);
                }
            }
            else
            {
                var lowerValue = value.ToLowerInvariant();
                var filtered = _allVaultItems.Where(i =>
                    (i.Title != null && i.Title.ToLowerInvariant().Contains(lowerValue)) ||
                    (i.Category != null && i.Category.ToLowerInvariant().Contains(lowerValue)) ||
                    (i.Username != null && i.Username.ToLowerInvariant().Contains(lowerValue)));

                foreach (var item in filtered)
                {
                    FilteredVaultItems.Add(item);
                }
            }

            SelectedVaultItem = FilteredVaultItems.FirstOrDefault();
        }

        [RelayCommand]
        private async Task CopyToClipboardAsync(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ToastMessage = "Copied to clipboard";
                IsToastVisible = true;

                var currentCounter = Interlocked.Increment(ref _toastCounter);
                await Task.Delay(2000);

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
