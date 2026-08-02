import re

with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

# Add using System.Threading.Tasks; and System.Linq;
content = content.replace("using System.Windows;", "using System.Windows;\nusing System.Threading.Tasks;\nusing System.Linq;")

# We will completely replace the class content
class_content = """    public partial class MainViewModel : ObservableObject
    {
        [ObservableProperty]
        private ObservableCollection<VaultItem> _vaultItems = new();

        [ObservableProperty]
        private ObservableCollection<VaultItem> _filteredVaultItems = new();

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
                if (SetProperty(ref _searchText, value))
                {
                    UpdateSearchFilter();
                }
            }
        }

        [ObservableProperty]
        private string _toastMessage = string.Empty;

        [ObservableProperty]
        private bool _isToastVisible;

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
                Notes = "Use this account for personal open source contributions.\\n\\nAssociated email: alex.c@example.com\\nRecovery codes are stored in offline physical safe.",
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
            SelectedVaultItem = mockItem;
        }

        private void UpdateSearchFilter()
        {
            if (string.IsNullOrWhiteSpace(SearchText))
            {
                FilteredVaultItems = new ObservableCollection<VaultItem>(VaultItems);
            }
            else
            {
                var lowerSearch = SearchText.ToLowerInvariant();
                FilteredVaultItems = new ObservableCollection<VaultItem>(
                    VaultItems.Where(i =>
                        (i.Title != null && i.Title.ToLowerInvariant().Contains(lowerSearch)) ||
                        (i.Category != null && i.Category.ToLowerInvariant().Contains(lowerSearch)) ||
                        (i.Username != null && i.Username.ToLowerInvariant().Contains(lowerSearch))
                    )
                );
            }
        }

        private async void ShowToast(string message)
        {
            ToastMessage = message;
            IsToastVisible = true;
            await Task.Delay(3000);
            IsToastVisible = false;
        }

        [RelayCommand]
        private void CopyToClipboard(string text)
        {
            if (!string.IsNullOrEmpty(text))
            {
                Clipboard.SetText(text);
                ShowToast("Copied to clipboard!");
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
    }"""

content = re.sub(r'public partial class MainViewModel : ObservableObject\s*\{.*\}', class_content, content, flags=re.DOTALL)

with open("CipherVault/ViewModels/MainViewModel.cs", "w") as f:
    f.write(content)
