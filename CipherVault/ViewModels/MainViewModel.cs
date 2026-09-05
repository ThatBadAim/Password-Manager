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
        private ObservableCollection<VaultItem> _vaultItems = new();

        [ObservableProperty]
        private ObservableCollection<VaultItem> _filteredVaultItems = new();

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

        private int _toastCounter = 0;

        public MainViewModel()
        {
            // Initialize with mock data for GitHub Dev Account
            var mockItem = new VaultItem
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

            VaultItems.Add(mockItem);
            FilteredVaultItems = new ObservableCollection<VaultItem>(VaultItems);
            SelectedVaultItem = FilteredVaultItems.FirstOrDefault();
        }

        partial void OnSearchTextChanged(string value)
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                FilteredVaultItems = new ObservableCollection<VaultItem>(VaultItems);
            }
            else
            {
                var lowerValue = value.ToLowerInvariant();
                var filtered = VaultItems.Where(i => i.Title?.ToLowerInvariant().Contains(lowerValue) == true || i.Subtitle?.ToLowerInvariant().Contains(lowerValue) == true);
                FilteredVaultItems = new ObservableCollection<VaultItem>(filtered);
            }
            SelectedVaultItem = FilteredVaultItems.FirstOrDefault();
        }

        private async void ShowToast(string message)
        {
            ToastMessage = message;
            IsToastVisible = true;

            var currentCounter = Interlocked.Increment(ref _toastCounter);

            await Task.Delay(2000);

            if (currentCounter == _toastCounter)
            {
                IsToastVisible = false;
            }
        }

        [RelayCommand]
        private void CopyToClipboard(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ShowToast("Copied to clipboard");
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
