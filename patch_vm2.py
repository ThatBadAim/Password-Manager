with open("CipherVault/ViewModels/MainViewModel.cs", "r") as f:
    content = f.read()

# Fix newline in string literal
content = content.replace('Notes = "Use this account for personal open source contributions.\n\nAssociated email: alex.c@example.com\nRecovery codes are stored in offline physical safe.",',
'Notes = "Use this account for personal open source contributions.\\n\\nAssociated email: alex.c@example.com\\nRecovery codes are stored in offline physical safe.",')

with open("CipherVault/ViewModels/MainViewModel.cs", "w") as f:
    f.write(content)
