with open("CipherVault/ViewModels/MainViewModel.cs", "r", encoding="utf-8") as f:
    content = f.read()

import re

search_pattern = r'''        partial void OnSearchTextChanged\(string value\)
        \{
            FilteredVaultItems\.Clear\(\);
            if \(string\.IsNullOrWhiteSpace\(value\)\)
            \{
                foreach \(var item in VaultItems\)
                \{
                    FilteredVaultItems\.Add\(item\);
                \}
            \}
            else
            \{
                var lowerValue = value\.ToLowerInvariant\(\);
                foreach \(var item in VaultItems\)
                \{
                    if \(item\.Title\?\.ToLowerInvariant\(\)\.Contains\(lowerValue\) == true \|\|
                        item\.Category\?\.ToLowerInvariant\(\)\.Contains\(lowerValue\) == true\)
                    \{
                        FilteredVaultItems\.Add\(item\);
                    \}
                \}
            \}
        \}'''

new_search = r'''        partial void OnSearchTextChanged(string value)
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
                var lowerValue = value.ToLowerInvariant();
                foreach (var item in VaultItems)
                {
                    if (item.Title?.ToLowerInvariant().Contains(lowerValue) == true ||
                        item.Category?.ToLowerInvariant().Contains(lowerValue) == true)
                    {
                        FilteredVaultItems.Add(item);
                    }
                }
            }

            // Update the active context logically since there is no master list view
            SelectedVaultItem = FilteredVaultItems.Count > 0 ? FilteredVaultItems[0] : null;
        }'''

content = re.sub(search_pattern, new_search, content, flags=re.MULTILINE)

with open("CipherVault/ViewModels/MainViewModel.cs", "w", encoding="utf-8") as f:
    f.write(content)
