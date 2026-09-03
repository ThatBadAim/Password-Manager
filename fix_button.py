with open("CipherVault/MainWindow.xaml", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the incorrect button style definition
old_button = r'''<Button Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}">
                                                <Button.Style>
                                                    <Style TargetType="Button" BasedOn="{StaticResource ActionBtn}">'''

new_button = r'''<Button Command="{Binding TogglePasswordVisibilityCommand}">
                                                <Button.Style>
                                                    <Style TargetType="Button" BasedOn="{StaticResource ActionBtn}">'''

content = content.replace(old_button, new_button)

with open("CipherVault/MainWindow.xaml", "w", encoding="utf-8") as f:
    f.write(content)
