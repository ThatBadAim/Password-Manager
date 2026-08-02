with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

# Add missing using statement for ObservableCollection just in case, but it's already there!
# using System.Collections.ObjectModel; is at line 3
