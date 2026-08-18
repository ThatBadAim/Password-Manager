using System.Linq;
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
        private VaultItem _selectedVaultItem;

        [ObservableProperty]
        private bool _isPasswordVisible;

        private string _searchText = string.Empty;
        public string SearchText
        {
            get => _searchText;
            set
            {
                SetProperty(ref _searchText, value);
                FilterVaultItems();
            }
        }

        [ObservableProperty]
        private ObservableCollection<VaultItem> _filteredVaultItems;

        private ObservableCollection<VaultItem> _allVaultItems;

        private void FilterVaultItems()
        {
            if (string.IsNullOrWhiteSpace(SearchText))
            {
                FilteredVaultItems = new ObservableCollection<VaultItem>(_allVaultItems);
            }
            else
            {
                var lowerSearch = SearchText.ToLower();
                var filtered = _allVaultItems.Where(item =>
                    item.Title.ToLower().Contains(lowerSearch) ||
                    item.Username.ToLower().Contains(lowerSearch) ||
                    item.Url.ToLower().Contains(lowerSearch));
                FilteredVaultItems = new ObservableCollection<VaultItem>(filtered);
            }
        }


        [ObservableProperty]
        private bool _isToastVisible;

        [ObservableProperty]
        private string _toastMessage = string.Empty;

        private async System.Threading.Tasks.Task ShowToast(string message)
        {
            ToastMessage = message;
            IsToastVisible = true;
            await System.Threading.Tasks.Task.Delay(2000);
            IsToastVisible = false;
        }

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

            _selectedVaultItem = mockItem;
            _allVaultItems = new ObservableCollection<VaultItem> { mockItem };
            _filteredVaultItems = new ObservableCollection<VaultItem>(_allVaultItems);
        }

        [RelayCommand]
        private async System.Threading.Tasks.Task CopyToClipboard(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                await ShowToast("Copied to clipboard");
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
        private async System.Threading.Tasks.Task EditItem()
        {
            await ShowToast("Edit item triggered");
        }

        [RelayCommand]
        private async System.Threading.Tasks.Task DeleteItem()
        {
            if (SelectedVaultItem != null)
            {
                _allVaultItems.Remove(SelectedVaultItem);
                FilterVaultItems();
                SelectedVaultItem = _allVaultItems.FirstOrDefault();
                await ShowToast("Item deleted");
            }
        }

        [RelayCommand]
        private async System.Threading.Tasks.Task AddNewItem()
        {
            await ShowToast("Add new item triggered");
        }
    }
}
