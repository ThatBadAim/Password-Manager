import re

with open("CipherVault/MainWindow.xaml", "r") as f:
    content = f.read()

# 1. Update Top Header Segoe MDL2 Assets
top_utils_original = """                        <!-- Header Utils -->
                        <Button Content="🔄" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="❓" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="👤" Style="{StaticResource ActionBtn}" Margin="0,0,16,0"/>"""

top_utils_new = """                        <!-- Header Utils -->
                        <Button Content="&#xE895;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="&#xE897;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" Margin="0,0,4,0"/>
                        <Button Content="&#xE77B;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" Margin="0,0,16,0"/>"""

content = content.replace(top_utils_original, top_utils_new)


# 2. Update form field buttons in Vault Details
# Username Copy Button
username_copy_original = """                                        <Button Content="Copy" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}"/>"""
username_copy_new = """                                        <Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.Username}" ToolTip="Copy Username"/>"""
content = content.replace(username_copy_original, username_copy_new)

# Password Show/Copy Buttons
password_buttons_original = """                                            <Button Content="Show" Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}"/>
                                            <Button Content="Copy" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}"/>"""
password_buttons_new = """                                            <Button Style="{StaticResource ActionBtn}" Command="{Binding TogglePasswordVisibilityCommand}" ToolTip="Toggle Visibility">
                                                <TextBlock FontFamily="Segoe MDL2 Assets" FontSize="16">
                                                    <TextBlock.Style>
                                                        <Style TargetType="TextBlock">
                                                            <Setter Property="Text" Value="&#xE18B;"/>
                                                            <Style.Triggers>
                                                                <DataTrigger Binding="{Binding IsPasswordVisible}" Value="True">
                                                                    <Setter Property="Text" Value="&#xE18A;"/>
                                                                </DataTrigger>
                                                            </Style.Triggers>
                                                        </Style>
                                                    </TextBlock.Style>
                                                </TextBlock>
                                            </Button>
                                            <Button Content="&#xE8C8;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" Command="{Binding CopyToClipboardCommand}" CommandParameter="{Binding SelectedVaultItem.EncryptedPassword}" ToolTip="Copy Password"/>"""
content = content.replace(password_buttons_original, password_buttons_new)

# URL Launch Button
url_launch_original = """                                        <Button Content="Open" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}"/>"""
url_launch_new = """                                        <Button Content="&#xE8A7;" FontFamily="Segoe MDL2 Assets" FontSize="16" Style="{StaticResource ActionBtn}" HorizontalAlignment="Right" Margin="4" Command="{Binding LaunchExternalUrlCommand}" CommandParameter="{Binding SelectedVaultItem.Url}" ToolTip="Open URL"/>"""
content = content.replace(url_launch_original, url_launch_new)

with open("CipherVault/MainWindow.xaml", "w") as f:
    f.write(content)
