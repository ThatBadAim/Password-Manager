with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

# Fix the class indentation
content = content.replace("        public partial class MainViewModel : ObservableObject", "    public partial class MainViewModel : ObservableObject")

with open("CipherVault/ViewModels/MainViewModel.cs", "w") as f:
    f.write(content)
