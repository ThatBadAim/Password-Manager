using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using System.Collections.ObjectModel;
using CipherVault.Models;
using System;
using System.Diagnostics;
using System.Windows;
using System.Threading.Tasks;
using System.Threading;
using System.Linq;

namespace CipherVault.ViewModels
{
    public partial class MainViewModel : ObservableObject
    {
        private ObservableCollection<VaultItem> _allVaultItems;

        [ObservableProperty]
        private ObservableCollection<VaultItem> _filteredVaultItems;

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

        private int _toastRequestCount;

        public MainViewModel()
        {
            // Initialize with mock data for GitHub Dev Account
            _allVaultItems = new ObservableCollection<VaultItem>
            {
                new VaultItem
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
                        new AuditLogEntry { Timestamp = DateTime.Now.AddMinutes(-5), ActionType = "Password Updated", ActionDescription = "Password changed via settings", IconType = "Pencil" }, // literal string to be resolved in View or ViewModel
                        new AuditLogEntry { Timestamp = DateTime.Now.AddDays(-2), ActionType = "Password Viewed", ActionDescription = "Password revealed in UI", IconType = "Eye" },
                        new AuditLogEntry { Timestamp = DateTime.Now.AddDays(-5), ActionType = "Username Copied", ActionDescription = "Username copied to clipboard", IconType = "Copy" },
                        new AuditLogEntry { Timestamp = DateTime.Now.AddMonths(-6), ActionType = "Entry Created", ActionDescription = "Vault item initially created", IconType = "Plus" }
                    }
                }
            };

            _filteredVaultItems = new ObservableCollection<VaultItem>(_allVaultItems);
            _selectedVaultItem = _filteredVaultItems.FirstOrDefault();
        }

        partial void OnSearchTextChanged(string value)
        {
            if (string.IsNullOrWhiteSpace(value))
            {
                FilteredVaultItems = new ObservableCollection<VaultItem>(_allVaultItems);
            }
            else
            {
                var lowerVal = value.ToLowerInvariant();
                FilteredVaultItems = new ObservableCollection<VaultItem>(
                    _allVaultItems.Where(i => (i.Title?.ToLowerInvariant().Contains(lowerVal) ?? false) ||
                                              (i.Subtitle?.ToLowerInvariant().Contains(lowerVal) ?? false) ||
                                              (i.Username?.ToLowerInvariant().Contains(lowerVal) ?? false))
                );
            }

            SelectedVaultItem = FilteredVaultItems.FirstOrDefault();
        }

        [RelayCommand]
        private async Task CopyToClipboardAsync(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                await ShowToastAsync("Copied to clipboard");
            }
        }

        private async Task ShowToastAsync(string message)
        {
            ToastMessage = message;
            IsToastVisible = true;

            int currentRequest = Interlocked.Increment(ref _toastRequestCount);
            await Task.Delay(2000);

            if (currentRequest == _toastRequestCount)
            {
                IsToastVisible = false;
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
        private async Task EditItemAsync()
        {
            await ShowToastAsync("Edit mode enabled");
        }

        [RelayCommand]
        private async Task DeleteItemAsync()
        {
            await ShowToastAsync("Item deleted");
        }

        [RelayCommand]
        private async Task AddNewItemAsync()
        {
            await ShowToastAsync("Add new item dialogue opened");
        }
    }
}
