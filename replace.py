import re

with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

new_methods = """
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
"""

content = content.replace("    }\n}", new_methods)

with open("CipherVault/ViewModels/MainViewModel.cs", "w") as f:
    f.write(content)
